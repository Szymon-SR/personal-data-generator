# Generated by Django 3.2.13 on 2022-06-01 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postaddress',
            name='city',
            field=models.TextField(default='Warszawa'),
            preserve_default=False,
        ),
    ]