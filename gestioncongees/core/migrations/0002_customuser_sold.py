# Generated by Django 5.0 on 2023-12-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='sold',
            field=models.IntegerField(default=24, null=True),
        ),
    ]