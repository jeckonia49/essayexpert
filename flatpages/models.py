from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=timezone.now)
    comments = models.BigIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    
    # def get_comments(self):
    #     return self.post_comment.all()
    
    # def save(self, *args, **kwargs):
    #     # self.comments=self.get_comments().count()
    #     return super(Post, self).save(*args, **kwargs)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    comment = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=timezone.now)
    is_validated = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"comment on {self.post.title}"
    

