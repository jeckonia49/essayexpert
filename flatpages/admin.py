from django.contrib import admin
from .models import (
    Post, 
    PostComment
)

def mark_is_validated(modeladmin, request, queryset):
    queryset.updatae(is_validated=True)
mark_is_validated.short_decsription="Mark Validated"


def unmark_is_validated(modeladmin, request, queryset):
    queryset.updatae(is_validated=False)
unmark_is_validated.short_decsription="Unmark Validated"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title',"createdAt" ,"updatedAt", "comments"]



@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = [
        "post",
        "createdAt",
        "updatedAt",
        "is_validated",
    ]
    actions = (mark_is_validated,unmark_is_validated)
    

