from django.db import models
import uuid

def file_path(_, filename):
    # image.jpg
    extenstion = filename.split('.')[-1]
    unique_id = uuid.uuid4().hex
    new_filename = 'images/'+unique_id+'.'+extenstion
    return  new_filename


class FileModel(models.Model):
    name = models.CharField(max_length=100)

    # file = models.CharField(max_length=100)
    file = models.FileField(upload_to=file_path)