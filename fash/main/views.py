from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import ContactForm, SnippetForm
# Create your views here.

def index(request):
    return render(None,'ind.html')

def pyfun(request):
    print("Hello")
    return render(request,"pred.html",{'major':['symmetrical skirt',
 'regular (fit) bag, wallet',
 'symmetrical jacket',
 'zip-up bag, wallet'],'minor':['collarless collar',
 'collarless neckline',
 'v-neck neckline',
 'wrist-length sleeve']})
    
def pred(request):
    if request.method=="POST":
        print("Im here")
        print(request.POST)
        return render(request,"tags.html")
    return render(None,'pred.html')

def tags(request):
    if request.method=="POST":
        print("Im here")
        print(request.POST)
    return render(None,'tags.html')    


def v1(request):
    return HttpResponse("<h1>Hello</h1>")


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name)

    else:
        form = ContactForm()

    return render(request, 'form.html', {'form': form})


def snippet_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()


    form = SnippetForm()
    return render(request, 'form.html', {'form': form})
