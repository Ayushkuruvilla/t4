from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import ContactForm, SnippetForm
import warnings
warnings.filterwarnings("ignore")
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
        m=[]
        m.append(request.POST['options1'])
        m.extend(request.POST.getlist('options2'))
        #print(request.POST)
        ans=webcrawler(m)
        return render(request,"tags.html",{'links':ans})
    return render(None,'pred.html')

def tags(request):
    if request.method=="POST":
        print(request.POST['options1'])
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

from requests_html import HTMLSession
import json
from bs4 import BeautifulSoup
import os,json

def webcrawler(m):
    label_description_path=r'C:\Users\91948\proj\label_descriptions.json'
    with open(label_description_path, 'r') as file:
        label_desc = json.load(file)

    links=[]
    #m=['symmetrical jacket','collarless collar','wrist-length sleeve']
    #print(m)
    w1="-".join(m).replace(' ','-')
    w2="+".join(m).replace(' ','+')
    w3="%20".join(m).replace(' ','%20')


    #Website1
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

    s = HTMLSession()
    res = s.get("https://www.myntra.com/"+w1+"?p=1&plaEnabled=false", headers=headers, verify=False)

    soup = BeautifulSoup(res.text,"html.parser")
    #print(soup.html)

    val=json.loads(soup.find_all('script', type='application/ld+json')[1].string)
    linksw1=[]
    for i in val['itemListElement']:
        linksw1.append(i['url'])
    #print(linksw1)
    links.extend(linksw1[0:2])

    #Website2
    linksw2=[]
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

    s = HTMLSession()
    res = s.get("https://www2.hm.com/en_in/search-results.html?q="+w2, headers=headers, verify=False)

    soup = BeautifulSoup(res.text,"lxml")
    #print(soup.html)
    if(soup.find_all('h1', attrs={'class': 'heading'})[0].contents[0]=='NO MATCHING ITEMS')==True:
        links.extend(linksw1[2:4])
    else:
        for item in soup.select('.hm-product-item'):
            linksw2.append(item.select('.item-link')[0]['href'])
        links.extend(linksw2[0:2])

    #website3
    linksw3=[]
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

    s = HTMLSession()
    res = s.get("https://www.ajio.com/search/?text="+w3, headers=headers, verify=False)

    soup = BeautifulSoup(res.text,"html.parser")
    #print(soup.html)
    try:
      val=json.loads(soup.find_all('script', type='application/ld+json')[2].string)
    except:
      links.extend(linksw1[4:6])

    for i in val['itemListElement']:
        linksw3.append(i['url'])
    #print(linksw3)
    links.extend(linksw3[0:2])

    #print("final")
    return links
