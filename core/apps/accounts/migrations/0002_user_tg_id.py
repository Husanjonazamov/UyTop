# Generated by Django 5.1.3 on 2025-07-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_id',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
