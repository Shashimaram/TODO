from django import forms
from .models import Notes_model

class newnote(forms.ModelForm):
    note  = forms.CharField(max_length=200, required=True)
    is_complete = forms.BooleanField(required=False)
    
    class Meta:
        model = Notes_model
        fields = ['note','is_complete']

class EditNote(forms.ModelForm):
    note = forms.CharField(max_length=200, required=True)
    
    class Meta:
        model = Notes_model
        fields = ['note']