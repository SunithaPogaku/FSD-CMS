# Generated by Django 4.0.4 on 2022-07-29 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='Some string', max_length=30, unique=True)),
                ('lastName', models.CharField(default='Some string', max_length=30, unique=True)),
                ('username', models.CharField(default='Some string', max_length=30, unique=True)),
                ('DOB', models.DateField()),
                ('email', models.CharField(default='Some string', max_length=30, unique=True)),
                ('password', models.CharField(default='Some string', max_length=30)),
                ('password2', models.CharField(default='Some string', max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Regform',
        ),
    ]
