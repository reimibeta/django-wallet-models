from django.conf.urls import url
from django.urls import path, include
from wallet_models import views
from rest_framework import routers

router = routers.DefaultRouter()
""" Product supply api """
router.register('wallet', views.WalletViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
