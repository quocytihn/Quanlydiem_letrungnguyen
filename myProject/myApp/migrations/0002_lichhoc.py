# Generated by Django 5.1.2 on 2024-11-25 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LichHoc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ngay_hoc', models.DateField()),
                ('giang_duong', models.CharField(max_length=100)),
                ('ma_lop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.lop')),
                ('ma_mh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.monhoc')),
            ],
        ),
    ]
