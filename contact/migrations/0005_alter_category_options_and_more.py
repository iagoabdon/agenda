# Generated by Django 5.1.4 on 2024-12-23 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_rename_category_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Category',
            new_name='category',
        ),
    ]
