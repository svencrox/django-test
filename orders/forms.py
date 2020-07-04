from django import forms
from .models import uploaded_file

class UploadFileForm(forms.ModelForm):
    # title = forms.CharField(max_length=200)
    # content = forms.FileField()
    class Meta:
    	model = uploaded_file
    	fields = ['content', 'title',]