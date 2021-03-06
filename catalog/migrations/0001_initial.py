# Generated by Django 4.0.1 on 2022-01-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First name of the fighter', max_length=100)),
                ('last_name', models.CharField(help_text='Last name of the fighter', max_length=100)),
                ('nickname', models.CharField(blank=True, help_text='Nickname of the fighter, if exist', max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('start_carrier', models.DateField(blank=True, null=True, verbose_name='Start carrier')),
                ('end_carrier', models.DateField(blank=True, null=True, verbose_name='End carrier')),
                ('end_carrier1', models.DateField(blank=True, null=True, verbose_name='End carrier')),
            ],
        ),
    ]
