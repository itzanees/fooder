# Generated by Django 5.1.1 on 2024-12-28 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_alter_dish_category_alter_dish_shop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='descritpion',
            new_name='description',
        ),
    ]
