from django.shortcuts import render, get_object_or_404
from .models import Chat,Message


def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    for i in chat.messages.order_by('-timestamp').all()[:10]:
             print(i.content)
    return chat.messages.order_by('-timestamp').all()[:10]