from django import forms
from .models import *
from django.core.exceptions import ValidationError


class PhraseForm(forms.ModelForm):

    class Meta:
        model = Phrase
        fields = ['original', 'translation']
        widgets = {
            'original': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Original',
                'autocomplete': 'off'
            }),
            'translation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Translation',
                'autocomplete': 'off'
            })
        }