from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.contrib.auth.forms import SetPasswordForm
from crispy_forms.helper import FormHelper
from .models import Account, Profile



class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        
    }),validators=[validate_password])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email','mobile_number','password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError(
                "Passwords do not match!"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['mobile_number'].widget.attrs['placeholder'] = 'Mobile Phone Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        
        # for key, field in self.fields.items():
        #     field.label = ''
        
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'

class MyPasswordResetForm(SetPasswordForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        
    }),validators=[validate_password])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['password',]

    def clean(self):
        cleaned_data = super(MyPasswordResetForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError(
                "Passwords do not match!"
            )

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
    
        self.helper.form_show_labels = False