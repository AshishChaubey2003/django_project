from django import forms
from .models import Zodiac, Horoscope

class ZodiacForm(forms.ModelForm):
    class Meta:
        model = Zodiac
        fields = ['name', 'description']

class HoroscopeForm(forms.ModelForm):
    class Meta:
        model = Horoscope
        fields = ['zodiac', 'date', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
