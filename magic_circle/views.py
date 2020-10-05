from magic_circle.forms import ImageForm
from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm
# Create your views here.

def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'magic_circle/showall.html',context)


def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('magic_circle:showall')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request,'magic_circle/upload.html',context)