
from .models import BotUser, Feedback
from rest_framework.serializers import ModelSerializer

class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ("name", "username", "user_id", "created_at", "subscribed")
       
class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("user_id",  "created_at", "body", "body1", "body2", "body3", "body4", "body5")