from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def about(request):
    return HttpResponse("<h2> О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def index(request):
    return HttpResponse('Первый проект на Django')
def about(request):
    return HttpResponse('<h2>О сайте</h2>')
def contact(request):
    return HttpResponse('<h2>Контакты</h2>')
def products(request, productid=1):
    output = "<h2>Продукт {0}</h2>".format(productid)
    return HttpResponse(output)
def users(request, id, name):
    output = "<h2>Пользователь</h2> <h3>id: {0} Имя:{1}</h3>".format(id, name)
    return HttpResponse(output)

def index(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        output = "<h2>Пользователь</h2> <h3>id: {0} Имя:{1}</h3>".format(id, name)
        return HttpResponse(output)
    else:
        userform=UserForm()
        return render(request, "index.html", {"form": userform})

