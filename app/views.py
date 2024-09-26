from django.shortcuts import render # type: ignore 
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

def player(request):
    return render(request, "modules/player.html")

def home(request):
    return render(request, "pages/home.html")

def carousel(request):
    return render(request, "module/carousel.html")

def navbar(request):
    return render(request, 'modules/navbar.html', {'request': request})

def podcast(request):
    return render(request, "pages/podcast.html")

def emissions(request):
    return render(request, "pages/emissions.html")

def charts(request):
    return render(request, "pages/charts.html")

def teams(request):
    return render(request, "pages/teams.html")

def news(request):
    return render(request, "pages/news.html")

def newevents(request):
    return render(request, "pages/newevents.html")

def contact(request):
    return render(request, "pages/contact.html")


def my_view(request):
    # Accéder aux paramètres GET
    parametre_get = request.GET.get('nom_du_parametre')

    # Accéder aux données envoyées par POST
    parametre_post = request.POST.get('nom_du_parametre')

    return HttpResponse('Voici la réponse à la requête')

def my_view(request):
    user_agent = request.META.get('HTTP_USER_AGENT', 'inconnu')

    return HttpResponse(f'Ton User-Agent est {user_agent}')

def my_view(request):
    cookie_valeur = request.COOKIES.get('mon_cookie', 'Pas de cookie trouvé')

    return HttpResponse(f'Valeur du cookie : {cookie_valeur}')

def my_view(request):
    ip_client = request.META.get('REMOTE_ADDR')

    return HttpResponse(f'Adresse IP du client : {ip_client}')

def upload_view(request):
    if request.method == 'POST' and request.FILES['document']:
        document = request.FILES['document']
        # Tu peux alors gérer ce fichier comme tu le souhaites
        return HttpResponse('Fichier téléchargé avec succès !')

    return HttpResponse('Pas de fichier téléchargé')