import customtkinter as ctk
import tkinter as tk,tkinter
from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import mysql.connector
import time as time
import re
import itertools
from threading import Thread

#DATABASE

'''conn = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM your_table")'''


#SIGN UP PAGE 
window=ctk.CTk()
window.configure(fg_color='#093e44')
window.title("Groceria")
window.geometry('1120x630')
my_font=ctk.CTkFont(family='Vivaldi Italic',size=50)
fnt=ctk.CTkFont(family='Vivaldi Italics',size=15)
fnt1=ctk.CTkFont(family='Vivaldi Italics',size=20)
fnt2=ctk.CTkFont(family='Vivaldi Italics',size=40)
logo_image=ctk.CTkImage(Image.open(r"logo1.png"),size=(80,80))
logo_image_one=ctk.CTkImage(Image.open(r"logo1.png"),size=(65,65))
background_image1=ctk.CTkImage(Image.open(r"groceria.png"),size=(450,450))
background_image=ctk.CTkImage(Image.open(r"groceria.png"),size=(800,300))


#Sign Up Mainframe
signup_mainframe=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
signup_mainframe.place(x=30,y=30)
signup_backimage=ctk.CTkLabel(signup_mainframe,text='',image=background_image1)
signup_backimage.place(x=575,y=30)

#ALL FRAMES
#LOGIN AND SIGNUP 
forgot_password_mainframe=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
login_mainframe=ctk.CTkFrame(window,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_width=3,border_color='white')

#SHOP 
shop_mainframe=ctk.CTkFrame(window,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_width=3,border_color='white')
tabs_frame = ctk.CTkFrame(shop_mainframe,height=530, width=250,fg_color='#294d61',corner_radius=40,bg_color='#05161a',border_width=3,border_color="#0f969c")  
shop_scrollframe1=ctk.CTkFrame(master=shop_mainframe,height=440,width=745,corner_radius=30,fg_color='#294d61',bg_color='#05161a',border_width=3,border_color="#0f969c")
shop_widgets=ctk.CTkFrame(master=shop_mainframe,height=70,width=740,fg_color='#05161a',bg_color='#05161a')
shop_widgets_menu=ctk.CTkFrame(master=shop_mainframe,height=70,width=740,fg_color='#05161a',bg_color='#05161a')
shop_widgets_menu.propagate(0)

#TAB FRAMES
supplies_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
fruits_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
dairy_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
vegetable_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
search_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
profile_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
orders_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
settings_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
supports_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
notification_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
cart_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
logo=ctk.CTkLabel(shop_mainframe,text='',fg_color='#05161a',image=logo_image)

frame_list=[signup_mainframe,forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]


#Images
open=ctk.CTkImage(Image.open(r"open.png"),size=(30,30))
prof=ctk.CTkImage(Image.open(r"user-interface.png"),size=(50,50)) 
carti=ctk.CTkImage(Image.open(r"user-interface.png"),size=(50,50))
logoutimg=ctk.CTkImage(Image.open(r"logout.png"),size=(50,50))
menu=ctk.CTkImage(Image.open(r"menu.png"),size=(60,60))
cartt=ctk.CTkImage(Image.open(r"shopcart.png"),size=(50,50))
notify=ctk.CTkImage(Image.open(r"notify.png"),size=(50,50))
seac=ctk.CTkImage(Image.open(r"search.png"),size=(40,40))

# category icons for main shop window
fru=ctk.CTkImage(Image.open(r"fruits.png"),size=(50,50))
essen=ctk.CTkImage(Image.open(r"essentials.png"),size=(50,50))
vegtab=ctk.CTkImage(Image.open(r"vegetables.png"),size=(50,50))
dair=ctk.CTkImage(Image.open(r"dairy.png"),size=(50,50))

#advertisement images for main shop window
juices = ctk.CTkImage(Image.open("juices.png"), size=(940, 160))
rice = ctk.CTkImage(Image.open("rice.png"), size=(940, 160))
cookies = ctk.CTkImage(Image.open("cookies.png"), size=(940, 160))
snacks = ctk.CTkImage(Image.open("snacks.png"), size=(940, 160))

#advertisement images for the shop window with menu button
juices_menu= ctk.CTkImage(Image.open("juices.png"), size=(690, 160))
rice_menu = ctk.CTkImage(Image.open("rice.png"), size=(690, 160))
cookies_menu= ctk.CTkImage(Image.open("cookies.png"), size=(690, 160))
snacks_menu = ctk.CTkImage(Image.open("snacks.png"), size=(690, 160))

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
close=ctk.CTkImage(Image.open(r"close.png"),size=(60,60))

def animation():

        def animate_gif(counter=0):
            gif_label.configure(image=frames[counter])
            counter +=1
            if counter == len(frames):
                counter = 0
            loading.after(40, animate_gif, counter)

        def long_running_process():
                time.sleep(10)
                loading.place_forget()
                show_login_frame()
                
        loading = ctk.CTkFrame(window, fg_color='#05161a', corner_radius=30, width=1060, height=580,border_width=3,border_color='white')
        loading.propagate(0)
        loading.place(x=30, y=30)

    # Load GIF
        gif = Image.open("animation.gif")
        frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]

    # Label to display GIF frames
        gif_label = ctk.CTkLabel(loading,fg_color='#05161a',text='',height=562,width=1000,corner_radius=30)
        gif_label.pack(pady=10)

        animate_gif()

    # Start the long-running process in a separate thread
        loading_thread = Thread(target=long_running_process)
        loading_thread.start()

#animation()

def load_animation():

        def animate_gif(counter=0):
            gif_label.configure(image=frames[counter])
            counter +=1
            if counter == len(frames):
                counter = 0
            loading.after(40, animate_gif, counter)

        def long_running_process():
                time.sleep(7)
                loading.place_forget()
                show_login_frame()
         
        loading = ctk.CTkFrame(window, fg_color='#05161a', corner_radius=30, width=1060, height=580,border_width=3,border_color='white')
        loading.propagate(0)
        loading.place(x=30, y=30)

    # Load GIF
        gif = Image.open("loading_animation.gif")
        frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]

    # Label to display GIF frames
        gif_label = ctk.CTkLabel(loading,fg_color='#05161a',text='',height=562,width=1000,corner_radius=30)
        gif_label.pack(pady=10)

        animate_gif()

    # Start the long-running process in a separate thread
        loading_thread = Thread(target=long_running_process)
        loading_thread.start()

#ALL DEFINED FUCTIONS FOR TAB
def fgpass():
    
    #load_animation()
    
    for i in frame_list:
            i.place_forget()
    
    forgot_password_mainframe.place(x=30,y=30)
    
    #FORGOT PASSWORD TAB
    forgottab_backimage=ctk.CTkLabel(forgot_password_mainframe,text='',image=background_image1)
    forgottab_backimage.place(x=575,y=30)
    forgottab_frame=ctk.CTkFrame(forgot_password_mainframe,height=520,width=480,bg_color='#05161a',fg_color='#072e33',corner_radius=30,border_width=3,border_color='white')
    forgottab_frame.place(x=30,y=30)
    
    #Widgets
    email_address=ctk.CTkEntry(forgottab_frame,height=80,width=440,corner_radius=30,border_width=3,                                 border_color='#0f969c',fg_color='#0c7075')
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
    feedback_label.place(x=380,y=20)
    
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
             
    #load_animation()
    
    for i in frame_list:
                        i.place_forget()
                      
    login_mainframe.place(x=30,y=30)
    login_backimage=ctk.CTkLabel(login_mainframe,text='',image=background_image1)
    login_backimage.place(x=575,y=30)     
    
    #RETURN TO SIGNUPN PAGE FUNCTION
    def signup_return():
        login_mainframe.place_forget()   
        signup_mainframe.place(x=30,y=30)
               
   #frame 
    loginframe=ctk.CTkFrame(login_mainframe,border_width=3,border_color='#093e44',height=520,width=480,bg_color='#05161a',fg_color='#072e33',corner_radius=30)
    loginframe.place(x=30,y=30)
    
    #buttons 
    login_button=ctk.CTkButton(loginframe,text='Login',font=('vivaldi italics',20),height=60,width=220,corner_radius=30,fg_color='#0c7075',hover_color='#0c7075',text_color='white',border_width=3,border_color='#0f969c',command=checked)
    login_label=ctk.CTkLabel(loginframe,text=' Log In',font=('vivaldi italics',40),text_color='white')
    google_button=ctk.CTkButton(loginframe,text="",image=google,fg_color='#072e33',hover_color='white',width=50)
    phon_button=ctk.CTkButton(loginframe,text="",image=phon,width=50,fg_color='#072e33',hover_color='white')
    instagram_button=ctk.CTkButton(loginframe,text="",image=instagram,width=50,fg_color='#072e33',hover_color='white')
    forgot_password_btn=ctk.CTkButton(loginframe,text='forgot password ? ',command=fgpass,fg_color='#072e33',text_color='white',hover_color='#072e33')
    signup_return=ctk.CTkButton(loginframe,text='Create Account ',fg_color='#072e33',text_color='white',hover_color='#072e33',command=signup_return)
 
       #ENTRIES
    email_address=ctk.CTkEntry(loginframe,height=80,width=440,corner_radius=30,border_width=3,fg_color='#0c7075',border_color='#0f969c')
    password=ctk.CTkEntry(loginframe,height=80,width=210,corner_radius=30,border_width=3,fg_color='#0c7075',border_color='#0f969c')    
    email_address_label=ctk.CTkLabel(email_address,text='Email',font=('vivaldi italics',10),text_color='white')
    password_label=ctk.CTkLabel(password,text='Password',font=('vivaldi italics',10),text_color='white')    
    
    #email validation
    valid_image = ctk.CTkImage(Image.open(r"valid.png"),size=(40,40))
    invalid_image = ctk.CTkImage(Image.open(r"invalid.png"),size=(40,40))
    feedback_label = ctk.CTkLabel(email_address, text="", font=("Helvetica", 16),bg_color='#0c7075',fg_color='#0c7075',        width=30,height=30)
    feedback_label.place(x=380,y=20)

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
    login_button.place(x=120,y=290)
    email_address.place(x=20,y=80)
    password.place(x=20,y=180)
    google_button.place(x=150,y=400)
    instagram_button.place(x=230,y=400)
    phon_button.place(x=310,y=400)
    signup_return.place(x=160,y=350)

def checked():
    
    #load_animation()
    for i in frame_list:
        i.place_forget()   
    logo.place(x=160,y=20)      
    shop_mainframe.place(x=30, y=30)    
    tabs_frame.propagate(0)
    shop_scrollframe=ctk.CTkScrollableFrame(shop_mainframe,height=380,width=960,corner_radius=30,fg_color='#294d61',bg_color='#05161a',border_width=0,border_color="#0f969c")
    shop_scrollframe.propagate(0)
            
    shop_scrollframe1.propagate(0)
    shop_scrollframe.place(x=25,y=110)      
     
        
    def supplie_products():
                        
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            supplies_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(supplies_frame,text='Supplies',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            def back():
                supplies_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
             
            bckbtn = ctk.CTkButton(supplies_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5) 
            logo=ctk.CTkButton(supplies_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(supplies_frame, height=400, width=960, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=20, y=70)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=100,height=1200)
            shop_scrollframe1.pack()

            products = [
    'Product1', 'Product2', 'Product3', 'Product4', 'Product5',
    'Product6', 'Product7', 'Product8', 'Product9', 'Product10',
    'Product11', 'Product12'
]

            positions = [ (10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),
    (10, 610), (480, 610), (10, 810), (480, 810), (10, 1010), (480, 1010)]

            for i, product in enumerate(products):
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=140, width=140, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=180, y=20)                                                
   
    def fruit_products():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
                
            fruits_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(fruits_frame,text='Fruits',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            def back():
                fruits_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
            
            bckbtn = ctk.CTkButton(fruits_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5)
            logo=ctk.CTkButton(fruits_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(fruits_frame, height=400, width=960, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=20, y=70)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=100,height=1200)
            shop_scrollframe1.pack()

            products = [
    'Product1', 'Product2', 'Product3', 'Product4', 'Product5',
    'Product6', 'Product7', 'Product8', 'Product9', 'Product10',
    'Product11', 'Product12'
]

            positions = [
    (10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),
    (10, 610), (480, 610), (10, 810), (480, 810), (10, 1010), (480, 1010)
]

            for i, product in enumerate(products):
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=140, width=140, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=180, y=20)         
    
    def dairy_products():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            dairy_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(dairy_frame,text='Dairy',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            def back():
                dairy_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
             
            bckbtn = ctk.CTkButton(dairy_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5)
            logo=ctk.CTkButton(dairy_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(dairy_frame, height=400, width=960, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=20, y=70)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=100,height=1200)
            shop_scrollframe1.pack()

            products = [
    'Product1', 'Product2', 'Product3', 'Product4', 'Product5',
    'Product6', 'Product7', 'Product8', 'Product9', 'Product10',
    'Product11', 'Product12'
]

            positions = [
     (10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),
    (10, 610), (480, 610), (10, 810), (480, 810), (10, 1010), (480, 1010)
]

            for i, product in enumerate(products):
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=140, width=140, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=180, y=20)                
    
    def vegetable_products():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            vegetable_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(vegetable_frame,text='Vegetables',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            def back():
                vegetable_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
    
            bckbtn = ctk.CTkButton(vegetable_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5)
            logo=ctk.CTkButton(vegetable_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(vegetable_frame, height=400, width=960, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=20, y=70)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=100,height=1200)
            shop_scrollframe1.pack()

            products = [
    'Product1', 'Product2', 'Product3', 'Product4', 'Product5',
    'Product6', 'Product7', 'Product8', 'Product9', 'Product10',
    'Product11','Product12'
]

            positions = [
     (10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),
    (10, 610), (480, 610), (10, 810), (480, 810), (10, 1010), (480, 1010)
]

            for i, product in enumerate(products):
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=140, width=140, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=180, y=20)                    
                                                             
    #widgets in scrollable frame   
    # Advertisement Frame
    show = ctk.CTkLabel(shop_scrollframe, width=960, height=700, fg_color='#294d61',text='')
    show.grid(column=0,row=0)
    advertisement = ctk.CTkLabel(shop_scrollframe, width=960, height=200, fg_color='#294d61',text='')
    advertisement.place(x=-10,y=0)
    
#CATEGORY TABS    
    category_frame=ctk.CTkFrame(shop_scrollframe,height=160,width=850,corner_radius=30,fg_color='#05161a',border_width=3,border_color='#0f969c') 
    product_frame=ctk.CTkFrame(shop_scrollframe,height=340,width=920,corner_radius=30,fg_color='#05161a',border_width=3,border_color='#0f969c')  
    category_label= ctk.CTkLabel(category_frame,text_color='white', width=100, height=60, fg_color='#05161a',text='Categories:',font=fnt1)
    sale_label= ctk.CTkLabel(shop_scrollframe,text_color='white', width=100, height=60, fg_color='#05161a',text='Grab the Trending Deals now !!',font=fnt1)  
    vegetables=ctk.CTkButton(category_frame,text='Veges',image=vegtab,height=70,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=vegetable_products)   
    fruits=ctk.CTkButton(category_frame,text='Fruits',image=fru,height=70,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=fruit_products)
    dairy=ctk.CTkButton(category_frame,text='Dairy',height=70,image=dair,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=dairy_products)   
    essentials=ctk.CTkButton(category_frame,text='Supplies',image=essen,height=70,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=supplie_products)
    
    #products
    product1=ctk.CTkLabel(product_frame,text='',height=240,width=158,fg_color='white',corner_radius=20)
    product1.place(x=25,y=80)
    product2=ctk.CTkLabel(product_frame,text='',height=240,width=158,fg_color='white',corner_radius=20)
    product2.place(x=203,y=80)
    product3=ctk.CTkLabel(product_frame,text='',height=240,width=158,fg_color='white',corner_radius=20)
    product3.place(x=381,y=80)
    product4=ctk.CTkLabel(product_frame,text='',height=240,width=158,fg_color='white',corner_radius=20)
    product4.place(x=559,y=80)
    product4=ctk.CTkLabel(product_frame,text='',height=240,width=158,fg_color='white',corner_radius=20)
    product4.place(x=737,y=80)
    
    #placing of tabs
    category_frame.place(x=50,y=180)
    sale_label.place(x=50,y=375)
    product_frame.place(x=10,y=360)
    category_label.place(x=30,y=10)
    dairy.place(x=430,y=70)
    fruits.place(x=220,y=70)
    vegetables.place(x=10,y=70)    
    essentials.place(x=640,y=70)      
    
    #scrollable frame with menu button on screen
    advertisement_menu= ctk.CTkLabel(shop_scrollframe1, width=700, height=300, fg_color='#294d61',text='')
    advertisement_menu.place(x=20,y=20)
    category_frame_menu=ctk.CTkFrame(tabs_frame,height=150,width=210,corner_radius=30,fg_color='#05161a',border_width=3,border_color='#0f969c')
    product_frame_menu=ctk.CTkFrame(shop_scrollframe1,height=210,width=675,corner_radius=30,fg_color='#05161a',border_width=3,border_color='#0f969c')
    
#CATEGORY TABS
    vegetables=ctk.CTkButton(category_frame_menu,text='',image=vegtab2,height=50,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=vegetable_products)    
    fruits=ctk.CTkButton(category_frame_menu,text='',image=fru2,height=50,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=fruit_products)    
    dairy=ctk.CTkButton(category_frame_menu,text='',height=50,image=dair2,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=dairy_products)    
    essentials=ctk.CTkButton(category_frame_menu,text='',image=essen2,height=50,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=supplie_products)
    
    product1=ctk.CTkLabel(product_frame_menu,text='',height=170,width=150,fg_color='white',corner_radius=20)
    product1.place(x=25,y=20)
    product2=ctk.CTkLabel(product_frame_menu,text='',height=170,width=150,fg_color='white',corner_radius=20)
    product2.place(x=185,y=20)
    product3=ctk.CTkLabel(product_frame_menu,text='',height=170,width=150,fg_color='white',corner_radius=20)
    product3.place(x=345,y=20)
    product4=ctk.CTkLabel(product_frame_menu,text='',height=170,width=150,fg_color='white',corner_radius=20)
    product4.place(x=505,y=20)
    
    
    #placing tabs and widgets  
    category_frame_menu.place(x=20,y=280)
    fruits.place(x=110,y=10)
    dairy.place(x=10,y=80)
    vegetables.place(x=10,y=10)
    essentials.place(x=110,y=80)
        
#DEFINING THE TABS

#SEARCH TAB
    def search_tab():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            search_frame.place(x=30,y=30)
            logo=ctk.CTkLabel(search_frame,image= logo_image_one,text='')
            logo.place(x=135,y=4)
            tab_namelabel=ctk.CTkLabel(search_frame,text='Search',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            def back():
                search_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
    
            bckbtn = ctk.CTkButton(search_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5) 
            bckbtn.place(x=40, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(search_frame, height=400, width=960, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=20, y=70)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=100,height=1200)
            shop_scrollframe1.pack()

            products = [
    'Product1', 'Product2', 'Product3', 'Product4', 'Product5',
    'Product6', 'Product7', 'Product8', 'Product9', 'Product10',
    'Product11', 'Product12'
]

            positions = [
     (10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),
    (10, 610), (480, 610), (10, 810), (480, 810), (10, 1010), (480, 1010)
]

            for i, product in enumerate(products):
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=140, width=140, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=180, y=20)      
                
#PROFILE TAB      
    def profile_tab():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            profile_frame.place(x=30,y=30)
            
            #widgets in profile tab     
            logo=ctk.CTkButton(profile_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)       
            tab_namelabel=ctk.CTkLabel(profile_frame,text='Profile',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')        
            profile_tab_one=ctk.CTkLabel(profile_frame,text='',fg_color='#294d61',height=480,width=600,corner_radius=50) 
            profile_tab_two=ctk.CTkLabel(profile_frame,text='',fg_color='#294d61',height=480,width=380,corner_radius=50)      
                
            prof_image=ctk.CTkButton(profile_tab_one,text='',corner_radius=50,image=prof,fg_color='#ffffff',border_width=3,width=200,height=200)
            edit_profile=ctk.CTkButton(profile_tab_one,text='Edit Profile',corner_radius=50,image=prof,fg_color='#0c7075',border_width=3,width=400,height=60)
            delete_button=ctk.CTkButton(profile_tab_two,text='Delete Acoount',font=('Helvetica',30),border_width=4,border_color='#811331',fg_color='#0c7075',height=60,width=280,corner_radius=30)
            terms_button=ctk.CTkButton(profile_tab_two,text='Terms & Conditions ',font=('Helvetica',30),border_width=0,border_color='#811331',fg_color='#0c7075',height=60,width=280,corner_radius=30)
            about_button=ctk.CTkButton(profile_tab_two,text='About Us',font=('Helvetica',30),border_width=0,border_color='#811331',fg_color='#0c7075',height=60,width=280,corner_radius=30)
            fullname_label=ctk.CTkLabel(profile_tab_one,text='First name',text_color='white',font=('vivaldi italics',20))         
            lastname_label=ctk.CTkLabel(profile_tab_one,text='Last name',text_color='white',font=('vivaldi italics',20))            
            email_address_label=ctk.CTkLabel(profile_tab_one,text='Email',text_color='white',font=('vivaldi italics',20))
            address=ctk.CTkLabel(profile_tab_one,text='Address',text_color='white',font=('vivaldi italics',20))
            pincode=ctk.CTkLabel(profile_tab_one,text='pincode',text_color='white',font=('vivaldi italics',20))
            
                     
            def back():
                profile_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
    
            bckbtn = ctk.CTkButton(profile_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5)
            
            #placing widgets           
            profile_tab_one.place(x=30,y=70)
            profile_tab_two.place(x=650,y=70)
            tab_namelabel.place(x=220, y=10)
            delete_button.place(x=20,y=400)
            terms_button.place(x=20,y=100)
            about_button.place(x=20,y=250)
            prof_image.place(x=40,y=40)
            edit_profile.place(x=100,y=400)
            bckbtn.place(x=40, y=10)
            
            lastname_label.place(x=450,y=40)
            email_address_label.place(x=300,y=100)
            fullname_label.place(x=300,y=40)
            address.place(x=300,y=200)
            pincode.place(x=300,y=300)

#  ORDERS TAB 

    def orders_tab():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            orders_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(orders_frame,text='Orders',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            def back():
                orders_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
             
            bckbtn = ctk.CTkButton(orders_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5) 
            logo=ctk.CTkButton(orders_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(orders_frame, height=400, width=960, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=20, y=70)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=100,height=1200)
            shop_scrollframe1.pack()

            '''  products = [ 
    'Product1', 'Product2', 'Product3', 'Product4', 'Product5',
    'Product6', 'Product7', 'Product8', 'Product9', 'Product10',
    'Product11', 'Product12'
]'''
            products=[]
            positions = [
     (10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),
    (10, 610), (480, 610), (10, 810), (480, 810), (10, 1010), (480, 1010)
]

            for i, product in enumerate(products):
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=140, width=140, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=180, y=20)      
          
            if len(products)==0:
              no_orders_label=ctk.CTkLabel(scroll_frame,text="No Orders Yet ",text_color="grey",font=fnt2)       
              no_orders_label.place(x=40,y=50)
            else:
                print('done')     
#SETTINGS TAB  
    
    def settings_tab():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            settings_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(settings_frame,text='Settings',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            def back():
                settings_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
    
            bckbtn = ctk.CTkButton(settings_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5) 
            logo=ctk.CTkButton(settings_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)
 
 #SUPPORTS TAB  
                     
    def supports_tab():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            supports_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(supports_frame,text='Contact Us',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=430, y=20)
            def back():
                supports_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
    
            bckbtn = ctk.CTkButton(supports_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5)
            logo=ctk.CTkButton(supports_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            help_namelabel=ctk.CTkLabel(supports_frame,text="We're here to help.",font=('Helvetica',35),fg_color='#05161a',text_color='grey')
            help_namelabel.place(x=390, y=90)
            divider=ctk.CTkFrame(supports_frame,width=700,height=3,border_width=0,border_color='grey',fg_color='grey',corner_radius=20)
            divider.place(x=215,y=135)
            help_sales=ctk.CTkLabel(supports_frame,text='Sales',fg_color='#0c7075',bg_color='#05161a',height=150,width=240,corner_radius=20,text_color='white',font=fnt1)
            help_returns=ctk.CTkLabel(supports_frame,text='Returns',fg_color='#0c7075',bg_color='#05161a',height=150,width=240,corner_radius=20,text_color='white',font=fnt1)
            help_complaints=ctk.CTkLabel(supports_frame,text='Complaints',fg_color='#0c7075',bg_color='#05161a',height=150,width=240,corner_radius=20,text_color='white',font=fnt1)
            help_marketing=ctk.CTkLabel(supports_frame,text='Marketing',fg_color='#0c7075',bg_color='#05161a',height=150,width=240,corner_radius=20,text_color='white',font=fnt1)
            help_sales.place(x=35,y=170)
            help_returns.place(x=285,y=170)
            help_complaints.place(x=535,y=170)
            help_marketing.place(x=785,y=170)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)
  
 #NOTIFICATION TAB   
       
    def notification_tab():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            notification_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(notification_frame,text='Notifications',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            def back():
                notification_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
    
            bckbtn = ctk.CTkButton(notification_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5) 
            logo=ctk.CTkButton(notification_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(notification_frame, height=400, width=960, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=20, y=70)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=100,height=1200)
            shop_scrollframe1.pack()

            '''  products = [ 
    'Product1', 'Product2', 'Product3', 'Product4', 'Product5',
    'Product6', 'Product7', 'Product8', 'Product9', 'Product10',
    'Product11', 'Product12'
]'''
            products=[]
            positions = [
     (10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),
    (10, 610), (480, 610), (10, 810), (480, 810), (10, 1010), (480, 1010)
]

            for i, product in enumerate(products):
                product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
                product_label.place(x=positions[i][0], y=positions[i][1])
    
                image_button= ctk.CTkButton(product_label, text='', height=140, width=140, corner_radius=20, fg_color='white', font=('Helvetica', 50),border_width=3)
                image_button.place(x=20, y=20)
                info_label=ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff',border_width=3)
                info_label.place(x=180, y=20)      
          
            if len(products)==0:
              no_orders_label=ctk.CTkLabel(scroll_frame,text="No Notifications ",text_color="grey",font=fnt2)       
              no_orders_label.place(x=40,y=50)
            else:
                print('done')     
            
#CART TAB      
    def cart_tab():
            
            frame_list=[ forgot_password_mainframe,login_mainframe,shop_mainframe,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame]
            for i in frame_list:
                i.place_forget()
            
            cart_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(cart_frame,text='Cart',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            def back():
                cart_frame.place_forget()
                shop_mainframe.place(x=30,y=30)
    
            bckbtn = ctk.CTkButton(cart_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5)
            logo=ctk.CTkButton(cart_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)                                                       
    
    #widgets in the menu
    orders = ctk.CTkButton(tabs_frame, text="Orders          ",image=open, fg_color="#05161a", font=fnt1, corner_radius=20, width=210, height=40,border_width=3,compound='right',text_color='white',command=orders_tab,border_color="#0f969c")
    profile = ctk.CTkButton(tabs_frame, text="   Hi user ", fg_color="#ffffff", font=fnt1, corner_radius=20, width=210, height=100,border_width=3,compound='left',text_color='black',image=prof,command=profile_tab)
    hpc = ctk.CTkButton(tabs_frame, text="Contact Us      ", fg_color="#05161a", font=fnt1, corner_radius=20, width=210, height=40,image=open,border_width=3,text_color='white',compound='right',command=supports_tab,border_color="#0f969c")
    settings = ctk.CTkButton(tabs_frame, text="Settings          ", fg_color="#05161a", font=fnt1, corner_radius=20, width=210, height=40,image=open,border_width=3,text_color='white',compound='right',command=settings_tab,border_color="#0f969c")
    logout= ctk.CTkButton(tabs_frame, text="", fg_color="#0f969c", font=fnt1, corner_radius=20, width=210, height=40, command=login,border_width=3,image=logoutimg,text_color='black')
    
    # placing tab buttons    
    profile.place(x=20, y=20)
    orders.place(x=20, y=130)
    hpc.place(x=20, y=180)
    settings.place(x=20, y=230)
    logout.place(x=20,y=450)
    
    #widgets with menu
    menu_searchbox=ctk.CTkEntry(shop_widgets_menu,fg_color='#0c7075',width=420,height=60,corner_radius=20,border_width=3,bg_color='#05161a')
    menu_notification_button=ctk.CTkButton(shop_widgets_menu,text='',image=notify,fg_color='#05161a',width=50,height=50,corner_radius=20,border_width=0,bg_color='#05161a',command=notification_tab)
    menu_cart_button=ctk.CTkButton(shop_widgets_menu,text='',image=cartt,fg_color='#0c7075',width=50,height=50,corner_radius=20,border_width=3,bg_color='#05161a',command=cart_tab)
    menu_search_button=ctk.CTkButton(shop_widgets_menu,text='',image=seac,fg_color='#05161a',width=50,height=30,corner_radius=20,border_width=3,bg_color='#0c7075',border_color='#0f969c',command=search_tab)
    
    #placing widgets with menu
    menu_notification_button.place(x=630,y=5)
    menu_cart_button.place(x=530,y=5)  
    menu_search_button.place(x=435,y=10)
    menu_searchbox.place(x=100,y=5)
    
    #widgets on shop without menu
    searchbox=ctk.CTkEntry(shop_widgets,fg_color='#0c7075',width=500,height=60,corner_radius=20,border_width=3,bg_color='#05161a')
    notification_button=ctk.CTkButton(shop_widgets,text='',image=notify,fg_color='#05161a',width=50,height=50,corner_radius=20,border_width=0,bg_color='#05161a',command=notification_tab)
    cart_button=ctk.CTkButton(shop_widgets,text='',image=cartt,fg_color='#0c7075',width=50,height=50,corner_radius=20,border_width=3,bg_color='#05161a',command=cart_tab)
    search_button=ctk.CTkButton(shop_widgets,text='',image=seac,fg_color='#05161a',width=50,height=30,corner_radius=20,border_width=3,bg_color='#0c7075',border_color='#0f969c',command=search_tab)    
    #placing the widgets without menu
    shop_widgets.place(x=270,y=25)
    notification_button.place(x=630,y=5)
    cart_button.place(x=520,y=5)
    search_button.place(x=420,y=10)
    searchbox.place(x=5,y=5)
    
#MENU BUTTON FUNCTIONING AND DEFINING
    def function_one():
        shop_scrollframe.place_forget()
        shop_scrollframe1.place(x=290,y=110)            
        tabs_frame.place(x=25,y=25)
        product_frame_menu.place(x=23,y=195)
        
        #withdrawing the widgets without menu
        menubtn.place_forget()     
        logo.place_forget()
        shop_widgets.place_forget()
        
        #placing the widgets with menu 
        shop_widgets_menu.place(x=285,y=25)        
        
    def function_two():
        menubtn.place(x=50,y=30)
        tabs_frame.place_forget()
        shop_scrollframe1.place_forget()   
        shop_scrollframe.place(x=25,y=110)
        
        #placing the widgets without menu
        logo.place(x=160,y=20)
        shop_widgets.place(x=270,y=25)
        
        #withdrawing the widgets without menu
        shop_widgets_menu.place_forget()              
      
    def click():
        global click_count
        click_count += 1
        if click_count == 1:
            function_one()
        elif click_count == 2:
            function_two()
            click_count = 0
    menubtn=ctk.CTkButton(shop_mainframe,text='',image=menu,fg_color='#05161a',command=click,corner_radius=20,height=40,width=40,hover_color='#05161a',border_width=0,bg_color='#05161a')
    menubtn.place(x=50,y=30)
    close_menu=ctk.CTkButton(shop_widgets_menu,text='',height=40,width=60,command=click,image=close,fg_color='#05171a') 
    close_menu.place(x=20,y=5)
# ADVERTISEMENT FUNCTION FOR SHOP WINDOW WITH MENU
    #image list
    canvas_menu = ctk.CTkCanvas(advertisement_menu, width=720, height=160)
    canvas_menu.configure(bg='#294d61')
    canvas_menu.place(x=0, y=0)
        
    images_menu = [juices_menu, rice_menu, cookies_menu, snacks_menu]
    commands = [fruit_products, vegetable_products, supplie_products, dairy_products]

    # Create buttons for each image with corresponding commands
    buttons_menu= [ctk.CTkButton(canvas_menu, image=image, width=720, fg_color='#294d61',height=150, command=command,text='') for image, command in zip(images_menu, commands)]

        # Function to animate the sliding effect
    def slide_images(canvas_menu, buttons_menu, duration=25, steps=30):
        button_iter = itertools.cycle(buttons_menu)  # Create an iterator that cycles through the buttons
        current_button = next(button_iter)
        window_id = canvas_menu.create_window(0, 0, anchor='nw', window=current_button)
        canvas_menu.update()

        def animate():
            nonlocal current_button, window_id
            next_button = next(button_iter)
            next_window_id = canvas_menu.create_window(canvas_menu.winfo_width(), 0, anchor='nw', window=next_button)
            canvas_menu.update()

            for step in range(steps + 1):
                offset = step / steps * canvas_menu.winfo_width()
                canvas_menu.coords(window_id, -offset, 0)
                canvas_menu.coords(next_window_id, canvas_menu.winfo_width() - offset, 0)
                canvas_menu.update()
                canvas_menu.after(duration // steps)

            canvas_menu.delete(window_id)
            current_button = next_button
            window_id = next_window_id
            canvas_menu.after(3000, animate)  # Schedule the next animation after 3000 milliseconds (3 seconds)

        animate()

    slide_images(canvas_menu, buttons_menu)
    
    
    
#ADVERTISEMENT FUCNTION FOR SHOP WINDOW WITHOUT MENU
    #Image list

# Create a canvas to hold the images
    canvas = ctk.CTkCanvas(advertisement, width=960, height=160)
    canvas.configure(bg='#294d61')
    canvas.place(x=0, y=0)
      
    images = [juices, rice, cookies, snacks]
    commands = [fruit_products, vegetable_products, supplie_products, dairy_products]

    # Create buttons for each image with corresponding commands
    buttons = [ctk.CTkButton(canvas, image=image,text='' ,width=960, fg_color='#294d61',height=150, command=command) for image, command in zip(images, commands)]

        # Function to animate the sliding effect
    def slide_images(canvas, buttons, duration=25, steps=30):
        button_iter = itertools.cycle(buttons)  # Create an iterator that cycles through the buttons
        current_button = next(button_iter)
        window_id = canvas.create_window(0, 0, anchor='nw', window=current_button)
        canvas.update()

        def animate():
            nonlocal current_button, window_id
            next_button = next(button_iter)
            next_window_id = canvas.create_window(canvas.winfo_width(), 0, anchor='nw', window=next_button)
            canvas.update()

            for step in range(steps + 1):
                offset = step / steps * canvas.winfo_width()
                canvas.coords(window_id, -offset, 0)
                canvas.coords(next_window_id, canvas.winfo_width() - offset, 0)
                canvas.update()
                canvas.after(duration // steps)

            canvas.delete(window_id)
            current_button = next_button
            window_id = next_window_id
            canvas.after(3000, animate)  # Schedule the next animation after 3000 milliseconds (3 seconds)

        animate()

    slide_images(canvas, buttons)

#SIGN UP PAGE SETUP
click_count=0
widgetframe_su=ctk.CTkFrame(signup_mainframe,height=520,width=480,fg_color='#072e33',bg_color='#05161a',corner_radius=30,border_width=3,border_color='#093e44')

#Frame for widgets
signup_label=ctk.CTkLabel(widgetframe_su,text='Create Account !',font=('vivaldi italics',25),text_color='white')

#entry boxes
fullname_entry=ctk.CTkEntry(widgetframe_su,height=80,width=210,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
lastname_entry=ctk.CTkEntry(widgetframe_su,height=80,width=210,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
confirm_password=ctk.CTkEntry(widgetframe_su,height=80,width=210,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
email_address=ctk.CTkEntry(widgetframe_su,height=80,width=440,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')
password=ctk.CTkEntry(widgetframe_su,height=80,width=210,corner_radius=30,border_width=3,border_color='#0f969c',fg_color='#0c7075')

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
existing_user.place(x=150,y=390)

#placing entry boxes
widgetframe_su.place(x=30,y=30)
lastname_entry.place(x=250,y=60)
fullname_entry.place(x=20,y=60)
email_address.place(x=20,y=150)
confirm_password.place(x=250,y=240)
password.place(x=20,y=240)

#buttons
signup_button=ctk.CTkButton(widgetframe_su,text='Sign Up',font=('vivaldi italics',20),height=60,width=220,corner_radius=30,fg_color='#0c7075',hover_color='white',border_color='#0f969c',border_width=3,command=login)
google_button=ctk.CTkButton(widgetframe_su,text="",image=google,fg_color='#072e33',hover_color='#072e33',width=60,border_width=0)
phon_button=ctk.CTkButton(widgetframe_su,text="",image=phon,width=60,fg_color='#072e33',hover_color='white')
instagram_button=ctk.CTkButton(widgetframe_su,text="",image=instagram,width=60,fg_color='#072e33',hover_color='white')

#placing the buttons
signup_label.place(x=50,y=10)
signup_button.place(x=120,y=330)
google_button.place(x=100,y=440)
instagram_button.place(x=200,y=440)
phon_button.place(x=300,y=440)

#email address validator
valid_image = ctk.CTkImage(Image.open(r"valid.png"),size=(40,40))
invalid_image = ctk.CTkImage(Image.open(r"invalid.png"),size=(40,40))
feedback_label = ctk.CTkLabel(email_address, text="", font=("Helvetica", 16),bg_color='#0c7075',fg_color='#0c7075',width=30,height=30)
feedback_label.place(x=380,y=20)

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