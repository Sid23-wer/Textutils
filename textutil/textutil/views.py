from django.http import HttpResponse
from django.shortcuts import render

def  index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=(request.GET.get('text','default'))
    pt=(request.GET.get('removepunc','off'))
    pr = (request.GET.get('capatial', 'off'))
    ps = (request.GET.get('small', 'off'))
    ms = (request.GET.get('newlineremover', 'off'))
    mt = (request.GET.get('countcharacter', 'off'))
    print(djtext)
    print(pt)
    analyzed=""
    if (pt == "on"):

        punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        params={'purpose': 'remove punctuation', 'pooi': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if (pr == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Captitalization', 'pooi': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(ps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'smaller', 'pooi': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(ms=="on"):
        analyzed = ""
        for char in djtext:
            if(char!="\n" and char!="\r"):
                analyzed = analyzed + char
        params = {'purpose': 'newlieremover', 'pooi': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(mt=="on"):
        count=0
        for char in djtext:
            t=len(char)
            count+=t
        analyzed=count
        params = {'purpose': 'count character', 'pooi': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)