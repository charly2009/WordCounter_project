#from django.http import HttpResponse
import operator

from django.shortcuts import render
def homepage(request):
    return render(request, 'home.html')
def count(request):
    full_text = request.GET["full-text"] # get the text typed into the form put it in dictionnary
    wordlist = full_text.split()
    #print(full_text)
    file = open('text.txt', 'w')
    file.write(full_text)
    wordictionary = {}
    for word in wordlist:
        if word in wordictionary:
            #increase
            wordictionary[word] += 1
        else:
            #add
            wordictionary[word] = 1
        sortedWord = sorted(wordictionary.items(), key= operator.itemgetter(1), reverse=True)
    return render (request,'count.html', dict(fulltext=full_text, count=len(wordlist), wordictionary=sortedWord)) # use {{ fulletxt}} into the count.html # wordictionary.items() convert it into list


def about(request):
    return render(request, 'about.html')
    print('hello')