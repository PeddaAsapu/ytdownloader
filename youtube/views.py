from django.http import HttpResponse
from django.shortcuts import render, redirect
from pytube import *
 
 
# defining function
def downlaod_yt_video(request):
 
    # checking whether request.method is post or not
    if request.method == 'POST':
       
        # getting link from frontend
        video_url = request.POST['link']
        video = YouTube(video_url)
 
        # setting video resolution
        stream = video.streams.get_lowest_resolution()
         
        # downloads video
        stream.download()
 
        # returning HTML page
        return render(request, 'youtube_home.html')
    #return HttpResponse('ok')
    return render(request, 'youtube_home.html')
