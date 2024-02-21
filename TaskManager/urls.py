"""
URL configuration for TaskManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from todo import views
from rest_framework import routers
from pizzaria.views import  OrderViewSet, PizzaViewSet, ToppingViewSet,BoxViewSet

router = routers.DefaultRouter()

router.register('tasks', views.ToDoViewSet, 'task')
#pizzaria  app urls

router.register("orders", OrderViewSet, "orders")
router.register("pizzas", PizzaViewSet, "pizzas")
router.register("toppings", ToppingViewSet, "toppings")
router.register("boxs", BoxViewSet, "boxs")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/upload/', views.csv_upload, name='csv_upload'),  # Define URL pattern for file upload
    #pizzaria apps
    path("pizzaria/", include(router.urls))

]