# Generated by Django 3.2.13 on 2022-11-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0002_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]