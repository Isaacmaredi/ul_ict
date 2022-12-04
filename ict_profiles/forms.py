from django import forms

from crispy_forms.helper import FormHelper

from ict_accounts.models import Profile

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields ='__all__'
        widgets = {
            'birth_date': DateInput(attrs={'placeholder':'yyyy-mm-dd'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProfileCreateForm, self).__init__(*args, **kwargs)
        self.fields["user"].disabled = True
        self.fields["user"].widget.attrs["readonly"] = True
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
    
        self.helper.form_show_labels = True