from rest_framework.serializers import HyperlinkedModelSerializer
from .models import MyUser


class MyUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
