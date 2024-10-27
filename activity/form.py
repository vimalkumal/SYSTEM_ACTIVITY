from django.forms import ModelForm
from .models import activityTypeMaster,activityMaster,activityMasterTemplate,activities

class ActivityTypeMasterForm(ModelForm):
    class Meta:
        model = activityTypeMaster
        fields = '__all__'
        
class ActivityMasterForm(ModelForm):
    class Meta:
        model = activityMaster
        fields = '__all__'

class ActivityMasterTemplatesForm(ModelForm):
    class Meta:
        model = activityMasterTemplate
        fields = '__all__'

class ActivityForm(ModelForm):
    class Meta:
        model = activities
        fields = '__all__'