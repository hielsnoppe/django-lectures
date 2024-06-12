from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def ex01_first_view(request):
    return HttpResponse('Hello World!')

def ex02_json(request):
    return JsonResponse({'text': 'Hello World!'})