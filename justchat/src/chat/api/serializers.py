from rest_framework import serializers

from chat.models import Chat, Contact
from chat.views import get_user_contact


class ContactSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants','memebers_name')
        read_only = ('id')

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        chat = Chat(save=False)
        chat.save()
        curr_user = self.context['request'].user

        if (len(Contact.objects.filter(user=curr_user)) == 0):
            Contact.objects.create(user=curr_user)

        for username in participants:
            contact = get_user_contact(username)
            chat.participants.add(contact)
        chat.save()
        return chat

