from rest_framework.serializers import HyperlinkedModelSerializer
from .models import MyUser
from rest_framework import serializers


class MyUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        # fields = '__all__'
        # fields = ['url', 'username', 'email', 'groups']
        fields = ['url', 'username', 'first_name', 'last_name', 'email']