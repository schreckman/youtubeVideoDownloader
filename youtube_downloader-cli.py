import time
import downloader

if __name__ == '__main__':
    link = input("Parse the video link here: ")
    format = input("MP3 or MP4? ")

    if format.lower() == "mp3":
        print("starting the download ...")
        start = time.perf_counter()
        success = downloader.downloadMP3(link)
        if success:
            stop = time.perf_counter()
            print("Successfully downloaded the MP3 video")
            print(f"The download the video in {stop - start:0.4f} seconds")

    elif format.lower() == "mp4":
        print("starting the download ...")
        start = time.perf_counter()
        success = downloader.downloadMP4(link)
        if success:
            stop = time.perf_counter()
            print("Successfully downloaded the MP4 video")
            print(f"The download the video in {stop - start:0.4f} seconds")
    else:
        exit(-1)
