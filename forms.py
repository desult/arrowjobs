from django import forms
from .models import Asp

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Asp
        fields = ['design_id', 'description', 'contact']
        #widgets = {'contact': forms.Select()}