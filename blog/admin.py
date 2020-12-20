from django.contrib import admin
from blog.models import Post,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','created','updated','status']
    list_filter=['publish','status','author']
    search_fields=['title','body']
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=['author']
    ordering=['status','publish']
    date_hierarchy='publish'
class CommentAdmin(admin.ModelAdmin):
    list_display=['post','name','email','body','created','updated','active']
    list_filter=['active','created','updated']
    search_fields=['name','email','body']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
