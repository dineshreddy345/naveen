from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def middleview(request):
    print(10/0)
    print('this line is from view')
    return HttpResponse ('<h1>custom middleware demo</h1>')

