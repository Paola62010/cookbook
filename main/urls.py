from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('public/<slug:slug>', views.PublicRecipeList.as_view(), name='public_recipes'),
    path('personal/<slug:slug>', views.PersonalRecipeList.as_view(), name='personal_recipes'),
]
