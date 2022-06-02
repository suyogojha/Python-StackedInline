
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/get-quiz/', views.get_quiz, name='get_quiz'),
    path('quiz/', views.quiz, name='quiz'),

]
