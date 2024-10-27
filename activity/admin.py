from django.contrib import admin
from .models import activities,activityEntity,activityMaster,activityMasterTemplate,activityTypeMaster
from django.contrib.admin.options import ModelAdmin

# Register your models here.


# Registering activityMaster model with all fields
class activityMasterAdmin(admin.ModelAdmin):
    list_display = (
        'iActivityMasterId', 
        'cActivityMasterName', 
        'cActivityMasterCode', 
        'tActivityConfig', 
        'eStatus', 
        'dAddedDate', 
        'dUpdatedDate'
    )

# Registering activityMasterTemplate model with all fields
class activityMasterTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'iActivityMasterTemplateID', 
        'iActivityMasterID', 
        'tActivityTempalte', 
        'eLanguage'
    )

# Registering activityTypeMaster model with all fields
class activityTypeMasterAdmin(admin.ModelAdmin):
    list_display = (
        'iActivityTypeMasterID', 
        'cActivityType', 
        'cActivityCode', 
        'eStatus'
    )

# Registering activities model with all fields
class activitiesAdmin(admin.ModelAdmin):
    list_display = (
        'iActivitiesId', 
        'iActivityForId', 
        'iActivityMasterID', 
        'iActivityTypeMasterID', 
        'dAddedDate', 
        'dAddedDateTime', 
        'tActivityParams', 
        'tExtraParams', 
        'iSystemDeleted'
    )

# Registering activityEntity model with all fields
class activityEntityAdmin(admin.ModelAdmin):
    list_display = (
        'iActivityEntityId', 
        'iActivitiesId', 
        'cEntity', 
        'iEntityId', 
        'dAddedDate', 
        'dAddedDateTime'
    )

admin.site.register(activities,activitiesAdmin)
admin.site.register(activityEntity,activityEntityAdmin)
admin.site.register(activityMaster,activityMasterAdmin)
admin.site.register(activityMasterTemplate,activityMasterTemplateAdmin)
admin.site.register(activityTypeMaster,activityTypeMasterAdmin)
