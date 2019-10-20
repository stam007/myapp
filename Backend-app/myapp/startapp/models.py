from django.db import models
from django.contrib.auth.models import User


from django.core.validators import MinLengthValidator
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import JSONField



class Details_Commercial(models.Model):
    CommercialDetails = models.OneToOneField(User, related_name='details_commercial', on_delete=models.CASCADE)
    Picture = models.TextField(null=True,blank=True,default=None)
    Phone = models.CharField('Phone Number', max_length=8, validators=[MinLengthValidator(8)], unique= True,blank=True, null=True)
    Location = models.TextField(null=True,blank=True)
    More_Info = models.TextField(null=True,blank=True,default=None)
    Name_Commercial_Shop = models.TextField(null=True,blank=True,default=None)
    Account_Status = models.BooleanField(default=False,blank=True,null=True)





class Details_Client(models.Model):
    ClientDetails = models.OneToOneField(User, related_name='details_client', on_delete=models.CASCADE)
    Picture = models.TextField(null=True,blank=True,default=None)




class Table(models.Model):
    
    Table_Commercial =models.ForeignKey(User, related_name='table_for_commercial',on_delete=models.CASCADE)
    Number_Table = models.IntegerField(blank=True,null=True)
class Category(models.Model):
    
    Category_Commercial =models.ForeignKey(User, related_name='category_for_commercial',on_delete=models.CASCADE)
    Category_Name =  models.TextField(null=True,blank=True,default=None)
class Product(models.Model):
    
    Product_Commercial_Category = models.ForeignKey(Category, related_name='product_for_commercial',on_delete=models.CASCADE)
    Product_Name =  models.TextField(null=True,blank=True,default=None)
    More_Info =  models.TextField(null=True,blank=True,default=None)
    Duration_To_Prepare = models.IntegerField(blank=True,null=True)
    Price = models.IntegerField(blank=True,null=True)
    Video = models.FileField(blank=True, null=True)
    Gif = models.FileField(blank=True, null=True)

    





class Oders(models.Model):
    
    Order_Commercial =models.ForeignKey(User, related_name='order_for_commercial',on_delete=models.CASCADE)
    Order_Table = models.ForeignKey(Table, related_name='order_for_table',on_delete=models.CASCADE)
    Order_Product = models.ForeignKey(Product, related_name='order_for_product',blank=True,null=True,on_delete=models.CASCADE)
    Order_Client = models.ForeignKey(User, related_name='order_for_client',blank=True,null=True,on_delete=models.CASCADE)
    Details_Order =  models.TextField(null=True,blank=True,default=None)
    Quantity = models.IntegerField(blank=True,null=True,default=None)
    Remove = models.BooleanField(default=False,blank=True,null=True)
    Confirm = models.BooleanField(default=False,blank=True,null=True)
    See = models.BooleanField(default=False,blank=True,null=True)



   

