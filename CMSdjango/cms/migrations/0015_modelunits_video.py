# Generated by Django 4.0.4 on 2022-08-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_rename_units_modelunits_alter_modelunits_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelunits',
            name='Video',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
