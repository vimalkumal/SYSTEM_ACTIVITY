from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path("",views.activityHomePage,name="homePage"),
    path("activityType/",views.activityTypeMasterListing,name="activityType"),
    path("activityTemplates/",views.activityMasterTemplateListing,name="activityTemplates"),
    path("activityMaster/",views.activityMasterListing,name="activityMaster"),
    path("addActivity/",views.addActivity,name="addActivity")
]
