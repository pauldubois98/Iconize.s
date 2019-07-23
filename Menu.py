import tkinter as tk

#classe barre de menu type pour un jeu
class menuIconize(tk.Menu):
    def __init__(self, boss=None, \
                 commandStartMulti=None, commandStartSingle=None, \
                 
                 commandRun=None, commandSelectImg=None, \
                 commandSelectDir=None, commandSelectMusic=None,\
                 
                 commandDoc=None, commandDocImg=None, commandDocDir=None, \
                 commandDocMusic=None, \
                 
                 commandAboutSoft=None, commandAboutMe=None, \

                 multi=True):
        ###MENUS
        self.menu_bar=tk.Menu(boss)
        
        ## Iconization Menu
        self.menu_iconization=tk.Menu(self.menu_bar, tearoff=0)
        self.menu_iconization.add_command(label="Iconizes", \
                                          activebackground='purple', \
                                          command=commandStartMulti)
        self.menu_iconization.add_command(label="Iconize", \
                                          activebackground='red', \
                                          command=commandStartSingle)
        self.menu_iconization.add_separator()
        self.menu_iconization.add_command(label="Quitter", \
                                          activebackground='black', \
                                          command=boss.destroy)
        #cascade
        self.menu_bar.add_cascade(label="Iconization", \
                                  menu=self.menu_iconization)
        
        ## Control Menu
        self.menu_controls=tk.Menu(self.menu_bar, tearoff=0)
        self.menu_controls.add_command(label="Run", \
                                       accelerator='Ctrl-R', \
                                       activebackground='yellow',\
                                       activeforeground='black',\
                                       command=commandRun)
        self.menu_controls.add_command(label="Select Image", \
                                       accelerator='Ctrl-I', \
                                       activebackground='orange',\
                                       activeforeground='black',\
                                       command=commandSelectImg)
        if multi:
            self.menu_controls.add_command(label="Select Folder", \
                                           accelerator='Ctrl-F', \
                                           activebackground='purple',\
                                           activeforeground='black',\
                                           command=commandSelectDir)
        else:
            self.menu_controls.add_command(label="Select Music", \
                                           accelerator='Ctrl-M', \
                                           activebackground='red',\
                                           activeforeground='black',\
                                           command=commandSelectMusic)

        #cascade
        self.menu_bar.add_cascade(label="Commands", menu=self.menu_controls)
        
        ## Help Menu
        self.menu_help=tk.Menu(self.menu_bar, tearoff=0)
        self.menu_help.add_command(label="General Use", \
                                       activebackground='yellow',\
                                       activeforeground='black',\
                                       command=commandDoc)
        self.menu_help.add_command(label="Help Image", \
                                       activebackground='orange',\
                                       command=commandDocImg)
        if multi:
            self.menu_help.add_command(label="Help Folder", \
                                           activebackground='purple',\
                                           command=commandDocDir)
        else:
            self.menu_help.add_command(label="Help Music", \
                                           activebackground='red',\
                                           command=commandDocMusic)
        #cascade
        self.menu_bar.add_cascade(label="Help", menu=self.menu_help)
        
        ## About Menu
        self.menu_about=tk.Menu(self.menu_bar, tearoff=0)
        self.menu_about.add_command(label="About this software",
                                   activebackground='dark grey', \
                                   activeforeground='black', \
                                   command=commandAboutSoft)
        self.menu_about.add_command(label="About me", \
                                   activebackground='black', \
                                   command=commandAboutMe)
        #cascade
        self.menu_bar.add_cascade(label="About", menu=self.menu_about)


        
        
        ###RACCOURCITS
        boss.bind("<Control-r>", commandRun)
        boss.bind("<Control-i>", commandSelectImg)
                
        if multi:
            boss.bind("<Control-f>", commandSelectDir)
        else:
            boss.bind("<Control-m>", commandSelectMusic)
        
        
        

if __name__=='__main__':
    def m():
        print('2+')
    def s():
        print('1')

    
    fen=tk.Tk()
    
    Fr=tk.Frame(fen, width=500, height=400)
    Fr.pack()
    
    menuBar=menuIconize(fen, m, s, commandDoc=lambda a: print('doc'))
    fen.config(menu=menuBar.menu_bar)
    
    fen.mainloop()
