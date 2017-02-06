# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-26 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('editado_em', models.DateTimeField(auto_now=True)),
                ('categoria', models.CharField(choices=[('Aleatorio', 'Aleatorio'), ('Eletronico', 'Eletronico'), ('Eletrodomestico', 'Eletrodomestico')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('editado_em', models.DateTimeField(auto_now=True)),
                ('quantidade', models.IntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Produto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='balcao',
            name='itens',
            field=models.ManyToManyField(to='app.Item'),
        ),
    ]
