from django.contrib import admin
from django.urls import path,include
from activity_api.views import ActivityMasterViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'activityMaster',ActivityMasterViewSet)

urlpatterns = [
    path('',include(router.urls))
]