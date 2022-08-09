from rest_framework import serializers
from .models import User
oldest_user = 0

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'city']