from django.urls import path
from . import views

app_name = 'magic_circle'

urlpatterns = [
    path('showall/',views.showall, name='showall')
]