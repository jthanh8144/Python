from django import forms

class uploadMulti(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))