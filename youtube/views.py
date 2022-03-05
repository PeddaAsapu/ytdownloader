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
        destination = request.POST['destination']
        # setting video resolution
        stream = video.streams.get_lowest_resolution()
         
        # downloads video
        stream.download(output_path=destination)

        #return HttpResponse(destination)
        # returning HTML page
        return render(request, 'youtube_home.html', {'message' : 'Your video has been downloaded', 'path' : destination})
    #return HttpResponse('ok')
    return render(request, 'youtube_home.html')
