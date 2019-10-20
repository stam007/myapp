from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from rest_framework.authtoken.views import ObtainAuthToken
from .views import UserDetailCommercialViewSet,UserCommercialViewSet,LoginCommercial,LoginClient,UserDetailClientViewSet,UserClientViewSet,TabletViewSet,CategoryViewSet,ProductViewSet,OrdersViewSet


router = routers.DefaultRouter()

router.register(r'userscommercial', UserCommercialViewSet)
router.register(r'userscommercialdetails', UserDetailCommercialViewSet)


router.register(r'usersclient', UserClientViewSet)
router.register(r'usersclientdetails', UserDetailClientViewSet)
router.register(r'table', TabletViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'orders', OrdersViewSet)


urlpatterns = [

    url('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls')),
    #url('auth/', ObtainAuthToken.as_view()),
    path('logincommercial/', LoginCommercial),
    path('loginclient/', LoginClient),



]
