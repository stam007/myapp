# Generated by Django 2.2.6 on 2019-10-13 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startapp', '0003_auto_20191013_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oders',
            name='Order_Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_name', to='startapp.Product'),
        ),
    ]
