import django_filters
from django_filters import rest_framework as filters
from .models import Project, ToDo
from django_filters.widgets import RangeWidget


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class ToDoFilter(filters.FilterSet):
    project__name = filters.CharFilter(lookup_expr='contains')
    date_create = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = ToDo
        fields = ['project__name', 'date_create']