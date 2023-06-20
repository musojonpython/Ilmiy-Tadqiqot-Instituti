from .models import NewsUrl

def footer_news(request):
    footer_news = NewsUrl.objects.all().order_by('-created_at')[5:8]

    context = {
        'footerNews': footer_news
    }
    return context
