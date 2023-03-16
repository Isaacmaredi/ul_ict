from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Row, Column, Button

from .models import License, LicenseRenewal
 
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
        
class LicenseRenewalForm(ModelForm):
    class Meta:
        model = LicenseRenewal
        fields = ('license','renewal_date','renewal_amount',
                'pr_number','po_number')
        
        widgets = widgets = {
            'renewal_date':DateInput(attrs={'placeholder':'yyyy-mm-dd'}),
        } 
        
    def __init__(self, *args, **kwargs):
        super(LicenseRenewalForm, self).__init__(*args, **kwargs)
        self.fields['license'].widget.attrs['read-only'] = True
        self.fields['license'].disabled = True
        self.fields['license'].required = False
        self.fields['renewal_date'].label = "Renewal Date"
        # self.fields['start_date'].required = True
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
           
        
    
    