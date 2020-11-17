# Generated by Django 3.1.3 on 2020-11-16 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreApellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('tratamiento', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
    ]