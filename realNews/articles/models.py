from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver


def upload_location(instance, filename, **kwargs):
    file_path = 'articles/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path

class Article(models.Model):
    title=models.CharField(max_length=300, null=False, blank=False)
    body = models.TextField(max_length=5000, null=False, blank=False)
    image=models.ImageField(upload_to=upload_location, null=False, blank=False)
    date_published=models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated=models.DateTimeField(auto_now=True, verbose_name="date updated")
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)
    
    class meta:
        verbose_name_plural='Articles'
        
    def __str__(self):
        return self.title

@receiver(post_delete, sender=Article)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
    
def pre_save_article_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_article_receiver, sender=Article)

class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    comment=models.TextField()
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.comment
    
class Category(models.Model):
    title=models.CharField(max_length=100)
    category_image=models.ImageField(upload_to='img/')
    
    class meta:
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.title       