import time

from django.http import JsonResponse
from django.shortcuts import render


def he(request):
    return render(request, "index.html")


def ping(request):
    return JsonResponse({"message": f"pong {time.time()}"})
