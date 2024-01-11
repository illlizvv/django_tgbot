
from django.urls import path
from .views import BotUsersApiView, FeedbacksApiView
from .views import BotUserUpdateAPIView
from .views import broadcast_message_view, send_broadcast_message



urlpatterns = [
                path('bot-users', BotUsersApiView.as_view(), name='bot-users'),
                path('feedbacks', FeedbacksApiView.as_view(), name='feedbacks'),
                path('bot-users/<str:user_id>/update', BotUserUpdateAPIView.as_view(), name='bot-user-update'),
                path('send-broadcast/', send_broadcast_message, name='send_broadcast'),
                path('message/', broadcast_message_view, name='broadcast_message'),
]