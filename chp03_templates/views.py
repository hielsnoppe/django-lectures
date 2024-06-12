from django.shortcuts import render

# Create your views here.

def ex01(request):
    return render(request, 'chp03/ex01_static.html')

def ex02(request):
    context = {
        'my_variable': 'Some value',
        'person': {
            'firstname': 'Donald',
            'lastname': 'Duck'
        },
        'my_html': '<a href="https://example.com">Click me!</a>'
    }
    return render(request, 'chp03/ex02_context.html', context)

def ex03(request):
    context = {
        'my_bool': True,
        'my_bool2': False,
        'my_list': [ 'Apple', 'Banana', 'Lime' ],
        'my_dict': {
            'Apple': 'Red',
            'Banana': 'Yellow',
            'Lime': 'Green'
        }
    }
    return render(request, 'chp03/ex03_control.html', context)

def ex04(request):
    return render(request, 'chp03/ex04_include.html')

def ex05(request):
    return render(request, 'chp03/ex05_extends.html')