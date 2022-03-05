# importing all the required modules
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pytube import *
 
 
# defining function
def downlaod_yt_video(request):
 
    # checking whether request.method is post or not
    if request.method == 'POST':
       
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
 
        # setting video resolution
        stream = video.streams.get_lowest_resolution()
         
        # downloads video
        stream.download()
 
        # returning HTML page
        return render(request, 'youtube_home.html')
    #return HttpResponse('ok')
    return render(request, 'youtube_home.html')

def hello(request) :
    #return HttpResponse('ok done')
    return render(request, 'hello.html')