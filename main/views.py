from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Category, Recipe


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'index.html'


class PublicRecipeList(View):
    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        queryset = Recipe.objects.filter(public=True, category__slug=slug).order_by('-created_on')
        context = {
            'object_list': queryset,
            'category': category
            }

        return render(
            request,
            'public_recipes.html',
            context
        )


class PersonalRecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(public=False).order_by('-created_on')
    template_name = 'personal_recipes.html'
