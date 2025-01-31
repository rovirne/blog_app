from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Message(models.Model):
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    content = models.TextField(max_length = 256,blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    replies = models.ForeignKey('self', on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self): 
        return self.content


class CustomUser(AbstractUser):
    username = models.CharField(max_length=25, unique=True, blank=False)
    tag = models.SlugField(max_length=25, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    first_name = None
    last_name = None


    def save(self, *args, **kwargs): 
        if not self.tag: 
            self.tag = slugify(self.username)
        super().save(*args,**kwargs)

    def __str__(self): 
        return self.username 
    
    