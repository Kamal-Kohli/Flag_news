from django.shortcuts import render
import requests
API_KEY = '2228671f48644d399e8cc37fb14015f6'

# Create your views here.
def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)
