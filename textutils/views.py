#i have created this file-Vipul Wadekar
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    param={'name':'vipul','place':'Mars'}
    return render(request,'index.html',param)


def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    #check box value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    #checkbox which checkbox is on 
    if removepunc == "on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punc:
                    analyzed=analyzed+char
        
        params={'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        
   
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()  
        
        params={'purpose':'Changed to upperCase','analyzed_text':analyzed}
        djtext=analyzed
         
    
    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed=analyzed + char  
          
                
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        djtext=analyzed
         
    
    if extraspaceremover == "on":
        analyzed=""
        for index,char in enumerate (djtext):
            if not (djtext[index] == "" and djtext[index+1]==""):
                analyzed= analyzed + char  
        
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        djtext=analyzed
        
    
    if charcount == "on":
        analyzed=len(djtext)
        params={'purpose':'Number of characters','analyzed_text':analyzed}
        djtext=analyzed
        
    if (removepunc!="on" and fullcaps!= "on" and newlineremover!="on" 
and extraspaceremover!="on" and charcount!="on") :
        return HttpResponse("please select any operation and try again")


    return render(request,'analyze.html',params)    



