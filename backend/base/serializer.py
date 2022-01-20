from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import Person, Musician
from .models import User, Role, Rule


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'


# class MusicianSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Musician
#         fields = '__all__'
