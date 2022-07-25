from django.db import models
from vle.storage import OverwriteStorage

class Thing(models.Model):
    image = models.ImageField(
        max_length=SOME_CONST, storage=OverwriteStorage(), upload_to=image_path)




    