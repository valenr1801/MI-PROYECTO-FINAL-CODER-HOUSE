# Generated by Django 4.1.3 on 2022-12-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Educación', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('facultad', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=200)),
            ],
        ),
    ]
