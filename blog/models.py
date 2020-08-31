from django.db import models
from django.contrib.auth.models import User
import random, os
from django.urls import reverse
from django.template.defaultfilters import slugify

STATUS = ((0, "Draft"), (1, "Publish"))


class Entry(models.Model):
    entry_title = models.CharField(max_length=1000)
    entry_text = models.TextField(max_length=50000)
    entry_tags = models.TextField(max_length=50000)
    site_sub_id = models.CharField(max_length=1000)
    image = models.FileField(upload_to="media", blank=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=5000, null=True, blank=True, unique=True)
    status = models.IntegerField(choices=STATUS, default=1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.entry_title)
        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.entry_title

    class Meta:
        verbose_name_plural = "blog entries"

    def __str__(self):
        return self.entry_title
