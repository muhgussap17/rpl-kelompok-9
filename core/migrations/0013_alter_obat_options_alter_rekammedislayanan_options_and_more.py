# Generated by Django 5.2.1 on 2025-05-30 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_rekammedis_layanan_atau_tindakan_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='obat',
            options={'ordering': ['nama'], 'verbose_name_plural': 'Master Data Obat'},
        ),
        migrations.AlterModelOptions(
            name='rekammedislayanan',
            options={'verbose_name': 'Layanan dalam Rekam Medis', 'verbose_name_plural': 'Tambahkan Layanan'},
        ),
        migrations.AlterModelOptions(
            name='rekammedisobat',
            options={'ordering': ['rekam_medis', 'obat'], 'verbose_name': 'Obat dalam Rekam Medis', 'verbose_name_plural': 'Tambahkan Obat'},
        ),
        migrations.AlterModelOptions(
            name='rekammedistindakan',
            options={'verbose_name': 'Tindakan dalam Rekam Medis', 'verbose_name_plural': 'Tambahkan Tindakan'},
        ),
        migrations.AlterModelOptions(
            name='rekammedisvaksin',
            options={'verbose_name': 'Vaksin dalam Rekam Medis', 'verbose_name_plural': 'Tambahkan Vaksin'},
        ),
        migrations.AlterField(
            model_name='obat',
            name='dosis_nilai',
            field=models.PositiveIntegerField(default=1, help_text='Contoh: 500, 5, dll'),
        ),
        migrations.AlterField(
            model_name='obat',
            name='dosis_satuan',
            field=models.CharField(choices=[('g', 'Gram'), ('mg', 'Miligram'), ('ml', 'Mililiter'), ('IU', 'IU'), ('tablet', 'Tablet'), ('kapsul', 'Kapsul'), ('unit', 'Unit'), ('cc', 'cc'), ('ampul', 'Ampul'), ('tetes', 'Tetes')], max_length=20),
        ),
        migrations.AlterField(
            model_name='obat',
            name='keterangan',
            field=models.TextField(blank=True, help_text='Contoh: Aturan pakai, efek samping, dll', null=True),
        ),
        migrations.AlterField(
            model_name='rekammedisobat',
            name='catatan',
            field=models.CharField(blank=True, help_text='Catatan tambahan seperti cara minum, waktu, dll', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rekammedisobat',
            name='jumlah',
            field=models.PositiveIntegerField(default=1, help_text='Jumlah unit yang diberikan (tidak boleh nol)'),
        ),
        migrations.AlterField(
            model_name='rekammedisobat',
            name='obat',
            field=models.ForeignKey(help_text='Obat yang diberikan kepada pasien', on_delete=django.db.models.deletion.PROTECT, to='core.obat'),
        ),
    ]
