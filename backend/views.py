from django.shortcuts import render, get_object_or_404
from .models import (
NewsUrl,
JournalFilesUrl
)
def projectDetail10(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }

    return render(request, "projects-details-10.html", context)

def projectDetail9(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }

    return render(request, "projects-details-9.html", context)

def projectDetail8(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }

    return render(request, "projects-details-8.html", context)

def projectDetail7(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }

    return render(request, "projects-details-7.html", context)


def projectDetail6(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }

    return render(request, "projects-details-6.html", context)


def projectDetail5(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }

    return render(request, "projects-details-5.html", context)


def projectDetail4(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }

    return render(request, "projects-details-4.html", context)

def projectDetail3(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }

    return render(request, "projects-details-3.html", context)

def projectDetail2(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }

    return  render(request, 'projects-details-2.html', context)

def projectDetail1(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }
    return render(request, 'projects-details-1.html', context)

def projectDetail(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }
    return render(request, 'projects-details.html', context)


def firstProjectsList(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[:4]
    }
    return render(request, 'events-list.html', context)

def secondProjectsList(request):
    context = {
        "footerNews": NewsUrl.objects.all().order_by("created_at")[5:8]
    }
    return render(request, 'event-list2.html', context)
def aboutPage(request):
    context = {
    "footerNews":NewsUrl.objects.all().order_by("created_at")[5:8]
    }
    return render(request, "old-about.html", context)

def homePages(request):
    context = {}
    lastJournal = JournalFilesUrl.objects.all().order_by("-created_at")[:4]
    lastNews = NewsUrl.objects.all().order_by("-created_at")[:4]
    footerNews = NewsUrl.objects.all().order_by("-created_at")[5:8]

    context = {
        "lastJournal": lastJournal,
        "lastNewses": lastNews,
        "footerNews": footerNews
    }
    return render(request, "index.html", context)

def activityPages(request):
    context = {}
    return render(request, 'faoliyat.html', context)

def newsPages(request):
    listNewses = NewsUrl.objects.all()
    footerNews = NewsUrl.objects.all().order_by("created_at")[5:8]
    context = {
        "listNewses": listNewses,
        "footerNews": footerNews
    }
    return render(request, 'blog-list.html', context)

def connectPages(request):
    context = {}
    return render(request, 'page-404.html', context)

def openBudgetPages(request):
    context = {}
    return render(request, 'open-budget.html', context)

def scienceJournal(request):
    journalList = JournalFilesUrl.objects.all().order_by("-created_at")
    context = {}
    return render(request, 'index.html', context)

def newsDetail(request, id):
    news = get_object_or_404(NewsUrl, id=id)
    newsesList = NewsUrl.objects.all().order_by("-created_at")[:6]
    context = {
        "news": news,
        "newsesList": newsesList
    }

    return render(request, "blog.html", context)


# def employeeList(request):
#     context = {}
#     context["employees"] = Employee.objects.all()
#     return render(request, "main-files/index_test.html", context)
#
# def newsUrls(request):
#     context = {}
#     # context["newsUrls"] = NewsUrl.objects.all()
#     newsObjects = NewsUrl.objects.all()
#     print(newsObjects)
#     return render(request, "main-files/index_test.html", context)
#
# def journalFilesUrl(request):
#     context = {}
#     context["journalList"] = JournalFilesUrl.objects.all().order_by("-created_at")
#
#     return render(request, "journal.html", context)


# def photosGallery(request, id):
#     context = {}
#     postImages = PostName.objects.get(id=id).postimages_set.all()
#
#     print(postImages)
#     context = {"postImage": postImages}
#
#     return render(request, "index_test.html", context)
#
# def videoGallery(request, id):
#     context = {}
#     postVideos = VideoName.objects.get(id=id).videonameurls_set.all()
#
#     contect = {"postVideos": postVideos}
#     return render(request, "main-files/index_test.html", context)

