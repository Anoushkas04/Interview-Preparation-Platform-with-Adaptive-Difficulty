from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Topic, Question, Attempt, UserProfile, AdaptiveState
import random

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome to InterviewPrep!")
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'interview_prep/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'interview_prep/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

@login_required
def dashboard(request):
    topics = Topic.objects.all()
    return render(request, 'interview_prep/dashboard.html', {'topics': topics})

@login_required
def practice_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    
    # Get or create adaptive state for this user and topic
    state, created = AdaptiveState.objects.get_or_create(user=request.user, topic=topic)
    
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('answer')
        question = get_object_or_404(Question, id=question_id)
        
        is_correct = (selected_option == question.correct_option)
        
        # Log the attempt
        Attempt.objects.create(
            user=request.user,
            question=question,
            user_answer=selected_option,
            is_correct=is_correct
        )
        
        # Update User Profile Statistics
        profile = request.user.userprofile
        profile.total_attempts += 1
        if is_correct:
            profile.correct_answers += 1
        profile.save()
        
        # --- ADAPTIVE LOGIC (Threshold: 4) ---
        if is_correct:
            state.consecutive_correct += 1
            state.consecutive_incorrect = 0
            
            # Promote if threshold reached
            if state.consecutive_correct >= 4:
                if state.current_difficulty == 'Easy':
                    state.current_difficulty = 'Medium'
                elif state.current_difficulty == 'Medium':
                    state.current_difficulty = 'Hard'
                state.consecutive_correct = 0 # Reset after promotion
                messages.success(request, f"Great job! You've been promoted to {state.current_difficulty} level!")
        else:
            state.consecutive_incorrect += 1
            state.consecutive_correct = 0
            
            # Demote if threshold reached
            if state.consecutive_incorrect >= 4:
                if state.current_difficulty == 'Hard':
                    state.current_difficulty = 'Medium'
                elif state.current_difficulty == 'Medium':
                    state.current_difficulty = 'Easy'
                state.consecutive_incorrect = 0 # Reset after demotion
                messages.warning(request, f"Keep practicing! Switching to {state.current_difficulty} level for reinforcement.")
        
        state.save()
        
        if is_correct:
            messages.success(request, "Correct Answer!")
        else:
            messages.error(request, f"Incorrect. The correct answer was {question.correct_option}.")
            
        return redirect('practice_topic', topic_id=topic.id)

    # GET Request: Fetch next question based on current difficulty
    # Filter questions by current difficulty
    questions_at_level = Question.objects.filter(topic=topic, difficulty=state.current_difficulty)
    
    # Get IDs of questions already answered by this user in this topic
    answered_ids = Attempt.objects.filter(user=request.user, question__topic=topic).values_list('question_id', flat=True)
    
    # Exclude answered questions from the pool
    remaining_questions = questions_at_level.exclude(id__in=answered_ids)
    
    if remaining_questions.exists():
        question = random.choice(remaining_questions)
    elif questions_at_level.exists():
        # If all questions at this level are answered, reset the pool (pick from all at this level)
        question = random.choice(questions_at_level)
    else:
        # Fallback: if no questions at current level, try any level
        all_questions = Question.objects.filter(topic=topic)
        if all_questions.exists():
            question = random.choice(all_questions)
        else:
            messages.warning(request, "No questions available for this topic yet.")
            return redirect('dashboard')
    
    context = {
        'topic': topic,
        'question': question,
        'state': state,
    }
    return render(request, 'interview_prep/practice.html', context)

@login_required
def history(request):
    attempts = Attempt.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'interview_prep/history.html', {'attempts': attempts})

@login_required
def profile(request):
    profile = request.user.userprofile
    return render(request, 'interview_prep/profile.html', {'profile': profile})
