# Generated by Django 3.1.2 on 2020-10-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0015_auto_20201012_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='last_updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]