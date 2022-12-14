# Generated by Django 3.0.5 on 2020-04-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRApp', '0003_auto_20200428_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='abstract',
            field=models.CharField(default='1', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='duration',
            field=models.CharField(default='5 Days / 6 Nights', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='itenary_titles',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
    ]
