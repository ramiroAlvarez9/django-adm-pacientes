# Generated by Django 2.2.12 on 2021-05-21 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_auto_20210521_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.BigIntegerField(),
        ),
    ]
