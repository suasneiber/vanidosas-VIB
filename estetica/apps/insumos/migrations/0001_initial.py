# Generated by Django 3.1.3 on 2020-11-16 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insumos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('cantidad', models.CharField(max_length=3)),
                ('precioCosto', models.CharField(max_length=4)),
                ('precioVenta', models.CharField(max_length=4)),
                ('codigo', models.CharField(max_length=13)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
    ]
