# Generated by Django 4.2.7 on 2023-11-13 17:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='Priority',
        ),
        migrations.RenameField(
            model_name='priority',
            old_name='type_of_note',
            new_name='priority_of_note',
        ),
        migrations.AddField(
            model_name='category',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='type',
            field=models.CharField(choices=[('маловажно', 'Маловажно'), ('важно', 'Важно')], max_length=20),
        ),
    ]
