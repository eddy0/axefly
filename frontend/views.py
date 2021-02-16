from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

# Create your views here.
from frontend.models import Login
from frontend.serializers import LoginSerializer


def index(request):
    return HttpResponse('<h1>this is header</h1>')


class LoginView(generics.ListAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
