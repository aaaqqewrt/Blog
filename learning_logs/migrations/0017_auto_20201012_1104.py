# Generated by Django 3.1.2 on 2020-10-12 03:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0016_auto_20201012_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created_date']},
        ),
        migrations.RemoveField(
            model_name='entry',
            name='last_updated_date',
        ),
        migrations.AddField(
            model_name='entry',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entry',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
