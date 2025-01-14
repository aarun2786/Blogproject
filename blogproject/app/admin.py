from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Bloger)
class BlogerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','bio_data']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','get_tag','bloger','title','text_content','pub_date','slug','views','is_publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['bloger','post','comment','pub_date']


@admin.register(Tag)
class BlogerAdmin(admin.ModelAdmin):
    list_display = ['tag_name','taged_post']
