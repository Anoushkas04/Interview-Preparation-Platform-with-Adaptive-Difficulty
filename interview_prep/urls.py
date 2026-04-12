from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('practice/<int:topic_id>/', views.practice_topic, name='practice_topic'),
    path('history/', views.history, name='history'),
    path('profile/', views.profile, name='profile'),
]
