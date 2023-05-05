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
from .negation import negate_image
from .thresholding import threshold_image
from .contrastenhance import enhance_contrast
import json 

# Create your views here.
def home(request):
    if request.method == "POST":
        Img = request.FILES["inputImg"]
        value=request.POST.get('submit_button')
        print(value)
        pil_img = Image.open(Img)
        cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_BGR2GRAY)

        if(value == "type1"):
            # hist specification
            print("Here")
            probs = [1 , 1 , 1 , 1 ]
            len_proba = len(probs)
            histIm = custom_histogram_equalization(cv_img,probs,len_proba)
            pil_gray_img = Image.fromarray(histIm)
        elif(value == "type2"):
            # negation 
            negated = negate_image(cv_img)
            pil_gray_img = Image.fromarray(negated)
        elif(value == "type3"):
            # thresholding
            t_value = 100
            image_thresholded = threshold_image(cv_img,t_value)
            pil_gray_img = Image.fromarray(image_thresholded)
        elif(value == "type4"):
            # contrast enhancement
            a1 = 3
            b2 = 50
            contrast_enhanced = enhance_contrast(cv_img,a1, b2)
            pil_gray_img = Image.fromarray(contrast_enhanced)

        
        
    
        # probs = [1 , 1 , 1 , 1 ]
        # len_proba = len(probs)
        # histIm = custom_histogram_equalization(cv_img,probs,len_proba)
        # pil_gray_img = Image.fromarray(histIm)


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
