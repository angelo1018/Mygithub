# Generated by Django 3.0.3 on 2020-03-01 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robotweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='account',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
