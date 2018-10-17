import datetime

def calcQuan(full_quantity, current_quantity):
    quantityPercentage =  float(current_quantity) / float(full_quantity)
    quantityPercentage = round(quantityPercentage * 100, 2)
    return quantityPercentage

def calcPricePerQuan(full_quantity, price):
    pricePerQuantity = float(price) / float(full_quantity)
    pricePerQuantity = round(pricePerQuantity, 2)
    return pricePerQuantity

def calcAeoo(date, aeoo_int):
    #takes a queryset date as 'date' argument
    #add optional arg later for freedom or iso format?
    date = str(date)
    date_object = datetime.datetime.strptime(date, '%Y-%m-%d')
    aeoo_date = date_object + datetime.timedelta(days=aeoo_int)
    aeoo_date = aeoo_date.date().isoformat()
    return aeoo_date
