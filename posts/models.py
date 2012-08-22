from django.db import models
from django.contrib.auth.models import User


class AbstractPost(models.Model):
    author = models.ForeignKey(User, editable=False)
    headline = models.CharField(max_length=255)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']
        abstract = True

    def __unicode__(self):
        return self.headline


class Post(AbstractPost):
    pass

class PositionPostMixin(models.Model):
    position = models.IntegerField()

    class Meta:
        ordering = ['position']
        abstract = True

class LinkPostMixin(models.Model):
    link_url = models.URLField()
    link_name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class ImagePostMixin(models.Model):
    image = models.CharField(max_length=40)

    class Meta:
        abstract = True
