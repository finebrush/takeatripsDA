from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)

def get_image_filename(instance, filename):
    id = instance.post.id
    return "post_images/%s" % (id)  


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')


                  