from venv import logger

from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissons import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer
from .models import Women, Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


# Create your views here.
def home(request):
    return HttpResponse(f"<mark> Hello</mark>, My home <hr> "
                        f"Request method: <b style='color:green;'>{request.method}</b>")


def home2(request):
    import random
    a = random.randint(1, 100)
    b = random.randint(100, 1000)
    c = a + b
    return HttpResponse(f"Random: {a} + {b} = {c} ")


def calc(request):
    a = 10
    b = 3
    c = a + b
    return HttpResponse(f" {a} + {b} = {c} ")


def calc_int(request, number):
    a = 10
    b = 3
    c = a + b + number
    return HttpResponse(f" {a} + {b} + {number} = {c} ")


def get_data(request, text):
    context = {
        "vorisxon": "Salom men Vorisxon yoshim 22 da",
        "muhammad": "Salom men Muhammad yoshim 24 da"
    }
    return HttpResponse(context.get(text, "Kechirasiz bunaqa ma'lumot mavjud emas"))



class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication,)



class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)