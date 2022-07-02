from django.shortcuts import render
from django.http import HttpResponse
from . import models
from math import ceil

# Create your views here.


def all_rooms(request):
    page = int(request.GET.get("page", 1))
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    objects_count = models.Room.objects.count()
    pages_count = ceil(objects_count / page_size)
    pages_range = range(1, pages_count + 1)
    all_rooms = models.Room.objects.all()[offset:limit]

    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "pages_count": pages_count,
            "pages_range": pages_range,
        },
    )
