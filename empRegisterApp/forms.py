from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee # we have already created Employee model, we are using it here
        fields = '__all__' # to get all the properties of model: Employee insdie form
        #fields = ('fullname','empcode','mobile','position') #this shows custom filed, if you want to remove any field like mobile
                                                             #then you just have to remove it from this tuple only
                                                             #it will not render in HTML page.
        labels = {
            'fullname': 'Full Name',
            'empcode': 'Emp. code',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select' #give name 'Select' to dropdown instead of '-----'
        self.fields['empcode'].required = False # remove from mandatory field, 'empcode' is name from models.py