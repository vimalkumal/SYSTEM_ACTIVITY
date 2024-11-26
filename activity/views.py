from django.conf import settings
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,FileResponse
from .form import ActivityTypeMasterForm,ActivityMasterForm,ActivityMasterTemplatesForm,ActivityForm
from .models import activityMasterTemplate,activityMaster,activityTypeMaster,activities,activityEntity
from .activity_tempalates import activityTemplates as at
from django.utils import timezone

import json
import os
# Create your views here.

def activityHomePage(request):
    activity_data = []
    entity_name = 'user'  # Set your desired entity name
    entity_id = 10  # Set your desired entity type
    
    activity_entities = activityEntity.objects.filter(cEntity=entity_name, iEntityId=entity_id)
    activity_entities = activityEntity.objects.all()
    
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
    # print(contex)
    return render(request,'activity/home_page.html',contex)

# Activity Type Master Listing : START
def activityTypeMasterListing(request):
    if request.method == "POST":

        # --------------------------------------------
        activityTypeName = request.POST.get('inputActivityTypeName')
        activityTypeCode = request.POST.get('inputActivityTypeCode')
        activityTypeStatus     = request.POST.get('inputActivityTypeStatus')

        activity_type_master = activityTypeMaster(
            cActivityType   =   activityTypeName,
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

# Activity Type Master Listing : END

# Activity Type Master Form View : START
def activityTypeMasterForm(request,pk=None):
    
    # If PK is provided, fetch the existing object; else create a new instance
    instance = get_object_or_404(activityTypeMaster, pk=pk) if pk else None
    
    if request.method == 'POST':

        activityTypeName        = request.POST.get('inputActivityTypeName')
        activityTypeCode        = request.POST.get('inputActivityTypeCode')
        activityTypeStatus      = request.POST.get('inputActivityTypeStatus')

        POST_DATA = request.POST.copy()
        POST_DATA['cActivityType']   =   activityTypeName
        POST_DATA['cActivityCode']   =   activityTypeCode
        POST_DATA['eStatus']         =   activityTypeStatus

        form = ActivityTypeMasterForm(POST_DATA, instance=instance)
        if form.is_valid():
            
            # activity_type_master = activityTypeMaster(
            #     cActivityType   =   activityTypeName.title(),
            #     cActivityCode   =   activityTypeCode,
            #     eStatus         =   activityTypeStatus
            # )
            # activity_type_master.save()

            form.save()
            return redirect('activityType')  # Redirect to a list or success page
    else:
        form = ActivityTypeMasterForm(instance=instance)
    
    return render(request, 'activity/activity_type_form.html', {'form': form, 'instance': instance})

# Activity Type Master Form View : END

# Activity Master Listing : START
def activityMasterListing(request):
    
    if request.method == 'POST':

        activityMasterName = request.POST.get('inputActivityMasterName')
        activityMasterCode = request.POST.get('inputActivityMasterCode')
        activityConfig     = request.POST.get('inputActivityConfig')
        status             = request.POST.get('inputActivityMasterStatus')

        activity_master = activityMaster(
            cActivityMasterName=activityMasterName,
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

# Activity Master Listing : END

# Activity Master Form : START
def activityMasterFormView(request,pk=None):

    instance = get_object_or_404(activityMaster, pk=pk) if pk else None
    # print("call............................")
    if request.method == 'POST':

       
        activityMasterName = request.POST.get('inputActivityMasterName')
        activityMasterCode = request.POST.get('inputActivityMasterCode')
        activityConfig     = request.POST.get('inputActivityConfig')
        status             = request.POST.get('inputActivityMasterStatus')

        POST_DATA                           = request.POST.copy()
        
        POST_DATA['cActivityMasterName']    = activityMasterName
        POST_DATA['cActivityMasterCode']    = activityMasterCode.strip()
        POST_DATA['tActivityConfig']        = activityConfig
        POST_DATA['eStatus']                = status

        if instance==None:
            POST_DATA['dAddedDate']         = timezone.now().date()

        POST_DATA['dUpdatedDate']           = timezone.now().date()

        try:
            form = ActivityMasterForm(POST_DATA, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('activityMaster')  # Redirect to a list or success page
            else:
                return HttpResponse("Somthing Went Wrong!!")
            # activity_master = activityMaster(
            #     cActivityMasterName=activityMasterName.title(),
            #     cActivityMasterCode=activityMasterCode,
            #     tActivityConfig=activityConfig,
            #     eStatus=status,
            #     dAddedDate = timezone.now().date(),
            #     dUpdatedDate = timezone.now().date()
            # )
            # activity_master.save()
            # from_validate.save()
            # return redirect('activityMaster')
        except Exception as e:
            return HttpResponse("Somthing went wrong!!",e)
    else:
        form = ActivityMasterForm(instance=instance)

    return render(request, 'activity/activity_master_form.html', {'form': form, 'instance': instance})

# Activity Master Form : END

# Activity Master Template Form : START
def activityMasterTemplateFormView(request,pk=None):

    instance = get_object_or_404(activityMasterTemplate, pk=pk) if pk else None
    if request.method == 'POST':
        
        POST_DATA                   = request.POST.copy()
        activityMasterId            = request.POST.get('inputActivityMasterId')
        activityTemplate            = request.POST.get('inputActivityTemplate')
        activityTemplateLng         = request.POST.get('inputActivityTemplateLng')
        activity_master_instance    = get_object_or_404(activityMaster, pk=activityMasterId)

        POST_DATA['iActivityMasterID']      =   activity_master_instance
        POST_DATA['tActivityTempalte']      =   activityTemplate
        POST_DATA['eLanguage']              =   activityTemplateLng
        
        form = ActivityMasterTemplatesForm(POST_DATA, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('activityTemplates')  # Redirect to a list or success page
        else:
            return HttpResponse("Somthing Went Wrong!!")

        # activity_template_master = activityMasterTemplate(
        #     iActivityMasterID   =   activity_master_instance,
        #     tActivityTempalte   =   activityTemplate,
        #     eLanguage         =   activityTemplateLng
        # )
        # activity_template_master.save()
        # from_validate.save()
        # return redirect('activityTemplates')
        # --------------------------------------------
    else:
        form = ActivityMasterTemplatesForm(instance=instance)

    print(instance)
    print(form)



    return render(request, 'activity/activity_master_templates_form.html', {'form': form, 'instance': instance})
    # return render(request,'activity/activity_master_templates.html',context)
    
# Activity Master Template Form : END


# Activity Master Template Listing : START
def activityMasterTemplateListing(request):
    if request.method == 'POST':
        print(request.POST.get)
        # --------------------------------------------
        activityMasterId            = request.POST.get('inputActivityMasterId')
        activityTemplate            = request.POST.get('inputActivityTemplate')
        activityTemplateLng         = request.POST.get('inputActivityTemplateLng')
        activity_master_instance    = get_object_or_404(activityMaster, pk=activityMasterId)


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

# Activity Master Template Listing : END



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



# Download Files : START
def downloadHelpFile(request):
    # raise Http404("File not found")

    filename = "projectInfo.pdf"
    file_path = os.path.join(settings.BASE_DIR,'static','images','documents',filename)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path,'rb'),as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    else:
        raise Http404("File not found")
    
# Download Files : END

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


