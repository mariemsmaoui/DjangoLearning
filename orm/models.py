from django.db import models
from django.utils import timezone

#proxy
class BooksContent(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

class BooksOrder(BooksContent):
    class Meta:
        proxy=True
        ordering=['created']
    def created_on(self):
        return timezone.now()
        self.created




#Multi table inheritance

class Books(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
class ISBN(Books):
    ISBN = models.TextField()






#abstarct mdoel

class BaseItem(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract= True
        ordering=['title']
        app_label = 'orm'
class ItemA(BaseItem):
    content = models.TextField()

    class Meta:
        ordering=['-created']
        app_label = 'orm'


class ItemB(BaseItem):
    content = models.FileField(upload_to='files')


class ItemC(BaseItem):
    content = models.FileField(upload_to='images')


class ItemD(BaseItem):
    slug = models.SlugField(max_length=255, unique=True)