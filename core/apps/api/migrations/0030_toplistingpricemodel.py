# Generated by Django 5.1.3 on 2025-07-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_listingmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToplistingpriceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('day', models.CharField(help_text='7', max_length=255, verbose_name='Kun')),
                ('price', models.CharField(blank=True, max_length=100, null=True, verbose_name='Narx')),
            ],
            options={
                'verbose_name': 'ToplistingpriceModel',
                'verbose_name_plural': 'ToplistingpriceModels',
                'db_table': 'TopListingPrice',
            },
        ),
    ]
