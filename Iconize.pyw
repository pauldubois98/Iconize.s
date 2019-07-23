#GUI
import tkinter as tk
import tkinter.filedialog
#sys
import os
import subprocess
from threading import Timer
from threading import Thread
#perso modules
import Menu
import Iconizes
import Help

### command line:
#ffmpeg -i in.mp3 -i icon.png -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" out.mp3
            




class Iconizer(tk.Frame):
    def __init__(self, master, **arg):
        tk.Frame.__init__(self, master, **arg)

        ######################################################################
        line=1

        
        ### single file
        #bt
        tk.Button(self, text="Music:", fg='red', \
                  command=Help.docMusic, relief='flat')\
                  .grid(column=1, row=line, sticky='e')
        #entry
        self.en_music=tk.Entry(self, width=120, insertbackground='red', \
                               selectbackground='red4')
        self.en_music.grid(column=2, row=line, sticky='w')

        #bt pick
        self.bt_pick_music_ico=tk.PhotoImage(file='img/selectMusic.gif')
        self.bt_pick_music=tk.Button(self, text="Pick Single Music file", \
                                   image=self.bt_pick_music_ico, \
                                   command=self.get_music)
        self.bt_pick_music.grid(row=line, column=3, padx=0)
        line+=1

        ### image
        tk.Button(self, text="Image:", fg='orange', \
                  command=Help.docImg, relief='flat')\
                  .grid(column=1, row=line, sticky='e')
        #entry
        self.en_img=tk.Entry(self, width=120, insertbackground='orange', \
                             selectbackground='orange4')
        self.en_img.grid(column=2, row=line, sticky='w')
        #bt pick
        self.bt_pick_img_ico=tk.PhotoImage(file='img/selectImage-Single.gif')
        self.bt_pick_img=tk.Button(self, text="Pick image", \
                                   image=self.bt_pick_img_ico, \
                                   command=self.get_img)
        self.bt_pick_img.grid(row=line, column=3, padx=0)
        line+=1
        
        ### start
        self.bt_start_ico=tk.PhotoImage(file='img/engine.gif')
        self.bt_start=tk.Button(self, text="Start", \
                                   image=self.bt_start_ico, \
                                   command=self.start)
        self.bt_start.grid(row=line, column=1, columnspan=3)

        

        
    def _disp_(self, txt, param='std'):
        print(param+':')
        print(txt)

    def get_music(self, event=None):
        music_types=[("Music", '*.mp3;*.aac;*.wma;*.flac;*.oga'), ("All", '*')]
        file_name = tkinter.filedialog.askopenfilename(title='Single File', \
                                                       filetypes=music_types)
        self.en_music.delete(0, 'end')
        self.en_music.insert(0, file_name)
    
    def get_img(self, event=None):
        icon_types=[("Images", '*.png;*.jpg;*.jpeg;*.ico'), ("All", '*')]
        img_name = tkinter.filedialog.askopenfilename(title='Icon image', \
                                                      filetypes=icon_types)
        self.en_img.delete(0, 'end')
        self.en_img.insert(0, img_name)

    def start(self, event=None):
        music_path=self.en_music.get()
        image_path=self.en_img.get()
        if not os.path.isfile(music_path):
            self._disp_("Music file is not valid", 'err')
        elif not os.path.isfile(image_path):
            self._disp_("Image file is not valid", 'err')
        else:
            #rename as a dummy file
            file_out=music_path[:-4]+'-temp_copy'+music_path[-4:]
            #process
            cmd='ffmpeg -i "'+music_path+'" -i "'+image_path+'" \
-map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" \
-metadata:s:v comment="Cover (front)" "'+file_out+'"'
            #print(cmd)
            popen=subprocess.Popen(cmd, shell=True)
            print(file_out, '=>', music_path)
            overwrite(file_out, music_path)
            #delete
            self.en_music.delete(0, 'end')

    def multi(self, ev=None):
        self.master.destroy()
        Iconizes.main()
            



def overwrite(old, new):
    t_del = Timer(2.0, lambda: os.remove(new))
    t_ren = Timer(3.0, lambda: os.rename(old, new))
    t_del.start()
    t_ren.start()





def main():
    #root
    root=tk.Tk()
    root.title('Iconize')
    root.iconbitmap('img/Iconize-256.ico')

    #main app
    iconizer=Iconizer(root, padx=3, pady=3)
    iconizer.pack()

    #menu
    menuBar = Menu.menuIconize(root, \
                               commandStartMulti=iconizer.multi, \
                               commandStartSingle=iconizer.bell, \

                               commandRun=iconizer.start, \
                               commandSelectImg=iconizer.get_img, \
                               commandSelectDir=None, \
                               commandSelectMusic=iconizer.get_music,\

                               commandDoc=Help.docSingle, \
                               commandDocImg=Help.docImg, \
                               commandDocDir=None, \
                               commandDocMusic=Help.docMusic, \
                               
                               commandAboutSoft=Help.aboutSoft, \
                               commandAboutMe=Help.aboutMe, \

                               multi=False)
    root.config(menu=menuBar.menu_bar)

    #loop
    root.mainloop()
    


if __name__=='__main__':
    main()
    
