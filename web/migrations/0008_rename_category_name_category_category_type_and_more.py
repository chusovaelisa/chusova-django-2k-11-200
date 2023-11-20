# Generated by Django 4.2.7 on 2023-11-20 16:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0007_note_content"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="category_name",
            new_name="category_type",
        ),
        migrations.RemoveField(
            model_name="category",
            name="users",
        ),
        migrations.DeleteModel(
            name="UserCategory",
        ),
    ]
