from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug


class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT)
    tags = models.ManyToManyField('Tag')
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question


class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['category']


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:tag', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag']
