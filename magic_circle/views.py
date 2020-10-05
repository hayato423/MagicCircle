from magic_circle.forms import ImageForm
from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm

import base64
import cv2
import numpy as np
# Create your views here.

def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'magic_circle/showall.html',context)


def upload(request):
    if request.method == "POST":
        data = request.POST['picture'].split(',')
        print(data[1])
        img_base64 = data[1]
        img_binary = base64.b64decode(img_base64)
        jpg = np.frombuffer(img_binary,dtype=np.uint8)
        image_file = 'decode.jpg'
        img = cv2.imdecode(jpg,cv2.IMREAD_COLOR)
        cv2.imshow('window title',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return render(request,'magic_circle/upload.html')