from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from channels.layers import get_channel_layer
from time import sleep
from app.models import UserMessage
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
import asyncio
import json
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        # print("connect")
        self.send({
            'type':'websocket.accept',
        })
        # print(event)

    def websocket_receive(self,event):
        # print("receive")
        for i in range(10):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            # sleep(1)
        # print(event)

    def websocket_disconnect(self,event):
        # print("disconnect")
        raise StopConsumer()
    
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        await self.send({
            'type':'websocket.accept'
        })
        # print("a")
        self.user = self.scope['user']
        # if self.user.is_authenticated:
            
            # print(self.user.username)
        
        await self.channel_layer.group_add(self.user.username,self.channel_name)
        # print('b')
        # print(self)
    async def websocket_receive(self,event):
        # for i in range(10):
        #     await self.send({
        #         'type':'websocket.send',
        #         'text':str(i)
        #     })
        #     await asyncio.sleep(1)
        # print(self.channel_layer)
        # print(self.channel_name)
        # self.channel_layer.group_add('mychannel',self.channel_name)
        # user =await database_sync_to_async(User.objects.get)(username="admin")
        # user = self.scope['user']
        # print(self.user)
        # ch = get_channel_layer()
        # exists = await self.channel_layer.group_exists(self.sender)
        # print(ch.)
        # print(await self.channel_layer.group_channels('hrhg'))
        # m = Message(sender=user, receiver=user,message=event['text'])
        # await m.save()
        if self.user.is_authenticated:
            # group =await database_sync_to_async(Group.objects.get)(name=self.group_name)
            # print('get')
            # self.receiver = 'admin'
            self.data = json.loads(event['text'])
            self.receiver =self.data['user']
            self.re = await database_sync_to_async(User.objects.get)(username=self.receiver)
            # print('post')
            print(self.receiver)
            # print(msg)
            # await database_sync_to_async(msg.save)()
            # print('c')
            # self.sender =  "user1"
            # ch = await self.channel_layer.group_exists(self.sender)
            # ch = get_channel_layer()
            # exists = await self.channel_layer.group_exists(self.sender)
            # print(exists)
            # print(ch)
            
            msg = UserMessage(sender=self.user,receiver=self.re,message=self.data['msg'])
            await database_sync_to_async(msg.save)()
            # print(event['text'])
            
            
            await self.channel_layer.group_send(self.user.username,{
                'type':'chat.msg',
                'message':event['text']
            })
            await self.channel_layer.group_send(self.receiver,{
                'type':'chat.msg',
                'message':event['text']
            })
            
            # await self.channel_layer.group_send(self.user,{
            #     'type':'chat.msg',
            #     'message':event['text']
            # })
        else:
            await self.send({
                'type':'websocket.send',
                'text':'loginn first'
            })
        # print('d')
    async def chat_msg(self,event):
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })
    async def websocket_disconnect(self,event):
        # print(self.user)
        raise StopConsumer()