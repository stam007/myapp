from django.contrib.auth.models import User

from rest_framework import serializers
from startapp.models import Details_Commercial,Details_Client,Table,Category,Product,Oders
from rest_framework.response import Response
from django.http import JsonResponse

from django.forms.models import model_to_dict



class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields =  '__all__'


class TableSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Table
        fields =  '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product_for_commercial = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields =  '__all__'
        



class DetailsSerializerCommercial(serializers.ModelSerializer):
   
    class Meta:
        model = Details_Commercial
        fields =  '__all__'



class UserCommercialSerializer(serializers.ModelSerializer):
    details_commercial = DetailsSerializerCommercial(many=False, read_only=True)
    table_for_commercial = TableSerializer(many=True, read_only=True)
    category_for_commercial = CategorySerializer(many=True, read_only=True)
  
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name','last_name','details_commercial','table_for_commercial','category_for_commercial')
        extra_kwargs ={'password':{'write_only': True , 'required':True}}

    def create(self, validated_data):
          
           user=User.objects.create_user(**validated_data)
           
           return user



class DetailsSerializerClient(serializers.ModelSerializer):
   
    class Meta:
        model = Details_Client
        fields =  '__all__'



class UserClientSerializer(serializers.ModelSerializer):
    details_client = DetailsSerializerClient(many=False, read_only=True)
    
    class Meta:
        model = User
        #fields =  '__all__'
        fields = ('id', 'username', 'email', 'password','first_name','last_name','details_client')
        extra_kwargs ={'password':{'write_only': True , 'required':True}}

    def create(self, validated_data):
          
           user=User.objects.create_user(**validated_data)
           
           return user           

class OrdersSerializer(serializers.ModelSerializer):
    """order_for_commercial = UserCommercialSerializer(many=True, read_only=True)
    order_for_table = TableSerializer(many=True, read_only=True)
    order_for_product = ProductSerializer(many=True, read_only=True)
    order_for_client = UserClientSerializer(many=True, read_only=True)"""
    
    
   

    class Meta:
        model = Oders
        fields =  '__all__'

    Order_Product = ProductSerializer(read_only=True)
    

   
