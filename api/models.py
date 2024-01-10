from django.db import models

class BotUser(models.Model):
    user_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120, null=True, blank=True)
    subscribed = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Feedback(models.Model):
    user_id = models.CharField(max_length=120,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=120, null=True, blank=True)
    body1 = models.CharField(max_length=120, null=True, blank=True)
    body2 = models.CharField(max_length=120, null=True, blank=True)
    body3 = models.CharField(max_length=120, null=True, blank=True)
    body4 = models.CharField(max_length=120, null=True, blank=True)
    body5 = models.CharField(max_length=120, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.body)    
