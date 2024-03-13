from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name="receiver")
    message =  models.CharField(max_length=1023)
    timestemp = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    # group = models.ForeignKey('Group', on_delete=models.CASCADE)
    

# class Group(models.Model):
#     name = models.CharField(max_length=20)
#     def __str__(self):
#         return self.name

    