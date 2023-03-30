from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'Daief','place':'USA'}
    return render(request, 'index.html',params)

    # return HttpResponse("Home")

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    print(djtext)
    punctuations = '''!()-{}[];:;"\,<>./?@#$^&*_~%'''
    analyzed = ""
    print(removepunc)
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctions','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
            else:
                analyzed = analyzed + " "
        params = {'purpose':'New Line Remove','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif extraspaceremover == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'New Space Remove','analyzed_text':analyzed}
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
