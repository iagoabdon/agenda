# Generated by Django 5.1.3 on 2024-12-11 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_category_contact_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category',
            new_name='name',
        ),
    ]
