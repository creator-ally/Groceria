import customtkinter as ctk
import tkinter as tk,tkinter
from tkinter import *
from PIL import Image,ImageTk
prof=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/user-interface.png"),size=(300,300)) 
window=ctk.CTk()
window.configure(fg_color='#1D1D1D')
profile_backlabel=ctk.CTkLabel(window,text='',fg_color='white',height=700,width=1200,corner_radius=50)
profile_backlabel.place(x=40,y=20)
prof_image=ctk.CTkButton(profile_backlabel,text='',image=prof,corner_radius=50,state=DISABLED,fg_color='white',border_width=4)
prof_image.place(x=100,y=40)
window.mainloop()