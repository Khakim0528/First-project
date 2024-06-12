from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def home4(request):
    return HttpResponse(f"<mark> Hello</mark>, My home <hr> "
                        f"Request method: <b style='color:green;'>{request.method}</b>")

def home3(request):
    import random
    a=random.randint(1, 100)
    b=random.randint(100,1000)
    c=a+b
    return HttpResponse(f"Random: {a}*{b}={c}")

