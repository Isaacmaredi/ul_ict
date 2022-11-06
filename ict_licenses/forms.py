from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Row, Column, Button

from .models import License

class DateInput(forms.DateInput):
    input_type = 'date'
    
class LicenseCreateForm(ModelForm):
    
    class Meta:
        model = License
        exclude = ['owner']
        widgets = {
            'start_date':DateInput(attrs={'placeholder':'yyyy-mm-dd'}), 
            'name':forms.TextInput(attrs= {'placeholder':'License Unique Name'}),  
            'description':forms.Textarea(attrs= {'placeholder':'License Description'}),    
        } 
    

    def __init__(self, *args, **kwargs):
        super(LicenseCreateForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs = {'rows':3}
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
    
        self.helper.form_show_labels = True
        
    