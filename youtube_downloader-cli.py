import time
from src import downloader
import gettext
import os

# run in console if new translations are includes:
# msgfmt -o i18n/de/LC_MESSAGES/messages.mo i18n/de/LC_MESSAGES/messages.po
# msgfmt -o i18n/en/LC_MESSAGES/messages.mo i18n/en/LC_MESSAGES/messages.po

LOCALE = os.getenv('LANG', 'de-DE')
_ = gettext.translation('messages', localedir='i18n', languages=[LOCALE]).gettext

if __name__ == '__main__':
    link = input(_("Parse the video link here: "))
    format = input(_("MP3 or MP4? "))

    if format.lower() == "mp3":
        print(_("starting the download ..."))
        start = time.perf_counter()
        success = downloader.downloadMP3(link)
        if success:
            stop = time.perf_counter()
            print(_("Successfully downloaded the MP3 video"))
            print(f"The download the video in {stop - start:0.4f} seconds")

    elif format.lower() == "mp4":
        print(_("starting the download ..."))
        start = time.perf_counter()
        success = downloader.downloadMP4(link, quality="highest")
        if success:
            stop = time.perf_counter()
            print(_("Successfully downloaded the MP4 video"))
            print(f"The download the video in {stop - start:0.4f} seconds")
    else:
        exit(-1)
