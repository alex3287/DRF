from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from my_projects.models import Project, ToDo
from my_users.serializers import MyUserModelSerializer
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    users = MyUserModelSerializer(many=True)
    creator = MyUserModelSerializer()

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['date_create', 'name', 'users']


class ToDoSerializer(serializers.ModelSerializer):
    creator = MyUserModelSerializer()
    project = ProjectSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'