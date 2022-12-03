# Importing Required Modules & libraries
from tkinter import *
import os
import sys
import vlc
from pathlib import Path
import random
from PIL import Image,ImageTk
import time
import pandas as pd

# Initiating VLC
Instance = vlc.Instance()
# Initiating VLC Player
player = Instance.media_player_new()



# Defining MusicPlayer Class
class MusicPlayer(object):
  # Defining Constructor
  def __init__(self,root,emotionStr):
    self.root = root
    # Title of the window
    self.root.title("Emotion Music Player")
    # Window Geometry
    self.root.geometry("1000x700+100+50")
    # Declaring track Variable
    self.track = StringVar()
    # Declaring Status Variable
    self.status = StringVar()
    # Creating Track Frame for Song label & status label
    trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=620,height=100)
    # Inserting Song Track Label
    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Status Label
    trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",18,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=5,pady=5)
    # Creating Button Frame
    buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    buttonframe.place(x=0,y=100,width=620,height=100)
    # Inserting Play Button
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Pause Button
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=10,pady=5)
    # Inserting Unpause Button
    playbtn = Button(buttonframe,text="SHUFFLE",command=self.shufflesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=10,pady=5)
    # Inserting Stop Button
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=10,pady=5)
    playbtn = Button(buttonframe,text="NEXT",command=self.nextsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=4,padx=10,pady=5)
    # Creating Playlist Frame
    songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    songsframe.place(x=600,y=0,width=400,height=200)
    # Inserting scrollbar
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    # Inserting Playlist listbox
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
    # Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
    # Changing Directory for fetching Songs
    os.chdir(str(Path(__file__).parent.absolute())+"\songs\\"+emotionStr+"\\")
    # Fetching Songs
    songtracks = os.listdir()
    self.songtracks = songtracks
    # Inserting Songs into Playlist
    for track in songtracks:
      self.playlist.insert(END,track)
    if(player.is_playing() == 0):
      ranSong = random.choice(self.songtracks)
      self.pos = self.songtracks.index(ranSong)
      self.track.set(ranSong)
      self.status.set("-Playing "+emotionStr)
      Media = Instance.media_new(ranSong)
      player.set_media(Media)
      player.play()

  
  #================ code starts here
    '''
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH1 = os.path.join(ROOT_DIR, 'quotes','image1.jpg')
    CONFIG_PATH2 = os.path.join(ROOT_DIR, 'quotes','image2.png')
    
    self.image1 = ImageTk.PhotoImage(file=CONFIG_PATH1)
    self.lbl1 = Label(self.root, image=self.image1, bd=0)
    self.lbl1.place(x = 500,y = 500, width=500, height=400)
    self.image2 = ImageTk.PhotoImage(file=CONFIG_PATH2)
    self.lbl2 = Label(self.root, image=self.image2, bd=0)
    self.lbl2.place(x = 400, y = 300, width=500, height=400)
    '''

    QuoteChangebtn = Button(self.root,text="Change Quote",command=self.ChangeQuote,width=12,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").place(x=10,y=200)
    '''
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH1 = os.path.join(ROOT_DIR, 'quotes')
    CONFIG_PATH2 = os.path.join(ROOT_DIR, 'quotes','image2.png')
    AllQuotes = os.listdir(CONFIG_PATH1)
    for i in AllQuotes:
      CONFIG_PATH2 = os.path.join(ROOT_DIR, 'quotes',i)
      self.image1 = ImageTk.PhotoImage(file=CONFIG_PATH2)
      self.lbl1 = Label(self.root, image=self.image1, bd=0)
      self.lbl1.place(x = 100,y = 400, width=800, height=500)
      print(CONFIG_PATH2)
      time.sleep(3)
    '''
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH1 = os.path.join(ROOT_DIR, 'quotes')
    AllQuotes = os.listdir(CONFIG_PATH1)
    randomQuote = random.choice(AllQuotes)
    CONFIG_PATH2 = os.path.join(ROOT_DIR, 'quotes',randomQuote)
    img_old=Image.open(CONFIG_PATH2)
    img_resized=img_old.resize((400,400))
    self.image1 = ImageTk.PhotoImage(img_resized)
    self.lbl1 = Label(self.root, image=self.image1, bd=0)
    self.lbl1.place(x = 200,y = 200, width=500, height=500)
    
    def StatsExcel(self):
      ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
      df = pd.read_csv(ROOT_DIR+'/EmotionStats.csv')
      print(df)
      if(emotionStr == "Neutral"):
        df.iloc[0, 4] = df.iloc[0, 4] + 1
      print("After")
      print(df)
      df.to_csv(ROOT_DIR+'/EmotionStats.csv', mode='w', header=True, index=False)

    StatsExcel(self)

  #================
      
  # Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    self.track.set(self.playlist.get(ACTIVE))
    # Displaying Status
    self.status.set("-Playing")
    # Loading Selected Song
    Media = Instance.media_new(self.playlist.get(ACTIVE))
    player.set_media(Media)
    player.play()
   # pygame.mixer.music.play()
  def stopsong(self):
    # Displaying Status
    self.status.set("-Stopped")
    # Stopped Song
    player.stop()
    self.root.destroy()
    os.chdir(str(Path(__file__).parent.absolute()))
    os.system("python emotions.py")
    #quit()

  def pausesong(self):
    # Displaying Status
    self.status.set("-Paused")
    # Paused Song
    player.pause()
  """ def unpausesong(self):
    # Displaying Status
    self.status.set("-Playing")
    # Playing back Song
    player.pause() """

  def nextsong(self):
    i=0
    while i< len(self.songtracks):
      if i == self.pos:
        i = i+1
        if i >= len(self.songtracks):
          i= 0
        nsong = self.songtracks[i]
        self.pos = i
      i = i + 1
    player.stop()
    self.track.set(nsong)
    # Loading Selected Song
    Media = Instance.media_new(nsong)
    player.set_media(Media)
    player.play()
    #Quote
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH1 = os.path.join(ROOT_DIR, 'quotes')
    AllQuotes = os.listdir(CONFIG_PATH1)
    randomQuote = random.choice(AllQuotes)
    CONFIG_PATH2 = os.path.join(ROOT_DIR, 'quotes',randomQuote)
    img_old=Image.open(CONFIG_PATH2)
    img_resized=img_old.resize((400,400))
    self.image1 = ImageTk.PhotoImage(img_resized)
    self.lbl1 = Label(self.root, image=self.image1, bd=0)
    self.lbl1.place(x = 200,y = 200, width=500, height=500)
    self.StatsExcel()

  def shufflesong(self):
    self.status.set("-Shuffle Play")
    song2 =random.choice(self.songtracks)
    self.pos = self.songtracks.index(song2)
    player.stop()
    self.track.set(song2)
    # Loading Selected Song
    Media = Instance.media_new(song2)
    player.set_media(Media)
    player.play()

  def ChangeQuote(self):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH1 = os.path.join(ROOT_DIR, 'quotes')
    AllQuotes = os.listdir(CONFIG_PATH1)
    randomQuote = random.choice(AllQuotes)
    CONFIG_PATH2 = os.path.join(ROOT_DIR, 'quotes',randomQuote)
    img_old=Image.open(CONFIG_PATH2)
    img_resized=img_old.resize((400,400))
    self.image1 = ImageTk.PhotoImage(img_resized)
    self.lbl1 = Label(self.root, image=self.image1, bd=0)
    self.lbl1.place(x = 200,y = 200, width=500, height=500)
    #self.root.destroy()
    #root = Tk()
    #MusicPlayer(root,"Happy")
    #self.shufflesong()    
    #root.mainloop()
    
# Creating TK Container
#root = Tk()
# Passing Root to MusicPlayer Class
# Root Window Looping
#root.mainloop()



