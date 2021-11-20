from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('public', views.PublicRecipeList.as_view(), name='public_recipes'),
    path('personal', views.PersonalRecipeList.as_view(), name='personal_recipes'),
]
