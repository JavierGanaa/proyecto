# Generated by Django 4.2.5 on 2023-11-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=30)),
            ],
        ),
    ]
