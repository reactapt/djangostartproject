from lib2to3.fixes.fix_input import context
from . import models
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def video_page(request: HttpRequest) -> HttpResponse:
    video = models.Video.objects.get(pk=1)
    context = {'video': video}
    return render(request, 'templates/index.html',)

