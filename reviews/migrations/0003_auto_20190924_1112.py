# Generated by Django 2.2.5 on 2019-09-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_reviews_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Review'},
        ),
        migrations.AddField(
            model_name='reviews',
            name='poster',
            field=models.ImageField(blank=True, upload_to='possters/'),
        ),
    ]