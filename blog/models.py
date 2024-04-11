from django.db import models
from config.base_models import BaseModel
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class PostTag(BaseModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='blog/posts/')
    body = RichTextField()
    tags = models.ManyToManyField(PostTag)

    is_published = models.BooleanField(default=True)
    is_advertised = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    message = models.TextField()

    def __str__(self):
        return self.name
