from django.contrib import admin
from . import models

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "fio", "rank", "mobile_phone_number", "email"]
    ordering = ["-id"]
    search_fields = ["fio", "rank"]

@admin.register(models.NewsUrl)
class NewsUrlAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", 'published_time', "status", "image"]
    list_filter = ['status', 'created_at', 'published_time']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']
    ordering = ['status', 'published_time']

class PostImageInline(admin.TabularInline):
    model = models.PostImages
    readonly_fields = ('id', 'post')
    extra = 1

@admin.register(models.PostName)
class PostImageAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, ]

@admin.register(models.BannerImages)
class BannerImagesAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]


class ProjectNameUrlsInline(admin.TabularInline):
    model = models.ProjectsList
    readonly_fields = ('id', 'projectName')
    extra = 1

@admin.register(models.ProjectName)
class ProjectListAdmin(admin.ModelAdmin):
    inlines = [ProjectNameUrlsInline]

class OpenBudgetFilesAdmin(admin.ModelAdmin):
    list_display = ["title", "files"]
    search_fields = ["title", "files"]


class JournalFilesAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "files"]
    search_fields = ["title", "image", "files"]

admin.site.register(models.JournalFilesUrl, JournalFilesAdmin)
admin.site.register(models.OpenBudgetFiles, OpenBudgetFilesAdmin)

