from django.db import models

# Create your models here.


class ImageModel(models.Model):
    name = models.CharField(max_length=100, default="SOME_STRING")
    inputImg = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name
