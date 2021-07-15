from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
# 여기에 data table 만들기

class Category(models.Model):
    name= models.CharField(max_length=50, unique=True)
    slug= models.SlugField(max_length=200, unique=True, allow_unicode=True)
    class Meta:
        verbose_name_plural= 'Categories'

class Post(models.Model):
    title= models.CharField(max_length=30)
    content= models.TextField()

    head_image= models.ImageField(upload_to= 'blog/images/%Y/%m/%d/', blank= True)
    file_upload= models.FileField(upload_to= 'blog/files/%Y/%m/%d/', blank= True)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    #author= models.ForeignKey(User, on_delete=models.CASCADE)   #ForeignKey-> DB 용어, models.CASCADE-> author 지우면 같이 지워지게!
    author= models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    category= models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'[{self.pk}]    {self.title} :: {self.author}'   #pk(primary key) -> id

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    #파일 이름을 가져오는 함수
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    #파일 확장자를 가져오는 함수
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]