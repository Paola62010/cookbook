from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    category_image = models.ImageField(upload_to="categories", blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipe_posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    servings = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    recipe_image = models.ImageField(upload_to="recipes", blank=True)
    public = models.BooleanField(default=False)
    favourites = models.ManyToManyField(User, blank=True, related_name="recipe_favourites")
    likes = models.ManyToManyField(User, related_name="recipe_likes", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")

    def __str__(self):
        return self.name


class Step(models.Model):
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_steps")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
