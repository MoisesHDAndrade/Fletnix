# Generated by Django 3.1.2 on 2021-02-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20210104_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
