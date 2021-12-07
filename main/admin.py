from django.contrib import admin
from .models import Category, Recipe, Ingredient, Step, Comment


# Register your models here.
admin.site.site_header = 'CookBook Administration'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_on', 'updated_on',)
    list_filter = ('created_on', 'updated_on',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class InLineIngredient(admin.StackedInline):
    model = Ingredient
    extra = 1


class InLineStep(admin.StackedInline):
    model = Step
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [InLineIngredient, InLineStep]
    list_display = ('title', 'slug', 'author', 'created_on', 'updated_on',)
    list_filter = ('created_on', 'updated_on',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'body', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('recipe', 'author',)
