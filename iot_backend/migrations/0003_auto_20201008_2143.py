# Generated by Django 3.1.2 on 2020-10-08 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iot_backend', '0002_auto_20201008_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot_backend.device'),
        ),
    ]
