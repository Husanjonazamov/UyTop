# Generated by Django 5.1.3 on 2025-06-28 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_buildingmaterialmodel_listingmodel_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingmodel',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.buildingmaterialmodel', verbose_name='Qurilish Materiallari'),
        ),
    ]
