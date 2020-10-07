from sys import flags
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
        img_base64 = data[1]
        img_binary = base64.b64decode(img_base64)
        jpg = np.frombuffer(img_binary,dtype=np.uint8)
        img = cv2.imdecode(jpg,cv2.IMREAD_COLOR)
        ImageProcessing(img)
    return render(request,'magic_circle/upload.html')


def ImageProcessing(img):
    circle_img_path = "D:\DjangoProject\ShibaLab\media\images\circle.png"
    circle_img = cv2.imread(circle_img_path,0)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    diff_img = cv2.absdiff(img_grey,circle_img)
    diff_img = np.float32(diff_img)
    #Harrisのコーナー検出
    dst = cv2.cornerHarris(diff_img,2,3,0.04)
    dst = cv2.dilate(dst,None)
    corner_num = np.sum(dst > 0)
    img[dst>0.01*dst.max()] = [0,0,255]

    cv2.imshow('window title',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
