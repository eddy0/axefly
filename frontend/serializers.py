from rest_framework import serializers

from frontend.models import Login


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = ('username', 'password', 'created_at')
