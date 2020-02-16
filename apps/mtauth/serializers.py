from rest_framework.serializers import ModelSerializer
from .models import MTUser
from django.contrib.auth.models import Group

# class GroupSerializer(ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['id','name']

class UserSerializer(ModelSerializer):
    # groups = GroupSerializer(many=True)
    class Meta:
        model = MTUser
        exclude = ['password']
