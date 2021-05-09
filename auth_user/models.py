from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class user_extend(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='related_user',related_query_name='user_query')
    user_profile = models.ImageField(upload_to='profile')


    def __str__(self):
         return str(self.user).title()
