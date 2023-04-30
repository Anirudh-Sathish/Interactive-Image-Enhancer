from django.shortcuts import render, redirect
from .models import ImageModel


# Create your views here.
def home(request):
    if request.method == "POST":
        # print(request.FILES["inputImg"])
        Img = request.FILES["inputImg"]
        name = "amit"
        inputImg = ImageModel(name=name, inputImg=Img)
        inputImg.save()
        outputImg = "efge"
        context = {
            "inputImg": inputImg,
            "outputImg": outputImg,
        }
        return render(request, "output.html", context)
    return render(request, "index.html")


def output(request):
    return render(request, "output.html")


def output2(request):
    return render(request, "output2.html")
