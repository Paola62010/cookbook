from django.db.models import fields
from django import forms
from django.forms import formset_factory
from .models import Recipe, Ingredient, Step, Comment
from extra_views import InlineFormSetFactory


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

    def __init__(self, *args, **kwargs):
        self.recipe = kwargs.pop('recipe')
        super(IngredientForm, self).__init__(*args, **kwargs)


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = (
            'description',
        )


class IngedientInline(InlineFormSetFactory):
    model = Ingredient
    fields = ['name', 'quantity']
    prefix = 'Ingredients'
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': True}


class StepInline(InlineFormSetFactory):
    model = Step
    fields = ['description']
    prefix = 'Steps'
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': True}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'body',
        )
