import os,json
from .models import activities,activityMaster,activityMasterTemplate
class activityTemplates():

    def __init__(self):
        pass



    def getActivityTemplatesValue(objActivityEntity):
        activity_context = []
        # print(objActivityEntity)
        # os._exit(1)
        activity_id = objActivityEntity.iActivitiesId

        activity_obj                = activities.objects.get(iActivitiesId=activity_id)
        activity_master_obj         = activity_obj.iActivityMasterID

        activity_master_id          = activity_master_obj.iActivityMasterId
        activity_master_template    = activityMasterTemplate.objects.get(iActivityMasterID=activity_master_id,eLanguage='en')

        params_str = activity_obj.tActivityParams
        templates = activity_master_template.tActivityTempalte
        new_templates = templates
        params_array = json.loads(params_str)
        # print(params_array)
        # print(templates)
        # print(params_array['USER_NAME'])
        for dict in params_array:
            serch_key = '#'+dict+'#'
            # print(dict)
            if serch_key in templates:
                new_templates = new_templates.replace(serch_key,params_array[dict])
                # print(new_templates)

        activity_context = {
            'message':new_templates
        }
        # exit()


        # print(new_templates)
        # s.replace("World", "Python")

        # print(type(params_array))
        # print(activity_obj.tActivityParams)
        # print(activity_master_template.tActivityTempalte)
        # activity_data = activities.objects.select_related( 'iActivityMasterID').prefetch_related('iActivityMasterID__activitymastertemplate_set').get(iActivitiesId=activity_id)
        # print(activity_data)
        # print(activity_obj.iActivityMasterID)
        # print(type(activity_obj))
        # print( type(activity_id))

        # os._exit(1)

        return activity_context
        