from django.db import models

# Create your models here.
# 여기에 data table 만들기

class Post(models.Model):
    title= models.CharField(max_length=30)
    content= models.TextField()
    head_image= models.ImageField(upload_to= 'blog/images/%Y/%m/%d/', blank= True)
    file_upload= models.FileField(upload_to= 'blog/files/%Y/%m/%d/', blank= True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'[{self.pk}]    {self.title}'   #pk(primary key) -> id

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'