# Generated by Django 5.1.3 on 2025-06-30 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_listingmodel_bot_user'),
        ('users', '0003_alter_botusersmodel_name_alter_botusersmodel_tg_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('listing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.listingmodel', verbose_name='elon')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='users.botusersmodel')),
            ],
            options={
                'verbose_name': 'FavoriteModel',
                'verbose_name_plural': 'FavoriteModels',
                'db_table': 'favorite',
                'unique_together': {('user', 'listing')},
            },
        ),
    ]
