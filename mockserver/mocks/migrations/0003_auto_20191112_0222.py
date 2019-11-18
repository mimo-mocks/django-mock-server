# Generated by Django 2.1.11 on 2019-11-12 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '__latest__'),
        ('mocks', '0002_multi_tenancy_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mock',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant'),
        ),
    ]
