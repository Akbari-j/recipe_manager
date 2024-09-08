from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    instructions = models.TextField()
    cooking_time = models.IntegerField(null=True, blank=True)  # Optional, in minutes
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)  # Optional, for storing recipe images
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
