from django.db import models

class NewsUrl(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to="newsphoto/")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

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

class JournalFilesUrl(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="journalImages/")
    files = models.FileField(upload_to="journalFiles/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
