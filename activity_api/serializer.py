from rest_framework import serializers
from activity.models import activityMaster

class ActivityMasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model   = activityMaster
        fields  = '__all__'