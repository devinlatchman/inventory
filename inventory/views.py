# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse

from .forms import ItemForm, UseForm, DateUseForm
from .models import Item, DatesUsed
from .calc import calcQuan, calcPricePerQuan

# Create your views here.


#all_items = Item.objects.all()


def index(request):
    all_items = Item.objects.all()
    context = {'all_items': all_items}
    return render(request, 'inventory/index.html', context)

def view(request, Item_id):
    item = Item.objects.get(id=Item_id)
    context = {'item': item}
    return render(request, 'inventory/view.html', context)

def use(request, Item_id):
    item = Item.objects.get(id=Item_id)
    form = UseForm(request.POST)
    dates = list(DatesUsed.objects.filter(item=item))
    if form.is_valid():
        current_quantity = form.cleaned_data['currentQuantity']
        item.current_quantity = current_quantity
        #set non user-variables
        #full_quantity = item.full_quantity
        #item.quantity_percentage = calcQuan(full_quantity, current_quantity)
        new_date = form.cleaned_data['date']
        newDatesUsed = DatesUsed(item=item, date=new_date)
        newDatesUsed.save()
        item.save()
        return redirect('view', Item_id=Item_id)
    context = {'item': item, 'form': form, 'dates': dates}
    return render(request, 'inventory/use.html', context)

def add(request):
    if request.method == 'POST':
        form = ItemForm(data=request.POST)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.save()
            #set non user-variables
            #full_quantity = new_item.full_quantity
            #new_item.current_quantity = full_quantity
            #if new_item.price:
                #price = new_item.price
                #price_per_quantity = calcPricePerQuan(full_quantity, price)            
                #new_item.price_per_quantity = price_per_quantity
            #new_item.save()
            Item_id = new_item.id
            return redirect('view', Item_id=Item_id)
    else:
        form = ItemForm()

    return render(request, 'inventory/add.html', {'form': form})

def edit(request, Item_id):
    instance = get_object_or_404(Item, id=Item_id)
    form = ItemForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('view', Item_id=Item_id)
    return render(request, 'inventory/edit.html', {'form': form})

def delete(request, Item_id):
    item = Item.objects.get(id=Item_id)
    return render(request, 'inventory/delete.html', {'item': item})

def deleteTrue(request, Item_id):
    item = Item.objects.get(id=Item_id)
    item.delete()
    return redirect('index')