# Generated by Django 4.2.4 on 2023-08-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-2-2'),
            preserve_default=False,
        ),
    ]
