from django import forms
from .models import *


class CombineSaveForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    subcategory = forms.CharField(max_length=200)

    class Meta:
        model = Combine
        fields = ('category', 'subcategory')