from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('public/<slug:slug>', views.PublicRecipeList.as_view(), name='public_recipes'),
    path('personal/<slug:slug>', views.PersonalRecipeList.as_view(), name='personal_recipes'),
    path('recipe/<slug:slug>/<int:id>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/<int:id>', views.RecipeLike.as_view(), name='recipe_like'),
    path('favourite/<slug:slug>/<int:id>', views.RecipeFavourite.as_view(), name='recipe_favourite'),
    path('favourites', views.FavouritesList.as_view(), name='favourites'),
    path('create_recipe', views.CreateRecipe.as_view(), name='create_recipe'),
    path('upate_recipe/<int:pk>', views.UpdateRecipe.as_view(), name='update_recipe'),
    path('delete_recipe/<int:id>', views.DeleteRecipe.as_view(), name='delete_recipe'),
    path('search_results', views.SearchResults.as_view(), name='search_results'),
]
