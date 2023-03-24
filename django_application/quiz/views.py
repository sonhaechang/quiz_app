import random

from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Quiz
from quiz.serializers import QuizSerializer


# Create your views here.
class RandomQuizAPIView(APIView):
    serializer_class = QuizSerializer

    def get_object(self):
        return Quiz.objects.all()
    
    def get(self, request):
        randomQuizs = random.sample(list(self.get_object()), self.kwargs['pk'])
        serializer = self.serializer_class(randomQuizs, many=True)
        return Response(serializer.data)