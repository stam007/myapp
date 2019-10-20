# Generated by Django 2.2.6 on 2019-10-12 13:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.TextField(blank=True, default=None, null=True)),
                ('Category_Commercial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_for_commercial', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_Table', models.IntegerField(blank=True, null=True)),
                ('Table_Commercial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_for_commercial', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.TextField(blank=True, default=None, null=True)),
                ('More_Info', models.TextField(blank=True, default=None, null=True)),
                ('Duration_To_Prepare', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Video', models.FileField(blank=True, null=True, upload_to='')),
                ('Product_Commercial_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_for_commercial', to='startapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Oders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Details_Order', models.TextField(blank=True, default=None, null=True)),
                ('Quantity', models.IntegerField(blank=True, default=None, null=True)),
                ('Order_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_for_client', to=settings.AUTH_USER_MODEL)),
                ('Order_Commercial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_for_commercial', to=settings.AUTH_USER_MODEL)),
                ('Order_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_for_product', to='startapp.Product')),
                ('Order_Table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_for_table', to='startapp.Table')),
            ],
        ),
        migrations.CreateModel(
            name='Details_Commercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.TextField(blank=True, default=None, null=True)),
                ('Phone', models.CharField(blank=True, max_length=8, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Phone Number')),
                ('Location', models.TextField(blank=True, null=True)),
                ('More_Info', models.TextField(blank=True, default=None, null=True)),
                ('Name_Commercial_Shop', models.TextField(blank=True, default=None, null=True)),
                ('Account_Status', models.BooleanField(blank=True, default=False, null=True)),
                ('CommercialDetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details_commercial', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Details_Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.TextField(blank=True, default=None, null=True)),
                ('ClientDetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details_client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]