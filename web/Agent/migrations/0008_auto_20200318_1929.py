# Generated by Django 3.0.3 on 2020-03-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0007_auto_20200318_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentuploads',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
