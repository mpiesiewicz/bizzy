from django.shortcuts import render, HttpResponse
# from .models import EventItem
# Create your views here.


def home(request):
    return render(request, "home.html")


def events(request):
    items = EventItem.objects.all()
    return render(request, "events.html", {"events": items})
