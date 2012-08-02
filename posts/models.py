from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, editable=False)
    headline = models.CharField(max_length=255)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']

    def __unicode__(self):
        return self.headline

