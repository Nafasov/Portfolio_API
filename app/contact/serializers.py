from rest_framework import serializers

from .models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'name', 'subject', 'email', 'message', 'created_date']
        read_only_fields = ['created_date']

    def create(self, validated_data):
        return Contacts.objects.create(**validated_data)
