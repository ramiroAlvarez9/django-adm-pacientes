# Generated by Django 2.2.12 on 2021-04-26 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('sintomas', models.CharField(max_length=200)),
            ],
        ),
    ]
