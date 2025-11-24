from django import forms
from . models import *

class RecipeForm(forms.ModelForm):

    class Meta:

        model = Recipe
        fields = '__all__'