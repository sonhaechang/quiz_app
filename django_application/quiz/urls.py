from django.urls import path

from quiz.views import RandomQuizAPIView


app_name = 'quiz'

urlpatterns = [
    path("<int:pk>/", RandomQuizAPIView.as_view(), name='random_quiz'),
]