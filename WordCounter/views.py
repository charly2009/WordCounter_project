#from django.http import HttpResponse
import operator
from tkinter import messagebox
from django.shortcuts import render
def homepage(request):
    return render(request, 'home.html')
def count(request):

    full_text= request.GET["full-text"]
    if full_text == '' :
        return render(request, 'home.html', {'error': 'Please fill the form'} )
        messagebox.ERROR('error')
    else:
        #full_text = request.GET["full-text"]  # get the text typed into the form put it in dictionnary
        wordlist = full_text.split()  # this takes the content of the text-area and divide it in different word
        file = open('text.txt', 'w')
        file.write(full_text)
        # check the text and divide by the word and find the number of a word exists in the text
        wordictionary = {}
        for word in wordlist:
            if word in wordictionary:
                # increase
                wordictionary[word] += 1
            else:
                # add
                wordictionary[word] = 1
                #If reverse is assigned True, then the sorting will be in descending order:
                #ascending =  high level 
        sortedWord = sorted(wordictionary.items(), key=operator.itemgetter(1), reverse=True)
        return render(request, 'count.html',
                              {'fulltext':full_text,'count':len(wordlist),'sortedwords':sortedWord})


def about(request):
    return render(request, 'about.html')
