from django.db import models
from users.models import Profile

# Create your models here.

reactions = [('0', 'none'),
             ('1', 'like'),
             ('2', 'dislike')
             ]
status = [('1', 'publish'),
          ('2', 'draft')]

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_content = models.TextField(max_length=2000, null=False)
    media = models.FileField(upload_to='post_files',blank=True,null=True)
    likes = models.ManyToManyField(Profile, blank=True, related_name='post_likes')
    dislikes = models.ManyToManyField(Profile, blank=True, related_name='post_dislikes')
    created_on = models.DateTimeField(auto_now_add=True)
    post_status = models.CharField(max_length=7, null=False, choices=status)
    
    
class PostComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField(max_length=500, null=False, blank=False)
    likes = models.ManyToManyField(Profile, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(Profile, blank=True, related_name='comment_dislikes')

    