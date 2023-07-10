from django.shortcuts import render, get_object_or_404
import requests
from datetime import datetime
from .models import (
NewsUrl,
JournalFilesUrl,
BannerImages
)

def homePages(request):
    lastJournal = JournalFilesUrl.objects.all().order_by("-created_at")[:4]
    lastNews = NewsUrl.objects.all().order_by("-created_at")[:4]
    banners = BannerImages.objects.all().order_by("-created_at")
    pollution = requests.get("https://api.airvisual.com/v2/nearest_city?key=62d478cb-427d-4308-9042-70b480b96594").json()['data']

    now = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
    city = pollution['city']
    aqius = int(pollution['current']['pollution']['aqius'])
    mainus = pollution['current']['pollution']['mainus']
    tp = pollution['current']['weather']['tp']
    hu = pollution['current']['weather']['hu']
    wd = pollution['current']['weather']['ws']
    ic = pollution['current']['weather']['ic']

    ic = 'images/weather-icons/' + ic + ".png"
    status = 'Hazardous'
    statusColor = "#a06a7b"

    if aqius <= 50 and aqius >= 0:
        statusEn = 'Good'
        statusUz = 'Yaxshi'
        statusColor = '#9cd84e'
        statusImg = 'images/weather-icons/ic-face-green.svg'
    if aqius >= 51 and aqius <= 100:
        statusEn = 'Moderate'
        statusUz = "O'rtacha"
        statusColor = '#facf39'
        statusImg = 'images/weather-icons/ic-face-yellow.svg'
    if aqius >= 101 and aqius <= 150:
        statusUz = "Nozik guruhlar uchun nosog'lom"
        statusEn = 'Unhealthy for Sensitive Groups'
        statusColor = '#f99049'
        statusImg = 'images/weather-icons/ic-face-orange.svg'
    if aqius >= 151 and aqius <= 200:
        statusEn = "Unhealthy"
        statusUz = "Nosog'lom"
        statusColor = '#f65e5f'
        statusImg = 'images/weather-icons/ic-red-orange.svg'
    if aqius >= 201 and aqius <= 300:
        statusEn = "Very Unhealthy"
        statusUz = "Juda Nosog'lom"
        statusColor = '#a070b6'
        statusImg = 'images/weather-icons/ic-red-orange.svg'

    context = {
        "statusUz": statusUz,
        "statusImg": statusImg,
        'statusColor': statusColor,
        "lastJournal": lastJournal,
        "lastNewses": lastNews,
        "banners": banners,
        "now": now,
        "aqius": aqius,
        "mainus": mainus,
        "tp": tp,
        "hu": hu,
        "wd": wd,
        "ic": ic,
        "city": city
    }
    return render(request, "index.html", context)

def activityPages(request):
    context = {}
    return render(request, 'faoliyat.html', context)

def newsPages(request):
    listNewses = NewsUrl.objects.all()

    context = {
        "listNewses": listNewses,
    }
    return render(request, 'news-list.html', context)

def connectPages(request):
    context = {}
    return render(request, 'page-404.html', context)

def openBudgetPages(request):
    context = {}
    return render(request, 'open-budget.html', context)

def scienceJournal(request):
    journals = JournalFilesUrl.objects.all().order_by("-created_at")
    context = {
        "journals": journals
    }
    return render(request, 'journals-list.html', context)

def newsDetail(request, id):
    news = get_object_or_404(NewsUrl, id=id)
    newsesList = NewsUrl.objects.all().order_by("-created_at")[:6]

    context = {
        "news": news,
        "newsesList": newsesList
    }

    return render(request, "news-detail.html", context)

def redBook(request):
    context = {}
    return render(request, "qizilKitob.html", context)

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
    return render(request, 'eventsls'
                           '-list2.html', context)
def aboutPage(request):

    return render(request, "about.html")
