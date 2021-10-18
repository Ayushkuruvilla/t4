from requests_html import HTMLSession
import json
from bs4 import BeautifulSoup
import os,json
from webcrawler import webcrawler
import warnings
warnings.filterwarnings("ignore")
m=['symmetrical jacket','collarless collar','wrist-length sleeve']
ans=webcrawler(m)
print(ans[0])
