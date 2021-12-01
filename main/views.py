from django.db import models, transaction
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Category, Ingredient, Recipe, Step, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .forms import RecipeForm, IngredientInlineFormset, StepInlineFormset
from django.views.generic.edit import CreateView, UpdateView


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'index.html'


class PublicRecipeList(View):
    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        queryset = Recipe.objects.filter(public=True, category__slug=slug).order_by('-created_on')
        context = {
            'recipe_list': queryset,
            'category': category
            }

        return render(
            request,
            'public_recipes.html',
            context
        )


class PersonalRecipeList(View):
    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        queryset = Recipe.objects.filter(author=request.user, category__slug=slug).order_by('-created_on')
        context = {
            'recipe_list': queryset,
            'category': category
            }

        return render(
            request,
            'personal_recipes.html',
            context
        )


class RecipeDetail(View):
    def get(self, request, id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=id)
        ingredients = Ingredient.objects.filter(recipe=id)
        steps = Step.objects.filter(recipe=id)
        liked = False
        if recipe.likes.filter(id=request.user.id).exists():
            liked = True
        favourite = False
        if recipe.favourites.filter(id=request.user.id).exists():
            favourite = True

        context = {
            'recipe': recipe,
            'ingredients': ingredients,
            'steps': steps,
            'liked': liked,
            'favourite': favourite
        }

        return render(
            request,
            'recipe_detail.html',
            context
        )


class RecipeLike(View):
    def post(self, request, id, slug):
        recipe = get_object_or_404(Recipe, id=id)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse("recipe_detail", args=[slug, id]))


class RecipeFavourite(View):
    def post(self, request, id, slug):
        recipe = get_object_or_404(Recipe, id=id)
        if recipe.favourites.filter(id=request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)

        return HttpResponseRedirect(reverse("recipe_detail", args=[slug, id]))


class FavouritesList(View):
    def get(self, request):
        favourites = User.objects.prefetch_related('recipe_favourites').get(id=request.user.id).recipe_favourites.all()

        return render(
            request,
            'favourites.html',
            {'favourites': favourites}
        )


class CreateRecipe(CreateView):
    model = Recipe
    template_name = 'create_recipe.html'
    form_class = RecipeForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CreateRecipe, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientInlineFormset(self.request.POST, self.request.FILES)
            data['steps'] = StepInlineFormset(self.request.POST, self.request.FILES)
        else:
            data['ingredients'] = IngredientInlineFormset()
            data['steps'] = StepInlineFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        steps = context['steps']
        with transaction.atomic():
            form.instance.author = self.request.user
            self.object = form.save()
            if ingredients.is_valid():
                ingredients.instance = self.object
                ingredients.save()
            if steps.is_valid():
                steps.instance = self.object
                steps.save()
        return super(CreateRecipe, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')


class UpdateRecipe(UpdateView):
    model = Recipe
    template_name = 'update_recipe.html'
    form_class = RecipeForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(UpdateRecipe, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientInlineFormset(self.request.POST, self.request.FILES, instance=self.object)
            data['steps'] = StepInlineFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['ingredients'] = IngredientInlineFormset(instance=self.object)
            data['steps'] = StepInlineFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        steps = context['steps']
        with transaction.atomic():
            form.instance.author = self.request.user
            self.object = form.save()
            if ingredients.is_valid():
                ingredients.instance = self.object
                ingredients.save()
            if steps.is_valid():
                steps.instance = self.object
                steps.save()
        return super(UpdateRecipe, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')
