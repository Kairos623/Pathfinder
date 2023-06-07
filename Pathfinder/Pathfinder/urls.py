
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from PathBase import views
router = routers.DefaultRouter()
router.register(r'Session', views.SessionViewSet)
router.register(r'Users', views.UserViewSet)
router.register(r'FullSession', views.SessionFullViewSet)
router.register(r'SessionPer', views.SessionViewSetPer)
router.register(r'SessionFullPer', views.SessionFullViewSetPer)
router.register(r'CharacterPer', views.CharacterViewSetPer)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
