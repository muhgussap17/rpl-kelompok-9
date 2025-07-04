# Generated by Django 5.2.1 on 2025-06-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_pasien_jenis_pasien'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rekammedis',
            old_name='catatan_diagnosis',
            new_name='diagnosis',
        ),
        migrations.AddField(
            model_name='rekammedis',
            name='medikamentosa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rekammedis',
            name='non_medikamentosa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rekammedis',
            name='status_pulang',
            field=models.CharField(blank=True, choices=[('berobat_jalan', 'Berobat Jalan'), ('sehat', 'Sehat'), ('rujuk', 'Rujuk')], max_length=20, null=True),
        ),
    ]
