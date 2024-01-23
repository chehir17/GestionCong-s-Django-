from django import forms
from .models import Tache

INPUT_CLASSES = 'w-full py-4 px-6 rounded-md border'

class AddTachForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ('user_id', 'titre', 'duree')
        widgets = {
            'user_id': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),            
            'titre': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'duree': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

class EditTache(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ('user_id', 'titre', 'duree')
        widgets = {
            'user_id': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),            
            'titre': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'duree': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }