from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'Daief','place':'USA'}
    return render(request, 'index.html',params)

    # return HttpResponse("Home")

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(djtext)
    punctuations = '''!()-{}[];:;"\,<>./?@#$^&*_~%'''
    analyzed = ""
    print(removepunc)
    if removepunc == 'off':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctions','analyzed':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")
def removepunc(request):
    print(request.GET.get('text','default'))
    return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")
