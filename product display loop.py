import customtkinter as ctk
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

dairystab = ctk.CTk()
dairystab.title('Cart')
dairystab.geometry('500x550')
dairystab.configure(fg_color='#1D1D1D')
dairystab.attributes('-fullscreen', True)

lbl = ctk.CTkLabel(dairystab, text='Dairy', font=('Helvetica', 40), fg_color='#1D1D1D', text_color='#FFFFFF')
lbl.place(x=100, y=10)

scroll_frame = ctk.CTkScrollableFrame(dairystab, height=650, width=1210, fg_color='#1D1D1D', corner_radius=40, border_width=3)
scroll_frame.place(x=5, y=80)
anframe=ctk.CTkLabel(scroll_frame,text='',width=1110,height=1400)
anframe.pack()

products = [
    'Product1', 'Product2', 'Product3', 'Product4', 'Product5',
    'Product6', 'Product7', 'Product8', 'Product9', 'Product10',
    'Product11', 'Product12'
]

positions = [
    (10, 10), (600, 10), (10, 290), (600, 290), (10, 570), (600, 570),
    (10, 850), (600, 850), (10, 1130), (600, 1130), (10, 1410), (600, 1410)
]

for i, product in enumerate(products):
    product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=550, height=250, fg_color='#811331', corner_radius=20)
    product_label.place(x=positions[i][0], y=positions[i][1])
    
    image_label = ctk.CTkLabel(product_label, text=product, height=200, width=200, corner_radius=20, fg_color='#ffffff', font=('Helvetica', 50))
    image_label.place(x=20, y=20)

dairystab.mainloop()