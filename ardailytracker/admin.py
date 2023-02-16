from django.contrib import admin, messages
from django.db import models
from .models import Detail
from website.widgets import CustomDatePickerWidget
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms # from utils.excel_export import ExcelExportAdmin
# from admin_multidate_hierarchy.admin import MultiFieldDateHierarchy


# stom form defines a __init__ method that sets the input_formats argument for the my_date_field to ['%m/%d/%Y'], which is the US date format (MM/DD/YYYY).
# class DetailAdminForm(forms.ModelForm):
#     class Meta:
#         model = Detail
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['received'].input_formats = ['%m/%d/%Y']  #interferes choosing calender input option ,requires entering date as mm/dd/yyyy, but not diplaying it in US format
#         self.fields['service_Date'].input_formats = ['%m/%d/%Y']        
#         self.fields['follow_up_Date'].input_formats = ['%m/%d/%Y'] #use only editable fields,not read only
        



#adding functions in admin page for bulk edit


def update_status(self, request, queryset):
        
        if request.POST.get('field_name') and request.POST.get('new_value'):
            field_name = request.POST.get('field_name')
            new_value = request.POST.get('new_value')
            
            # The user clicked submit on the intermediate form.
            # Perform our update action:
            queryset.update(**{field_name: new_value})
            
            # Redirect to our admin view after our update has 
            # completed with a nice little info message saying 
            # our models have been updated:
            self.message_user(request,
                              "Changed status on selected {} tasks".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
                        
        return render(request,
                      'myapp/change_field.html',
                      context={'orders':queryset})

update_status.short_description = "Update status" #for customizing the label in the action dropdown box.




class DetailAdmin(admin.ModelAdmin):

    # form = DetailAdminForm  #form attribute of MyModelAdmin is set to DetailAdminForm
    list_display = ['account_or_Claim_Number','received','client','disposition', 'final_Status','assigned_To','aging_Lag'] #   for what to display from model in django admin page
    ordering = ['final_Status']
    readonly_fields=('status_history','worked_On','worked_By','allocation_Date') #,
    actions = [update_status] #include custom actions in action list
    search_fields = ['received','account_or_Claim_Number','client','disposition', 'final_Status','assigned_To','aging_Lag'] #   ,'allocation_Date'  ,'aging_Lag' for a search function in admin page
    date_hierarchy ='received'
    date_format = 'm/d/Y'


admin.site.register(Detail,DetailAdmin)





