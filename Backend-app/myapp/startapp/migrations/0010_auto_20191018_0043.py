# Generated by Django 2.2.6 on 2019-10-17 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startapp', '0009_auto_20191018_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oders',
            name='Order_Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_for_product', to='startapp.Product'),
        ),
    ]
