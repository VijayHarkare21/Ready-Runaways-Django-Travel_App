# Generated by Django 3.2.4 on 2021-06-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRApp', '0008_remove_destination_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]