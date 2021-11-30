from django.db.models import fields
from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient, Step, Comment


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'slug',
            'category',
            'servings',
            'recipe_image',
            'public'
        )


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = (
            'name',
            'quantity'
        )


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = (
            'description',
        )


IngredientInlineFormset = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    extra=3,
    can_delete=True,
    )

StepInlineFormset = inlineformset_factory(
    Recipe,
    Step,
    form=StepForm,
    extra=1,
    can_delete=True
    )
