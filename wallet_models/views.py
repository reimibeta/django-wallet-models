from django.shortcuts import render

# Create your views here.
# pip install git+https://github.com/django/django.git
# pip3 install git + ssh: // git @ github.com / wallet_project_web.git
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_utils.pagination import StandardResultsSetPagination

from wallet_models.class_models.wallet import Wallet
from wallet_models.serializers import WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.order_by('-id').all()
    pagination_class = StandardResultsSetPagination
    serializer_class = WalletSerializer
