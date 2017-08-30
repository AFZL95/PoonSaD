# ======================
# imports
# ======================

import tkinter as tk
from tkinter import ttk


class PoonSaD():
    def __init__(self):
        # Constructor area
        self.win = tk.Tk()

        self.win.title("PoonSad")
        self.create_widgets()

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def create_widgets(self):

        # ~ Tab Control Stuff here
        tab_control = ttk.Notebook(self.win)  # Create Tab Control

        tab1 = ttk.Frame(tab_control)  # Create a tab
        tab_control.add(tab1, text='Download Area')  # Add the tab

        tab2 = ttk.Frame(tab_control)  # Add a second tab
        tab_control.add(tab2, text='Preview Area')  # Make second tab visible

        tab_control.pack(expand=1, fill="both")  # Pack to make visible

        # Creating a container frame to hold all other widgets
        self.my_first_frame = ttk.LabelFrame(tab1, text="Download Area")
        self.my_first_frame.grid(row=0, column=0, padx=8, pady=4)

        # Creating a Menu Bar
        menuBar = tk.Menu(self.my_first_frame)
        self.win.config(menu=menuBar)

        # Add menu items
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_command(label="Exit")
        menuBar.add_cascade(label="File", menu=fileMenu)

        # Add another Menu to the Menu Bar and an item
        helpMenu = tk.Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About")
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # welcoming users
        ttk.Label(self.my_first_frame,
                  text="Welcome to PoonSaD,if U in Iran, U need a VPN connection to proceed,").grid(column=0, row=0,
                                                                                                    sticky='W')

        # adding widgets
        url_label = ttk.Label(self.my_first_frame, width=10, text="Pic url:")
        url_label.grid(row=1, column=0, sticky='W', padx=20, pady=20)

        url_entry = ttk.Entry(self.my_first_frame, width=50)  # used to get url for pic
        url_entry.grid(row=1, column=0, sticky='W', padx=80, pady=20)

        savepath_label = ttk.Label(self.my_first_frame, width=10, text="File Path:")
        savepath_label.grid(row=2, column=0, sticky='W', padx=20, pady=10)

        savepath_entry = ttk.Entry(self.my_first_frame, width=50)  # used to get save path
        savepath_entry.grid(row=2, column=0, sticky='W', padx=80, pady=10)

        btn_download = ttk.Button(self.my_first_frame, text="Download", command='')
        btn_download.grid(row=3, column=0)
        btn_quit = ttk.Button(self.my_first_frame, text="Quit", command='')
        btn_quit.grid(row=3, column=1)

        # progress bar area
        progress_bar = ttk.Progressbar(self.my_first_frame, orient="horizontal", length=200, mode="indeterminate")
        progress_bar.grid(row=4, column=0)
        progress_bar.grid()

        progress_bar["maximum"] = 100
        progress_bar["value"] = 20

        progress_bar.start()

        v = tk.StringVar()  # from Tkinter
        self._label = v
        status = tk.Label(self.win, textvariable=self._label)

        self.win.mainloop()


# ======================
# Start GUI
# ======================
if __name__ == '__main__':
    app = PoonSaD()
