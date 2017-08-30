# ======================
# imports
# ======================
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox



class PoonSaD():
    def __init__(self):
        # Constructor area
        self.win = tk.Tk()
        self.win.title("PoonSad")
        self.win.maxsize(450, 255)
        self.win.minsize(450, 255)
        print("Hellow there !")
        self.create_widgets()


    def create_widgets(self):

        # ~ Tab Control Stuff here
        tab_control = ttk.Notebook(self.win)  # Create Tab Control

        tab1 = ttk.Frame(tab_control)  # Create a tab
        tab_control.add(tab1, text='Download Area')  # Add the tab

        tab2 = ttk.Frame(tab_control)  # Add a second tab
        tab_control.add(tab2, text='Check things Area')  # Make second tab visible

        tab_control.pack(expand=1, fill="both")  # Pack to make visible

        # Creating a container frame to hold all widgets
        self.my_first_frame = ttk.LabelFrame(tab1, text="Download Area")
        self.my_first_frame.grid(row=0, column=0, padx=8, pady=(10,0))


        # Creating a Menu Bar
        menuBar = tk.Menu(self.my_first_frame)
        self.win.config(menu=menuBar)

        # welcoming users
        ttk.Label(self.my_first_frame,
                  text="Welcome to PoonSaD, if you are in Iran, U need a VPN connection to proceed").grid(column=0, row=0,
                                                                                                    sticky='W')

        # adding widgets
        url_label = tk.Label(self.my_first_frame, width=10, text="Pic url:")
        url_label.grid(row=1, column=0, sticky='W', pady=10)

        self.url_entry = tk.Entry(self.my_first_frame, width=56)  # used to get url for pic
        self.url_entry.grid(row=1, column=0, sticky='W', padx=70, pady=10)

        savepath_label = tk.Label(self.my_first_frame, width=10, text="File Path:")
        savepath_label.grid(row=2, column=0, sticky='W', pady=10)

        self.savepath_entry = tk.Entry(self.my_first_frame, width=52)  # used to get save path
        self.savepath_entry.grid(row=2, column=0, sticky='W', padx=70, pady=10)

        btn_setpath = tk.Button(self.my_first_frame, text="...", width=2, command=self.setpath)
        btn_setpath.grid(row=2, column=0, sticky='W',padx=388, pady=10)

        # progress bar area
        progress_bar = ttk.Progressbar(self.my_first_frame, orient="horizontal", length=400, mode="indeterminate")
        progress_bar.grid(row=3, column=0,sticky='W',padx=13)
        progress_bar.grid()

        progress_bar["maximum"] = 100
        progress_bar["value"] = 20

        progress_bar.start()

        btn_download = tk.Button(self.my_first_frame, text="Download",width=40, command=self.download)
        btn_download.grid(row=4, column=0, sticky='W', padx = 10 , pady=10)
        btn_quit = tk.Button(self.my_first_frame, text="Quit",width=15, command=self.on_exit)
        btn_quit.grid(row=4, column=0, sticky='W', padx = 300 , pady=10)


        # Status area

        v = tk.StringVar()  # from Tkinter
        self._label = v
        status = tk.Label(self.win, textvariable=self._label)
        # status.grid()
        # status.grid(row=4, pady=20, sticky='W')
        status.pack()
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


        self.win.mainloop()

    def setpath(self):
        self.savepath_entry.delete(0, END)
        self.savepath_entry.insert(0, filedialog.askdirectory() + '/')

    def on_exit(self):
        # self.win.quit()
        self.win.destroy()
        # exit()

    def about_me(self):
        messagebox.showinfo("About PoonSaD", "Hello All Fellows !!! It's an Illegal attempt to save '500px.com' pictures on python supported device. "
                                             "for legal prosecution saty in touch with afzl95.github.io  ")

    def download(self):
        import urllib.request
        import urllib.parse
        import urllib.error
        link = self.url_entry.get().strip()
        print("the link that you Entered is: "+ str(link))
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
                self._label.set("photo downloaded on: {0}".format(name))
                print("photo downloaded on: {0}".format(name))
            except Exception as e:
                self._label.set("download fail! {0}".format(e))
                print("download fail! {0}".format(e))
        else:
            self._label.set('please input url and save path')
            print("please input url and save path")


# ======================
# Start GUI
# ======================
if __name__ == '__main__':
    app = PoonSaD()
