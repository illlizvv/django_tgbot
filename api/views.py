from .models import BotUser, Feedback
from .serializers import BotUserSerializer, FeedbackSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from .models import BotUser
import requests
from django.shortcuts import render

class BotUsersApiView(ListCreateAPIView):
    queryset = BotUser.objects.all() 
    serializer_class  = BotUserSerializer

class FeedbacksApiView(ListCreateAPIView):
    queryset = Feedback.objects.all() 
    serializer_class  = FeedbackSerializer

class BotUserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer #преобразуютcя данные сложных типов 
    lookup_field = 'user_id'


