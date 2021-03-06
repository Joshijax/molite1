# Generated by Django 3.0.3 on 2020-03-29 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moborise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertype',
            name='About',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertype',
            name='Business_Name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertype',
            name='Employment_status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertype',
            name='Facebook_link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertype',
            name='Successfully_trans',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usertype',
            name='img',
            field=models.FileField(default=1, upload_to='gallery/profile/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertype',
            name='phone',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertype',
            name='whatapp_number',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProfilPicx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profilePicx', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
