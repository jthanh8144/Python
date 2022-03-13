from django import forms
from . models import UpForm

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UpForm
        fields = ['title', 'image', 'body']


# class UploadFileForm(forms.ModelForm):
#     title = forms.CharField(max_length=255)
#     image = forms.FileField()
#     body = forms.CharField(widget=forms.Textarea)
