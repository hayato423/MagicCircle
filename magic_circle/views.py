from sys import flags
from django.shortcuts import render,redirect
from django.utils import timezone

import base64
import cv2
import numpy as np
import datetime
from .udp_client import udpsend

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
        parameter = get_parameter(img)
        data = ''
        for p in parameter:
            data = data + str(p) + ','
        data = data + str(img_base64)
        udp = udpsend()
        udp.send(data=data)
    return render(request,'magic_circle/upload.html')


def get_parameter(img):
    circle_img_path = "D:\DjangoProject\ShibaLab\media\images\circle.png"
    circle_img = cv2.imread(circle_img_path,0)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    diff_img = cv2.absdiff(img_grey,circle_img)
    diff_img = np.float32(diff_img)
    #Harrisのコーナー検出
    corners = detect_corner(diff_img)
    corners = corners>0.01*corners.max()
    corners_num =  np.count_nonzero(corners==True)

    #直線検出
    lines = detect_lines(diff_img)
    lines_num = 0
    if lines is not None and len(lines) > 0:
        lines_num = len(lines)
    #円検出
    circles = detect_circles(diff_img)
    circles_num = 0
    if circles is not None and len(circles) > 0:
        circles_num = len(circles[0])

    #画像描画
    # img[corners] = [0,0,255]
    # if lines is not None and len(lines) > 0:
    #     for line in lines:
    #         x1, y1, x2, y2 = line[0]
    #         cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    # #円描画
    # if circles is not None and len(circles) > 0:
    #     for (x,y,r) in circles[0]:
    #         x, y, r = int(x), int(y), int(r)
    #         cv2.circle(img,(x,y),r,(255,0,0),2)
    # cv2.imshow('window title',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    lines_num = int(lines_num / 2)
    corners_num = int(corners_num/8 - lines_num)
    parameter = [corners_num, lines_num, circles_num]
    return parameter


def detect_corner(img):
    dst = cv2.cornerHarris(img,blockSize=2,ksize=3,k=0.15)
    dst = cv2.dilate(dst,None)
    return dst


def detect_lines(img):
    img_uint8 = np.uint8(img)
    edges = cv2.Canny(img_uint8,0,0)
    minLineLength = 10
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength,maxLineGap)
    return lines


def detect_circles(img):
    img_uint8 = np.uint8(img)
    edges = cv2.Canny(img_uint8,0,0)
    circles = cv2.HoughCircles(img_uint8,cv2.HOUGH_GRADIENT,dp=2,minDist=50,param1=50,param2=40,minRadius=5,maxRadius=20)
    return circles

