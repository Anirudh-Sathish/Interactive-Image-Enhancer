from django.db import models
import numpy as np 
import cv2 
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.


class ImageModel(models.Model):
    name = models.CharField(max_length=100, default="SOME_STRING")
    inputImg = models.ImageField(upload_to="images")
    outputImg=models.ImageField(upload_to="images/output")

    def __str__(self):
        return self.name
    # def save(self, *args, **kwargs):
        

    #     # open image
    #     pil_img = Image.open(self.inputImg)

    #     # convert the image to array and do some processing
    #     cv_img = np.array(pil_img)
    #     img_output = cv2.cvtColor(cv_img,cv2.COLOR_BGR2GRAY)
    #     # img = get_filtered_image(cv_img, self.action)

    #     # convert back to pil image
    #     im_pil = Image.fromarray(img_output)

    #     # save
    #     buffer = BytesIO()
    #     im_pil.save(buffer, format='png')
    #     image_png = buffer.getvalue()
    #     self.outputImg.save(str(self.outputImg), ContentFile(image_png), save=False)

    #     super().save(*args, **kwargs)
