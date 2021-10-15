# Imports
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import webbrowser


class OpenURLs:
    """Primary class for UI with operations defined as methods"""
    def __init__(self, root):
        """Iinitialize the UI components and place them in grid"""
        self.root = root # root object
        
        p1 = tk.PhotoImage(file='logo.png') # Window Icon file
        self.root.iconphoto(False, p1)
        
        self.root.title("Open URLs") # Set Title
        self.root.resizable(0, 0) # Prohibit resizing of the window
        
        ttk.Label(self.root, text="Enter URLs:",
                  font=("Calibri", 25, 'bold')).grid(column=0, row=0) # Top Label
        
        ttk.Label(self.root, text="(Each URL should be in a new line)",
                  font=("Bold", 9)).grid(column=0, row=1) # Instructional Label
        
        self.urls_list = ScrolledText(self.root, wrap=tk.WORD,
                                      width=125, height=8,
                                      font=("Calibri", 11)) # Scrollable text input component    
        self.urls_list.grid(column=0, row=2, pady=10, padx=10)
        
        self.open_urls_btn = tk.Button(
            self.root, text='Open URLs', command=self.open_urls) # This button opens the URLs
        self.open_urls_btn.grid(column=0, row=3, pady=10, padx=10)

    def open_urls(self):
        """Fetch the URLs and open them in browser"""
        self.urls = self.urls_list.get('1.0', tk.END)
        for url in self.urls.split('\n'):
            if url:
                webbrowser.open(url)
        self.root.destroy() # Close the application after all URLs have been opened


root = tk.Tk()
window = OpenURLs(root)
root.mainloop()
