import tkinter as tk,tkinter
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

window=tkinter.Tk()
window.title( 'Login Page')
window.geometry('600x500')
a='#811331'
window.configure(bg=a)
bg1=ctk.CTkImage(Image.open(r"/storage/emulated/0/Pcs/bg1.png"),size=(1300,800))
bglabel=ctk.CTkLabel(window,text=' ',image=bg1)
bglabel.pack()
fm=ctk.CTkFrame(window,height=700,width=500,fg_color='#FFFFFF',border_color='cyan',border_width=5)

# all images
imge1 = ctk.CTkImage(Image.open(r"/storage/emulated/0/download/logo.png"),size=(250,250))
bckimg =ctk.CTkImage(Image.open(r"/storage/emulated/0/Pcs/back.png"))
crtimg=ctk.CTkImage(Image.open(r"/storage/emulated/0/Pcs/cart.png"),size=(25,25))
setimg=ctk.CTkImage(Image.open(r"/storage/emulated/0/Pcs/set.png"))
profimg=ctk.CTkImage(Image.open(r"/storage/emulated/0/Pcs/prof.png"))
bg2=ctk.CTkImage(Image.open(r"/storage/emulated/0/Pcs/bg2.png"))
lbal=ctk.CTkLabel(fm,image=imge1,text=" ",bg_color='#FFFFFF',corner_radius=50)
lbal.place(x=110,y=5)

#shops main window after login
def checked():
     
         window.withdraw()
         shop=Toplevel()
         tab=Frame(shop ,width=100,height=600,bg="#811331")
         upd=Frame(shop,bg='#811331')
         shop.title('Dashboard')
         shop.geometry('600x500')
         shop.configure(bg='#811331')
         shop.attributes('-fullscreen',True)
         
         #defining the tabs
         
         #cart 
         def cart():
                       shop.withdraw()
                       cart=Toplevel()
                       cart.title('Cart')      
                       cart.geometry('500x600')    
                       cart.configure(bg='#811331')   
                       cart.attributes('-fullscreen', True)   
                       
                       #back button
                       def back():
                                shop.deiconify()
                                cart.destroy()
                       bckbtn=ctk.CTkButton(cart,text=" ",image=bckimg,command=back,height=30,width=30,compound=LEFT,corner_radius=50,fg_color="#FF5F55")
                       
                       #placing widgets in cart tab
                       bckbtn.place(x=20,y=10)
                                 
         #orders
         def ord():
                      shop.withdraw()
                      ordtab=Toplevel()
                      ordtab.title('Orders')
                      ordtab.geometry('600x500')
                      ordtab.configure(bg='#811331')
                      ordtab.attributes('-fullscreen', True)
                     
                      #Labels in order tab
                      orlbl=ctk.CTkLabel(ordtab,text="Orders",fg_color='#FF5F55',font=("Arial",40),corner_radius=20)
                      
                      #back button to home tab
                      def back():
                                shop.deiconify()
                                ordtab.destroy()
                      bckbtn=ctk.CTkButton(ordtab,text=" ",image=bckimg,compound=LEFT,command=back,height=30,width=30,corner_radius=50,fg_color="#FF5F55")          
                     
        
              
              #placing of widgets in order tab
                      orlbl.pack()
                      bckbtn.place(x=20,y=10)
                      
         
         #profile         
         def pro():
              shop.withdraw()        
              protab=Toplevel()
              protab.title('Profile')
              protab.geometry('600x500')
              protab.configure(bg='#811331')
              protab.attributes('-fullscreen', True)
              
              #Labels in profile tab
              ptlbl=ctk.CTkLabel(protab,text="Profile",fg_color='#FF5F55',font=("Arial",40),corner_radius=20)
              #back button to home tab
              def back():
                                shop.deiconify()
                                
              bckbtn=ctk.CTkButton(protab,text=" ",image=bckimg,compound=LEFT,command=back,height=30,width=30,corner_radius=50,fg_color="#FF5F55")
              
              
              #placing of widgets in profile tab
              ptlbl.pack()
              bckbtn.place(x=20,y=10)
    
    
          #coupons
         def cou():
              shop.withdraw()   
              coutab=Toplevel()      
              coutab.title("Coupons") 
              coutab.geometry('600x500')
              coutab.configure(bg='#811331')
              coutab.attributes('-fullscreen', True)
              #Labels in coupons tab
              colbl=ctk.CTkLabel(coutab,text="Coupons",fg_color='#FF5F55',font=("Arial",40),corner_radius=20)
              
               #back button to home tab
              def back():
                                shop.deiconify()
                                
              bckbtn=ctk.CTkButton(coutab,text=" ",image=bckimg,compound=LEFT,command=back,height=30,width=30,corner_radius=50,fg_color="#FF5F55")
              
              
              #placing of widgets in coupons tab
              
              colbl.pack()
              bckbtn.place(x=20,y=10)
 
             #help center
         def hp():
               shop.withdraw()   
               hptab=Toplevel()
               hptab.title("Help center")
               hptab.geometry("600x500")
               hptab.configure(bg='#811331')
               hptab.attributes('-fullscreen', True)
               #Labels in help center tab
               hplbl=ctk.CTkLabel(hptab,text="Help Centet",fg_color='#FF5F55',font=("Arial",40),corner_radius=20)
               #back button to home tab
               def back():
                                shop.deiconify()
                                
               bckbtn=ctk.CTkButton(hptab,text=" ",image=bckimg,compound=LEFT,command=back,height=30,width=30,corner_radius=50,fg_color="#FF5F55")
              
              
              
              #placing of widgets in help center tab
               hplbl.pack()
               bckbtn.place(x=20,y=10)
               
          #settings
         def set():
              shop.withdraw()
              settab=Toplevel()
              settab.title('Settings')
              settab.geometry('600x500')
              settab.configure(bg='#811331')
              settab.attributes('-fullscreen', True)
              #Labels in settings tab
              stlbl=ctk.CTkLabel(settab,text="settings",fg_color='#FF5F55',font=("Arial",40),corner_radius=20)
              
              
              #theme changing 
              def cng():
                  a='#black'
              thmbtn=ctk.CTkButton(master=settab,text="dark",fg_color="#FF5F55",bg_color="#811331",command=cng)
                #back button to home tab
              def back():
                                shop.deiconify()
                                
              bckbtn=ctk.CTkButton(settab,text=" ",image=bckimg,compound=LEFT,command=back,corner_radius=60,height=30,width=30,fg_color="#FF5F55")
              
              
              
              #placing of widgets in settings tab
              stlbl.pack()
              bckbtn.place(x=20,y=10)
              thmbtn.pack()
         
         
         # tabs for the shop in the home page
         orders=ctk.CTkButton(master=tab,text="Orders",fg_color="#FF5F55",font=("Arial",10), corner_radius=20,width=50,height=50, command=ord)
         
         profile=ctk.CTkButton(master=tab,text=" ",fg_color="#FF5F55",font=("Arial",10), corner_radius=20,width=50,height=50,command=pro,image=profimg,compound=LEFT)
         
         coupons=ctk.CTkButton(master=tab,text="Coupons",fg_color="#FF5F55",font=("Arial",10), corner_radius=20,width=50,height=50,command=cou)
         
         hpc=ctk.CTkButton(master=tab,text="Help Center",fg_color="#FF5F55",font=("Arial",10), corner_radius=20,width=50,height=50,command=hp)
         
         settings=ctk.CTkButton(master=tab,text=" ",fg_color="#FF5F55",font=("Arial",10), corner_radius=20,width=50,height=40,command=set,image=setimg,compound=LEFT)
                
         
         #icon buttons on the home page

         search=ctk.CTkEntry(master=shop,corner_radius=20,width=300,height=30)
         
         seabtn=ctk.CTkButton(master=shop,text="search",fg_color="#FF5F55",corner_radius=20,width=50)
         
         crtbtn=ctk.CTkButton(shop,text=" ",image=crtimg,command=cart,compound=LEFT,fg_color="#FF5F55",corner_radius=10,width=25)
         
        #placing the frames 
         tab.place(x=40,y=80)
         tab.pack_propagate(0)
         
         
         #placing the tabs
         orders.pack(pady=30)
         profile.pack(pady=10)
         coupons.pack(pady=30)
         hpc.pack(pady=10)
         settings.pack(pady=30)
         
         #placing the icons on the home page
         search.place(x=300,y=5)
         seabtn.place(x=510,y=5)
         crtbtn.place(x=650,y=5)
         
         shop.mainloop()
  
#variables and login labels
login_label = ctk.CTkLabel(fm,text="Grocery Store",font=("Harlow Solid Italic",20),bg_color='#FFFFFF' , text_color='cyan')
username_label=ctk.CTkLabel(fm,text="Username",bg_color='#FFFFFF',font=("Arial",10) ,text_color='cyan')
username_entry=ctk.CTkEntry(fm,show='+',font=("Arial",10), corner_radius=20,width=400, height=35 ,text_color='cyan')
password_label=ctk.CTkLabel(fm,text="Password",bg_color='#FFFFFF',font=("Arial",10) ,text_color='cyan')
password_entry=ctk.CTkEntry(fm,show='*',font=("Arial",10),corner_radius=20, width=400,height=35 ,text_color='cyan')
login_button = ctk.CTkButton(
    master=fm, 
    text="Login",
    bg_color="#811331",  
    fg_color="#FFFFFF",
    font=("Arial",15),
    corner_radius=20, height =40,width=200, command=checked ,text_color='#00BFFF')
fgpass=ctk.CTkButton(fm,text="forgot password ?",bg_color="#811331",fg_color="#FFFFFF",hover_color='#811311',text_color='cyan',border_color='#00BFFF')
    

# placing widgets on the screen
login_label.place(x=135,y=230)
username_label.place(x=70,y=290)
username_entry.place(x=50,y=320)
password_label.place(x=70,y=360)
password_entry.place(x=50,y=390)
fgpass.place(x=60, y=430)
login_button.place(x=150,y=470)
fm.place(x=700,y=20)
fm.pack_propagate(0)

window.mainloop()