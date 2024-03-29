from django import forms
from django.contrib.auth.models import User
from studytrackerapp.models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return confirm_password
    
class BioUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']   