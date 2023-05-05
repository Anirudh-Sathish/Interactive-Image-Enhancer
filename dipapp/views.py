from django.shortcuts import render, redirect
from .models import ImageModel
import cv2
import copy
from PIL import Image 
from io import BytesIO
import numpy as np 
import os 
from django.core.files.base import ContentFile
from .histEQ import custom_histogram_equalization

# Create your views here.
def home(request):
    if request.method == "POST":
        Img = request.FILES["inputImg"]

        pil_img = Image.open(Img)
        cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_BGR2GRAY)
        
        # modify this later 
        probs = [0.25 , 0.25 , 0.25 , 0.25 ]
        len_proba = len(probs)
        histIm = custom_histogram_equalization(cv_img,probs,len_proba)
        pil_gray_img = Image.fromarray(histIm)


        # save
        buffer = BytesIO()
        pil_gray_img.save(buffer, format='PNG')
        output_img = ContentFile(buffer.getvalue())


        name = "Modified"
        imageSeries1 = ImageModel(name=name, inputImg=Img,outputImg = '')
        imageSeries1.save()

        imageSeries1.outputImg.save('output.png', output_img)

        # context = {
        #     "inputImg": inputImg,
        #     "outputImg": outputImg,
        # }
        # return render(request, "output.html", context)
        return redirect("output", permanent=True, pk=imageSeries1.pk)
    return render(request, "index.html")


def output(request, pk):
    my_object = ImageModel.objects.get(pk=pk)
    print(my_object)
    context = {
        "image_obj": my_object,
    }
    return render(request, "output.html", context)


def output2(request):
    return render(request, "output2.html")
