from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Contract

class DateInput(forms.DateInput):
    input_type = 'date'

class ContractCreateForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
        
        widgets = {
            'start_date':DateInput(),
            'end_date':DateInput(),
            'date_signed':DateInput(),            
        } 
        
    def __init__(self, *args, **kwargs):
        super(ContractCreateForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs ={'rows':3}
        self.fields['supplier'].empty_label = 'Select a supplier'
        self.fields['comments'].widget.attrs ={'rows':3}
        self.fields['agreement_type'].empty_label = 'Select agreement type'
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_show_labels = True
        
    