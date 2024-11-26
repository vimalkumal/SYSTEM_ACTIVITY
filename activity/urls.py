from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path("",views.activityHomePage,name="homePage"),
    
    path("activityType/",views.activityTypeMasterListing,name="activityType"),
    path('activityType/add/', views.activityTypeMasterForm, name='activityTypeAdd'),
    path('activityType/edit/<int:pk>/', views.activityTypeMasterForm, name='activityTypeEdit'),


    path("activityTemplates/",views.activityMasterTemplateListing,name="activityTemplates"),
    path('activityTemplates/add/', views.activityMasterTemplateFormView, name='activityMasterTemplatesAdd'),
    path('activityTemplates/edit/<int:pk>/', views.activityMasterTemplateFormView, name='activityMasterTemplatesEdit'),
    
    path("activityMaster/",views.activityMasterListing,name="activityMaster"),
    path('activityMaster/add/', views.activityMasterFormView, name='activityMasterAdd'),
    path('activityMaster/edit/<int:pk>/', views.activityMasterFormView, name='activityMasterEdit'),

    
    path("addActivity/",views.addActivity,name="addActivity"),

    path('help-doc/',views.downloadHelpFile,name="helpDoc")
]
