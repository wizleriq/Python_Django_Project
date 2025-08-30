from django.urls import path, include
from .views import ProductViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'users', UserViewSet, basename='users' )

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token)
]

# urlpattern = [
#     path('api/', ProductViewSet.as_view(), name='product')
# ]