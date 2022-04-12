from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from my_users.views import MyUserModelViewSet


router = DefaultRouter()
router.registry('users', MyUserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
