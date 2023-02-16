"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

import ardailytracker.views
from website import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required, user_passes_test
from ardailytracker.views import prem, Import_Excel_pandas


urlpatterns = [
    path('admin/',admin.site.urls),
    path('accounts/',include("django.contrib.auth.urls")),
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    #path('',include('ardailytracker.urls')),

    # path("nav/",views.HomePageView.as_view(),name="navigation"),
    # path('Import_Excel_pandas/', ardailytracker.views.Import_Excel_pandas,name="Import_Excel_pandas"), #FOR UPLOADING EXCEL FILE TO DATABASE 'DETAIL'
    path('Import_excel/',ardailytracker.views.Import_excel,name="Import_excel"),
    path('index/', ardailytracker.views.index,name="index"),
    path('assign/',ardailytracker.views.Resource,name='assign'), #for resource assignment form
    path('res_assign/',ardailytracker.views.showform,name='res_assign_form'), #for resource assignment form with modelform method
    path('update_fields/',ardailytracker.views.UpdateFields,name='update_fields'), #for update fields with modelform method
    path('add_details/', ardailytracker.views.add_details,name="add_details"),
    path('view_resource/', ardailytracker.views.record1,name="view_resource"),
    path('view_detail/', ardailytracker.views.tablemodel,name="view_detail"),
    path('upload/', ardailytracker.views.my_view,name="upload"),
    
    
    path('curruser/', ardailytracker.views.sample_view,name="currentuser"),
    
    path('topuser/update/<int:id>', ardailytracker.views.updatebyleader, name='updatebyleader'), #for updating existing records of model from website 
    path('topuser/update/updaterecord/<int:id>', ardailytracker.views.updaterecord, name='updaterecordleader'),
    path('taskalloted/', ardailytracker.views.testing,name="taskalloted"),
    path('taskalloted/update/<int:id>', ardailytracker.views.update, name='updatebymember'), #for updating existing records of model from website 
    path('taskalloted/update/updaterecord/<int:id>', ardailytracker.views.updaterecord1, name='updaterecordmember'),

    path('export/xls/', ardailytracker.views.export_users_xlsx,name="export_users_xls"),
    path('excellikefilter/', ardailytracker.views.excellikefilter,name="excellikefilter"),
    path('testpurp/', ardailytracker.views.testpurp,name="testpurp"),
    
    path('topuser/', login_required(user_passes_test(lambda u: u.has_perm('ardailytracker.can_access_prem'))(prem)), name='topuser'),
    path('Import_Excel_pandas/', login_required(user_passes_test(lambda u: u.has_perm('ardailytracker.can_access_Import_Excel_pandas'))(Import_Excel_pandas)), name='Import_Excel_pandas'),

    # add this:
    path('accounts/', include('django.contrib.auth.urls')),


    # path('topuser/', ardailytracker.views.prem,name="topuser"),
    # path('taskalloted/', ardailytracker.views.testing,name="taskalloted"),
    # path('customer_list/', ardailytracker.views.customer_list,name="customer_list"),

    # path('restricted/', login_required(user_passes_test(lambda u: u.has_perm('ardailytracker.can_access_restricted_view'))(restricted_view)), name='restricted_view'),



    
]

