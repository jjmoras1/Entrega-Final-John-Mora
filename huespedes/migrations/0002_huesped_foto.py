# Generated by Django 5.0.6 on 2024-07-24 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huespedes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='huesped',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='huespedes/'),
        ),
    ]
