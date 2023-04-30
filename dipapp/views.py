from django.shortcuts import render, redirect
from .models import ImageModel


# Create your views here.
def home(request):
    if request.method == "POST":
        Img = request.FILES["inputImg"]
        name = "amit"
        inputImg = ImageModel(name=name, inputImg=Img)
        inputImg.save()
        outputImg = "efge"
        context = {
            "inputImg": inputImg,
            "outputImg": outputImg,
        }
        # return render(request, "output.html", context)
        return redirect("output", permanent=True, pk=inputImg.pk)
    return render(request, "index.html")


def output(request, pk):
    my_object = ImageModel.objects.get(pk=pk)
    print(my_object)
    context = {
        "inputImg": my_object,
        # "outputImg": outputImg,
    }
    return render(request, "output.html", context)


def output2(request):
    return render(request, "output2.html")
