from django.db import models
from django.contrib.auth.models import User


class Priority(models.Model):
    priority_of_note = models.CharField(max_length=256)

class Category(models.Model):
    category_name = models.CharField(max_length=256)
    users = models.ManyToManyField(User)

class Note(models.Model):
    note_date = models.DateField()
    title = models.CharField(max_length=256)
    is_valid = models.BooleanField(default=True, db_column='is_valid')
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='todo/', null=True, blank=True)


    TYPE_CHOICES = [
        ('маловажно', 'Маловажно'),
        ('важно', 'Важно'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)