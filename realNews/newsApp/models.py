from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    category_image=models.ImageField(upload_to='img/')
    
    class meta:
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.title
    
class Article(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='img/')
    content=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name_plural='Article'
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    comment=models.TextField()
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.comment
    