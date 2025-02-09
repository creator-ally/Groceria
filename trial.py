import customtkinter as ctk
import tkinter as tk,tkinter
from tkinter import *
from PIL import Image,ImageTk

#Images
open=ctk.CTkImage(Image.open(r"open.png"),size=(30,30))
sett=ctk.CTkImage(Image.open(r"gear.png"),size=(50,50))
helpc=ctk.CTkImage(Image.open(r"customer-service.png"),size=(50,50)) 
prof=ctk.CTkImage(Image.open(r"user-interface.png"),size=(50,50)) 
carti=ctk.CTkImage(Image.open(r"user-interface.png"),size=(50,50))
order=ctk.CTkImage(Image.open(r"order.png"),size=(50,50)) 
logoutimg=ctk.CTkImage(Image.open(r"logout.png"),size=(50,50))
menu=ctk.CTkImage(Image.open(r"menu.png"),size=(70,70))
cartt=ctk.CTkImage(Image.open(r"shopcart.png"),size=(50,50))
notify=ctk.CTkImage(Image.open(r"notify.png"),size=(50,50))
seac=ctk.CTkImage(Image.open(r"search.png"),size=(40,40))
fru=ctk.CTkImage(Image.open(r"fruits.png"),size=(80,80))
essen=ctk.CTkImage(Image.open(r"essentials.png"),size=(80,80))
vegtab=ctk.CTkImage(Image.open(r"vegetables.png"),size=(80,80))
dair=ctk.CTkImage(Image.open(r"dairy.png"),size=(80,80))
bg1=ctk.CTkImage(Image.open(r"wpg.png"),size=(500,500))
#login images
insta=ctk.CTkImage(Image.open(r"instagram.png"),size=(50,50)) 
google=ctk.CTkImage(Image.open(r"google.png"),size=(50,50)) 
phon=ctk.CTkImage(Image.open(r"phone.png"),size=(50,50)) 
backbutn=ctk.CTkImage(Image.open(r"back-button.png"),size=(50,50)) 

#SIGN UP PAGE 
window=ctk.CTk()
window.configure(fg_color='#072e33')
my_font=ctk.CTkFont(family='Vivaldi Italic',size=50)
fnt=ctk.CTkFont(family='Vivaldi Italics',size=15)
fnt1=ctk.CTkFont(family='Vivaldi Italics',size=20)
background_image1=ctk.CTkImage(Image.open(r"/storage/emulated/0/csproject/wpg.png"),size=(400,400))
signup_backlabel=ctk.CTkLabel(window,text="",fg_color='#05161a',corner_radius=60,height=700,width=1200)
signup_backlabel.place(x=40,y=20)
signup_backimage=ctk.CTkLabel(signup_backlabel,text='',image=background_image1)
signup_backimage.place(x=400,y=100)

#ALL DEFINED FUCTIONS FOR TAB
def fgpass():
    window.withdraw()
    forgot_tab=Toplevel()
    forgot_tab.configure(bg='#072e33')
    forgot_tab.attributes('-fullscreen',True)
    #FORGOT PASSWORD TAB
    forgottab_backlabel=ctk.CTkLabel(forgot_tab,text="",fg_color='#05161a',corner_radius=60,height=700,width=1200)
    forgottab_backlabel.place(x=40,y=20)
    forgottab_backimage=ctk.CTkLabel(forgottab_backlabel,text='',image=background_image1)
    forgottab_backimage.place(x=200,y=100)
    forgottab_frame=ctk.CTkFrame(forgottab_backlabel,height=600,width=540,bg_color='#05161a',fg_color='#072e33',corner_radius=30,border_width=3,border_color='#093e44')
    forgottab_frame.place(x=50,y=50)
    
    
def login():
    window.withdraw()
    login_tab=Toplevel()
    login_tab.configure(bg='#072e33')
    login_tab.attributes('-fullscreen',True)
    #LOGIN TAB
    login_backlabel=ctk.CTkLabel(login_tab,text="",fg_color='#05161a',corner_radius=60,height=700,width=1200)
    login_backlabel.place(x=40,y=20)
    login_backimage=ctk.CTkLabel(login_backlabel,text='',image=background_image1)
    login_backimage.place(x=200,y=100)
   
    #frame 
    loginframe=ctk.CTkFrame(login_backlabel,border_width=3,border_color='#093e44',height=600,width=540,bg_color='#05161a',fg_color='#072e33',corner_radius=30)
    loginframe.place(x=50,y=50)
    #buttons and entries
    log_btn=ctk.CTkButton(loginframe,text='Login',font=('vivaldi italics',20),height=60,width=220,corner_radius=30,command=checked,fg_color='#0c7075',hover_color='#0c7075',text_color='white',border_width=3,border_color='#0f969c')
    emadd=ctk.CTkEntry(loginframe,height=80,width=490,corner_radius=30,border_width=3,fg_color='#0c7075',border_color='#0f969c')
    pwd=ctk.CTkEntry(loginframe,height=80,width=240,corner_radius=30,border_width=3,fg_color='#0c7075',border_color='#0f969c')
    forgot_password_btn=ctk.CTkButton(loginframe,text='forgot password ? ',command=fgpass,fg_color='#072e33',text_color='white',hover_color='#072e33')
    emadd_lbl=ctk.CTkLabel(emadd,text='Email',font=('vivaldi italics',10),text_color='white')
    pwd_lbl=ctk.CTkLabel(pwd,text='Password',font=('vivaldi italics',10),text_color='white')    
    wlbl=ctk.CTkLabel(loginframe,text=' Log In',font=('vivaldi italics',40),text_color='white')
    google_button=ctk.CTkButton(loginframe,text="",image=google,fg_color='white',hover_color='white',width=50)
    phon_button=ctk.CTkButton(loginframe,text="",image=phon,width=50,fg_color='white',hover_color='white')
    insta_button=ctk.CTkButton(loginframe,text="",image=insta,width=50,fg_color='white',hover_color='white')
    
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
    shop.configure(bg='#072e33')
    shop.attributes('-fullscreen', True)
    
     #frame
    combine_frame=ctk.CTkLabel(shop,text='',fg_color='#05161a',height=700,width=1220,corner_radius=40)
    combine_frame.place(x=30,y=20)
    tabs_frame = ctk.CTkFrame(shop,height=680, width=240,fg_color='#c1e8ff',corner_radius=40,bg_color='#05161a')  
    shop_scrollframe=ctk.CTkScrollableFrame(shop,height=540,width=1140,corner_radius=30,fg_color='#294d61',bg_color='#05161a')
    shop_scrollframe1=ctk.CTkScrollableFrame(master=shop,height=540,width=880,corner_radius=30,fg_color='#294d61',bg_color='#05161a')
    shop_scrollframe.place(x=50,y=110)

#menu button  
    def function_one():
        shop_scrollframe.place_forget()
        shop_scrollframe1.place(x=300,y=100)   
        menubtn.place_forget()
        close_menu.place(x=100,y=60)
        tabs_frame.place(x=50,y=30)
    def function_two():
        menubtn.place(x=50,y=30)
        close_menu.place_forget()
        tabs_frame.place_forget()
        shop_scrollframe1.place_forget()   
        shop_scrollframe.place(x=50,y=110)   
    def click():
        global click_count
        click_count += 1
        if click_count == 1:
            function_one()
        elif click_count == 2:
            function_two()
            click_count = 0
    menubtn=ctk.CTkButton(shop,text='',image=menu,fg_color='#05161a',command=click,corner_radius=20,height=40,width=40,hover_color='#05161a',border_width=0,bg_color='#05161a')
    menubtn.place(x=50,y=30)
    close_menu=ctk.CTkButton(shop,text='close',height=40,width=60,command=click) 

    
    def vegetabpro():
            vegetablestab=Toplevel()
            shop.withdraw()
            vegetablestab.title('Cart')      
            vegetablestab.geometry('500x600')    
            vegetablestab.configure(bg='#072e33')   
            vegetablestab.attributes('-fullscreen', True)
            tab_namelabel=ctk.CTkLabel(vegetablestab,text='Vegetables',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
            tab_namelabel.place(x=100,y=10)
            def back():
                shop.deiconify()
                vegetablestab.destroy()
    
            bckbtn = ctk.CTkButton(vegetablestab, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(vegetablestab, height=650, width=1200, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=5, y=80)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=1110,height=1400)
            shop_scrollframe1.pack()

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
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=580, height=250, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=200, width=200, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=200, width=320, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=240, y=20)            

            
    def fruitpro():
        fruitstab= Toplevel()
        shop.withdraw()
        fruitstab.title('Cart')      
        fruitstab.geometry('500x600')    
        fruitstab.configure(bg='#072e33')   
        fruitstab.attributes('-fullscreen', True)
        
        def back():
            shop.deiconify()
            fruitstab.destroy()
    
        bckbtn = ctk.CTkButton(master=fruitstab, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
        bckbtn.place(x=10, y=10)      
        tab_namelabel = ctk.CTkLabel(fruitstab, text='Fruits', font=('Helvetica', 40), fg_color='#1D1D1D', text_color='#FFFFFF')
        tab_namelabel.place(x=100, y=10)
        scroll_frame = ctk.CTkScrollableFrame(fruitstab, height=650, width=1200, fg_color='#05161a',                               corner_radius=40, border_width=3)
        scroll_frame.place(x=5, y=80)
        shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=1110,height=1400)
        shop_scrollframe1.pack()

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
            product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=580, height=250, fg_color='white', corner_radius=20)
            product_label.place(x=positions[i][0], y=positions[i][1])
    
            image_button= ctk.CTkButton(product_label, text='', height=200, width=200, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
            image_button.place(x=20, y=20)
            info_label=ctk.CTkFrame(product_label, height=200, width=320, corner_radius=20, fg_color='#ffffff',border_width=3)
            info_label.place(x=240, y=20)             
            
    def dairypro():
            dairystab=Toplevel()
            shop.withdraw()
            dairystab.title('Cart')      
            dairystab.geometry('500x600')    
            dairystab.configure(bg='#072e33')   
            dairystab.attributes('-fullscreen', True)
            tab_namelabel=ctk.CTkLabel(dairystab,text='Dairy',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
            tab_namelabel.place(x=100,y=10)
            def back():
                    shop.deiconify()
                    dairystab.destroy()
    
            bckbtn = ctk.CTkButton(master=dairystab, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)
            scroll_frame = ctk.CTkScrollableFrame(dairystab, height=650, width=1200, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=5, y=80)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=1110,height=1400)
            shop_scrollframe1.pack()

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
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=580, height=250, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=200, width=200, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=200, width=320, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=240, y=20)              
            
    #supplies 
    def suppliepro():
            suppliestab=Toplevel()
            shop.withdraw()
            suppliestab.title('Cart')      
            suppliestab.geometry('500x600')    
            suppliestab.configure(bg='#072e33')   
            suppliestab.attributes('-fullscreen', True)
            tab_namelabel=ctk.CTkLabel(suppliestab,text='Supplies',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                shop.deiconify()
                suppliestab.destroy()
    
            bckbtn = ctk.CTkButton(suppliestab, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(suppliestab, height=650, width=1200, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=5, y=80)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=1110,height=1400)
            shop_scrollframe1.pack()

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
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=580, height=250, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=200, width=200, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=200, width=320, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=240, y=20)          
         
                                                               
    #widgets    in sclframe wihout menu button in screen
    offlbl=ctk.CTkLabel(shop_scrollframe,text='',image=background_image1)
    offlbl.pack()
    category_frame=ctk.CTkFrame(shop_scrollframe,height=180,width=900,corner_radius=30,fg_color='#072e33',border_width=3,border_color='#093e44')
    category_frame.pack(pady=20)
    vegetables=ctk.CTkButton(category_frame,text='Veges',image=vegtab,height=140,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,command=vegetabpro,border_width=3,border_color='#0f969c')
    vegetables.place(x=20,y=20)
    fruits=ctk.CTkButton(category_frame,text='Fruits',image=fru,height=140,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,command=fruitpro,border_width=3,border_color='#0f969c')
    fruits.place(x=240,y=20)
    dairy=ctk.CTkButton(category_frame,text='Dairy',height=140,image=dair,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,command=dairypro,border_width=3,border_color='#0f969c')
    dairy.place(x=460,y=20)
    essentials=ctk.CTkButton(category_frame,text='Supplies',image=essen,height=140,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,command=suppliepro,border_width=3,border_color='#0f969c')
    essentials.place(x=680,y=20)
    
    #scrollable frame with menu button on screen
    offlbl=ctk.CTkLabel(shop_scrollframe1,text='',image=background_image1)
    offlbl.pack()
    category_frame=ctk.CTkFrame(shop_scrollframe1,height=180,width=820,corner_radius=30,fg_color='#072e33',border_width=3,border_color='#093e44')
    category_frame.pack(pady=20)
    vegetables=ctk.CTkButton(category_frame,text='Veges',image=vegtab,height=140,width=180,fg_color='#0c7075',corner_radius=20,font=fnt,command=vegetabpro,border_width=3,border_color='#0f969c')
    vegetables.place(x=15,y=20)
    fruits=ctk.CTkButton(category_frame,text='Fruits',image=fru,height=140,width=180,fg_color='#0c7075',corner_radius=20,font=fnt, command=fruitpro,border_width=3,border_color='#0f969c')
    fruits.place(x=215,y=20)
    dairy=ctk.CTkButton(category_frame,text='Dairy',height=140,image=dair,width=180,fg_color='#0c7075',corner_radius=20,font=fnt,command=dairypro,border_width=3,border_color='#0f969c')
    dairy.place(x=415,y=20)
    essentials=ctk.CTkButton(category_frame,text='Supplies',image=essen,height=140,width=180,fg_color='#0c7075',corner_radius=20,font=fnt,command=suppliepro,border_width=3,border_color='#0f969c')
    essentials.place(x=615,y=20)
       
    # defining the tabs
    def search():
        shop.withdraw()
        search= Toplevel()
        search.title('Cart')      
        search.geometry('500x600')    
        search.configure(bg='#072e33')   
        search.attributes('-fullscreen', True)
        def back():
                shop.deiconify()
                search.destroy()
                            
        bckbtn = ctk.CTkButton(search, text="", command=back, image=backbutn, fg_color='white',hover_color='white', height=55, width=55, corner_radius=5) 
        bckbtn.place(x=10, y=10)      
        scroll_frame = ctk.CTkScrollableFrame(search, height=650, width=1200, fg_color='#05161a', corner_radius=40, border_width=3)
        scroll_frame.place(x=5, y=80)
        shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=1110,height=1400)
        shop_scrollframe1.pack()    
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
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=580, height=250, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=200, width=200, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)                 
                info_label=ctk.CTkFrame(product_label, height=200, width=320, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=240, y=20)      
        
    def notification():
        shop.withdraw()
        notification= Toplevel()
        notification.title('Cart')      
        notification.geometry('500x600')    
        notification.configure(bg='#072e33')   
        notification.attributes('-fullscreen', True)
        tab_namelabel=ctk.CTkLabel(notification,text='Notification',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        tab_namelabel.place(x=100,y=10)
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
        cart.configure(bg='#072e33')   
        cart.attributes('-fullscreen', True)
        tab_namelabel=ctk.CTkLabel(cart,text='Cart',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        tab_namelabel.place(x=100,y=10)
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
        ordtab.configure(bg='#072e33')
        shop.withdraw()
        tab_namelabel=ctk.CTkLabel(ordtab,text='Orders',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        tab_namelabel.place(x=100,y=10)
        def back():
                                shop.deiconify()
                                ordtab.destroy()
        bckbtn=ctk.CTkButton(ordtab,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=5) 
        bckbtn.place(x=10,y=10)   
        
    def pro():
        shop.withdraw()        
        profile_tab = Toplevel()
        profile_tab.title('Profile')
        profile_tab.geometry('600x500')
        profile_tab.configure(bg='#072e33')
        profile_tab.attributes('-fullscreen', True)
        tab_namelabel=ctk.CTkLabel(profile_tab,text='Profile',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
        tab_namelabel.place(x=100,y=10)
        profile_backlabel=ctk.CTkLabel(profile_tab,text='',fg_color='#ffffff',height=600,width=1100,corner_radius=50)
        profile_backlabel.place(x=60,y=100)
        prof_image=ctk.CTkButton(profile_backlabel,text='',corner_radius=50,state=DISABLED,fg_color='#ffffff',border_width=3,width=200,height=200)
        delete_button=ctk.CTkButton(profile_backlabel,text='Delete Acoount',font=('Helvetica',30),text_color='#811331',border_width=4,                    border_color='#811331',fg_color='#ffffff',height=60,width=800,corner_radius=30)
        delete_button.place(x=100,y=400)
        prof_image.place(x=100,y=40)
        def back():
                                shop.deiconify()
                                profile_tab.destroy()
        bckbtn=ctk.CTkButton(profile_tab,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=4) 
        bckbtn.place(x=10,y=10)
    
    def hp():
        shop.withdraw()   
        hptab = Toplevel()
        hptab.title("Help center")
        hptab.geometry("600x500")
        hptab.configure(bg='#072e33')
        hptab.attributes('-fullscreen', True)
        tab_namelabel=ctk.CTkLabel(hptab,text='Help',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        tab_namelabel.place(x=100,y=10)
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
        settab.configure(bg='#072e33')
        settab.attributes('-fullscreen', True)
        tab_namelabel=ctk.CTkLabel(settab,text='Settings',font=('Helvetica',40),fg_color='#1D1D1D',text_color='#FFFFFF')
        tab_namelabel.place(x=100,y=10)
        def back():
                                shop.deiconify()
                                settab.destroy()
        bckbtn=ctk.CTkButton(settab,text="",command=back ,image=backbutn,fg_color='white',hover_color='white',height=55,width=55,corner_radius=4) 
        bckbtn.place(x=10,y=10)
    
    # tab buttons #49BEB7
    orders = ctk.CTkButton(tabs_frame, text="Orders              ",image=open, fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50, command=ord,border_width=3,compound='right',text_color='black')
    profile = ctk.CTkButton(tabs_frame, text="   Hi user ", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=120, command=pro, image=prof,border_width=3,compound='left',text_color='black')
    hpc = ctk.CTkButton(tabs_frame, text="Contact Us      ", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50, command=hp,image=open,border_width=3,text_color='black',compound='right')
    settings = ctk.CTkButton(tabs_frame, text="Settings          ", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50, command=set,image=open,border_width=3,text_color='black',compound='right')
    logout= ctk.CTkButton(tabs_frame, text="", fg_color="#0f969c", font=fnt1, corner_radius=20, width=210, height=50, command=login,border_width=3,image=logoutimg,text_color='black')
    
    #other buttons
    searchbox=ctk.CTkEntry(shop,fg_color='#0c7075',width=700,height=60,corner_radius=20,border_width=3,bg_color='#05161a',border_color='#0f969c',text_color='white',font=('Helvetica',20))
    notification_btn=ctk.CTkButton(shop,text='',image=notify,fg_color='#7C93C3',width=50,height=50,corner_radius=20,command=notification,border_width=3,bg_color='#05161a')
    cart_btn=ctk.CTkButton(shop,text='',image=cartt,fg_color='#7C93C3',width=50,height=50,corner_radius=20,command=cart,border_width=3,bg_color='#05161a')
    search_btn=ctk.CTkButton(shop,text='',image=seac,fg_color='#05161a',width=50,height=30,corner_radius=20,command=search,border_width=3,bg_color='#0c7075',border_color='#0f969c')    
    
    # placing tab buttons    
    profile.place(x=10, y=30)
    orders.place(x=10, y=200)
    hpc.place(x=10, y=270)
    settings.place(x=10, y=340)
    logout.place(x=10,y=410)
    notification_btn.place(x=1000,y=30)
    cart_btn.place(x=1100,y=30)
    search_btn.place(x=900,y=35)
    searchbox.place(x=300,y=30)
    
#signup page
click_count=0
widgetframe_su=ctk.CTkFrame(signup_backlabel,height=600,width=540,fg_color='#072e33',bg_color='#05161a',corner_radius=30,border_width=3,border_color='#093e44')

#labels

wlbl=ctk.CTkLabel(widgetframe_su,text='Sign Up !',font=('vivaldi italics',40),text_color='white')

#entry boxes
fname=ctk.CTkEntry(widgetframe_su,height=80,width=240,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
lname=ctk.CTkEntry(widgetframe_su,height=80,width=240,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
uname=ctk.CTkEntry(widgetframe_su,height=80,width=240,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
emadd=ctk.CTkEntry(widgetframe_su,height=80,width=500,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
pwd=ctk.CTkEntry(widgetframe_su,height=80,width=240,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')

#labels
fname_lbl=ctk.CTkLabel(fname,text='First name',text_color='white',font=('vivaldi italics',10))
fname_lbl.place(x=20,y=4)
lname_lbl=ctk.CTkLabel(lname,text='Last name',text_color='white',font=('vivaldi italics',10))
lname_lbl.place(x=20,y=4)
uname_lbl=ctk.CTkLabel(uname,text='Username',text_color='white',font=('vivaldi italics',10))
uname_lbl.place(x=20,y=4)
emadd_lbl=ctk.CTkLabel(emadd,text='Email',text_color='white',font=('vivaldi italics',10))
emadd_lbl.place(x=20,y=4)
pwd_lbl=ctk.CTkLabel(pwd,text='Password',text_color='white',font=('vivaldi italics',10))
pwd_lbl.place(x=20,y=4)
aldlbl=ctk.CTkButton(widgetframe_su,text='Existing User ? Login',font=('vivaldi italics',15),text_color='white',hover_color='#072e33',fg_color='#072e33',command=login)
aldlbl.place(x=180,y=415)


#placing entry boxes
widgetframe_su.place(x=50,y=50)
lname.place(x=280,y=80)
fname.place(x=20,y=80)
emadd.place(x=20,y=170)
uname.place(x=20,y=260)
pwd.place(x=280,y=260)

#buttons
signup_btn=ctk.CTkButton(widgetframe_su,text='Sign Up',font=('vivaldi italics',20),height=60,width=220,command=login,corner_radius=30,fg_color='#0c7075',hover_color='#0c7075',border_color='#0f969c',border_width=3)
google_button=ctk.CTkButton(widgetframe_su,text="",image=google,fg_color='#0c7075',hover_color='white',width=50)
phon_button=ctk.CTkButton(widgetframe_su,text="",image=phon,width=50,fg_color='white',hover_color='white')
insta_button=ctk.CTkButton(widgetframe_su,text="",image=insta,width=50,fg_color='white',hover_color='white')

#placing the buttons
wlbl.place(x=50,y=20)
signup_btn.place(x=150,y=350)
google_button.place(x=150,y=500)
insta_button.place(x=230,y=500)
phon_button.place(x=310,y=500)

window.mainloop()