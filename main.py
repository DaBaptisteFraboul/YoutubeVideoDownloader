import PyQt5.QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import pytube
import sys
import app_stylesheet
import video_downloader
import re

explanation_text = """
- You can use this application to download videos from Youtube
- You can download entire playlists and videos with their url :
    - Simply copy/paste the url in the field
    - Select your output file
    - Select your file format
    - Press Download
- Youtube prevent access to age-restricted video stream, you 
can't download them with this app. 
- You can download up to 720p, higher resolutions have their 
video and audio stream separated. Auto merge feature to come
- You can download the audio only with .wav and .mp3 format
- If this window freeze when processing, dont quit.
Enjoy !                         Github : DaBaptisteFraboul
"""
class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setGeometry(200,200,500,500)
        self.window.setWindowTitle("Youtube - Video Downloader")
        self.window.setWindowIcon(PyQt5.QtGui.QIcon("Icon.png"))
        self.window.setFixedSize(500,500)
        self.window.show()
        self.UI_setup()
        self.app.setStyleSheet(app_stylesheet.stylesheet_1)
        self.video = None
        self.download_format = ".wav"
        self.output_path = r"C:/Users/Default/Downloads"
        self.is_playlist = None
        sys.exit(self.app.exec_())


    def UI_setup(self):
        self.background = QtWidgets.QWidget(self.window)
        self.background.setGeometry(0,0,500,500)
        self.background.show()

        self.Video_label = QtWidgets.QLabel(self.window)
        self.Video_label.setGeometry(5,5,50,10)
        self.Video_label.setText("Video title and errors")
        self.Video_label.setStyleSheet("font-style : italic;")
        self.Video_label.adjustSize()
        self.Video_label.show()

        self.Input_url = QtWidgets.QLineEdit(self.window)
        self.Input_url.setGeometry(5,30,350,30)
        self.Input_url.textChanged.connect(self.get_video_title)
        self.Input_url.show()

        self.url_label = QtWidgets.QLabel(self.window)
        self.url_label.setGeometry(360,35,50,10)
        self.url_label.setText("playlist / video")
        self.url_label.setStyleSheet("font-weight : bold;")
        self.url_label.adjustSize()
        self.url_label.show()

        """self.extract_audio_checkbox = QtWidgets.QCheckBox(self.window)
        self.extract_audio_checkbox.setGeometry(5,65,30,100)
        self.extract_audio_checkbox.setText("Extract Audio only")
        self.extract_audio_checkbox.adjustSize()
        self.extract_audio_checkbox.setChecked(False)
        semf.extract_audio_checkbox.show()"""


        self.file_format_list = QtWidgets.QListWidget(self.window)
        self.file_format_list.setGeometry(5, 100,70,120)
        self.file_format_list.insertItem(0, ".mp3")
        self.file_format_list.insertItem(1, ".wav")
        self.file_format_list.insertItem(2, ".mov")
        self.file_format_list.insertItem(3, ".mp4")
        self.file_format_list.clicked.connect(self.set_download_format)
        self.file_format_list.show()

        self.output_path_input = QtWidgets.QLineEdit(self.window)
        self.output_path_input.setText("C:/Users/Default/Downloads")
        self.output_path_input.setGeometry(5,65,350,30)
        self.output_path_input.show()

        self.browse_button = QtWidgets.QPushButton(self.window)
        self.browse_button.setText("Output Folder")
        self.browse_button.setGeometry(360,64,40,30)
        self.browse_button.adjustSize()
        self.browse_button.clicked.connect(self.browse_output_folder)
        self.browse_button.show()

        self.download_button = QtWidgets.QPushButton(self.window)
        self.download_button.setText("Download")
        self.download_button.setStyleSheet("font-size:10pt ; font-weight : bold ;")
        self.download_button.setGeometry(100,100, 350,125)
        self.download_button.clicked.connect(self.Download)
        self.download_button.show()

        self.download_status = QtWidgets.QLabel(self.window)
        self.download_status.setGeometry(5,205,265,490)
        #self.download_status.setStyleSheet("font-weight : bold ;")
        self.download_status.setText(explanation_text)
        self.download_status.adjustSize()
        self.download_status.show()

    def Download(self):
        url = self.Input_url.text()
        regex_playlist = r"playlist\?list"
        print(bool(re.search(regex_playlist, url)))
        if bool(re.search(regex_playlist, url)) :
            self.download_playlist()
        else :
            self.download_video()


    def download_playlist(self):
        if self.download_format == '.mp3' or self.download_format == '.wav' :
            print("starting playlist download")
            video_downloader.download_playlist_audio(self.Input_url.text(), self.output_path, self.download_format, self.download_status)



    def download_video(self):
        #self.download_status.setText("Donwload ongoing")
        #self.download_status.adjustSize()
        #self.download_status.update()
        if self.download_format == '.mp4' or self.download_format == '.mov' :
            try :
                video_downloader.download_video(self.Input_url.text(),self.output_path,self.download_format)
            except:
                print("Error during Download")
        else :
            try:
                video_downloader.download_audio(self.Input_url.text(),self.output_path,self.download_format)
            except :
                print("Error during Download")

    def get_video_title(self):
        url = self.Input_url.text()
        regex_playlist = r"playlist\?list"
        if bool(re.search(regex_playlist, url)):
            try :
                playlist = pytube.Playlist(url)
                self.Video_label.setText("Playlist : {}".format(playlist.title))
                self.Video_label.adjustSize()
            except :
                self.Video_label.setText("Error, not a valid url")
        else :
            try :
                video = pytube.YouTube(url)
                self.Video_label.setText(video.title)
                self.Video_label.adjustSize()
            except :
                self.Video_label.setText("Error, not a valid url")

    def set_download_format(self):
        item = self.file_format_list.currentItem()
        self.download_format = item.text()

    def browse_output_folder(self):
        self.output_path = QtWidgets.QFileDialog.getExistingDirectory(self.window,"Select output directory")
        self.output_path_input.setText(self.output_path)

app = Application()

