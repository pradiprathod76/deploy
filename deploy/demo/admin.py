from django.contrib import admin
from .models import Post,Category,Audio,Pic
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Audio)
admin.site.register(Pic)