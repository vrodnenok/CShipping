from django.contrib import admin
from models import Vessels, Operations, Ports, Voyages
from blog.models import Post
from django.contrib import auth

admin.site.register(Vessels)
admin.site.register(Post)
admin.site.register(Operations)
admin.site.register(Ports)
admin.site.register(Voyages)