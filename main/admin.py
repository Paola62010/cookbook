from django.contrib import admin
from .models import Category, Recipe, Ingredient, Step, Comment


# Register your models here.
admin.site.site_header = 'CookBook Administration'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_on', 'updated_on',)
    list_filter = ('created_on', 'updated_on',)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
