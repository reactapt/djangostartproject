from django.http import HttpResponse, HttpRequest


def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("ФСБ России - Все рейды - Смотреть бесплатно")
