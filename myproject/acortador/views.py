from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, \
HttpResponseRedirect, HttpResponseBadRequest
from models import Urls
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


formulario = "<form action='' method='POST'>Request your URL: "
formulario += "<input type='text' name='url' value='' /><br>"
formulario += "<input type='submit' value='Send'></form>"


def url(request, url):
    try:
        dir = Urls.objects.get(id=url)
    except Urls.DoesNotExist:
        return notfound(request, url)
    return HttpResponseRedirect(dir.url)


def post(url):
    if url == "":
        return HttpResponseBadRequest("Empty post")
    elif not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url


@csrf_exempt
def all(request):
    if request.method == "GET":
        list = Urls.objects.all()
        out = "<html><body><ul>\n"
        for i in list:
            out += "<li><a href=" + i.url + ">" + str(i.id) + "</a></li>\n"
        out += "</ul>" + formulario + "</body></html>"
    elif request.method == "POST":
        url = request.POST.get("url")
        url = post(url)
        try:
            out = "Old URL"
            new = Urls.objects.get(url=url)
        except Urls.DoesNotExist:
            new = Urls(url=url)
            new.save()
            out = "New URL"
        out += "<html><body><ul>\n"
        out += "<li><a href=" + new.url + ">Url Original</a></li>\n"
        out += "<li><a href=" + str(new.id) + ">Url corta</a></li>\n"
        out += "</ul>" + formulario + "</body></html>"
    else:
        out = "Request not found"
    return HttpResponse(out)


def notfound(request, url):
    out = ("Not found: " + url)
    return HttpResponseNotFound(out)
