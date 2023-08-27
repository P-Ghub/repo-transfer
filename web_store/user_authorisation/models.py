from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=130)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=20)

