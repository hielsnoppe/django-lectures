from django.shortcuts import render

# Create your views here.

def ex01(request):
    return render(request, 'chp03/ex01_static.html')

def ex02(request):
    context = {
        'my_variable': 'Some value'
    }
    return render(request, 'chp03/ex02_context.html', context)

def ex03(request):
    context = {
        'my_list': [],
        'my_dict': {
            'key1': 'value1'
        }
    }
    return render(request, 'chp03/ex03_control.html', context)

def ex04(request):
    return render(request, 'chp03/ex04_include.html')

def ex05(request):
    return render(request, 'chp03/ex05_extends.html')