# Generated by Django 2.2.5 on 2019-09-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20190921_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.CharField(max_length=5),
        ),
    ]
