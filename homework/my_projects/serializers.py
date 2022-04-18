from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from my_projects.models import Project, ToDo
from my_users.serializers import MyUserModelSerializer


class ProjectSerializer(ModelSerializer):
    users = MyUserModelSerializer(many=True)
    creator = MyUserModelSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    creator = MyUserModelSerializer()
    project = ProjectSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'