# ======================
# imports
# ======================
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import time


class PoonSaD():
    def __init__(self):
        # Constructor area
        self.win = tk.Tk()
        self.win.title("PoonSad")
        self.win.maxsize(450, 255)
        self.win.minsize(450, 255)

        v = tk.StringVar()  # from Tkinter
        self._label = v

        print("Hellow there! program is going to start !")
        self.create_widgets()

    def create_widgets(self):

        # ~ Tab Control Stuff here
        tab_control = ttk.Notebook(self.win)  # Create Tab Control

        tab1 = ttk.Frame(tab_control)  # Create a tab
        tab_control.add(tab1, text='Download Area')  # Add the tab

        tab2 = ttk.Frame(tab_control)  # Add a second tab
        tab_control.add(tab2, text='Check things Area')  # Make second tab visible

        tab_control.pack(expand=1, fill="both")  # Pack to make visible

        # Creating a container frame to hold all initial widgets
        self.my_first_frame = ttk.LabelFrame(tab1, text="Download Area")
        self.my_first_frame.grid(row=0, column=0, padx=8, pady=(10, 0))

        # Creating a Menu Bar
        menuBar = tk.Menu(self.my_first_frame)
        self.win.config(menu=menuBar)

        # welcoming users
        ttk.Label(self.my_first_frame,
                  text="Welcome to PoonSaD, if you are in Iran, U need a VPN connection to proceed").grid(column=0,
                                                                                                          row=0,
                                                                                                          sticky='W')

        # adding widgets
        url_label = tk.Label(self.my_first_frame, width=10, text="Image url:")
        url_label.grid(row=1, column=0, sticky='W', pady=10)

        self.url_entry = tk.Entry(self.my_first_frame, width=56)  # used to get url for pic
        self.url_entry.grid(row=1, column=0, sticky='W', padx=70, pady=10)

        savepath_label = tk.Label(self.my_first_frame, width=10, text="Save Path:")
        savepath_label.grid(row=2, column=0, sticky='W', pady=10)

        self.savepath_entry = tk.Entry(self.my_first_frame, width=52)  # used to get save path
        self.savepath_entry.grid(row=2, column=0, sticky='W', padx=70, pady=10)

        btn_setpath = tk.Button(self.my_first_frame, text="...", width=2, command=self.setpath,
                                activebackground="#33B5E5")
        btn_setpath.grid(row=2, column=0, sticky='W', padx=388, pady=10)

        # progress bar area
        progress_bar = ttk.Progressbar(self.my_first_frame, orient="horizontal", length=400, mode="indeterminate")
        progress_bar.grid(row=3, column=0, sticky='W', padx=13)
        progress_bar.grid()

        progress_bar["maximum"] = 100
        progress_bar["value"] = 20

        progress_bar.start()

        btn_download = tk.Button(self.my_first_frame, text="Download", width=40,
                                 command=self.download,
                                 activebackground="#33B5E5")
        btn_download.grid(row=4, column=0, sticky='W', padx=10, pady=10)
        btn_quit = tk.Button(self.my_first_frame, text="Quit", width=15, command=self.on_exit,
                             activebackground="#33B5E5")
        btn_quit.grid(row=4, column=0, sticky='W', padx=300, pady=10)

        # Status area for first tab
        # v = tk.StringVar()  # from Tkinter
        # self._label = v
        status = tk.Label(self.win, textvariable=self._label)
        status.pack()

        self._label.set("Specify the URL and choose a saving path, then press download to continue...")

        # Creating a Menu Bar
        menuBar = tk.Menu(tab1)
        self.win.config(menu=menuBar)

        # Add menu items
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Exit", command=self.on_exit)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # Add another Menu to the Menu Bar and an item
        helpMenu = tk.Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About", command=self.about_me)
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # ********* SECOND TAB AREA *********

        # Creating a container frame to hold second tab widgets widgets
        self.my_second_frame = ttk.LabelFrame(tab2, text="Checktion Area")
        self.my_second_frame.grid(row=0, column=0, padx=8, pady=(10, 0))

        # informing users
        ttk.Label(self.my_second_frame,
                  text="Here you can firstly check "
                       "is there any suitable connection to '500px' or not.").grid(column=0, row=0, sticky='W')

        # add a scroll text
        scr = scrolledtext.ScrolledText(self.my_second_frame, width=50, height=6, wrap=tk.WORD)
        scr.grid(row=1, column=0)

        # connection check
        import requests
        url = 'https://500px.com'
        try:
            r = requests.get(url)
            r.raise_for_status()
            scr.insert(INSERT, "everything is alright, you can proceed with your downloading...", 'my_msg')
            scr.tag_config('my_msg', foreground='blue')
        except requests.ConnectionError as err:
            print(err)
            scr.insert(INSERT,
                       "500px is not reachable, probably because of Internet censorship, or a weak connection! ",
                       'my_msg')
            scr.tag_config('my_msg', foreground='blue')
            scr.insert(INSERT, err)
            # scr.insert(END, "this is the END")
            # sys.exit(1)

        # create a huge button for displaying recent picture downloaded
        show_pic_btn = tk.Button(self.my_second_frame, text="Show me the recent picture I downloaded", width=60,
                                 command=self.showing_photo, activebackground="#33B5E5")
        show_pic_btn.grid(row=2, column=0, pady=5)

        # create a huge button for displaying recent picture directory
        show_pic_dir = tk.Button(self.my_second_frame, text="Show me the recent downloading directory", width=60,
                                 command=self.showing_photo_dir, activebackground="#33B5E5")
        show_pic_dir.grid(row=3, column=0)

        self.win.mainloop()

    def showing_photo_dir(self):
        import os
        path = self.savepath_entry.get()
        # print(path)
        os.startfile(path, 'open')
    def showing_photo(self):
        from PIL import Image
        import re
        path = str(self.savepath_entry.get()) + ".jpg"
        # print(path)

        try:
            im = Image.open(path)
            im.show()
        except: self._label.set("You haven't downloaded any pictures yet :(")

        # im = Image.open(path)
        # im.show()

    def setpath(self):
        self.savepath_entry.delete(0, END)
        self.savepath_entry.insert(0, filedialog.askdirectory() + '/')

    def on_exit(self):
        # self.win.quit()
        self.win.destroy()
        # exit()

    def about_me(self):
        messagebox.showinfo("About PoonSaD",
                            "Hello All Fellows !!! It's an Illegal attempt to save '500px.com' pictures on python supported device. "
                            "for legal prosecution saty in touch with afzl95.github.io  ")


    def download(self):
        import urllib.request
        import urllib.parse
        import urllib.error
        link = self.url_entry.get().strip()
        # print("the link that you Entered is: "+ str(link))
        name = self.savepath_entry.get().strip()

        if link and name:
            try:
                f = urllib.request.urlopen(link)
                pageResource = f.read().decode()
                pattern = "{\"size\":2048,\"url\":"
                start = pageResource.find(pattern) + 20
                end = pageResource.find("\"", start + 2)
                imgLink = pageResource[start:end]
                imgLink = imgLink.replace("\\", "")
                urllib.request.urlretrieve(imgLink, name + '.jpg')
                self._label.set("Photo downloaded on: {0}".format(name))
                # print("Photo downloaded on: {0}".format(name))
            except Exception as e:
                self._label.set("Download fail! {0}".format(e))
                # print("Download fail! {0}".format(e))
        else:
            self._label.set('Please input url and save path')
            # print("Please input url and save path")


# ======================
# Start GUI
# ======================
if __name__ == '__main__':
    app = PoonSaD()
