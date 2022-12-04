from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

from .models import Vendor

class DateInput(forms.DateInput):
    input_type = 'date'

class VendorCreateForm(ModelForm):
    
    class Meta:
        model = Vendor
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(VendorCreateForm, self).__init__(*args, **kwargs)
        self.fields['location_footprint'].empty_label = 'Select vendor location footprint'
        self.fields['supplier_channel'].empty_label = 'Select supplier channel type'
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
    

        
    