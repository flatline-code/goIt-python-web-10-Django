# Generated by Django 4.1.7 on 2023-04-09 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='quote',
            new_name='text',
        ),
    ]