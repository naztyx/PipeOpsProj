from django import forms
from .models import MedicalRecord

class MedRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['data']
        