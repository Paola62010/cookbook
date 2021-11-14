from django.contrib import admin
from .models import Category, Recipe, Ingredient, Step, Comment


# Register your models here.
admin.site.site_header = 'CookBook Administration'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
