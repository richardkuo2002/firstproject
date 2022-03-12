# Generated by Django 4.0.3 on 2022-03-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sName', models.CharField(max_length=20)),
                ('sSex', models.CharField(default='M', max_length=2)),
                ('sBirthday', models.DateField()),
                ('sEmail', models.EmailField(blank=True, default='', max_length=50)),
                ('sPhone', models.CharField(blank=True, default='', max_length=20)),
                ('sAddress', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]