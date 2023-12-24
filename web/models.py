from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category_type = models.CharField(max_length=255)

    def __str__(self):
        return self.category_type


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos/")
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.user.username} - {self.caption}"


Note = None


class Note(models.Model):
    note_date = models.DateField(default=date.today)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_valid = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="todo/", null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.category}"
