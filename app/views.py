"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from pytube import YouTube
from pathlib import Path

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def download(request):
     val = request.GET.get('link')
     val2 = request.GET.get('format')
     val1 = ""
     filename = Path("C:/Users/Public")
     try:
        #myVar.set("Downloading...")
        #root.update()
        val1 = "Download in progress...."
        if val2 == "audio":
            a= YouTube(val).streams.get_audio_only().download(filename)
            val1 = "Audio downloaded successfully at: "+a
        else :
            b = YouTube(val).streams.get_highest_resolution().download(filename)
            val1 = "Video downloaded successfully at: "+b

        
        #link.set("Video downloaded successfully")
     except Exception as e:
        #myVar.set("Mistake")
        #root.update()
        val1 = e
        #link.set("Enter correct link")


     assert isinstance(request, HttpRequest)
     return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'Result':val1
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
