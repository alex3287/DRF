from rest_framework.serializers import HyperlinkedModelSerializer
from .models import MyUser


class MyUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        # fields = '__all__'
        # fields = ['url', 'username', 'email', 'groups']
        fields = ['url', 'username', 'first_name', 'last_name', 'email']