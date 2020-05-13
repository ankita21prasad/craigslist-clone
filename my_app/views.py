from django.shortcuts import render
# from requests.compat import quote_plus
from bs4 import BeautifulSoup
from . import models
import requests

BASE_CRAIGSLIST_URL = 'https://hyderabad.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/'

def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search = search)
    final_url = BASE_CRAIGSLIST_URL.format(search)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    final_posting = []

    post_listings = soup.find_all('li', {'class': 'result-row'})

    for post in post_listings:
        post_url = post.find('a', {'class': 'result-title hdrlnk'}).get('href')
        post_title = post.find('a', {'class': 'result-title hdrlnk'}).text
        post_price = 'N/A'
        if post.find('span', {'class': 'result-price'}):
            post_price = post.find('span', {'class': 'result-price'}).text

        post_image_url = 'https://craigslist.org/images/peace.jpg'

        image_page = requests.get(post_url).text
        image_soup = BeautifulSoup(image_page, features='html.parser')

        if image_soup.find('div', {'class': 'gallery'}):
            image_url = image_soup.find('div', {'class': 'slide first visible'})
            post_image_url = image_url.find('img').get('src')
            # print(image_url)
            # print(post_image_url)

        final_posting.append((post_title, post_url, post_price, post_image_url))

    context = {
        'search': search,
        'final_postings': final_posting,
    }
    return render(request, 'my_app/new_search.html', context)