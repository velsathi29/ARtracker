from django import forms
from .models import Detail

# for form
# class UpdateDetailsForm(forms.ModelForm):
#     class Meta:
#         model = Detail
#         fields=['comment_1','comment_2','call_Type','disposition','denial_Code','step','next_Best_Action_For_Success_Rate','follow_up_Date','follow_up_Comments','status_1','final_Status']
        

# Creating a form to add an article.
# form=DetailForm()


# # Creating a form to change an existing article.
# detail = Detail.objects.get(pk=1)
# form = DetailForm(instance=article)






# class ResourceAssignmentForm(forms.Form):

#     client_Name=forms.CharField(label="Enter Client Name",max_length=500)

#     patient_Name=forms.CharField(label="Enter Patient Name",max_length=500)

#     Patient_Account_Number=forms.CharField(label="Enter Patient Account Number",max_length=500)

#     Date_Of_Surgery=forms.DateField(label="Enter Surgery Date")

#     Physician_Name=forms.CharField(label="Enter Physician Name",max_length=500)

#     cPT_Code=forms.CharField(label="Enter CPT Code",max_length=500)

#     payer=forms.CharField(label="Enter Payer Name",max_length=500)

#     payer_ID=forms.CharField(label="Enter Payer ID",max_length=500)

#     payer_Phone=forms.CharField(label="Enter Payer Phone Number",max_length=500)

#     resource_Assigned=forms.CharField(label="Resource Assigned To",max_length=500)




# A model form which is used to validate model fields and create a model object

class MyModelForm(forms.ModelForm):

    class Meta:
        model = Detail
        fields="__all__"

# A form based on django.forms.Form which is used to get the file from request

class FileUploadForm(forms.Form):

    file = forms.FileField()

    def clean_file(self):
        data = self.cleaned_data["file"]
        # read and parse the file, create a Python dictionary `data_dict` from it
        form = MyModelForm(data_dict)
        if form.is_valid():
            # we don't want to put the object to the database on this step
            self.instance = form.save(commit=False) 
        else:
            # You can use more specific error message here
            raise forms.ValidationError(u"The file contains invalid data.")
        return data

    def save(self):
        # We are not overriding the `save` method here because `form.Form` does not have it. 
        # We just add it for convenience.
        instance = getattr(self, "instance", None)
        if instance:
            instance.save()
        return instance

    


class Det_Form(forms.Form):  
    date = forms.DateField(label="Enter date")  
     
    file = forms.FileField() # for creating file input  




# for file upload
# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()