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

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super(RecipeForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Recipe.objects.filter(author=self.author, title=title).exists():
            raise forms.ValidationError("You have already written a recipe with same title.")
        return title


class UpdateRecipeForm(forms.ModelForm):
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
