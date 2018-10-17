# Generated by Django 2.0.7 on 2018-07-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.CharField(choices=[('u', 'units'), ('oz', 'oz'), ('g', 'g')], default='g', max_length=2),
        ),
    ]
