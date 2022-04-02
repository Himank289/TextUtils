
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyse(request):
    djtext=request.GET.get('text', 'default')
    remove=request.GET.get('remove','off')
    analyse=request.GET.get('analyse', 'default')
    print(djtext)
    print(analyse)

    uppercase=request.GET.get('uppercase','default')
    cc = request.GET.get('cc', 'default')
    if remove=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed=""
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
        params={'purpose':'removepunctuations', 'analysed_text':analysed}
        return render(request, 'analyse.html', params)
    elif uppercase=='on':
        analysed=''
        for char in djtext:
            analysed=analysed+char.upper()
        params = {'purpose': 'capitalised sentence', 'analysed_text': analysed}
        return render(request,'analyse.html',params)
    elif cc=='on':
        count=0
        for char in djtext:
            count=count+1
            print("the count of all characters is",count)
        params={"puprose":"count of all characters is", "analysed_text":count}
        return render(request,'analyse.html',params)
    else:
        return HttpResponse("error")

def nav(request):
    return render(request, 'navigation.html')

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'index.html')

def address(request):
    return render(request,'address.html')

def contact(request):
    return render(request,'contact.html')

def email(request):
    return render(request,'email.html')














