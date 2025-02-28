from django.contrib.auth.models import Group, User
from rest_framework import serializers

# Serializer for User model
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']  # Include fields for the User model

# Serializer for Group model
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name'] 