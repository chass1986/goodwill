# Generated by Django 3.2.13 on 2022-06-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_territories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='territories',
            name='population',
            field=models.BigIntegerField(blank=None, null=True),
        ),
    ]
