# Generated by Django 3.1.2 on 2020-10-12 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0012_remove_entry_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
