#GUI
import tkinter as tk
from PIL import ImageTk, Image
#non-blocking
from threading import Thread
#work
import webbrowser


def HelpWindow(w_title='Help', title='Specific Help', \
               text="You'll find help in here", icon=None, color='black'):
    root=tk.Tk()
    root.title(w_title)
    if not icon is None:
        root.iconbitmap(icon)

    mainFrame = tk.Frame(root, bg='white')
    mainFrame.pack()
    
    tk.Label(mainFrame, text=title, font=('TkDefaultFont', 20), \
             bg='white', fg=color).pack(padx=30, pady=0)
    tk.Label(mainFrame, text=text, font=('TkDefaultFont', 12), \
             bg='white', fg='black', justify='left').pack(padx=20, pady=10)
    Thread(target=root.mainloop)

def docFFmpeg():
    root=tk.Tk()
    root.title("What is FFmpeg?")
    root.iconbitmap('img/ffmpeg.ico')

    mainFrame = tk.Frame(root, bg='white')
    mainFrame.pack()
    
    tk.Label(mainFrame, text="FFmpeg", font=('TkDefaultFont', 20), \
             bg='white', fg='green').pack(padx=30, pady=0)
    tk.Label(mainFrame, text="\
FFmpeg is a free and open-source project consisting of a vast software suite \n\
of libraries and programs for handling video, audio, and other multimedia \n\
files and streams. At its core is the FFmpeg program itself, designed for \n\
command-line-based processing of video and audio files, and widely used for\n\
format transcoding, basic editing (trimming and concatenation), video \n\
scaling, video post-production effects, and standards compliance (SMPTE, ITU).\n\
FFmpeg includes libavcodec, an audio/video codec library used by many \n\
commercial and free software products.\n\
FFmpeg is published under the GNU Lesser General Public License 2.1+ or GNU \n\
General Public License 2+ (depending on which options are enabled).\
", font=('TkDefaultFont', 12), justify='left', \
             bg='white', fg='black').pack(padx=5, pady=10)

    tk.Button(mainFrame, text='FFmpeg', fg='green', \
              command=lambda: webbrowser.open("https://ffmpeg.org/")).pack()

    Thread(target=root.mainloop)

def docMulti():
    root=tk.Tk()
    root.title("Iconizers")
    root.iconbitmap('img/Iconizes-256.ico')

    mainFrame = tk.Frame(root, bg='white')
    mainFrame.pack()

    line=1
    tk.Label(mainFrame, text="Iconizers", font=('TkDefaultFont', 20), \
             bg='white', fg='purple')\
             .grid(column=1, columnspan=2, padx=30, pady=0)
    tk.Label(mainFrame, text="\
Iconizes & Iconize enable you to add icon to mp3 files.\n\
You can do that file by file with Iconize, \
or a full folder at a time with Iconizes.\n\
It is based on FFmpeg, you might need to install it.", \
             font=('TkDefaultFont', 12), justify='left', \
             bg='white', fg='black')\
             .grid(column=1, columnspan=2, padx=5, pady=10)

    tk.Button(mainFrame, text='FFmpeg', \
              command=lambda: webbrowser.open("https://ffmpeg.org/"))\
              .grid(row=10, column=1, sticky='e')
    tk.Button(mainFrame, text='What is FFmpeg?', bitmap='info', \
              command=docFFmpeg)\
              .grid(row=10, column=2, sticky='w')

    Thread(target=root.mainloop)

def docSingle():
    root=tk.Tk()
    root.title("Iconizer")
    root.iconbitmap('img/Iconize-256.ico')

    mainFrame = tk.Frame(root, bg='white')
    mainFrame.pack()

    line=1
    tk.Label(mainFrame, text="Iconizer", font=('TkDefaultFont', 20), \
             bg='white', fg='red')\
             .grid(column=1, columnspan=2, padx=30, pady=0)
    tk.Label(mainFrame, text="\
Iconizes & Iconize enable you to add icon to mp3 files.\n\
You can do that file by file with Iconize, \
or a full folder at a time with Iconizes.\n\
It is based on FFmpeg, you might need to install it.", \
             font=('TkDefaultFont', 12), justify='left', \
             bg='white', fg='black')\
             .grid(column=1, columnspan=2, padx=5, pady=10)

    tk.Button(mainFrame, text='FFmpeg', \
              command=lambda: webbrowser.open("https://ffmpeg.org/"))\
              .grid(row=10, column=1, sticky='e')
    tk.Button(mainFrame, text='What is FFmpeg?', bitmap='info', \
              command=docFFmpeg)\
              .grid(row=10, column=2, sticky='w')

    Thread(target=root.mainloop)

def docImg():
    txt="\
Select the image that you want to use as an icon.\n\
Use an image format (as .png .jpeg .jpg .ico)."
    HelpWindow("Image", "Select Icon Image", txt, \
               'img/selectImage.ico', 'dim grey')

def docDir():
    txt="Select the folder where all music files \
will get the selected image as an icon."
    HelpWindow("Folder", "Select Folder", txt, \
               'img/selectFolder.ico', 'dim grey')

def docExt():
    txt="Select the files extensions to be considered as music files.\n\
Such files in the folder will get the selected image as an icon."
    HelpWindow("Extension", "Select Extension", txt, \
               'img/selectFolder.ico', 'dim grey')

def docMusic():
    txt="\
Select the music file that you want to add an icon on.\n\
Use a music format (as .mp3 .acc .wma .flac .oga)."
    HelpWindow("Music", "Select Music File", txt, \
               'img/selectMusic.ico', 'dim grey')
    

def aboutSoft():
    webbrowser.open("https://fr.wikipedia.org/wiki/Fourmi_de_Langton")

def aboutMe():
    webbrowser.open("https://pauldubois98.github.io")



if __name__=='__main__':
    HelpWindow()
    
##    docMulti()
##    docSingle()
##    docImg()
##    docDir()
##    docExt()
##    docMusic()



