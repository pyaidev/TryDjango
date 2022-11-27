from django import forms
from .models import Recipe, RecipeIngredient


class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['slug', 'user', 'is_active']


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'
        exclude = ['recipe']
