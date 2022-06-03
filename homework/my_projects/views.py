# from rest_framework.decorators import parser_classes
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectSerializer, ToDoSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from .filters import ProjectFilter, ToDoFilter


class ToDoLimitPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectLimitPagination(LimitOffsetPagination):
    default_limit = 10


# @parser_classes((JSONRenderer,))
class ProjectViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    # pagination_class = ProjectLimitPagination
    filter_class = ProjectFilter


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # pagination_class = ToDoLimitPagination
    filter_class = ToDoFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'закрыто'
        self.perform_create(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)