from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
class Blog(models.Model):

    author = models.ForeignKey(get_user_model(), null = True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to="photos", max_length=None, null = True)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title