# Generated by Django 3.0.5 on 2020-05-11 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0008_technology_code_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='organizations', through='tenants.OrganizationMembership', to='tenants.Tenant'),
        ),
    ]