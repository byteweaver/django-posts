from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class AbstractPost(models.Model):
    author = models.ForeignKey(User, editable=False, related_name = "%(app_label)s_%(class)s")
    headline = models.CharField(_("Headline"), max_length=255)
    text = models.TextField(_("Text"))
    creation_date = models.DateTimeField(_("Creation Date"), auto_now_add=True)

    class Meta:
        ordering = ['-creation_date']
        abstract = True

    def __unicode__(self):
        return self.headline

class Post(AbstractPost):
    slug = models.SlugField(_("Slug"), max_length=150)

    @models.permalink
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

class VisibilityPostManagerMixin(models.Manager):
    def get_visible(self):
        return self.filter(visible=True)

class VisibilityPostMixin(models.Model):
    visible = models.BooleanField(_("Visible"), default=True)

    class Meta:
        abstract = True

class PositionPostMixin(models.Model):
    position = models.IntegerField(_("Position"))

    class Meta:
        ordering = ['position']
        abstract = True

class LinkPostMixin(models.Model):
    link_url = models.URLField(_("Link URL"), blank=True)
    link_name = models.CharField(_("Link Name"), max_length=255, blank=True)

    class Meta:
        abstract = True

class ImagePostMixin(models.Model):
    image = models.CharField(_("Image"), max_length=40)

    class Meta:
        abstract = True
