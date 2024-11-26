from django.shortcuts import render
from activity_api.serializer import ActivityMasterSerializer
from activity.models import activityMaster
from rest_framework import viewsets
# Create your views here.

class ActivityMasterViewSet(viewsets.ModelViewSet):
    queryset = activityMaster.objects.all()
    serializer_class = ActivityMasterSerializer

