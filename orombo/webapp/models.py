# vim: ai sts=4 ts=4 et sw=4
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    '''The post model stores posts that are submitted on the site.'''
    title = models.CharField(max_length=255, help_text="The title for the post")
    url = models.URLField(verify_exists=True, help_text="A valid url to the resource")
    description = models.CharField(max_length=255, help_text="A description for the post")
    author = models.ForeignKey(User, help_text="The user that authored the post")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    post = models.ForeignKey(Post)
    voter = models.ForeignKey(User)
    points = models.IntegerField()

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    comment = models.CharField(max_length=5000, help_text="The comment not exceeding 5000 characters")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
