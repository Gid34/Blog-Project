from django.db import models
from django.conf import settings #Use the auth_user model from Django
from django.contrib.auth.models import User
from django.shortcuts import reverse #New Line
from datetime import datetime


# CATEGORY_CHOICES = (
#     ('JP', 'Japan'),
#     ('AU', 'Australia'),
#     ('DK', 'Denmark')
# )


COUNTRY_CHOICES = (
    ('JP', 'Japan'),
    ('AU', 'Australia'),
    ('DK', 'Denmark')
)

LABEL_CHOICES = (
    ('F', 'Free'),
    ('P', 'Paid')
)


# Create your models here.

class Post(models.Model):
    author_id = models.ForeignKey(User, on_delete = models.CASCADE) 
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 1000000)
    created_at = models.DateTimeField(default = datetime.now, blank=True)

#Destination
class Destination(models.Model):
    name = models.CharField(max_length=100)
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    price = models.FloatField(blank=True, null=True) #Some places are free
    discount_price = models.FloatField(blank=True, null=True)
    
  
    def __str__(self):
        return self.name

    #This code is complete
    def get_absolute_url(self):
        return reverse("myapp:destinations", kwargs={
            'slug': self.slug
        })

    #WORK ON THESE BELOW
    # def get_req_add_to_log(self):
    #     return reverse("core:add-to-cart", kwargs={
    #     'slug': self.slug
    #     })

    #WORK ON THESE BELOW
    # def get_req_remove_from_log(self):
    #     return reverse("core:remove-from-cart", kwargs={
    #         'slug': self.slug
    #     })




#Able to create Destination Object via admin

#DestinationLog - Relationship Between Trip and Destination
# class OrderItem(models.Model):
#     pass

#Multiple destination logs are stored in a trip
# class Trip(models.Model):
#     pass