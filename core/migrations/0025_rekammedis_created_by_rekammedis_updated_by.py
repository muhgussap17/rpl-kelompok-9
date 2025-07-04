# Generated by Django 5.2.1 on 2025-06-12 15:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_pasien_agama_alter_pasien_golongan_darah_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rekammedis',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rekam_dibuat', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rekammedis',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rekam_diubah', to=settings.AUTH_USER_MODEL),
        ),
    ]
