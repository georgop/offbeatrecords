from django import forms
from .models import info

class EmailForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model = info
        fields = ['email',]