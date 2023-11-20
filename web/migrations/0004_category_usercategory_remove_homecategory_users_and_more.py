# Generated by Django 4.2.7 on 2023-11-20 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0003_rename_category_familycategory_remove_note_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('home', 'Дом'), ('work', 'Работа'), ('family', 'Семья'), ('shop', 'Магазин')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='homecategory',
            name='users',
        ),
        migrations.RemoveField(
            model_name='shopcategory',
            name='users',
        ),
        migrations.RemoveField(
            model_name='workcategory',
            name='users',
        ),
        migrations.RemoveField(
            model_name='note',
            name='family_category',
        ),
        migrations.RemoveField(
            model_name='note',
            name='home_category',
        ),
        migrations.RemoveField(
            model_name='note',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='note',
            name='shop_category',
        ),
        migrations.RemoveField(
            model_name='note',
            name='work_category',
        ),
        migrations.DeleteModel(
            name='FamilyCategory',
        ),
        migrations.DeleteModel(
            name='HomeCategory',
        ),
        migrations.DeleteModel(
            name='Priority',
        ),
        migrations.DeleteModel(
            name='ShopCategory',
        ),
        migrations.DeleteModel(
            name='WorkCategory',
        ),
        migrations.AddField(
            model_name='category',
            name='users',
            field=models.ManyToManyField(through='web.UserCategory', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='web.category'),
        ),
    ]
