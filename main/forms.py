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


# class AddIngredientOrStep(forms.models.BaseInlineFormSet):
#     def clean(self):

#         if self.has_changed() is False:
#             raise forms.ValidationError('Please add at least one entry.')


IngredientInlineFormset = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True
    )

StepInlineFormset = inlineformset_factory(
    Recipe,
    Step,
    form=StepForm,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True
    )
