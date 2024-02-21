
from .models import ToDo
from rest_framework import serializers

#python manage.py startapp
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
     model= ToDo
     fields = ('id','title', 'description','completed' )
