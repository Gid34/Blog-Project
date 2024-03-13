from django.contrib import admin
from .models import *

# Register your models here.
class post_details(admin.ModelAdmin):
    list_display = ("author_id", "id","title", "body", "created_at")

class destination_details(admin.ModelAdmin):
    list_display = ("name", "country","label", "slug", "description", "price", "discount_price", "image")

# admin.site.register(Post)
admin.site.register(Post, post_details)
admin.site.register(Destination, destination_details )