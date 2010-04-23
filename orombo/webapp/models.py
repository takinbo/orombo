# vim: ai sts=4 ts=4 et sw=4
from django.db import models

class Post(models.Model):
    '''The post model stores posts that are submitted on the site.
    TODO: include a field for the author'''
    title = models.CharField(max_length=255, help_text="The title for the post")
    url = models.URLField(verify_exists=True, help_text="A valid url to the resource")
    description = models.CharField(max_length=255, help_text="A description for the post")
    slug = models.SlugField(max_length=255, unique=True)
    time = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    post = models.ForeignKey(Post)
    points = models.IntegerField()

class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment = models.CharField(max_length=5000, help_text="The comment not exceeding 5000 characters")
