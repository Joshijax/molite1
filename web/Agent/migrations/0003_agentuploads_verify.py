# Generated by Django 3.0.3 on 2020-03-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0002_auto_20200309_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentuploads',
            name='verify',
            field=models.TextField(default='Not verified', max_length=100),
        ),
    ]
