# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .calc import calcQuan, calcPricePerQuan, calcAeoo

import datetime

# Create your models here.test

class Item(models.Model):
    item_alert_choices = (
        ('0', "Don't alert"),
        ('1', "Optional alert"),
        ('2', "Alert always"),
    )
    unit_choices = (
        ('u', "units"),
        ('oz', "oz"),
        ('g', "g"),
    )
    item_name = models.CharField(max_length=30)
    generic_item_id = models.PositiveIntegerField()
    full_quantity = models.DecimalField(max_digits=5, decimal_places=2)
    current_quantity = models.DecimalField(
        blank=True, 
        null=True, 
        max_digits=5, 
        decimal_places=2
    )
    unit = models.CharField(
        max_length=2,
        choices=unit_choices,
        default='g'
    )
    quantity_percentage = models.DecimalField(
        default='100',
        max_digits=5, 
        decimal_places=2
    )
    expiry_date = models.DateField(
        blank=True,
        null=True,
    )
    aeoo_bool = models.BooleanField(
        help_text="Set to true if item will expire quicker after it's opened, ex. Meat"
    )
    aeoo_int = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text='If item is an AEOO item, this is the number of days it will expire after being opened'
    )
    pack_bool = models.BooleanField(help_text='Set to true if item will need a QR code generated for each unit for effective tracking')
    pack_int = models.PositiveIntegerField( 
        blank=True,
        null=True,
        help_text='If item is pack item, this is the number of required QR codes for this item'
    )
    aeoo_date = models.DateField(blank=True, null=True)
    barcode = models.CharField(max_length=12)
    indv_barcode = models.CharField(
        max_length=12, 
        blank=True,
        help_text='Enter if units within an item are labeled for resale, ex. Beer'
    )
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        blank=True, 
        null=True,)
    price_per_quantity = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        blank=True,
        null=True,)
    item_alert = models.CharField(
        max_length=1,
        choices=item_alert_choices,
        default='2'
    )
    def __str__(self):
        return self.item_name
    
    def save(self, *args, **kwargs):
        full_quantity = self.full_quantity
        if self.price is not None:
            price = self.price
            self.price_per_quantity = calcPricePerQuan(full_quantity, price)
        if self.current_quantity is not None:
            current_quantity = self.current_quantity
            self.quantity_percentage = calcQuan(full_quantity, current_quantity)
        else:
            self.current_quantity = full_quantity
            self.quantity_percentage = calcQuan(full_quantity, self.current_quantity)
        
        if self.aeoo_bool:
            if self.aeoo_int is not None:
                try:
                    DatesUsedList = list(DatesUsed.objects.filter(item=self).order_by('date'))
                    first_date = DatesUsedList[0]
                    aeoo_date = calcAeoo(first_date, self.aeoo_int)
                    self.aeoo_date = aeoo_date
                except:
                    pass


        super().save(*args, **kwargs)

class DatesUsed(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
    


class Recipes(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    recipe = models.CharField(max_length=70)

    def __str__(self):
        return self.recipe


