# Generated by Django 5.0.6 on 2024-07-23 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]