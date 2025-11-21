from django import forms 
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = CustomUser
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match.")
        return cleaned_data