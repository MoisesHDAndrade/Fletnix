# Generated by Django 3.1.2 on 2021-04-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20210422_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='certification',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='relevance',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
