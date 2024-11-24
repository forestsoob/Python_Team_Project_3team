# Generated by Django 5.1.3 on 2024-11-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='satisfaction',
            field=models.IntegerField(choices=[(1, 'Bad'), (2, 'Neutral'), (3, 'Good')]),
        ),
    ]
