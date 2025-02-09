import customtkinter as ctk
import tkinter as tk,tkinter
from tkinter import *
from PIL import Image,ImageTk

#SIGN UP PAGE 
window=ctk.CTk()
window.configure(fg_color='#1D1D1D')
my_font=ctk.CTkFont(family='Vivaldi Italic',size=50)
bg1=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/wpr.png"),size=(450,450))
bglabel=ctk.CTkLabel(window,text="",image=bg1,fg_color='black',bg_color='#1D1D1D',corner_radius=60,height=500,width=500)
bglabel.place(x=700,y=200)
fnt=ctk.CTkFont(family='Vivaldi Italics',size=15)
fnt1=ctk.CTkFont(family='Vivaldi Italics',size=20)

#Images
open=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/open.png"),size=(30,30))
sett=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/gear.png"),size=(50,50))
helpc=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/customer-service.png"),size=(50,50)) 
prof=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/user-interface.png"),size=(50,50)) 
carti=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/user-interface.png"),size=(50,50))
order=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/order.png"),size=(50,50)) 
logoutimg=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/logout.png"),size=(50,50))
menu=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/menu.png"),size=(50,50))
cartt=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/shopcart.png"),size=(50,50))
notify=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/notify.png"),size=(50,50))
seac=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/search.png"),size=(50,50))
fru=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/fruits.png"),size=(80,80))
essen=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/essentials.png"),size=(80,80))
vegtab=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/vegetables.png"),size=(80,80))
dair=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/dairy.png"),size=(80,80))

#login images
insta=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/instagram (1).png"),size=(50,50)) 
google=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/google.png"),size=(50,50)) 
phon=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/phone.png"),size=(50,50)) 
backbutn=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/back-button.png"),size=(50,50)) 

#ALL DEFINED FUCTIONS FOR TAB
def fgpass():
    window.withdraw()
    forgot_tab=Toplevel()
    forgot_tab.configure(bg='#1D1D1D')
    forgot_tab.attributes('-fullscreen',True)
    #FORGOT PASSWORD TAB
    bglbl=ctk.CTkLabel(forgot_tab,text=' ',image=bg,fg_color='#1D1D1D')
    bglbl.place(x=0,y=180)   
    frame2=ctk.CTkLabel(forgot_tab,text=' ',height=600,width=540,bg_color='#1D1D1D',fg_color='#FFFFFF',corner_radius=30)
    frame2.place(x=400,y=50)
    
    
def login():
    window.withdraw()
    login_tab=Toplevel()
    login_tab.configure(bg='#1D1D1D')
    login_tab.attributes('-fullscreen',True)
    #LOGIN TAB
    
    #bg image and logo
    bglbl=ctk.CTkLabel(login_tab,text=' ',fg_color='#1D1D1D')
    bglbl.place(x=0,y=180)
    
    #frame 
    frame2=ctk.CTkLabel(login_tab,text=' ',height=600,width=540,bg_color='#1D1D1D',fg_color='#FFFFFF',corner_radius=30)
    frame2.place(x=400,y=50)
    #buttons and entries
    log_btn=ctk.CTkButton(frame2,text='Login',font=('vivaldi italics',20),height=60,width=220,corner_radius=30,command=checked)
    emadd=ctk.CTkEntry(frame2,height=80,width=490,corner_radius=30,border_width=3)
    pwd=ctk.CTkEntry(frame2,height=80,width=240,corner_radius=30,border_width=3)
    forgot_password_btn=ctk.CTkButton(frame2,text='forgot password ? ',command=fgpass,fg_color='white',text_color='black')
    emadd_lbl=ctk.CTkLabel(emadd,text='Email',text_color='grey',font=('vivaldi italics',10))
    pwd_lbl=ctk.CTkLabel(pwd,text='Password',text_color='grey',font=('vivaldi italics',10))    
    wlbl=ctk.CTkLabel(frame2,text=' Log In',font=('vivaldi italics',40))
    google_button=ctk.CTkButton(frame2,text="",image=google,fg_color='white',hover_color='white',width=50)
    phon_button=ctk.CTkButton(frame2,text="",image=phon,width=50,fg_color='white',hover_color='white')
    insta_button=ctk.CTkButton(frame2,text="",image=insta,width=50,fg_color='white',hover_color='white')
    
    # placing buttons and widgets
    wlbl.place(x=120,y=10)
    emadd_lbl.place(x=20,y=4)
    pwd_lbl.place(x=20,y=4)
    forgot_password_btn.place(x=30,y=260)    
    log_btn.place(x=160,y=290)
    emadd.place(x=20,y=80)
    pwd.place(x=20,y=180)
    google_button.place(x=150,y=400)
    insta_button.place(x=230,y=400)
    phon_button.place(x=310,y=400)

def checked():
    window.withdraw()
    shop = Toplevel()
    btnlbl = ctk.CTkLabel(shop, fg_color='#FFFFFF', text='', corner_radius=50, height=400, width=150)
    upd = Frame(shop, bg='#7C93C3', height=100, width=100)
    shop.title('Dashboard')
    shop.geometry('600x500')
    shop.configure(bg='#1D1D1D')
    shop.attributes('-fullscreen', True)
   
    #fruits
    def fruitpro():
        fruitstab=Toplevel()
        shop.withdraw()
        fruitstab.title('Cart')      
        fruitstab.geometry('500x600')    
        fruitstab.configure(bg='#1D1D1D')   
        fruitstab.attributes('-fullscreen', True)
        lbl=ctk.CTkLabel(fruitstab,text='Fruits',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        lbl.place(x=100,y=10)
        frm=ctk.CTkScrollableFrame(fruitstab,height=720,width=1190,fg_color='#1D1D1D',corner_radius=40)
        frm.place(x=5,y=80)

        products = [
            'Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5', 'Product 6',
            'Product 7', 'Product 8', 'Product 9', 'Product 10', 'Product 11', 'Product 12' ]

        for product in products:
            label = ctk.CTkLabel(frm, text=product, height=250, width=1300, corner_radius=20, fg_color='#811331',                  font=('Helvetica', 50))
            label.pack(pady=10)
        def back():
                                shop.deiconify()
                                fruitstab.destroy()
        bckbtn=ctk.CTkButton(fruitstab,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=5) 
        bckbtn.place(x=10,y=10)
        
        
        
    
     #frame
    utabfrm=ctk.CTkButton(shop,text='',height=595,width=250,fg_color='#811331',corner_radius=40,border_width=5,state=DISABLED)   
    tabfrm = ctk.CTkLabel(shop, text='',height=555, width=220,fg_color='#811331',corner_radius=20,bg_color='#811331')
    anframe1=ctk.CTkScrollableFrame(shop,height=540,width=1150,corner_radius=30,fg_color='#811331')
    anframe=ctk.CTkScrollableFrame(shop,height=540,width=880,corner_radius=30,fg_color='#811331')
    anframe1.place(x=40,y=120)    

#menu button  
    def function_one():
        anframe1.place_forget()
        utabfrm.place(x=37,y=120)
        tabfrm.place(x=48, y=140)       
        anframe.place(x=320,y=120)       
    def function_two():
        utabfrm.place_forget()
        tabfrm.place_forget()
        anframe.place_forget()   
        anframe1.place(x=40,y=120)   
    def click():
        global click_count
        click_count += 1
        if click_count == 1:
            function_one()
        elif click_count == 2:
            function_two()
            click_count = 0
    menubtn=ctk.CTkButton(shop,text='',image=menu,fg_color='#FFFFFF',command=click,corner_radius=20,height=50,width=50,hover_color='#FFFFFF',border_width=3)
    menubtn.place(x=50,y=30)
    
    def vegetabpro():
            vegetablestab=Toplevel()
            shop.withdraw()
            vegetablestab.title('Cart')      
            vegetablestab.geometry('500x600')    
            vegetablestab.configure(bg='#1D1D1D')   
            vegetablestab.attributes('-fullscreen', True)
            lbl=ctk.CTkLabel(vegetablestab,text='Vegetables',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
            lbl.place(x=100,y=10)
            frm=ctk.CTkScrollableFrame(vegetablestab,height=720,width=1190,fg_color='#1D1D1D',corner_radius=40)
            frm.place(x=5,y=80)

            products = [
            'Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5', 'Product 6',
            'Product 7', 'Product 8', 'Product 9', 'Product 10', 'Product 11', 'Product 12' ]

            for product in products:
                label = ctk.CTkLabel(frm, text=product, height=250, width=1300, corner_radius=20, fg_color='#811331',                  font=('Helvetica', 50))
                label.pack(pady=10)
            def back():
                                shop.deiconify()
                                vegetablestab.destroy()
            bckbtn=ctk.CTkButton(vegetablestab,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=5) 
            bckbtn.place(x=10,y=10)
            
    def dairypro():
            dairystab=Toplevel()
            shop.withdraw()
            dairystab.title('Cart')      
            dairystab.geometry('500x600')    
            dairystab.configure(bg='#1D1D1D')   
            dairystab.attributes('-fullscreen', True)
            lbl=ctk.CTkLabel(dairystab,text='Dairy',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
            lbl.place(x=100,y=10)
            frm = ctk.CTkScrollableFrame(dairystab, height=720, width=1190, fg_color='#1D1D1D', corner_radius=40)
            frm.place(x=5, y=80)

            products = [
    'Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5', 'Product 6',
    'Product 7', 'Product 8', 'Product 9', 'Product 10', 'Product 11', 'Product 12'
]

            for i, product in enumerate(products):
                label = ctk.CTkLabel(frm, text=product, height=250, width=600, corner_radius=20, fg_color='#811331',                    font=('Helvetica', 50))
                label.grid(row=i//2, column=i%2, padx=10, pady=10)

            def back():
                    shop.deiconify()
                    dairystab.destroy()

            bckbtn = ctk.CTkButton(dairystab, text="", command=back, image=backbutn, fg_color='white',                              hover_color='white', height=55, width=55, corner_radius=5)
            bckbtn.place(x=10, y=10)

            
    #supplies 
    def suppliepro():
            suppliestab=Toplevel()
            shop.withdraw()
            suppliestab.title('Cart')      
            suppliestab.geometry('500x600')    
            suppliestab.configure(bg='#1D1D1D')   
            suppliestab.attributes('-fullscreen', True)
            lbl=ctk.CTkLabel(suppliestab,text='Supplies',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
            lbl.place(x=100, y=10)
            frm = ctk.CTkScrollableFrame(suppliestab, height=720, width=1190, fg_color='#1D1D1D', corner_radius=40)
            frm.place(x=5, y=80)

            products = [
    'Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5', 'Product 6',
    'Product 7', 'Product 8', 'Product 9', 'Product 10', 'Product 11', 'Product 12'
]

            for i, product in enumerate(products):
                label = ctk.CTkLabel(frm, text=product, height=250, width=600, corner_radius=20, fg_color='#811331',                    font=('Helvetica', 50))
                label.grid(row=i//2, column=i%2, padx=10, pady=10)

            def back():
                    shop.deiconify()
                    suppliestab.destroy()

            bckbtn = ctk.CTkButton(suppliestab, text="", command=back, image=backbutn, fg_color='white',                              hover_color='white', height=55, width=55, corner_radius=5)
            bckbtn.place(x=10, y=10)

                                  
    #widgets    in sclframe wihout menu button in screen
    offlbl=ctk.CTkLabel(anframe1,text='',image=bg1)
    offlbl.pack()
    sframe=ctk.CTkLabel(anframe1,text='',height=180,width=900,corner_radius=30,fg_color='#1D1D1D')
    sframe.pack(pady=20)
    vegetables=ctk.CTkButton(sframe,text='Veges',image=vegtab,height=140,width=200,fg_color='grey',corner_radius=20,font=fnt1,command=vegetabpro)
    vegetables.place(x=20,y=20)
    fruits=ctk.CTkButton(sframe,text='Fruits',image=fru,height=140,width=200,fg_color='grey',corner_radius=20,font=fnt1,command=fruitpro)
    fruits.place(x=240,y=20)
    dairy=ctk.CTkButton(sframe,text='Dairy',height=140,image=dair,width=200,fg_color='grey',corner_radius=20,font=fnt1,command=dairypro)
    dairy.place(x=460,y=20)
    essentials=ctk.CTkButton(sframe,text='Supplies',image=essen,height=140,width=200,fg_color='grey',corner_radius=20,font=fnt1,command=suppliepro)
    essentials.place(x=680,y=20)
    
    #scrollable frame with menu button on screen
    offlbl=ctk.CTkLabel(anframe,text='',image=bg1)
    offlbl.pack()
    sframe=ctk.CTkLabel(anframe,text='',height=180,width=820,corner_radius=30,fg_color='#1D1D1D')
    sframe.pack(pady=20)
    vegetables=ctk.CTkButton(sframe,text='Veges',image=vegtab,height=140,width=180,fg_color='grey',corner_radius=20,font=fnt,command=vegetabpro)
    vegetables.place(x=15,y=20)
    fruits=ctk.CTkButton(sframe,text='Fruits',image=fru,height=140,width=180,fg_color='grey',corner_radius=20,font=fnt, command=fruitpro)
    fruits.place(x=215,y=20)
    dairy=ctk.CTkButton(sframe,text='Dairy',height=140,image=dair,width=180,fg_color='grey',corner_radius=20,font=fnt,command=dairypro)
    dairy.place(x=415,y=20)
    essentials=ctk.CTkButton(sframe,text='Supplies',image=essen,height=140,width=180,fg_color='grey',corner_radius=20,font=fnt,command=suppliepro)
    essentials.place(x=615,y=20)
       
    # defining the tabs
    def search():
        shop.withdraw()
        search= Toplevel()
        search.title('Cart')      
        search.geometry('500x600')    
        search.configure(bg='#1D1D1D')   
        search.attributes('-fullscreen', True)
        
        #products
        frm=ctk.CTkScrollableFrame(search,height=720,width=1190,fg_color='#1D1D1D',corner_radius=40)
        frm.place(x=5,y=80)

        products = [
            'Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5', 'Product 6',
            'Product 7', 'Product 8', 'Product 9', 'Product 10', 'Product 11', 'Product 12' ]

        for product in products:
            label = ctk.CTkLabel(frm, text=product, height=250, width=1300, corner_radius=20, fg_color='#811331',                  font=('Helvetica', 50))
            s=product
            i=products.index(product)
            if i%2==0:
                s.pack()
            else:
                product.pack(side=left)

        def back():
                                shop.deiconify()
                                search.destroy()
        bckbtn=ctk.CTkButton(search,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=5) 
        bckbtn.place(x=10,y=10)
        
    def notification():
        shop.withdraw()
        notification= Toplevel()
        notification.title('Cart')      
        notification.geometry('500x600')    
        notification.configure(bg='#1D1D1D')   
        notification.attributes('-fullscreen', True)
        lbl=ctk.CTkLabel(notification,text='Notification',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        lbl.place(x=100,y=10)
        def back():
                                shop.deiconify()
                                notification.destroy()
        bckbtn=ctk.CTkButton(notification,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=5) 
        bckbtn.place(x=10,y=10)
    
    def cart():
        backbutn=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/back-button.png"),size=(50,50))
        shop.withdraw()
        cart =Toplevel()
        cart.title('Cart')      
        cart.geometry('500x600')    
        cart.configure(bg='#1D1D1D')   
        cart.attributes('-fullscreen', True)
        lbl=ctk.CTkLabel(cart,text='Cart',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        lbl.place(x=100,y=10)
        def back():
                                global backbutn
                                shop.deiconify()
                                cart.destroy()
        bckbtn=ctk.CTkButton(cart,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=5) 
        bckbtn.place(x=10,y=10)
        
               
    def ord():      
        ordtab = Toplevel()
        ordtab.attributes('-fullscreen', True)        
        ordtab.title('Orders')
        ordtab.geometry('600x500')
        ordtab.configure(bg='#1D1D1D')
        shop.withdraw()
        lbl=ctk.CTkLabel(ordtab,text='Orders',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        lbl.place(x=100,y=10)
        def back():
                                shop.deiconify()
                                ordtab.destroy()
        bckbtn=ctk.CTkButton(ordtab,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=5) 
        bckbtn.place(x=10,y=10)   
        
    def pro():
        shop.withdraw()        
        protab = Toplevel()
        protab.title('Profile')
        protab.geometry('600x500')
        protab.configure(bg='#1D1D1D')
        protab.attributes('-fullscreen', True)
        lbl=ctk.CTkLabel(protab,text='Profile',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        lbl.place(x=100,y=10)
        def back():
                                shop.deiconify()
                                protab.destroy()
        bckbtn=ctk.CTkButton(protab,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=4) 
        bckbtn.place(x=10,y=10)
    
    def hp():
        shop.withdraw()   
        hptab = Toplevel()
        hptab.title("Help center")
        hptab.geometry("600x500")
        hptab.configure(bg='#1D1D1D')
        hptab.attributes('-fullscreen', True)
        lbl=ctk.CTkLabel(hptab,text='Help',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        lbl.place(x=100,y=10)
        def back():
                                shop.deiconify()
                                hptab.destroy()
        bckbtn=ctk.CTkButton(hptab,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=4) 
        bckbtn.place(x=10,y=10)
    
    def set():
        shop.withdraw()
        settab = Toplevel()
        settab.title('Settings')
        settab.geometry('600x500')
        settab.configure(bg='#1D1D1D')
        settab.attributes('-fullscreen', True)
        lbl=ctk.CTkLabel(settab,text='Settings',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        lbl.place(x=100,y=10)
        def back():
                                shop.deiconify()
                                settab.destroy()
        bckbtn=ctk.CTkButton(settab,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=4) 
        bckbtn.place(x=10,y=10)
    
    # tab buttons #49BEB7
    orders = ctk.CTkButton(tabfrm, text="Orders              ",image=open, fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50, command=ord,border_width=3,compound='right',text_color='black')
    profile = ctk.CTkButton(tabfrm, text="   Hi user ", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=120, command=pro, image=prof,border_width=3,compound='left',text_color='black')
    hpc = ctk.CTkButton(tabfrm, text="Contact Us      ", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50, command=hp,image=open,border_width=3,text_color='black',compound='right')
    settings = ctk.CTkButton(tabfrm, text="Settings          ", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50, command=set,image=open,border_width=3,text_color='black',compound='right')
    logout= ctk.CTkButton(tabfrm, text="", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50, command=login,border_width=3,image=logoutimg,text_color='black')
    
    #other buttons
    notification_btn=ctk.CTkButton(shop,text='',image=notify,fg_color='#7C93C3',width=50,height=50,corner_radius=20,command=notification,border_width=3)
    cart_btn=ctk.CTkButton(shop,text='',image=cartt,fg_color='#7C93C3',width=50,height=50,corner_radius=20,command=cart,border_width=3)
    search_btn=ctk.CTkButton(shop,text='',image=seac,fg_color='#7C93C3',width=50,height=50,corner_radius=20,command=search,border_width=3)
    searchbox=ctk.CTkEntry(shop,fg_color='#FFFFFF',width=400,height=55,corner_radius=20,border_width=3)
    
    # placing tab buttons    
    profile.place(x=10, y=30)
    orders.place(x=10, y=200)
    hpc.place(x=10, y=270)
    settings.place(x=10, y=340)
    logout.place(x=10,y=410)
    notification_btn.place(x=850,y=30)
    cart_btn.place(x=950,y=30)
    search_btn.place(x=750,y=30)
    searchbox.place(x=300,y=30)
    
#signup page
click_count=0
frame1=ctk.CTkLabel(window,text=' ',height=600,width=540,bg_color='#1D1D1D',fg_color='#9EB8D9',corner_radius=30)

#labels

wlbl=ctk.CTkLabel(frame1,text='Sign Up !',font=('vivaldi italics',40))

#entry boxes
fname=ctk.CTkEntry(frame1,height=80,width=240,corner_radius=30,border_width=3)
lname=ctk.CTkEntry(frame1,height=80,width=240,corner_radius=30,border_width=3)
uname=ctk.CTkEntry(frame1,height=80,width=240,corner_radius=30,border_width=3)
emadd=ctk.CTkEntry(frame1,height=80,width=500,corner_radius=30,border_width=3)
pwd=ctk.CTkEntry(frame1,height=80,width=240,corner_radius=30,border_width=3)

#labels
fname_lbl=ctk.CTkLabel(fname,text='First name',text_color='grey',font=('vivaldi italics',10))
fname_lbl.place(x=20,y=4)
lname_lbl=ctk.CTkLabel(lname,text='Last name',text_color='grey',font=('vivaldi italics',10))
lname_lbl.place(x=20,y=4)
uname_lbl=ctk.CTkLabel(uname,text='Username',text_color='grey',font=('vivaldi italics',10))
uname_lbl.place(x=20,y=4)
emadd_lbl=ctk.CTkLabel(emadd,text='Email',text_color='grey',font=('vivaldi italics',10))
emadd_lbl.place(x=20,y=4)
pwd_lbl=ctk.CTkLabel(pwd,text='Password',text_color='grey',font=('vivaldi italics',10))
pwd_lbl.place(x=20,y=4)
aldlbl=ctk.CTkLabel(frame1,text='Existing User ?',font=('vivaldi italics',15))
aldlbl.place(x=180,y=415)


#placing entry boxes
frame1.place(x=150,y=70)
lname.place(x=280,y=80)
fname.place(x=20,y=80)
emadd.place(x=20,y=170)
uname.place(x=20,y=260)
pwd.place(x=280,y=260)

#buttons
signup_btn=ctk.CTkButton(frame1,text='Sign Up',font=('vivaldi italics',20),height=60,width=220,command=login,corner_radius=30)
login_btn=ctk.CTkButton(frame1,text='Log In',font=('vivaldi italics',15),command=login,fg_color='white',text_color='blue',width=30)
google_button=ctk.CTkButton(frame1,text="",image=google,fg_color='white',hover_color='white',width=50)
phon_button=ctk.CTkButton(frame1,text="",image=phon,width=50,fg_color='white',hover_color='white')
insta_button=ctk.CTkButton(frame1,text="",image=insta,width=50,fg_color='white',hover_color='white')

#placing the buttons
wlbl.place(x=50,y=20)
signup_btn.place(x=150,y=350)
login_btn.place(x=285,y=415)
google_button.place(x=150,y=500)
insta_button.place(x=230,y=500)
phon_button.place(x=310,y=500)

window.mainloop()