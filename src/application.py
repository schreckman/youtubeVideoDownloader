import customtkinter as tk
import gettext
import os
import time
from src import downloader

tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")

LOCALE = os.getenv('LANG', 'de-DE')
_ = gettext.translation('messages', localedir='i18n', languages=[LOCALE]).gettext


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        # variables:
        self.language: str = "english"
        self.link: str = ""
        self.quality = "720p"

        # configure window
        self.title("Youtube Video Downloader")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create tabview
        self.tabview = tk.CTkTabview(master=self)
        self.tabview.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.tabview.add(_("Downloader"))
        self.tabview.add(_("Settings"))
        self.tabview.add(_("About"))

        # Downloader window
        self.appearance_mode_label_downloader1 = tk.CTkLabel(self.tabview.tab(_("Downloader")),
                                                             text=_("Current Link: ") + self.link,
                                                             anchor="w")
        self.appearance_mode_label_downloader1.grid(row=1, column=0, padx=20, pady=(10, 0))

        self.string_input_button = tk.CTkButton(master=self.tabview.tab(_("Downloader")),
                                                text=_("Insert link"),
                                                command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.string_input_button_mp3 = tk.CTkButton(master=self.tabview.tab(_("Downloader")),
                                                    text=_("Download MP3"),
                                                    command=self.download_MP3_event)
        self.string_input_button_mp3.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.string_input_button_mp4 = tk.CTkButton(master=self.tabview.tab(_("Downloader")),
                                                    text=_("Download MP4"),
                                                    command=self.download_MP4_event)
        self.string_input_button_mp4.grid(row=4, column=0, padx=20, pady=(10, 10))

        # Settings Window
        self.appearance_mode_label_settings1 = tk.CTkLabel(self.tabview.tab(_("Settings")),
                                                           text=_("Appearance Mode:"),
                                                           anchor="w")
        self.appearance_mode_label_settings1.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = tk.CTkOptionMenu(self.tabview.tab(_("Settings")),
                                                           values=["Light", "Dark", "System"],
                                                           command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionmenu.set("System")

        self.optionmenu_Settings1 = tk.CTkOptionMenu(self.tabview.tab(_("Settings")),
                                                    values=["144p", "240p", "360p", "480p", "720p"],
                                                    command=self.change_video_quality_event)
        self.optionmenu_Settings1.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.optionmenu_Settings1.set(_("Video Quality"))

    def download_MP3_event(self):
        if self.link.__contains__("youtube"):
            print("called MP3")
            start = time.perf_counter()
            success = downloader.downloadMP3(self.link)
            if success:
                stop = time.perf_counter()
                print(_("Successfully downloaded the MP3 video"))
                print(f"The download the video in {stop - start:0.4f} seconds")

    def download_MP4_event(self):
        if self.link.__contains__("youtube"):
            print("called MP4")
            start = time.perf_counter()
            success = downloader.downloadMP4(self.link, quality=self.quality)
            if success:
                stop = time.perf_counter()
                print(_("Successfully downloaded the MP4 video"))
                print(f"The download the video in {stop - start:0.4f} seconds")

    def open_input_dialog_event(self):
        dialog = tk.CTkInputDialog(text=_("Parse the video link here: "), title=_("Link"))
        self.link = dialog.get_input()
        print("Link: ", self.link)
        self.appearance_mode_label_downloader1.destroy()
        self.appearance_mode_label_downloader1 = tk.CTkLabel(self.tabview.tab(_("Downloader")),
                                                             text=_("Current Link: ")
                                                                  + self.link, anchor="w")
        self.appearance_mode_label_downloader1.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.update_idletasks()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        tk.set_appearance_mode(new_appearance_mode)

    def change_video_quality_event(self, quality: str):
        self.quality = quality
