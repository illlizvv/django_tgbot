from django.urls import path
from .views import BotUsersApiView, FeedbacksApiView
from .views import BotUserUpdateAPIView


urlpatterns = [
                path('bot-users', BotUsersApiView.as_view(), name='bot-users'),
                path('feedbacks', FeedbacksApiView.as_view(), name='feedbacks'),
                path('bot-users/<str:user_id>/update', BotUserUpdateAPIView.as_view(), name='bot-user-update'),
                ]