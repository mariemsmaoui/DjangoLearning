from django.db import models

# Create your models here.
class ToDo(models.Model):
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=500)
    completed=models.BooleanField(default="False")

    def __str__(self):
        return self.title
       # return self.description


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.title