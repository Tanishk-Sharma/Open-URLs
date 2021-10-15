import sys
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import webbrowser


class OpenURLs:
    def __init__(self, root):
        self.root = root
        # in which script is saved
        p1 = tk.PhotoImage(file='logo.png')
        # Setting icon of master window
        self.root.iconphoto(False, p1)
        self.root.title("Open URLs")
        self.root.resizable(0, 0)
        ttk.Label(self.root, text="Enter URLs:",
                  font=("Calibri", 25, 'bold')).grid(column=0, row=0)
        ttk.Label(self.root, text="(Each URL should be in a new line)",
                  font=("Bold", 9)).grid(column=0, row=1)
        self.urls_list = ScrolledText(self.root, wrap=tk.WORD,
                                      width=125, height=8,
                                      font=("Calibri", 11))
        self.urls_list.grid(column=0, row=2, pady=10, padx=10)
        self.save_btn = tk.Button(
            self.root, text='Open URLs', command=self.open_urls)
        self.save_btn.grid(column=0, row=3, pady=10, padx=10)

    def open_urls(self):
        self.urls = self.urls_list.get('1.0', tk.END)
        for url in self.urls.split('\n'):
            if url:
                webbrowser.open(url)
        self.root.destroy()


root = tk.Tk()
window = OpenURLs(root)
root.mainloop()
