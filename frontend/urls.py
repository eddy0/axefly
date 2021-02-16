
from django.urls import path, include
from . import views
from .views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='index'),
]
