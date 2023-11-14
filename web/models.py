from django.db import models
from django.contrib.auth.models import User

class Priority(models.Model):
    priority_of_note = models.CharField(max_length=256)

class HomeCategory(models.Model):
    category_name = models.CharField(max_length=256)
    users = models.ManyToManyField(User)

class WorkCategory(models.Model):
    category_name = models.CharField(max_length=256)
    users = models.ManyToManyField(User)

class FamilyCategory(models.Model):
    category_name = models.CharField(max_length=256)
    users = models.ManyToManyField(User)

class ShopCategory(models.Model):
    category_name = models.CharField(max_length=256)
    users = models.ManyToManyField(User)

class Note(models.Model):
    note_date = models.DateField()
    title = models.CharField(max_length=256)
    is_valid = models.BooleanField(default=True, db_column='is_valid')
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, null=True, blank=True)
    home_category = models.ForeignKey(HomeCategory, on_delete=models.PROTECT, null=True, blank=True)
    work_category = models.ForeignKey(WorkCategory, on_delete=models.PROTECT, null=True, blank=True)
    family_category = models.ForeignKey(FamilyCategory, on_delete=models.PROTECT, null=True, blank=True)
    shop_category = models.ForeignKey(ShopCategory, on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='todo/', null=True, blank=True)
