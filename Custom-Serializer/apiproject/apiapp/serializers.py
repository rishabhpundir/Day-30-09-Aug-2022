from rest_framework import serializers
from .models import User
oldest_user = 0

class UserSerializer(serializers.ModelSerializer):
    oldest = serializers.SerializerMethodField('get_oldest_age')

    def get_oldest_age(self, user_obj):
        global oldest_user
        age = getattr(user_obj, 'age')
        if age and age > oldest_user:
            oldest_user = age
            return oldest_user
        else:
            return oldest_user

    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'city', 'oldest']