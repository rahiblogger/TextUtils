# i have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyse(request):
    # get text from page
    djtext = request.POST.get('text', 'default')

    # check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspace = request.POST.get('extraspace', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on":
        analysed = ""
        for i in djtext:
            if i not in punctuations:
               analysed += i
        param = {"purpose": "Remove Punctuation", "analysed_text": analysed}
        djtext = analysed
        # return render(request, "analyse.html", param)

    if fullcaps == 'on':
        analysed = ""
        for i in djtext:
            analysed += i.upper()

        param = {"purpose": "Capitalized Sentense", "analysed_text": analysed}
        djtext = analysed
        # return render(request, 'analyse.html', param)

    if extraspace == "on":
        analysed = ""
        for index, data in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analysed += data
        param = {"purpose": "Extra Space remove", "analysed_text": analysed}
        djtext=analysed

    if (removepunc != "on" and fullcaps != 'on' and extraspace != "on"):
        return HttpResponse("Error")

    return render(request,'analyse.html', param)