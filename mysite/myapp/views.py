from posixpath import split
from unittest.mock import sentinel
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        sentence = request.POST['sentence']
        amount_of_words = sentence.split()
        aow = len(amount_of_words)
        return render(request, 'index.html')

    return render(request, 'index.html')