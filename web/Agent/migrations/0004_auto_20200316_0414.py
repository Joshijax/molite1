# Generated by Django 3.0.3 on 2020-03-16 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0003_agentuploads_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentuploads',
            name='price',
            field=models.IntegerField(),
        ),
    ]
