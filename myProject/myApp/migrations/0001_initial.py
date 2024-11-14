# Generated by Django 5.1.2 on 2024-11-12 06:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MonHoc',
            fields=[
                ('ma_mh', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ten_mh', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lop',
            fields=[
                ('ma_lop', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ten_lop', models.CharField(max_length=100)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HocVien',
            fields=[
                ('ma_hv', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('ma_lop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.lop')),
            ],
        ),
        migrations.CreateModel(
            name='Diem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoc_ki', models.IntegerField(choices=[(1, 'Học kỳ 1'), (2, 'Học kỳ 2')])),
                ('diem', models.FloatField()),
                ('ma_hv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.hocvien')),
                ('ma_lop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.lop')),
                ('ma_mh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.monhoc')),
            ],
        ),
    ]