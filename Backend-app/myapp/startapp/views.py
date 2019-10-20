from django.contrib.auth.models import User
from rest_framework import viewsets,mixins
from .models import Details_Commercial,Details_Client,Table,Category,Product,Oders
from startapp.serializers import UserCommercialSerializer,DetailsSerializerCommercial,DetailsSerializerClient,UserClientSerializer,TableSerializer,CategorySerializer,ProductSerializer,OrdersSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FileUploadParser
from rest_framework import filters
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
import json
from django.forms.models import model_to_dict
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.core import serializers
from django.db import connection
import datetime
from django.http import HttpResponse
from rest_framework import status

from moviepy.editor import *






class UserCommercialViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserCommercialSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        details = Details_Commercial.objects.create(CommercialDetails_id=serializer.data['id'])
        user = User.objects.get(id=serializer.data['id'])
        token = Token.objects.create(user=user)
        return JsonResponse({'User':model_to_dict(user),'Details':model_to_dict(details),'token': token.key})
       
  



class UserDetailCommercialViewSet(viewsets.ModelViewSet):
    
    queryset = Details_Commercial.objects.all()
    serializer_class = DetailsSerializerCommercial












class UserClientViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserClientSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        details = Details_Client.objects.create(ClientDetails_id=serializer.data['id'],Picture=request.data['Picture'])
        user = User.objects.get(id=serializer.data['id'])
        token = Token.objects.create(user=user)
        return JsonResponse({'User':model_to_dict(user),'Details':model_to_dict(details),'token': token.key})
       
  



class UserDetailClientViewSet(viewsets.ModelViewSet):
    
    queryset = Details_Client.objects.all()
    serializer_class = DetailsSerializerClient  



class TabletViewSet(viewsets.ModelViewSet):
   
    queryset = Table.objects.all()
    serializer_class = TableSerializer



class CategoryViewSet(viewsets.ModelViewSet):
   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        

        if(request.data.get('Video')):
            clipd = VideoFileClip(str(serializer.data['Video']),audio=False)

            clip = (VideoFileClip(str(serializer.data['Video']))
              .subclip((0),((clipd.duration)))
              .speedx((clipd.duration/60)*10)
              .resize(0.5))
            clip.write_gif("media/"+str(serializer.data['id'])+".gif", fps=1, fuzz=0)

            Product.objects.filter(id=serializer.data['id']).update(Gif=str(serializer.data['id'])+".gif")

            obj = Product.objects.get(id=serializer.data['id'])

            serialized_object = serializers.serialize('python', [obj])
            serialized_object[0]['fields']['id']=serializer.data['id']
            serialized_object[0]['fields']['Video']='http://127.0.0.1:8000/media/'+str(serialized_object[0]['fields']['Video'])
            serialized_object[0]['fields']['Gif']='http://127.0.0.1:8000/media/'+str(serialized_object[0]['fields']['Gif'])
            serialized_object=serialized_object[0]['fields']

     
       
            headers = self.get_success_headers(serialized_object)


            return Response(serialized_object, status=status.HTTP_201_CREATED,headers=headers)  




            

      

            


        

        return Response(serializer.data)


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        clipd = VideoFileClip(str(serializer.data['Video']),audio=False)

        clip = (VideoFileClip(str(serializer.data['Video']))
          .subclip((0),((clipd.duration)))
          .speedx((clipd.duration/60)*10)
          .resize(0.5))
        clip.write_gif("media/"+str(serializer.data['id'])+".gif", fps=1, fuzz=0)

        Product.objects.filter(id=serializer.data['id']).update(Gif=str(serializer.data['id'])+".gif")

        obj = Product.objects.get(id=serializer.data['id'])

        serialized_object = serializers.serialize('python', [obj])
        serialized_object[0]['fields']['id']=serializer.data['id']
        serialized_object[0]['fields']['Video']='http://127.0.0.1:8000/media/'+str(serialized_object[0]['fields']['Video'])
        serialized_object[0]['fields']['Gif']='http://127.0.0.1:8000/media/'+str(serialized_object[0]['fields']['Gif'])

        serialized_object=serialized_object[0]['fields']
       
        headers = self.get_success_headers(serialized_object)


        return Response(serialized_object, status=status.HTTP_201_CREATED,headers=headers)  




class OrdersViewSet(viewsets.ModelViewSet):
   
    queryset = Oders.objects.all().order_by('id').reverse()
    serializer_class = OrdersSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Order_Commercial','Remove']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)

        Oders.objects.create(Order_Product_id=request.data['Order_Product'],Order_Commercial_id=request.data['Order_Commercial'],Order_Table_id=request.data['Order_Table'],Quantity=request.data['Quantity'],Order_Client_id=request.data['Order_Client'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    





@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def LoginCommercial(request):
    
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    user = User.objects.get(id=user.id)
    details = Details_Commercial.objects.get(CommercialDetails_id=user.id)
    return JsonResponse({'User':model_to_dict(user),'Details':model_to_dict(details),'token': token.key})    

      

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def LoginClient(request):
    
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    user = User.objects.get(id=user.id)
    details = Details_Client.objects.get(ClientDetails_id=user.id)
    return JsonResponse({'User':model_to_dict(user),'Details':model_to_dict(details),'token': token.key})       