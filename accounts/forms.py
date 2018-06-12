from django import forms

class UserLoginForm(forms.Form):
    """
    Used by the user to enter login credentials
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


