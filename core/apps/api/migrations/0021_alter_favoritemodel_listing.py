# Generated by Django 5.1.3 on 2025-06-30 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_favoritemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritemodel',
            name='listing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.listingmodel', verbose_name='elon'),
            preserve_default=False,
        ),
    ]
