from django.shortcuts import render
from django.views import generic
from .models import Category, Recipe


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'index.html'


class PublicRecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(public=True).order_by('-created_on')
    template_name = 'public_recipes.html'


class PersonalRecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(public=False).order_by('-created_on')
    template_name = 'personal_recipes.html'
