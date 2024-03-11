from customtkinter import *
from customtkinter import filedialog as fd
from PIL import ImageTk, Image
import tkinter as tk
import cv2
import base64


FaceClass = cv2.CascadeClassifier('faceclassifier.xml')
PlateClass = cv2.CascadeClassifier('haarclassifierplate.xml')


api_url ='api_url'

Blackbox = CTk()
Blackbox.title('Computer Vision')
Blackbox.geometry('960x360')
Blackbox.resizable(False, False)

set_appearance_mode("system")

Paused = False
PausedText = None

def show_frame():
   global Paused, PausedText
   if not Paused:
       ret, frame = cap.read()
       if ret:
           frame = cv2.resize(frame, (640, 360))
           frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
           CamImg = Image.fromarray(frame)
           ImgTk = ImageTk.PhotoImage(image=CamImg)
           CamFeed.ImgTk = ImgTk
           CamFeed.configure(image=ImgTk)
       if PausedText:
           PausedText.destroy()
           PausedText = None
   else:
       if not PausedText:
           PausedText = CTkLabel(Blackbox, text="Feed Paused", font=("Arial", 20))
           PausedText.pack()
   Blackbox.after(10, show_frame)

cap = cv2.VideoCapture(0)

CamFeed = CTkLabel(Blackbox,text='')
CamFeed.pack(side=LEFT)

show_frame()

LogoButton = CTkFrame(Blackbox)
LogoButton.pack()

logo = ImageTk.PhotoImage(Image.open("logo.png"))
LogoLabel = CTkLabel(LogoButton, image=logo, text='')
LogoLabel.pack()

ButtonScroll = CTkScrollableFrame(LogoButton, width= 320, height= 210)
ButtonScroll.pack()

ButtGrid = CTkFrame(ButtonScroll)
ButtGrid.pack()

ProgBar = CTkProgressBar(LogoButton, progress_color='darkred', width= 300, mode= 'determinate', determinate_speed=(0.5))
ProgBar.set(0)
ProgBar.pack(pady = 5)

def OpenFile():
   fd.askopenfilename()

SelectFile = CTkButton(ButtGrid, text='Select File', width=140, height=100, command=OpenFile,
                        corner_radius= 15, border_width= 2, fg_color='darkred', hover_color='red', font=("Arial",15))
SelectFile.grid(row=0, column=0, sticky=W+E, padx = 3, )

def pause_video():
   global Paused
   Paused = not Paused

BttnPause = CTkButton(ButtGrid, text='Pause/Resume\nFeed', width=140, height=100, command=pause_video,
                   corner_radius= 15, border_width= 2, fg_color='darkred', hover_color='red', font=("Arial",15))
BttnPause.grid(row=0, column=1, sticky=W+E, padx = 3, pady = 3)

def RunDetection():
    global Paused, PausedText
    if not Paused:
        return 

    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = FaceClass.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        plates = PlateClass.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in plates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        
        frame = cv2.resize(frame, (640, 360))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        CamImg = Image.fromarray(frame)
        ImgTk = ImageTk.PhotoImage(image=CamImg)
        CamFeed.ImgTk = ImgTk
        CamFeed.configure(image=ImgTk)

    if len(faces) == 1 or len(plates) == 1:
        tk.messagebox.showinfo("Match Found", "User authenticated successfully!")
    else:
        tk.messagebox.showinfo("No Match Found", "User not found in the database.")


BttnDetection = CTkButton(ButtGrid, text='Run Detection', width=140, height=100,
                   corner_radius= 15, border_width= 2, fg_color='darkred', hover_color='red', font=("Arial",15), command= RunDetection)
BttnDetection.grid(row=1, column=0, sticky=W+E, padx = 3, pady = 3)

def StartProcessing():
    if ProgBar.get() > 0:
        ProgBar.stop()
        ProgBar.set(0)

        ProgBarStop = CTkToplevel()
        ProgBarStop.after(2500,lambda:ProgBarStop.destroy())
        ProgBarStop.title("")
        ProgBarStop.geometry('200x100')

        BarStop = CTkLabel(ProgBarStop, text='Processing Stopped', font=('Arial',20))
        BarStop.pack(pady=25)

    else:
        ProgBar.start()

ProcessButt = CTkButton(ButtGrid, text='Start/Stop\nProcessing', width=140, height=100
                  , corner_radius= 15, border_width= 2, fg_color='darkred', hover_color='red', font=("Arial",15), command= StartProcessing)
ProcessButt.grid(row=1, column=1, sticky=W+E, padx = 3, pady = 3)

def TriggerNoti():
    tk.messagebox.showinfo('Notification','Military alert: Match found!')
    

ButtTrigger = CTkButton(ButtGrid, text='Trigger\nNotification', width=140, height=100
                  , corner_radius= 15, border_width= 2, fg_color='darkred', hover_color='red', font=("Arial",15),command=TriggerNoti)
ButtTrigger.grid(row=2, column=0, sticky=W+E, padx = 3, pady = 3,)

def ShowNotiName():
    name = f' Hello, {EnterName.get()}!'
    tk.messagebox.showinfo('Notification',name,)


ButtName = CTkButton(ButtGrid, text='Submit\nName', width=140, height=100
                  , corner_radius= 15, border_width= 2, fg_color='darkred', hover_color='red', font=("Arial",15), command=ShowNotiName)
ButtName.grid(row=2, column=1, sticky=W+E, padx = 3, pady = 3)

EnterName = CTkEntry(ButtonScroll, placeholder_text='Enter Name')
EnterName.pack()

Blackbox.mainloop()

cap.release()
