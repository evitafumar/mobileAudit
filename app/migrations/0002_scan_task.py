# Generated by Django 3.1.5 on 2021-01-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='task',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
