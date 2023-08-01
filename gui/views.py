from django.shortcuts import render
import requests
import re

def index(request):
    if request.method == 'POST':
        search_word = request.POST.get('search_word')
        search_url = request.POST.get('search_url')
    else:
        search_word = None
        search_url = None

    # Wikipedia URL
    #wikipedia_url = 'https://en.wikipedia.org/wiki/Nanded'
    wikipedia_page = requests.get(search_url)

    if search_word and re.search(search_word, wikipedia_page.text):
        word_found = True
    else:
        word_found = False

   

    return render(request, 'index.html', {'search_word': search_word,  'word_found': word_found})



