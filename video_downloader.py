import pytube
import re

cleanning_regex= r"""['"@:=|`+! $\/}?{&*><#%]"""

def clean_filename(video_title) :
    clean_name = re.sub(cleanning_regex,"_",video_title)
    return clean_name

def get_streams(url, output_path) :

    video = pytube.YouTube(url=url)
    for stream in video.streams :
        print(stream)
        print("-------------------")


def download_audio(url, output_path, format):
    try :
        video = pytube.YouTube(url=url)
        stream = video.streams.get_by_itag(251)
        filename = clean_filename(video.title)
        print("starting download : {}".format(filename + format))
        stream.download(output_path=output_path,filename = filename + format)
    except :
        print("{} download failed".format(filename + format))
        print("-------------------------------")

def download_video(url, output_path, format):
    try:
        video = pytube.YouTube(url=url)
        stream = video.streams.get_by_itag(22)
        filename = clean_filename(video.title)
        print("starting download : {}".format(filename + format))
        stream.download(output_path=output_path,filename = filename + format)
        print("{} downloaded".format(filename + format))
        print("-------------------------------")
    except :
        print("{} download failed".format(filename + format))
        print("-------------------------------")

def download_playlist_audio(url, output_path, format, label):
    playlist = pytube.Playlist(url)
    for video in playlist.videos :
        try :
            stream = video.streams.get_by_itag(251)
            filename = clean_filename(video.title)
            #label.setText("{} \n Download Ongoing".format(filename))
            print("starting download : {}".format(filename + format))
            stream.download(output_path=output_path, filename=filename + format)
            print("{} downloaded".format(filename + format))
            print("-------------------------------")
        except :
            print("{} download failed".format(filename + format))
            print("-------------------------------")
            #label.setText("{} \n Download Failed".format(filename))

def download_playlist_video(url, output_path, format, label):
    playlist = pytube.Playlist(url)
    for video in playlist.videos :
        try :
            stream = video.streams.get_by_itag(251)
            filename = clean_filename(video.title)
            #label.setText("{} \n Download Ongoing".format(filename))
            print("starting download : {}".format(filename + format))
            stream.download(output_path=output_path, filename=filename + format)
            print("{} downloaded".format(filename + format))
            print("-------------------------------")
        except :
            print("{} download failed".format(filename + format))
            print("-------------------------------")
            #label.setText("{} \n Download Failed".format(filename))
