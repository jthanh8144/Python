from django import forms


class registerForm(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField()
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)

class loginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)
