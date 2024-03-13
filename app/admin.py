from django.contrib import admin
from app.models import UserMessage

# Register your models here.
@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['id','message','timestemp','sender','receiver']

# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ['id','name']