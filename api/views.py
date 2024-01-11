
from .models import BotUser, Feedback
from .serializers import BotUserSerializer, FeedbackSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
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

def broadcast_message_view(request):
    return render(request, 'broadcast.html')


@csrf_exempt # данные, которые сервер отправляет браузеру 
def send_broadcast_message(request):
    if request.method == 'POST':  # веб-сервер принимает данные, заключённые в тело сообщения
        message = request.POST.get('message', '')  # получаем сообщение
        subscribers = BotUser.objects.filter(subscribed=True)
        bot_token = '6871568319:AAHRNgDL4agpBzpi2ME_S1EUrpAqI9M07wY' 

        for subscriber in subscribers:
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            data = {'chat_id': subscriber.user_id, 'text': message}
            requests.post(url, data=data)

        return HttpResponse('Сообщение отправлено.')
    else:
        return HttpResponse('Ошибка', status=400)



