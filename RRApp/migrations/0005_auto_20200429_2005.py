# Generated by Django 3.0.5 on 2020-04-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRApp', '0004_auto_20200429_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]