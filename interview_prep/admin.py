from django.contrib import admin
from .models import Topic, Question, UserProfile, Attempt, AdaptiveState

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'question_count')
    search_fields = ('name',)

    def question_count(self, obj):
        return obj.questions.count()
    question_count.short_description = 'Number of Questions'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text_preview', 'topic', 'difficulty', 'correct_option')
    list_filter = ('topic', 'difficulty')
    search_fields = ('text', 'option_a', 'option_b', 'option_c', 'option_d')
    list_per_page = 20

    def text_preview(self, obj):
        return obj.text[:80] + "..." if len(obj.text) > 80 else obj.text
    text_preview.short_description = 'Question Text'

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_attempts', 'correct_answers', 'accuracy_display')
    search_fields = ('user__username',)

    def accuracy_display(self, obj):
        return f"{obj.accuracy}%"
    accuracy_display.short_description = 'Accuracy'

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'question_preview', 'is_correct', 'timestamp')
    list_filter = ('is_correct', 'timestamp', 'question__topic')
    search_fields = ('user__username', 'question__text')

    def question_preview(self, obj):
        return obj.question.text[:50] + "..."
    question_preview.short_description = 'Question'

@admin.register(AdaptiveState)
class AdaptiveStateAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'current_difficulty', 'consecutive_correct', 'consecutive_incorrect')
    list_filter = ('current_difficulty', 'topic')
    search_fields = ('user__username', 'topic__name')
