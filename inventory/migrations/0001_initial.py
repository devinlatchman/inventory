# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-14 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatesUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('generic_item_id', models.PositiveIntegerField()),
                ('full_quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('current_quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity_percentage', models.DecimalField(decimal_places=2, default='100', max_digits=5)),
                ('expiry_date', models.DateField()),
                ('aeoo_bool', models.BooleanField(help_text="Set to true if item will expire quicker after it's opened, ex. Meat")),
                ('aeoo_int', models.PositiveIntegerField(blank=True, help_text='If item is an AEOO item, this is the number of days it will expire after being opened')),
                ('pack_bool', models.BooleanField(help_text='Set to true if item will need a QR code generated for each unit for effective tracking')),
                ('pack_int', models.PositiveIntegerField(blank=True, help_text='If item is pack item, this is the number of required QR codes for this item')),
                ('aeoo_date', models.DateField(blank=True)),
                ('barcode', models.CharField(max_length=12)),
                ('indv_barcode', models.CharField(blank=True, help_text='Enter if units within an item are labeled for resale, ex. Beer', max_length=12)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('price_per_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('item_alert', models.CharField(choices=[('0', "Don't alert"), ('1', 'Optional alert'), ('2', 'Alert always')], default='2', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.CharField(max_length=70)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
            ],
        ),
        migrations.AddField(
            model_name='datesused',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item'),
        ),
    ]
