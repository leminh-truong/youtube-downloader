import tkinter as tk
import youtubedownload as dl
from functools import partial   

window = tk.Tk()
window.title("Youtube Downloader")

url = tk.StringVar()
def get_link():
    youtubeURL = url.get()
    dl.youtube_downloader(youtubeURL)
    url.set("")


frame1 = tk.Frame()
label1 = tk.Label(master=frame1, 
    text="Youtube Downloader", 
    fg="white", 
    bg="red", 
    relief=tk.FLAT, 
    borderwidth=5)
label1.pack(fill=tk.BOTH)
frame1.pack(fill=tk.BOTH, expand=True)

frame2 = tk.Frame()
entry2 = tk.Entry(master=frame2, 
    relief=tk.SUNKEN, 
    textvariable = url,
    borderwidth=5)
entry2.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
button2 = tk.Button(master=frame2, text="Click to download", command=get_link)
button2.pack(fill=tk.BOTH, expand=True,side=tk.LEFT)
frame2.pack(fill=tk.BOTH, expand=True)
window.mainloop()

