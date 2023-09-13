from django import forms
from .models import data


class dataform(forms.ModelForm):
    class Meta:
        model = data
        fields = ['name','email','phone']