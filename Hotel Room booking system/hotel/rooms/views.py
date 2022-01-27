from math import floor
from django.shortcuts import render
from django.core.paginator import Paginator
import requests
import math

# Create your views here.

def Index(request):
    try:
        page_number = int(request.GET.get('page'))
    except:
        page_number = 1

    if page_number:
        response = requests.get(f'http://127.0.0.1:8000/personView/?mypage={page_number}')
        allHotels = response.json()
    else:
        response = requests.get('http://127.0.0.1:8000/personView/')
        allHotels = response.json()

    previous = allHotels['previous']
    next = allHotels['next']

    total_pages = math.ceil(allHotels['count']/2)

    numberList = []
    for i in range(1, total_pages+1):
        numberList.append(i)

    if previous:
        previous_page = (previous[41:])
        if previous_page == '':
            prev = []
            prev.append(1)
            p = str(prev)
            q = p.replace("[", "")
            rep = q.replace("]", "")
            previous_page = rep
    else:
        previous_page = previous
    
    if next:
        next_page = (next[41:])
    else:
        next_page = next

    return render(request, 'index.html', {'allHotels':allHotels['results'], 'page_numbers':numberList, 'previous_page':previous_page, 'next_page':next_page, 'link_number':page_number})


def Hotel_Single_Page(request, hid):
    response = requests.get(f'http://127.0.0.1:8000/personView/{hid}')
    hotel = response.json()

    return render(request, 'hotel_single_page.html', {'hotel':hotel})
