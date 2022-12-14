from pytube import YouTube
import os


def downloadsPathWindows() -> str:
    """
    :return:  returns the Windows Downloads path
    """
    username = os.getlogin()
    paths = f"C:\\Users\\{username}\\Download"
    return paths


def downloadsPathLinux() -> str:
    """
    :return:  returns the Linux Downloads path
    """
    home = os.path.expanduser("~")
    return os.path.join(home, "Downloads")


def getDownloadsPath() -> str:
    """
    This will return either the Windows or Linux download path, depending on what you are using
    :return: the paths to your Downloads directory
    """
    if os.name == "nt":
        return downloadsPathWindows()
    else:
        return downloadsPathLinux()


def downloadMP3(link: str) -> bool:
    """
    This will download a youtube video as a MP3 file
    The file will be stored in the Downloads directory

    :param link: link to the youtube video MP3
    :return: True if the video was successfully downloaded, False if not
    """
    video = YouTube(link)
    video = video.streams.get_audio_only()
    try:
        downloads_dir = getDownloadsPath()
        output_file = video.download(output_path=downloads_dir, skip_existing=True)
        base, ext = os.path.splitext(output_file)
        new_file = base + ".mp3"
        os.rename(output_file, new_file)
    except:
        print("Error occurred while downloading the MP3")
        exit(-1)
    return True


def downloadMP4(link: str, quality="720p") -> bool:
    """
    This will download a youtube video as a MP4 file
    The file will be stored in the Downloads directory

    :param quality: optional parameter for the quality of the video
    :param link: link to the youtube video MP4
    :return: True if the video was successfully downloaded, False if not
    """
    video = YouTube(link)
    # video = video.streams.get_by_resolution(quality)

    try:
        downloads_dir = getDownloadsPath()
        if quality == "highest":
            video = video.streams.get_highest_resolution()
            video.download(output_path=downloads_dir, skip_existing=True)
        elif quality == "lowest":
            video = video.streams.get_lowest_resolution()
            video.download(output_path=downloads_dir, skip_existing=True)
        else:
            video = video.streams.filter(res=quality).first().download(output_path=downloads_dir, skip_existing=True)
    except:
        print("Error occurred while downloading the MP3")
        exit(-1)
    return True
