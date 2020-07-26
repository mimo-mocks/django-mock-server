# Generated by Django 3.0.5 on 2020-07-25 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocks', '0009_project_tenants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='endpoints', to='mocks.Category'),
        ),
        migrations.AlterField(
            model_name='headertype',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='httpverb',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
