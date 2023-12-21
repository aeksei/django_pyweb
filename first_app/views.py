import datetime

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View


def my_first_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"ТЕкущее время: {datetime.datetime.now()}")


def my_json_view(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"key": "value"})


# @csrf_exempt
# def show_http_method(request: HttpRequest) -> HttpResponse:
#     if request.method == "GET":
#
#     elif request.method == "POST":


class ShowHTTPMethodView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(f"Hello world")

    def post(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse(request.POST)