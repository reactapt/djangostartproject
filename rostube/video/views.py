from django.http import HttpRequest, HttpResponse


def video_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('ФСБ России')