from django.contrib import admin
from .models import ToDo

class toDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
# Register your models here.
#model name and admin name
admin.site.register(ToDo,toDoAdmin)

