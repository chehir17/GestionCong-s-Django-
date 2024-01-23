from django import forms
from .models import Cangees

INPUT_CLASSES = 'w-full py-4 px-6 rounded-md border'


class CongeForm(forms.ModelForm):
    class Meta:
        model = Cangees
        fields = ('sujet', 'dure', 'certif',)
        widgets = {
            'demandeur': forms.CharField(show_hidden_initial= True),
            'sujet': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'dure': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'certif': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            
        }


class EditCongeForm(forms.ModelForm):
    class Meta:
        model = Cangees
        fields = ('sujet', 'dure', 'certif')
        widgets = {
            'sujet': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'dure': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'certif': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            
        }


