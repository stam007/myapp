# Generated by Django 2.2.6 on 2019-10-13 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startapp', '0002_auto_20191013_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Order_Product',
        ),
        migrations.AddField(
            model_name='oders',
            name='Order_Product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_for_product', to='startapp.Product'),
            preserve_default=False,
        ),
    ]
