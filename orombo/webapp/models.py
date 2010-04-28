# vim: ai sts=4 ts=4 et sw=4
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField

class Post(models.Model):
    '''The post model stores posts that are submitted on the site.'''
    title = models.CharField(max_length=255, help_text="The title for the post")
    url = models.URLField(verify_exists=True, help_text="A valid url to the resource")
    description = models.TextField(blank=True, null=True, help_text="A description for the post")
    author = models.ForeignKey(User, help_text="The user that authored the post")
    slug = AutoSlugField(populate_from='title')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % (self.title)

class Vote(models.Model):
    post = models.ForeignKey(Post)
    voter = models.ForeignKey(User)
    points = models.IntegerField()

    def __unicode__(self):
        return u'%s (%d)' % (self.post.title, self.points)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    comment = models.TextField(help_text="A user comment for the post")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.comment)
