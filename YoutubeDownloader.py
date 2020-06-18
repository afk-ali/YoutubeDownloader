try:
    from pytube import YouTube
except:
  print("An error with the module has occurred")

def option():
    print("Welcome to the youtube downloader!")

    options = input("Would you like to download the audio or video of the file?: ")

    while options.lower() != 'audio' and options.lower() != 'video':
        options = input("Please enter the correct options (audio or video): ")

    if options.lower() == 'audio':
        audio()
    elif options.lower() == 'video':
        video()

def video():
    user_link = input("\nEnter the link of the video: ")
    yt_link = YouTube(' ' + user_link + ' ')

    for x in yt_link.streams.filter(file_extension='mp4'):
            print(x)

    yt_itag = input("\nEnter the itag number: ")

    download(yt_link, yt_itag)

def audio():
    user_link = input("\nEnter the link of the audio: ")
    yt_link = YouTube(' ' + user_link + ' ')

    for x in yt_link.streams.filter(only_audio=True):
            print(x)
    
    yt_itag = input("\nEnter the itag number: ")

    download(yt_link, yt_itag)

def download(yt_link, yt_itag):
    yt_video = yt_link.streams.get_by_itag(yt_itag)
    print(yt_video)
    
    path = input("\nEnter path: ")
    yt_video.download(path)

    print("\nDownloading " + yt_link.title)

option()