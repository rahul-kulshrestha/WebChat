from django.shortcuts import render
from app.models import UserMessage
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    # print(group_name)
    # user = UserMessage.objects.get(name=group_name)
    # print(group)
    # msg = []

    
    msg = UserMessage.objects.filter(receiver=request.user)
    user = User.objects.all()
    #     # print(msg)
    #     pass
  

    return render(request,'app/index.html',{'msg':msg,'users':user})