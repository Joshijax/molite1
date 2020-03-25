# Generated by Django 3.0.3 on 2020-03-20 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import moborise.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moborise', '0003_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilPicx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=moborise.models.user_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profilePicx', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
