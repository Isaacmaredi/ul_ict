from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Row, Column, Button

from .models import License, Renewal
 
class DateInput(forms.DateInput):
    input_type = 'date'
    
class LicenseCreateForm(ModelForm):
    
    class Meta:
        model = License
        exclude = ['owner','is_renewed']
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
        
class LicenseRenewForm(ModelForm):
    class Meta:
        model = License
        fields = ('start_date','current_cost',
                'service_provider','is_renewed')
        
        widgets = widgets = {
            'start_date':DateInput(attrs={'placeholder':'yyyy-mm-dd'}),
        } 
        
    def __init__(self, *args, **kwargs):
        super(LicenseRenewForm, self).__init__(*args, **kwargs)
        self.fields['service_provider'].widget.attrs['read-only'] = True
        self.fields['service_provider'].disabled = True
        self.fields['service_provider'].required = False
        self.fields['start_date'].label = "Renewal Date"
        self.fields['start_date'].required = True
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
           
        
    
    