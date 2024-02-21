from django.db import models
import uuid

#One-to-many(ForeignKey):a Pizza is associated with exactly one Order
#Order can have more than one Pizza

class Order(models.Model):
    # In this example, I'll use UUIDs for primary keys
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    customer = models.CharField(max_length=256, blank=False, null=False)
    address = models.CharField(max_length=512, blank=True, null=False)

#One-to-one a Pizza has exactly one Box,and each Box belongs to one Pizza.
class Box(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    color = models.CharField(max_length=32, default="white", blank=False, null=False)

#Many-to-many a Pizza can have more than one Topping
# a single Topping can be on more than one Pizza.
class Topping(models.Model):
    name = models.CharField(primary_key=True,max_length=64)


class Pizza(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    # related_name="pizzas":This attribute is used in the ForeignKey field that references
    # #the "pizzaria.Order" model.It specifies the name of the reverse relation from the Order model
    # back to the Pizza model. In this case, it indicates that each Order object
    # will have a reverse relation named "pizzas", which can be used to access all Pizza objects
    # related to that order.

    order = models.ForeignKey(
        "pizzaria.Order",
        on_delete=models.CASCADE,
        related_name="pizzas",
        null=False
    )

    box = models.OneToOneField(
        "pizzaria.Box",
        on_delete=models.SET_NULL,
        related_name="contents",
        null=True
    )

    toppings = models.ManyToManyField(
        "pizzaria.Topping",
        related_name='+'
    )