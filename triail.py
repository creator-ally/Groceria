import customtkinter as ctk
import tkinter as tk,tkinter
from tkinter import *
from PIL import Image,ImageTk
import re
import itertools

#SIGN UP PAGE 
window=ctk.CTk()
window.configure(fg_color='#093e44')
window.geometry('1240x780')
my_font=ctk.CTkFont(family='Vivaldi Italic',size=50)
fnt=ctk.CTkFont(family='Vivaldi Italics',size=15)
fnt1=ctk.CTkFont(family='Vivaldi Italics',size=20)
background_image1=ctk.CTkImage(Image.open(r"groceria.png"),size=(600,600))
background_image=ctk.CTkImage(Image.open(r"groceria.png"),size=(800,300))


#Sign Up Mainframe
signup_mainframe=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200,border_color='white')
signup_mainframe.place(x=40,y=20)
signup_backimage=ctk.CTkLabel(signup_mainframe,text='',image=background_image1)
signup_backimage.place(x=575,y=30)

#Images
open=ctk.CTkImage(Image.open(r"open.png"),size=(30,30))
prof=ctk.CTkImage(Image.open(r"user-interface.png"),size=(50,50)) 
carti=ctk.CTkImage(Image.open(r"user-interface.png"),size=(50,50))
logoutimg=ctk.CTkImage(Image.open(r"logout.png"),size=(50,50))
menu=ctk.CTkImage(Image.open(r"menu.png"),size=(60,60))
cartt=ctk.CTkImage(Image.open(r"shopcart.png"),size=(50,50))
notify=ctk.CTkImage(Image.open(r"notify.png"),size=(50,50))
seac=ctk.CTkImage(Image.open(r"search.png"),size=(40,40))
logo_image=ctk.CTkImage(Image.open(r"logo.png"),size=(100,100))

# category icons for main shop window
fru=ctk.CTkImage(Image.open(r"fruits.png"),size=(80,80))
essen=ctk.CTkImage(Image.open(r"essentials.png"),size=(80,80))
vegtab=ctk.CTkImage(Image.open(r"vegetables.png"),size=(80,80))
dair=ctk.CTkImage(Image.open(r"dairy.png"),size=(80,80))

#advertisement images for main shop window
juices = ImageTk.PhotoImage(Image.open("juices.png").resize((1000, 300)))
rice = ImageTk.PhotoImage(Image.open("rice.png").resize((1000, 300)))
cookies = ImageTk.PhotoImage(Image.open("cookies.png").resize((1000, 300)))
snacks = ImageTk.PhotoImage(Image.open("snacks.png").resize((1000, 300)))

#advertisement images for the shop window with menu button
juices_menu = ImageTk.PhotoImage(Image.open("juices.png").resize((770, 300)))
rice_menu = ImageTk.PhotoImage(Image.open("rice.png").resize((770, 300)))
cookies_menu = ImageTk.PhotoImage(Image.open("cookies.png").resize((770, 300)))
snacks_menu = ImageTk.PhotoImage(Image.open("snacks.png").resize((770, 300)))


#category icons for shop window with menu
fru2=ctk.CTkImage(Image.open(r"fruits.png"),size=(50,50))
essen2=ctk.CTkImage(Image.open(r"essentials.png"),size=(50,50))
vegtab2=ctk.CTkImage(Image.open(r"vegetables.png"),size=(50,50))
dair2=ctk.CTkImage(Image.open(r"dairy.png"),size=(50,50))
bg1=ctk.CTkImage(Image.open(r"wpg.png"),size=(500,500))

#login images
instagram=ctk.CTkImage(Image.open(r"instagram (1).png"),size=(50,50)) 
google=ctk.CTkImage(Image.open(r"google.png"),size=(50,50)) 
phon=ctk.CTkImage(Image.open(r"phone.png"),size=(50,50)) 
backbutn=ctk.CTkImage(Image.open(r"back-button.png"),size=(50,50)) 
close=ctk.CTkImage(Image.open(r"close.png"),size=(50,50))

#ALL DEFINED FUCTIONS FOR TAB
def fgpass():
    forgot_password_mainframe=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
    forgot_password_mainframe.place(x=40,y=20)
    
    #FORGOT PASSWORD TAB
    forgottab_backimage=ctk.CTkLabel(forgot_password_mainframe,text='',image=background_image1)
    forgottab_backimage.place(x=575,y=30)
    forgottab_frame=ctk.CTkFrame(forgot_password_mainframe,height=600,width=540,bg_color='#05161a',fg_color='#072e33',corner_radius=30,border_width=3,border_color='white')
    forgottab_frame.place(x=50,y=50)
    
    #Widgets
    email_address=ctk.CTkEntry(forgottab_frame,height=80,width=500,corner_radius=30,border_width=3,                                 border_color='#0f969c',fg_color='#0c7075')
    password=ctk.CTkEntry(forgottab_frame,height=80,width=240,corner_radius=30,border_width=3,                            border_color='#0f969c',fg_color='#0c7075')
    
    #labels
    email_address_label=ctk.CTkLabel(email_address,text='Email',text_color='white',font=('vivaldi italics',10))
    email_address_label.place(x=20,y=4)
    password_label=ctk.CTkLabel(password,text='Password',text_color='white',font=('vivaldi italics',10))
    password_label.place(x=20,y=4)

    #placing widgets
    email_address.place(x=20,y=140)
    password.place(x=20,y=240)
    
    #email validation
    valid_image = ctk.CTkImage(Image.open(r"valid.png"),size=(40,40))
    invalid_image = ctk.CTkImage(Image.open(r"invalid.png"),size=(40,40))
    feedback_label = ctk.CTkLabel(email_address, text="", font=("Helvetica", 16),bg_color='#0c7075',fg_color='#0c7075',        width=30,height=30)
    feedback_label.place(x=450,y=20)
    
    def validate_email(event):
        email = email_address.get()
        # Regular expression to check the validity of the email including domain
        email_regex = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
        valid_length = 5 <= len(email) <= 254  
        if re.match(email_regex, email) and valid_length:
            feedback_label.configure(image=valid_image, compound='left', fg_color="#0c7075")
        else:
            feedback_label.configure(image=invalid_image, compound='left', fg_color="#0c7075")

# Bind the validate_email function to the KeyRelease event
    email_address.bind("<KeyRelease>", validate_email)

def login():
    login_mainframe=ctk.CTkFrame(window,fg_color='#05161a',corner_radius=60,height=700,width=1200,border_width=3,border_color='white')
    login_mainframe.place(x=40,y=20)
    login_backimage=ctk.CTkLabel(login_mainframe,text='',image=background_image1)
    login_backimage.place(x=575,y=30)
   
    #frame 
    loginframe=ctk.CTkFrame(login_mainframe,border_width=3,border_color='#093e44',height=600,width=540,bg_color='#05161a',fg_color='#072e33',corner_radius=30)
    loginframe.place(x=50,y=50)
    #buttons and entries
    login_button=ctk.CTkButton(loginframe,text='Login',font=('vivaldi italics',20),height=60,width=220,corner_radius=30,fg_color='#0c7075',hover_color='#0c7075',text_color='white',border_width=3,border_color='#0f969c',command=checked)
    email_address=ctk.CTkEntry(loginframe,height=80,width=500,corner_radius=30,border_width=3,fg_color='#0c7075',border_color='#0f969c')
    password=ctk.CTkEntry(loginframe,height=80,width=240,corner_radius=30,border_width=3,fg_color='#0c7075',border_color='#0f969c')
    forgot_password_btn=ctk.CTkButton(loginframe,text='forgot password ? ',command=fgpass,fg_color='#072e33',text_color='white',hover_color='#072e33')
    email_address_label=ctk.CTkLabel(email_address,text='Email',font=('vivaldi italics',10),text_color='white')
    password_label=ctk.CTkLabel(password,text='Password',font=('vivaldi italics',10),text_color='white')    
    login_label=ctk.CTkLabel(loginframe,text=' Log In',font=('vivaldi italics',40),text_color='white')
    google_button=ctk.CTkButton(loginframe,text="",image=google,fg_color='white',hover_color='white',width=50)
    phon_button=ctk.CTkButton(loginframe,text="",image=phon,width=50,fg_color='white',hover_color='white')
    instagram_button=ctk.CTkButton(loginframe,text="",image=instagram,width=50,fg_color='white',hover_color='white')
    
    #email validation
    valid_image = ctk.CTkImage(Image.open(r"valid.png"),size=(40,40))
    invalid_image = ctk.CTkImage(Image.open(r"invalid.png"),size=(40,40))
    feedback_label = ctk.CTkLabel(email_address, text="", font=("Helvetica", 16),bg_color='#0c7075',fg_color='#0c7075',        width=30,height=30)
    feedback_label.place(x=450,y=20)

    def validate_email(event):
        email = email_address.get()
        # Regular expression to check the validity of the email including domain
        email_regex = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
        valid_length = 5 <= len(email) <= 254   
        if re.match(email_regex, email) and valid_length:
            feedback_label.configure(image=valid_image, compound='left', fg_color="#0c7075")
        else:
            feedback_label.configure(image=invalid_image, compound='left', fg_color="#0c7075")

    # Bind the validate_email function to the KeyRelease event
    email_address.bind("<KeyRelease>", validate_email)
    
    # placing buttons and widgets
    login_label.place(x=120,y=10)
    email_address_label.place(x=20,y=4)
    password_label.place(x=20,y=4)
    forgot_password_btn.place(x=30,y=260)    
    login_button.place(x=160,y=290)
    email_address.place(x=20,y=80)
    password.place(x=20,y=180)
    google_button.place(x=150,y=400)
    instagram_button.place(x=230,y=400)
    phon_button.place(x=310,y=400)

def checked():
    
    shop_mainframe=ctk.CTkFrame(window,fg_color='#05161a',corner_radius=60,height=700,width=1200)
    shop_mainframe.place(x=40,y=20)
    tabs_frame = ctk.CTkFrame(shop_mainframe,height=650, width=250,fg_color='#c1e8ff',corner_radius=40,bg_color='#05161a')  
    tabs_frame.propagate(0)
    shop_scrollframe=ctk.CTkFrame(shop_mainframe,height=560,width=1150,corner_radius=30,fg_color='#294d61',bg_color='#05161a')
    shop_scrollframe.propagate(0)
    shop_scrollframe1=ctk.CTkFrame(master=shop_mainframe,height=500,width=840,corner_radius=30,fg_color='#294d61',bg_color='#05161a')
    shop_scrollframe1.propagate(0)
    shop_scrollframe.place(x=25,y=110)       
        
    def supplie_products():
            supplies_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            supplies_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(supplies_frame,text='Supplies',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                supplies_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(supplies_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(supplies_frame, height=500, width=1100, fg_color='#05161a',                               corner_radius=40, border_width=3)
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
                               
   
    def fruit_products():
            fruits_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            fruits_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(fruits_frame,text='Fruits',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                fruits_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(fruits_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(fruits_frame, height=500, width=1100, fg_color='#05161a',                               corner_radius=40, border_width=3)
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
    
    def dairy_products():
            dairy_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            dairy_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(dairy_frame,text='Dairy',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                dairy_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(dairy_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(dairy_frame, height=500, width=1100, fg_color='#05161a',                               corner_radius=40, border_width=3)
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
    
    def vegetable_products():
            vegetable_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            vegetable_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(vegetable_frame,text='Vegetables',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                vegetable_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(vegetable_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(vegetable_frame, height=500, width=1100, fg_color='#05161a',                               corner_radius=40, border_width=3)
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
                                                             
    #widgets in scrollable frame   
    # Advertisement Frame
    advertisement = ctk.CTkLabel(shop_scrollframe, width=1000, height=300, fg_color='#294d61',image=background_image)
    advertisement.place(x=40,y=40)
    
#CATEGORY TABS
    category_frame=ctk.CTkFrame(shop_scrollframe,height=180,width=900,corner_radius=30,fg_color='#072e33',border_width=3,border_color='#093e44')    
    vegetables=ctk.CTkButton(category_frame,text='Veges',image=vegtab,height=140,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=vegetable_products)   
    fruits=ctk.CTkButton(category_frame,text='Fruits',image=fru,height=140,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=fruit_products)
    dairy=ctk.CTkButton(category_frame,text='Dairy',height=140,image=dair,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=dairy_products)   
    essentials=ctk.CTkButton(category_frame,text='Supplies',image=essen,height=140,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=supplie_products)
    
    #placing of tabs
    category_frame.place(x=100,y=350)
    dairy.place(x=460,y=20)
    fruits.place(x=240,y=20)
    vegetables.place(x=20,y=20)    
    essentials.place(x=680,y=20)      
    
    #scrollable frame with menu button on screen
    advertisement_menu= ctk.CTkLabel(shop_scrollframe1, width=750, height=300, fg_color='#294d61')
    advertisement_menu.place(x=40,y=40)
    category_frame1=ctk.CTkFrame(tabs_frame,height=150,width=210,corner_radius=30,fg_color='#072e33',border_width=3,border_color='#093e44')
    
#CATEGORY TABS
    vegetables=ctk.CTkButton(category_frame1,text='',image=vegtab2,height=50,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=vegetable_products)    
    fruits=ctk.CTkButton(category_frame1,text='',image=fru2,height=50,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=fruit_products)    
    dairy=ctk.CTkButton(category_frame1,text='',height=50,image=dair2,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=dairy_products)    
    essentials=ctk.CTkButton(category_frame1,text='',image=essen2,height=50,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=supplie_products)
    
    #placing tabs and widgets  
    category_frame1.place(x=20,y=400)
    fruits.place(x=110,y=10)
    dairy.place(x=10,y=80)
    vegetables.place(x=10,y=10)
    essentials.place(x=110,y=80)
        
#DEFINING THE TABS
    def search_tab():
            search_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            search_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(search_frame,text='Search',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                search_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(search_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(search_frame, height=500, width=1100, fg_color='#05161a',                               corner_radius=40, border_width=3)
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
      
    def profile_tab():
            profile_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            profile_frame.place(x=40,y=20)
            
            #widgets in profile tab            
            tab_namelabel=ctk.CTkLabel(profile_frame,text='Profile',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')          
            profile_backlabel=ctk.CTkLabel(profile_frame,text='',fg_color='#ffffff',height=580,width=1100,corner_radius=50)           
            prof_image=ctk.CTkButton(profile_backlabel,text='',corner_radius=50,state=DISABLED,fg_color='#ffffff',border_width=3,width=200,height=200)
            delete_button=ctk.CTkButton(profile_backlabel,text='Delete Acoount',font=('Helvetica',30),text_color='#811331',border_width=4,                    border_color='#811331',fg_color='#ffffff',height=60,width=800,corner_radius=30)           
            def back():
                profile_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(profile_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5)
            #placing widgets
            profile_backlabel.place(x=60,y=100)
            tab_namelabel.place(x=100, y=10)
            delete_button.place(x=100,y=400)
            prof_image.place(x=100,y=40)
            bckbtn.place(x=10, y=10) 
     
    def orders_tab():
            orders_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            orders_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(orders_frame,text='Orders',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                orders_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(orders_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)
    
    def settings_tab():
            settings_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            settings_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(settings_frame,text='Settings',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                settings_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(settings_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)
            
    def supports_tab():
            supports_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            supports_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(supports_frame,text='Help & Support',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                supports_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(supports_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)
      
    def notification_tab():
            notification_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            notification_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(notification_frame,text='Notifications',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                notification_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(notification_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)
    
    def cart_tab():
            cart_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=700,width=1200)
            cart_frame.place(x=40,y=20)
            tab_namelabel=ctk.CTkLabel(cart_frame,text='Cart',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=100, y=10)
            def back():
                cart_frame.place_forget()
                shop_mainframe.place(x=40,y=20)
    
            bckbtn = ctk.CTkButton(cart_frame, text="", command=back, image=backbutn, fg_color='white',                    hover_color='white', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=10, y=10)                                                       
    
    #widgets in the menu
    orders = ctk.CTkButton(tabs_frame, text="Orders              ",image=open, fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50,border_width=3,compound='right',text_color='black',command=orders_tab)
    profile = ctk.CTkButton(tabs_frame, text="   Hi user ", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=120,border_width=3,compound='left',text_color='black',image=prof,command=profile_tab)
    hpc = ctk.CTkButton(tabs_frame, text="Contact Us      ", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50,image=open,border_width=3,text_color='black',compound='right',command=supports_tab)
    settings = ctk.CTkButton(tabs_frame, text="Settings          ", fg_color="#FFFFFF", font=fnt1, corner_radius=20, width=210, height=50,image=open,border_width=3,text_color='black',compound='right',command=settings_tab)
    logout= ctk.CTkButton(tabs_frame, text="", fg_color="#0f969c", font=fnt1, corner_radius=20, width=210, height=50, command=login,border_width=3,image=logoutimg,text_color='black')
    
    # placing tab buttons    
    profile.place(x=20, y=30)
    orders.place(x=20, y=200)
    hpc.place(x=20, y=270)
    settings.place(x=20, y=340)
    logout.place(x=20,y=575)
    
    #widgets with menu
    menu_searchbox=ctk.CTkEntry(shop_mainframe,fg_color='#0c7075',width=560,height=60,corner_radius=20,border_width=3,bg_color='#05161a')
    menu_notification_button=ctk.CTkButton(shop_mainframe,text='',image=notify,fg_color='#7C93C3',width=50,height=50,corner_radius=20,border_width=3,bg_color='#05161a',command=notification_tab)
    menu_cart_button=ctk.CTkButton(shop_mainframe,text='',image=cartt,fg_color='#7C93C3',width=50,height=50,corner_radius=20,border_width=3,bg_color='#05161a',command=cart_tab)
    menu_search_button=ctk.CTkButton(shop_mainframe,text='',image=seac,fg_color='#05161a',width=50,height=30,corner_radius=20,border_width=3,bg_color='#0c7075',border_color='#0f969c',command=search_tab)
    
    #widgets on shop without menu
    searchbox=ctk.CTkEntry(shop_mainframe,fg_color='#0c7075',width=600,height=60,corner_radius=20,border_width=3,bg_color='#05161a')
    notification_button=ctk.CTkButton(shop_mainframe,text='',image=notify,fg_color='#7C93C3',width=50,height=50,corner_radius=20,border_width=3,bg_color='#05161a',command=notification_tab)
    cart_button=ctk.CTkButton(shop_mainframe,text='',image=cartt,fg_color='#7C93C3',width=50,height=50,corner_radius=20,border_width=3,bg_color='#05161a',command=cart_tab)
    search_button=ctk.CTkButton(shop_mainframe,text='',image=seac,fg_color='#05161a',width=50,height=30,corner_radius=20,border_width=3,bg_color='#0c7075',border_color='#0f969c',command=search_tab)    
    #placing the widgets without menu
    notification_button.place(x=910,y=30)
    cart_button.place(x=1020,y=30)
    search_button.place(x=790,y=35)
    searchbox.place(x=270,y=30)
    
#MENU BUTTON FUNCTIONING AND DEFINING
    def function_one():
        shop_scrollframe.place_forget()
        shop_scrollframe1.place(x=290,y=110)   
        menubtn.place_forget()
        close_menu.place(x=290,y=30)
        tabs_frame.place(x=25,y=25)
        
         #withdrawing the widgets without menu
        notification_button.place_forget()
        cart_button.place_forget()
        search_button.place_forget()
        searchbox.place_forget()
        logo.place_forget()
        
        #placing widgets with menu
        menu_notification_button.place(x=960,y=30)
        menu_cart_button.place(x=1070,y=30)
        menu_search_button.place(x=860,y=35)
        menu_searchbox.place(x=380,y=30)
        
    def function_two():
        menubtn.place(x=50,y=30)
        close_menu.place_forget()
        tabs_frame.place_forget()
        shop_scrollframe1.place_forget()   
        shop_scrollframe.place(x=25,y=120)
        
        #placing the widgets without menu
        notification_button.place(x=910,y=30)
        cart_button.place(x=1020,y=30)
        search_button.place(x=790,y=35)
        searchbox.place(x=270,y=30) 
        
        #withdrawing the widgets without menu
        menu_notification_button.place_forget()
        menu_cart_button.place_forget()
        menu_search_button.place_forget()
        menu_searchbox.place_forget()                    
      
    def click():
        global click_count
        click_count += 1
        if click_count == 1:
            function_one()
        elif click_count == 2:
            function_two()
            click_count = 0
    menubtn=ctk.CTkButton(shop_mainframe,text='',image=menu,fg_color='#05161a',command=click,corner_radius=20,height=40,width=40,hover_color='#05161a',border_width=0,bg_color='#05161a')
    menubtn.place(x=150,y=30)
    logo=ctk.CTkLabel(shop_mainframe,image= logo_image,text='')   
    logo.place(x=25,y=10)
    close_menu=ctk.CTkButton(shop_mainframe,text='',height=40,width=60,command=click,image=close,fg_color='#0c7075') 
    
# ADVERTISEMENT FUNCTION FOR SHOP WINDOW WITH MENU
    #image list
    image_menu= [cookies_menu, juices_menu, rice_menu, snacks_menu]

# Create a canvas to hold the images
    canvas_menu= ctk.CTkCanvas(advertisement_menu, width=750, height=300)
    canvas_menu.place(x=0, y=0)

# Function to animate the sliding effect
    def slide_images(canvas_menu, images, duration=50, steps=50):
        image_iter = itertools.cycle(image_menu)  # Create an iterator that cycles through the images
        current_image = canvas_menu.create_image(0, 0, anchor='nw', image=next(image_iter))
        canvas_menu.update()

        def animate():
            nonlocal current_image
            next_image = canvas_menu.create_image(canvas_menu.winfo_width(), 0, anchor='nw', image=next(image_iter))
            for step in range(steps + 1):
                offset = step / steps * canvas_menu.winfo_width()
                canvas_menu.move(current_image, -canvas_menu.winfo_width() / steps, 0)
                canvas_menu.move(next_image, -canvas_menu.winfo_width() / steps, 0)
                canvas_menu.update()
                canvas_menu.after(duration // steps)
            canvas_menu.delete(current_image)
            current_image = next_image
            canvas_menu.after(2000, animate)  # Schedule the next animation after 2000 milliseconds (2 seconds)

        animate()
    slide_images(canvas_menu, image_menu)
    
#ADVERTISEMENT FUCNTION FOR SHOP WINDOW WITHOUT MENU
    #Image list
    images = [cookies, juices, rice, snacks]

# Create a canvas to hold the images
    canvas = ctk.CTkCanvas(advertisement, width=980, height=300)
    canvas.place(x=0, y=0)

# Function to animate the sliding effect
    def slide_images(canvas, images, duration=50, steps=50):
        image_iter = itertools.cycle(images)  # Create an iterator that cycles through the images
        current_image = canvas.create_image(0, 0, anchor='nw', image=next(image_iter))
        canvas.update()

        def animate():
            nonlocal current_image
            next_image = canvas.create_image(canvas.winfo_width(), 0, anchor='nw', image=next(image_iter))
            for step in range(steps + 1):
                offset = step / steps * canvas.winfo_width()
                canvas.move(current_image, -canvas.winfo_width() / steps, 0)
                canvas.move(next_image, -canvas.winfo_width() / steps, 0)
                canvas.update()
                canvas.after(duration // steps)
            canvas.delete(current_image)
            current_image = next_image
            canvas.after(2000, animate)  # Schedule the next animation after 2000 milliseconds (2 seconds)

        animate()
    slide_images(canvas, images)       

#SIGN UP PAGE SETUP
click_count=0
widgetframe_su=ctk.CTkFrame(signup_mainframe,height=600,width=540,fg_color='#072e33',bg_color='#05161a',corner_radius=30,border_width=3,border_color='#093e44')

#Frame for widgets
signup_label=ctk.CTkLabel(widgetframe_su,text='Sign Up !',font=('vivaldi italics',40),text_color='white')

#entry boxes
fullname_entry=ctk.CTkEntry(widgetframe_su,height=80,width=240,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
lastname_entry=ctk.CTkEntry(widgetframe_su,height=80,width=240,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
confirm_password=ctk.CTkEntry(widgetframe_su,height=80,width=240,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
email_address=ctk.CTkEntry(widgetframe_su,height=80,width=500,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
password=ctk.CTkEntry(widgetframe_su,height=80,width=240,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')

#labels
fullname_label=ctk.CTkLabel(fullname_entry,text='First name',text_color='white',font=('vivaldi italics',10))
fullname_label.place(x=20,y=4)
lastname_label=ctk.CTkLabel(lastname_entry,text='Last name',text_color='white',font=('vivaldi italics',10))
lastname_label.place(x=20,y=4)
confirm_password_label=ctk.CTkLabel(confirm_password,text='Confirm Password',text_color='white',font=('vivaldi italics',10))
confirm_password_label.place(x=20,y=4)
email_address_label=ctk.CTkLabel(email_address,text='Email',text_color='white',font=('vivaldi italics',10))
email_address_label.place(x=20,y=4)
password_label=ctk.CTkLabel(password,text='Password',text_color='white',font=('vivaldi italics',10))
password_label.place(x=20,y=4)
existing_user=ctk.CTkButton(widgetframe_su,text='Existing User ? Login',font=('vivaldi italics',15),text_color='white',hover_color='#072e33',fg_color='#072e33',command=login)
existing_user.place(x=180,y=415)

#placing entry boxes
widgetframe_su.place(x=50,y=50)
lastname_entry.place(x=280,y=80)
fullname_entry.place(x=20,y=80)
email_address.place(x=20,y=170)
confirm_password.place(x=280,y=260)
password.place(x=20,y=260)

#buttons
signup_button=ctk.CTkButton(widgetframe_su,text='Sign Up',font=('vivaldi italics',20),height=60,width=220,corner_radius=30,fg_color='#0c7075',hover_color='#0c7075',border_color='#0f969c',border_width=3,command=login)
google_button=ctk.CTkButton(widgetframe_su,text="",image=google,fg_color='#072e33',hover_color='#072e33',width=50,border_width=3,border_color='#0c7075')
phon_button=ctk.CTkButton(widgetframe_su,text="",image=phon,width=50,fg_color='#072e33',hover_color='white')
instagram_button=ctk.CTkButton(widgetframe_su,text="",image=instagram,width=50,fg_color='white',hover_color='white')

#placing the buttons
signup_label.place(x=50,y=20)
signup_button.place(x=150,y=350)
google_button.place(x=150,y=500)
instagram_button.place(x=230,y=500)
phon_button.place(x=310,y=500)

#email address validator
valid_image = ctk.CTkImage(Image.open(r"valid.png"),size=(40,40))
invalid_image = ctk.CTkImage(Image.open(r"invalid.png"),size=(40,40))
feedback_label = ctk.CTkLabel(email_address, text="", font=("Helvetica", 16),bg_color='#0c7075',fg_color='#0c7075',width=30,height=30)
feedback_label.place(x=450,y=20)

def validate_email(event):
    email = email_address.get()
    # Regular expression to check the validity of the email including domain
    email_regex = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    valid_length = 5 <= len(email) <= 254    
    if re.match(email_regex, email) and valid_length:
        feedback_label.configure(image=valid_image, compound='left', fg_color="#0c7075")
    else:
        feedback_label.configure(image=invalid_image, compound='left', fg_color="#0c7075")

# Bind the validate_email function to the KeyRelease event
email_address.bind("<KeyRelease>", validate_email)

window.mainloop()