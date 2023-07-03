from django.utils import timezone

from django.db import models
from django.utils.translation import gettext_lazy as _


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=NewsUrl.Status.Published)

class NewsUrl(models.Model):

    objects = models.Manager()
    published = PublishedManager()

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = 'PB', 'Published'

    author = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    related_words = models.CharField(max_length=200)
    image = models.ImageField(upload_to="newsphoto/")
    published_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} {self.created_at}"

class ProjectName(models.Model):
    name = models.CharField(max_length=300)
    image = models.FileField(upload_to='projectImage/')
    description = models.TextField()

    def __str__(self):
        return self.name

class ProjectsList(models.Model):
    projectName = models.ForeignKey(ProjectName, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to='projectImage/')
    year = models.CharField(max_length=20, blank=True )

    def __str__(self):
        return self.title

class PostName(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PostImages(models.Model):
    post = models.ForeignKey(PostName, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return f"{self.post.name}  {self.images.url}"

class OpenBudgetFiles(models.Model):
    title = models.CharField(max_length=600)
    files = models.FileField(upload_to="openbudget/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BannerImages(models.Model):
    title = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to="bannerImages/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JournalFilesUrl(models.Model):
    class TypeJournalList(models.TextChoices):
        KITOB = "PDF", _("Kitoblar")
        WORD = "DOC", _("Wordlar")
        RASM = "JPG", _("Rasmlar")

    type_of_journal = models.CharField(
        max_length=3,
        choices=TypeJournalList.choices,
        default=TypeJournalList.KITOB,
    )

    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to="journalImages/")
    files = models.FileField(upload_to="journalFiles/")
    published_date = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
