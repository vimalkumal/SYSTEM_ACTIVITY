from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import json

# Create your models here.
class activityMaster(models.Model):

    ACTIVITY_MASTER_STATUS = (
        ("Active","Active"),
        ("Inactive","Inactive")
    )

    iActivityMasterId   = models.AutoField(primary_key=True)
    cActivityMasterName = models.CharField(max_length=256,null=False)
    cActivityMasterCode = models.CharField(max_length=256,null=False,unique=True) 
    tActivityConfig     = models.TextField(max_length=256,null=False,default='') 
    eStatus             = models.CharField(max_length=256,null=False,choices=ACTIVITY_MASTER_STATUS)
    dAddedDate          = models.DateField(null=True)
    dUpdatedDate        = models.DateField(null=True)

    def __str__(self):
        return self.cActivityMasterName


class activityMasterTemplate(models.Model):
    
    LANGUAGE = (("en","en"), ("fr","fr"))

    iActivityMasterTemplateID = models.AutoField(primary_key=True)
    iActivityMasterID       = models.ForeignKey(activityMaster,to_field='iActivityMasterId',on_delete=models.CASCADE)
    tActivityTempalte       = models.TextField(null=True)
    eLanguage               = models.CharField(max_length=216,choices=LANGUAGE,default='en')

    def __str__(self):
        return str(self.iActivityMasterTemplateID)

class activityTypeMaster(models.Model):
    
    TYPEMASTER = (
        ("Active","Active"),
        ("Inactive","Inactive")
    )

    iActivityTypeMasterID   = models.AutoField(primary_key=True)
    cActivityType           = models.CharField(max_length=256,null=True)
    cActivityCode           = models.CharField(max_length=256,null=True)
    eStatus                 = models.CharField(max_length=256,choices=TYPEMASTER)      

    def __str__(self) -> str:
        return str(self.cActivityType)
        # return "%s %s" % (self.cActivityType,self.cActivityCode)


class activities(models.Model):

    iActivitiesId           = models.AutoField(primary_key=True)
    iActivityForId          = models.IntegerField(null=False,default=0)
    iActivityMasterID       = models.ForeignKey(activityMaster,to_field="iActivityMasterId",on_delete=models.CASCADE,default=0)
    iActivityTypeMasterID   = models.ForeignKey(activityTypeMaster,to_field='iActivityTypeMasterID',on_delete=models.CASCADE,default=0)
    dAddedDate              = models.DateField(null=True)
    dAddedDateTime          = models.DateTimeField(null=True)
    tActivityParams         = models.TextField(null=True)
    tExtraParams            = models.TextField(null=True)
    iSystemDeleted          = models.IntegerField(default=0)

class activityEntity(models.Model):

    iActivityEntityId       = models.AutoField(primary_key=True)
    iActivitiesId           = models.ForeignKey(activities,to_field="iActivitiesId",on_delete=models.CASCADE) 
    cEntity                 = models.CharField(max_length=216)
    iEntityId               = models.IntegerField()
    dAddedDate              = models.DateField()
    dAddedDateTime          = models.DateTimeField()
   



# Singnals : START
# after activities save add data in to activityEntity
@receiver(post_save,sender=activities)
def addActivityEntitity(sender,instance,created,**kwatgs):
    if created:
        # Insert data into activity entity : START
        activities_id = instance.iActivitiesId
        activity_master_details = instance.iActivityMasterID
        activty_master_config = json.loads(activity_master_details.tActivityConfig)

        activity_params = json.loads(instance.tActivityParams)
        activity_master_entity = activty_master_config['applicable_entity']
        
        for entity_item in activity_master_entity:
            entity_val      = str(entity_item['entity'])
            entity_field    = entity_item['entity_key']
            

            if(int(activity_params[entity_field])>0):
            # insert data in activity entity
                newActivityEntity = activityEntity(
                    iActivitiesId       = instance,
                    cEntity             = entity_val,
                    iEntityId           = int(activity_params[entity_field]),
                    dAddedDate          = timezone.now().date(),
                    dAddedDateTime      = timezone.now()
                )
                newActivityEntity.save()
            # Insert data into activity entity : END
    pass
# Singnals : END