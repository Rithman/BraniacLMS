from django.http import HttpResponse
from django.views.generic import View


class HelloWorldView(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Hello there!<br>General Kenobi!")


def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")
