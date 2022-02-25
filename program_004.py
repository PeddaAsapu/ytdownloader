import pytube
import pyautogui
from pytube import YouTube

def download(src,dest):
    try:
        video = YouTube(src)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path = dest)
        pyautogui.alert("Enjoy the video buddy!!")
    except PermissionError:
        pyautogui.alert("Hey buddy!! check your path for the destination folder.")
    except pytube.exceptions.RegexMatchError:
        pyautogui.alert("Get me the correct URL manhh!!")
    except pytube.exceptions.VideoUnavailable:
        pyautogui.alert("The video is unavailable manhh!!")
    except:
        pyautogui.alert("Life sucks. So as our code too. Come back again buddy!!")

url = "https://www.youtube.com/watch?v=aWzlQ2N6"
folderPath = "/home/boss/Downloads"
download(url,folderPath)
