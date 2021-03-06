# Generated by Django 2.1.1 on 2018-09-12 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreC', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProd', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=70)),
                ('costo', models.CharField(max_length=15)),
                ('disponible', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
            ],
        ),
    ]
