from django.shortcuts import render
from .models import Image
# Create your views here.

def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'magic_circle/showall.html',context)