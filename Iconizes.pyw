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
import Iconize
import Help

### command line:
#ffmpeg -i in.mp3 -i icon.png -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" out.mp3
            




class Iconizers(tk.Frame):
    def __init__(self, master, **arg):
        tk.Frame.__init__(self, master, **arg)

        ######################################################################
        line=1

        
        ### directory
        #bt
        tk.Button(self, text="Directory:", fg='purple', \
                  command=Help.docDir, relief='flat')\
                  .grid(column=1, row=line, sticky='e')
        #entry
        self.en_dir=tk.Entry(self, width=120, insertbackground='purple', \
                             selectbackground='purple4')
        self.en_dir.grid(column=2, row=line, sticky='w')
        #bt pick
        self.bt_pick_dir_ico=tk.PhotoImage(file='img/selectFolder.gif')
        self.bt_pick_dir=tk.Button(self, text="Pick Folder", \
                                   image=self.bt_pick_dir_ico, \
                                   command=self.get_dir)
        self.bt_pick_dir.grid(row=line, column=3, padx=0)
        line+=1
        ##ext
        #bt
        tk.Button(self, text="Ext.:", fg='red', \
                  command=Help.docExt, relief='flat')\
                  .grid(column=1, row=line, sticky='e')
        #spinner
        self.sp_ext=tk.Spinbox(self, insertbackground='red', width=10, \
                               selectbackground='red4',\
                               values=('.mp3','.aac','.wma','.flac','.oga'))
        self.sp_ext.grid(row=line, column=2, sticky='w')
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
        self.bt_pick_img_ico=tk.PhotoImage(file='img/selectImage-Multi.gif')
        self.bt_pick_img=tk.Button(self, text="Pick image", \
                                   image=self.bt_pick_img_ico, \
                                   command=self.get_img)
        self.bt_pick_img.grid(row=line, column=3, padx=0)
        line+=1
        
        ### start
        self.bt_start_ico=tk.PhotoImage(file='img/engines.gif')
        self.bt_start=tk.Button(self, text="Start", \
                                   image=self.bt_start_ico, \
                                   command=self.start)
        self.bt_start.grid(row=line, column=1, columnspan=3)

        

        
    def _disp_(self, txt, param='std'):
        print(param+':')
        print(txt)

    def get_dir(self, event=None):
        dir_name = tkinter.filedialog.askdirectory(title='Album directory', \
                                                   mustexist=True)
        self.en_dir.delete(0, 'end')
        self.en_dir.insert(0, dir_name)
        #auto-load image if possible
        try:
            os.chdir(dir_name)
        except:
            pass
        else:
            for file in os.listdir():
                if file[-4:].lower() in ('.png', '.jpg', 'jpeg', '.ico'):
                    self.en_img.delete(0, 'end')
                    self.en_img.insert(0, dir_name+'/'+file)
    
    def get_img(self, event=None):
        icon_types=[("Images", '*.png;*.jpg;*.jpeg;*.ico'), ("All", '*')]
        img_name = tkinter.filedialog.askopenfilename(title='Icon image', \
                                                      filetypes=icon_types)
        self.en_img.delete(0, 'end')
        self.en_img.insert(0, img_name)

    def start(self, event=None):
        print()
        try:
            path=self.en_dir.get()
            os.chdir(path)
        except:
            self._disp_("Folder error", 'err')
        else:
            ext=self.sp_ext.get()
            lext=len(ext)
            image_path=self.en_img.get()
            if not os.path.isfile(image_path):
                self._disp_("Image file is not valid", 'err')
            else:
                files = os.listdir()
                for file in files:
                    if file[-lext:]==ext:
                        #rename as a dummy file
                        file_in=path+'/'+file
                        file_out=path+'/_'+file
                        #process
                        cmd='ffmpeg -i "'+file_in+'" -i "'+image_path+'" -map 0:0 -map 1:0 -c copy \
-id3v2_version 3 -metadata:s:v title="Album cover" \
-metadata:s:v comment="Cover (front)" "'+file_out+'"'
                        #print(cmd)
                        popen=subprocess.Popen(cmd, shell=True)
                        overwrite(file_out, file_in)

    def single(self, ev=None):
        self.master.destroy()
        Iconize.main()
                        



def overwrite(old, new):
    t_del = Timer(2.0, lambda: os.remove(new))
    t_ren = Timer(3.0, lambda: os.rename(old, new))
    t_del.start()
    t_ren.start()
    




def main():
    #root
    root=tk.Tk()
    root.title('Iconizes')
    root.iconbitmap('img/Iconizes-256.ico')

    #main app
    iconizers=Iconizers(root, padx=3, pady=3)
    iconizers.pack()

    #menu
    menuBar = Menu.menuIconize(root, \
                               commandStartMulti=iconizers.bell, \
                               commandStartSingle=iconizers.single, \

                               commandRun=iconizers.start, \
                               commandSelectImg=iconizers.get_img, \
                               commandSelectDir=iconizers.get_dir, \
                               commandSelectMusic=None,\

                               commandDoc=Help.docMulti, \
                               commandDocImg=Help.docImg, \
                               commandDocDir=Help.docDir, \
                               commandDocMusic=None, \
                               
                               commandAboutSoft=Help.aboutSoft, \
                               commandAboutMe=Help.aboutMe, \

                               multi=True)
    root.config(menu=menuBar.menu_bar)


    #loop
    root.mainloop()
    


if __name__=='__main__':
    main()
    

