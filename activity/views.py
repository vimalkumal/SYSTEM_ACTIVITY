from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .form import ActivityTypeMasterForm,ActivityMasterForm,ActivityMasterTemplatesForm,ActivityForm
from .models import activityMasterTemplate,activityMaster,activityTypeMaster,activities,activityEntity
from .activity_tempalates import activityTemplates as at
import json
from django.utils import timezone

# Create your views here.

def activityHomePage(request):
    activity_data = []
    entity_name = 'user'  # Set your desired entity name
    entity_id = 10  # Set your desired entity type
    
    activity_entities = activityEntity.objects.filter(cEntity=entity_name, iEntityId=entity_id)
    index = 0
    for obj in activity_entities:
        activityies_details = obj.iActivitiesId
        # print(activityies_details)
        activities_message_data = at.getActivityTemplatesValue(activityies_details)
        activitiesData = {
            'message':activities_message_data['message']
        }
        activity_data.append(activitiesData)
        # contex[index] = activitiesData
        # index+=1

    contex = {"activity_data":activity_data}
    # print(activity_entities)
    print(contex)
    return render(request,'activity/home_page.html',contex)

def activityTypeMasterListing(request):
    if request.method == "POST":

        # --------------------------------------------
        activityTypeName = request.POST.get('inputActivityTypeName')
        activityTypeCode = request.POST.get('inputActivityTypeCode')
        activityTypeStatus     = request.POST.get('inputActivityTypeStatus')

        activity_type_master = activityTypeMaster(
            cActivityType   =   activityTypeName.title(),
            cActivityCode   =   activityTypeCode,
            eStatus         =   activityTypeStatus
        )
        activity_type_master.save()
        # from_validate.save()
        return redirect('activityType')
        # --------------------------------------------

        '''
        from_validate = ActivityTypeMasterForm(request.POST)
        if from_validate.is_valid():
            from_validate.save()
            return redirect('activityType')
        '''

    else:
        formValues = ActivityTypeMasterForm()
        atmListing = activityTypeMaster.objects.all()
        context = {"atm_listing":atmListing,"form":formValues}
        
    return render(request,"activity/activity_type.html",context)


def activityMasterListing(request):
    
    if request.method == 'POST':

        activityMasterName = request.POST.get('inputActivityMasterName')
        activityMasterCode = request.POST.get('inputActivityMasterCode')
        activityConfig     = request.POST.get('inputActivityConfig')
        status             = request.POST.get('inputActivityMasterStatus')

        activity_master = activityMaster(
            cActivityMasterName=activityMasterName.title(),
            cActivityMasterCode=activityMasterCode,
            tActivityConfig=activityConfig,
            eStatus=status,
            dAddedDate = timezone.now().date(),
            dUpdatedDate = timezone.now().date()
        )
        activity_master.save()
        # from_validate.save()
        return redirect('activityMaster')
    
        '''
        form_validate = ActivityMasterForm(request.POST)
        if form_validate.is_valid():
            form_validate.save()
            
            return redirect('activityMaster')
        else:
            return render(request,'activity/error.html')
        '''
    else:
        formValues  = ActivityMasterForm()
        amListing   = activityMaster.objects.all()
        context = {'form':formValues,'amListing':amListing}
    
    return render(request,'activity/activity_master.html',context)

def activityMasterTemplateListing(request):
    if request.method == 'POST':
        print(request.POST.get)
        # --------------------------------------------
        activityMasterId = request.POST.get('inputActivityMasterId')
        activityTemplate = request.POST.get('inputActivityTemplate')
        activityTemplateLng     = request.POST.get('inputActivityTemplateLng')
        activity_master_instance = get_object_or_404(activityMaster, pk=activityMasterId)
        print(type(activityMasterId))
        activity_template_master = activityMasterTemplate(
            iActivityMasterID   =   activity_master_instance,
            tActivityTempalte   =   activityTemplate,
            eLanguage         =   activityTemplateLng
        )
        activity_template_master.save()
        # from_validate.save()
        return redirect('activityTemplates')
        # --------------------------------------------

        '''
        form_validate = ActivityMasterTemplatesForm(request.POST)

        if form_validate.is_valid():
            form_validate.save()
            return redirect('activityTemplates')

        '''

    else:
        formValues = ActivityMasterTemplatesForm()
        amtListing = activityMasterTemplate.objects.all()
        context = {'form':formValues,'amtListing':amtListing}
    
    return render(request,'activity/activity_master_templates.html',context)


def addActivity(request):
    
    if request.method == "POST":
        form_validate = ActivityForm(request.POST)
        if form_validate.is_valid():
            retData =form_validate.save()

            # Insert data into activity entity : START
            '''
            activities_id = retData.iActivitiesId
            activity_master_details = retData.iActivityMasterID
            activty_master_config = json.loads(activity_master_details.tActivityConfig)

            activity_params = json.loads(retData.tActivityParams)
            
            
            activity_master_entity = activty_master_config['applicable_entity']
            
            for entity_item in activity_master_entity:
                entity_val = entity_item['entity']
                entity_field = entity_item['entity_key']
                

                if(int(activity_params[entity_field])>0):
                #     # insert data in activity entity
                    newActivityEntity = activityEntity(
                        iActivitiesId       = retData,
                        cEntity             = entity_val,
                        iEntityId           = int(activity_params[entity_field]),
                        dAddedDate          = timezone.now().date(),
                        dAddedDateTime      = timezone.now()
                    )
                    newActivityEntity.save()
            # Insert data into activity entity : END
            '''
            return redirect('homePage')
        else:
            return redirect(request,"activity/error.html")
    else:
        formValues = ActivityForm()
        context = {'form':formValues}
        
        
        # return render(request,"activity/error.html")
    

    return render(request,"activity/activity_add.html",context)


def testing(request):

    activityId = 1
    activity_data = activities.objects.get(iActivitiesId=activityId)
    activity_master = activity_data.iActivityMasterID
    master_config = activity_master.tActivityConfig
    # print(json.loads(master_config))
    # activity_master_data = activity_data.activityMaster_set.all()
    # print(activities.objects.select_related('activityMaster').get(iActivityMasterID=activityId))
    # print(activity_data)
    # activity_master_data = activityMaster.objects.get(iActivityMasterId = activity_data.iActivityMasterID)
    # master_config = activity_master_data.tActivityConfig

    # dict_object = json.loads(master_config)
    # print(dict_object)

    # activity_master_data = activity_data.
    # print(activity_master_data)
    # print(activity_master.iActivityMasterId)
    # print(activity_params)
    # print( type(json.loads(activity_params)))
    
    return HttpResponse("Testing Ongoing")


