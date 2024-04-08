from rest_framework import serializers

from schedule_api.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'middle_name', 'date_of_birth', 'gender']
        extra_kwargs = {
                        'middle_name': {'write_only': True},
                        'gender': {'write_only': True}
                        }

