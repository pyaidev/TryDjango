from django.db import models

# Create your models here.
from django.db.models import Q
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is not None:
            lookup = Q(title__icontains=query) | Q(content__icontains=query)
            return self.filter(lookup)
        return self.none()

class SearchManager(models.Manager):

    def get_queryset(self):
        return ArticleQuerySet(self.model)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Article(models.Model):
    title = models.CharField(max_length=221)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    objects = SearchManager()

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        # return f'/{self.slug}/'
        return reverse('articles:article_detail', kwargs={'slug': self.slug})


    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    #     print('save')


@receiver(pre_save, sender=Article)
def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    # if instance.slug is None:
    #     instance.slug = slugify(instance.title)


def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        if instance.slug is None:
            instance.slug = slugify(instance.title)
            instance.save()


# pre_save.connect(article_pre_save, sender=Article)
# post_save.connect(article_post_save, sender=Article)
