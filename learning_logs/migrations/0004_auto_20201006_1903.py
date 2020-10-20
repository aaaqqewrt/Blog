# Generated by Django 3.1.2 on 2020-10-06 11:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='entry',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
