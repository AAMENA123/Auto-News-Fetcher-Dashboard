import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .models import NewsArticle
from datetime import datetime
from newsapi  import NewsApiClient



def home(request):
        if request.method == "POST":
            news =NewsFetcher()
            news.store_data()
            return news.display(request)
        return render(request,"dashboard.html")        
class NewsFetcher:
    def __init__(self):
            self.my_api_key = '3b8d899b0b6143cda9b2bf40b1418057'
            self.newsapi = NewsApiClient(api_key=self.my_api_key)
            self.data=self.newsapi.get_everything(domains="bbc.co.uk,techcrunch.com", language='en', 
                                           page_size=20)
            self.articles = self.data['articles']
        
            
    def display(self,request):  
        news = []
        for article in self.articles:
                news.append({
                    'title': article['title'],
                    'image': article['urlToImage']
                })
        return render(request, "dashboard.html", {'news': news})
        
    def store_data(self):
        count =0
        for article in self.articles:
            url = article.get('url')
            if url and not NewsArticle.objects.filter(url=url).exists():
                NewsArticle.objects.create(title=article.get('title'),
                summary=article.get('description'),
                source=article.get('source', {}).get('name'),
                published_at=article.get('publishedAt'),
                url=article.get('url'),
                url_to_image=article.get('urlToImage'))
        print(f'{count} news objects are created')