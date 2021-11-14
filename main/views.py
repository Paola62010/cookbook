from django.shortcuts import render
from django.views import generic
from .models import Category


class CategoryList(generic.ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'index.html'
