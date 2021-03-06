from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from devstagram.mainsite.models import Picture


class ChatRoom(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatroom_user_one')
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chatroom_user_two')
    last_msg_time = models.DateTimeField(auto_now=True)

    def update_last_msg_time(self):
        self.last_msg_time = timezone.now()
        self.save()


class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messagesender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messagereceiver')
    message = models.TextField()
    timestamp = models.TimeField(auto_now=True)
    datetimestamp = models.DateTimeField(auto_now=True)


class PostMessage(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.TimeField(auto_now=True)
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    post_image = models.ForeignKey(Picture, on_delete=models.CASCADE)
    datetimestamp = models.DateTimeField(auto_now=True)

