import customtkinter as ctk
import tkinter as tk,tkinter
from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import mysql.connector
import time as time
import re
import itertools
from threading import Thread
import smtplib
import sqlite3
import random
from hashlib import sha256
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
global search_frame

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "brajeswarighosh04@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "Swapneswar"        # Replace with your email password

def send_email(to_email, subject, body):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            message = MIMEMultipart()
            message["From"] = EMAIL_ADDRESS
            message["To"] = to_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            server.send_message(message)
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")


#### USER DATABASE  [SERVER] ####
with sqlite3.connect('groceria.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   email_id TEXT PRIMARY KEY,
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   pass_word TEXT NOT NULL,
                   address TEXT,
                   pincode TEXT)''')

def insert_user():
    email_id = email_address.get()
    first_name = fullname_entry.get()
    last_name = lastname_entry.get()
    pass_word = password.get()

    # Hash the password before storing it
    hashed_password = sha256(pass_word.encode()).hexdigest()

    with sqlite3.connect('groceria.db') as conn:
    	cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (email_id, first_name, last_name, pass_word) VALUES (?, ?, ?, ?)",
                       (email_id, first_name, last_name, hashed_password))
        messagebox.showinfo('Success','Successfully registered.')
    except sqlite3.IntegrityError:
        messagebox.showinfo('Error','Registered Email Id .')
        print("Error: Email ID already exists.")
               
 ### SALES TABLE ###
with sqlite3.connect('groceria.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                   product_id TEXT PRIMARY KEY,
                   exp_date TEXT NOT NULL,
                   price TEXT NOT NULL,
                   quantity TEXT NOT NULL,
                   discount TEXT NOT NULL,
                   product_name TEXT NOT NULL,
                   description TEXT NOT NULL)''')       
        

#### CATEGORY PRODUCT TABLES ####

## VEGETABLES ##
with sqlite3.connect('groceria.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS veges (
                   product_id TEXT PRIMARY KEY,
                   exp_date TEXT NOT NULL,
                   price TEXT NOT NULL,
                   quantity TEXT NOT NULL,
                   discount TEXT NOT NULL,
                   product_name TEXT NOT NULL,
                   description TEXT NOT NULL)''')

## FRUITS ##
with sqlite3.connect('groceria.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS fruits (
                   product_id TEXT PRIMARY KEY,
                   exp_date TEXT NOT NULL,
                   price TEXT NOT NULL,
                   quantity TEXT NOT NULL,
                   discount TEXT NOT NULL,
                   product_name TEXT NOT NULL,
                   description TEXT NOT NULL)''')


## DAIRY ##
with sqlite3.connect('groceria.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS dairy (
                   product_id TEXT PRIMARY KEY,
                   exp_date TEXT NOT NULL,
                   price TEXT NOT NULL,
                   quantity TEXT NOT NULL,
                   discount TEXT NOT NULL,
                   product_name TEXT NOT NULL,
                   description TEXT NOT NULL)''')


## ESSENTIALS ##
with sqlite3.connect('groceria.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS supplies (
                   product_id TEXT PRIMARY KEY,
                   exp_date TEXT NOT NULL,
                   price TEXT NOT NULL,
                   quantity TEXT NOT NULL,
                   discount TEXT NOT NULL,
                   product_name TEXT NOT NULL,
                   description TEXT NOT NULL)''')

# Dairy products
dairy_products = [
    ('d001', '15/01/2025', '250', '250g', '0', 'Paneer', 'Fresh Indian cheese'),
    ('d002', '18/01/2025', '125', '1 liter', '0', 'Milk', 'Fresh cow milk'),
    ('d003', '20/01/2025', '180', '200g', '0', 'Butter', 'Creamy butter'),
    ('d004', '22/01/2025', '200', '200g', '0', 'Cheese', 'Sliced cheddar cheese'),
    ('d005', '24/01/2025', '80', '500g', '0', 'Yogurt', 'Fresh, natural yogurt'),
    ('d006', '26/01/2025', '550', '500g', '0', 'Ghee', 'Pure clarified butter'),
    ('d007', '28/01/2025', '120', '200ml', '0', 'Cream', 'Thick, fresh cream'),
    ('d008', '30/01/2025', '70', '500g', '0', 'Curd', 'Fresh, natural curd'),
    ('d009', '01/02/2025', '40', '1 liter', '0', 'Buttermilk', 'Refreshing buttermilk'),
    ('d010', '03/02/2025', '30', '200ml', '0', 'Lassi', 'Sweetened lassi')
]

# Veges products
veges_products = [
    ('v001', '20/01/2025', '300', '1 kg', '0', 'Bell Pepper', 'Fresh and crunchy bell peppers'),
    ('v002', '22/01/2025', '80', '1 bunch', '0', 'Green Onion', 'Fresh green onions'),
    ('v003', '24/01/2025', '210', '1 kg', '0', 'Eggplant', 'Fresh eggplants'),
    ('v004', '26/01/2025', '120', '1 bunch', '0', 'Spinach', 'Fresh spinach leaves'),
    ('v005', '28/01/2025', '100', '1 head', '0', 'Lettuce', 'Fresh and crisp lettuce'),
    ('v006', '30/01/2025', '170', '1 piece', '0', 'Cabbage', 'Fresh green cabbage'),
    ('v007', '01/02/2025', '160', '1 kg', '0', 'Potatoes', 'Fresh potatoes'),
    ('v008', '03/02/2025', '250', '1 piece', '0', 'Cauliflower', 'Fresh cauliflower heads'),
    ('v009', '05/02/2025', '65', '1 bunch', '0', 'Coriander', 'Fresh coriander leaves'),
    ('v010', '07/02/2025', '90', '1 kg', '0', 'Carrot', 'Fresh carrots')
]

# Fruits products
fruits_products = [
    ('f001', '07/02/2025', '400', '1 piece', '0', 'Watermelon', 'Sweet and juicy watermelon'),
    ('f002', '09/02/2025', '330', '1 kg', '0', 'Apple', 'Fresh, crisp apples'),
    ('f003', '11/02/2025', '250', '1 kg', '0', 'Oranges', 'Fresh and tangy oranges'),
    ('f004', '13/02/2025', '80', '1 dozen', '0', 'Banana', 'Ripe bananas'),
    ('f005', '15/02/2025', '200', '1 kg', '0', 'Grapes', 'Fresh grapes'),
    ('f006', '17/02/2025', '300', '1 kg', '0', 'Mango', 'Sweet mangoes'),
    ('f007', '19/02/2025', '150', '1 piece', '0', 'Papaya', 'Fresh papaya'),
    ('f008', '21/02/2025', '200', '1 piece', '0', 'Pineapple', 'Sweet pineapple'),
    ('f009', '23/02/2025', '350', '1 kg', '0', 'Pomegranate', 'Juicy pomegranates'),
    ('f010', '25/02/2025', '250', '250g', '0', 'Strawberries', 'Fresh strawberries')
]

# Supplies products
supplies_products = [
    ('s001', '13/02/2025', '50', '500g', '0', 'Salt', 'Iodized salt, good for health'),
    ('s002', '15/02/2025', '150', '200g', '0', 'Chilli Powder', 'Authentic Kashmiri chilli powder'),
    ('s003', '17/02/2025', '200', '100g', '0', 'Garam Masala', 'Pure garam masala to elevate the taste'),
    ('s004', '19/02/2025', '100', '100g', '0', 'Turmeric Powder', 'Pure turmeric powder'),
    ('s005', '21/02/2025', '60', '1 kg', '0', 'Sugar', 'Granulated sugar'),
    ('s006', '23/02/2025', '120', '1 kg', '0', 'Rice', 'Basmati rice'),
    ('s007', '25/02/2025', '70', '1 kg', '0', 'Wheat Flour', 'Whole wheat flour'),
    ('s008', '27/02/2025', '80', '1 kg', '0', 'Pulses', 'Split chickpeas'),
    ('s009', '01/03/2025', '150', '250g', '0', 'Tea Powder', 'Strong tea powder'),
    ('s010', '03/03/2025', '180', '1 liter', '0', 'Cooking Oil', 'Sunflower cooking oil')
]

#SALES PRODUCTS
sales_products=[('s006', '23/02/2025', '120', '1 kg', '0', 'Rice', 'Basmati rice'),('f009', '23/02/2025', '350', '1 kg', '0', 'Pomegranate', 'Juicy pomegranates'),('v004', '26/01/2025', '120', '1 bunch', '0', 'Spinach', 'Fresh spinach leaves'),('d005', '24/01/2025', '80', '500g', '0', 'Yogurt', 'Fresh, natural yogurt'),('f010', '25/02/2025', '250', '250g', '0', 'Strawberries', 'Fresh strawberries')]

# Insert products into tables
with sqlite3.connect('groceria.db') as conn:
    cursor = conn.cursor()
    cursor.executemany('INSERT  OR REPLACE  INTO dairy (product_id, exp_date, price, quantity, discount, product_name, description) VALUES (?, ?, ?, ?, ?, ?, ?)', dairy_products)
    cursor.executemany('INSERT OR REPLACE INTO veges (product_id, exp_date, price, quantity, discount, product_name, description) VALUES (?, ?, ?, ?, ?, ?, ?)', veges_products)
    cursor.executemany('INSERT OR IGNORE INTO fruits (product_id, exp_date, price, quantity, discount, product_name, description) VALUES (?, ?, ?, ?, ?, ?, ?)', fruits_products)
    cursor.executemany('INSERT OR IGNORE INTO supplies (product_id, exp_date, price, quantity, discount, product_name, description) VALUES (?, ?, ?, ?, ?, ?, ?)', supplies_products)
    cursor.executemany('INSERT OR IGNORE INTO sales (product_id, exp_date, price, quantity, discount, product_name, description) VALUES (?, ?, ?, ?, ?, ?, ?)', sales_products)

#SIGN UP PAGE 
window=ctk.CTk()
window.configure(fg_color='#093e44')
window.title("Groceria")
window.geometry('1120x630')
cat_click_count=0
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
product_frame=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060)
pro_frame = ctk.CTkFrame(product_frame, fg_color="white",width=998,height=433,corner_radius=30)
transit_frame = ctk.CTkFrame(window, width=1060, height=580,corner_radius=60, fg_color='#05161a')
payment_frame = ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
details_frame_pay = ctk.CTkFrame(payment_frame, width=400, height=450, corner_radius=20, fg_color="white")
logo=ctk.CTkLabel(shop_mainframe,text='',fg_color='#05161a',image=logo_image)
logo.place(x=160,y=20)

frame_list=[product_frame,tabs_frame,signup_mainframe,shop_scrollframe1,shop_widgets,shop_widgets_menu,supplies_frame,fruits_frame,dairy_frame,vegetable_frame,search_frame,profile_frame,orders_frame,settings_frame,supports_frame,notification_frame,cart_frame,pro_frame,transit_frame,payment_frame,login_mainframe,details_frame_pay]

#Images
open=ctk.CTkImage(Image.open(r"open1.png"),size=(30,30))
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
bg1=ctk.CTkImage(Image.open(r"dairy.png"),size=(500,500))

#login images
instagram=ctk.CTkImage(Image.open(r"instagram (1).png"),size=(50,50)) 
google=ctk.CTkImage(Image.open(r"google.png"),size=(50,50)) 
phon=ctk.CTkImage(Image.open(r"phone.png"),size=(50,50)) 
backbutn=ctk.CTkImage(Image.open(r"back-button.png"),size=(50,50))
backpic=ctk.CTkImage(Image.open(r"back-button.png"),size=(60,60))  
close=ctk.CTkImage(Image.open(r"close.png"),size=(60,60))

#product images
pro1=ctk.CTkImage(Image.open(r'beetroot.png'),size=(100,100))
pro2=ctk.CTkImage(Image.open(r'carrot.png'),size=(100,100))
pro3=ctk.CTkImage(Image.open(r'pear.png'),size=(100,100))
pro4=ctk.CTkImage(Image.open(r'cheese.png'),size=(100,100))
pro5=ctk.CTkImage(Image.open(r'milk.png'),size=(100,100))

produce1=ctk.CTkImage(Image.open(r'beetroot.png'),size=(80,80))
produce2=ctk.CTkImage(Image.open(r'carrot.png'),size=(80,80))
produce3=ctk.CTkImage(Image.open(r'pear.png'),size=(80,80))
produce4=ctk.CTkImage(Image.open(r'cheese.png'),size=(80,80))


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
                
        loading = ctk.CTkFrame(window, fg_color='#05161a', corner_radius=30, width=1060, height=580,border_width=3,border_color='white')
        loading.propagate(0)
        loading.place(x=30, y=30)

    # Load GIF
        gif = Image.open("animation.gif")
        frames = [ctk.CTkImage(frame.copy(),size=(200,200)) for frame in ImageSequence.Iterator(gif)]

    # Label to display GIF frames
        gif_label = ctk.CTkLabel(loading,fg_color='#05161a',text='',height=562,width=1000,corner_radius=30)
        gif_label.pack(pady=10)

        animate_gif()

    # Start the long-running process in a separate thread
        loading_thread = Thread(target=long_running_process)
        loading_thread.start()

animation()

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
         
        loading = ctk.CTkFrame(window, fg_color='#05161a', corner_radius=30, width=1060, height=580,border_width=3,border_color='white')
        loading.propagate(0)
        loading.place(x=30, y=30)

    # Load GIF
        gif = Image.open("loading_animation.gif")
        frames = [ctk.CTkImage(frame.copy(),size=(200,200)) for frame in ImageSequence.Iterator(gif)]

    # Label to display GIF frames
        gif_label = ctk.CTkLabel(loading,fg_color='#05161a',text='',height=562,width=1000,corner_radius=30)
        gif_label.pack(pady=10)

        animate_gif()

    # Start the long-running process in a separate thread
        loading_thread = Thread(target=long_running_process)
        loading_thread.start()

def back():
              checked()
def sanitize_email(email):
	return email.replace('@', '_at_').replace('.', '_dot_')

def create_user_cart(email):
    sanitized_table_cart = sanitize_email(email)
    with sqlite3.connect('groceria.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {sanitized_table_cart}_cart (
                product_id TEXT NOT NULL,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        except sqlite3.Error as e:
            print(f"An error occurred: {e}") 

def create_user_table(email):
    sanitized_table_name = sanitize_email(email)
    with sqlite3.connect('groceria.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {sanitized_table_name} (
                    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id TEXT NOT NULL,
                    product_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL,
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    order_status TEXT NOT NULL,
                    payment_status TEXT NOT NULL
                )
            ''')
            #messagebox.showerror('Error',f"Table {sanitized_table_name} created successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

# 1. Send Welcome Email After Registration
def send_registration_email(email, first_name):
    subject = "Welcome to Groceria!"
    body = f"Hi {first_name},\n\nThank you for registering with Groceria! We are excited to have you.\n\nHappy Shopping!\nGroceria Team"
    send_email(email, subject, body)

# 2. Send Order Details Email After Order is Placed
def send_order_email(email, order_details):
    subject = "Your Groceria Order Details"
    body = f"Hi,\n\nYour order has been successfully placed!\n\nOrder Details:\n{order_details}\n\nThank you for shopping with us!\nGroceria Team"
    send_email(email, subject, body)

# 3. Send Forgot Password Email with New Password
def send_forgot_password_email(email):
    new_password = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=8))
    hashed_password = sha256(new_password.encode()).hexdigest()

    # Update password in the database
    with sqlite3.connect("groceria.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET pass_word = ? WHERE email_id = ?", (hashed_password, email))
        conn.commit()

    subject = "Reset Your Groceria Password"
    body = f"Hi,\n\nYour password has been reset. Use the new password below to log in:\n\nNew Password: {new_password}\n\nPlease change your password after logging in.\nGroceria Team"
    send_email(email, subject, body)                      
                                                                  
def signup_user():
    email = email_address.get().strip()
    first_name = fullname_entry.get().strip()
    last_name = lastname_entry.get().strip()
    password_value = password.get().strip()
    confirm_password_value = confirm_password.get().strip()

    if not all([email, first_name, last_name, password_value, confirm_password_value]):
        messagebox.showerror("Error", "All fields are required.")
        return

    if password_value != confirm_password_value:
        messagebox.showerror("Error", "Passwords do not match")
        return

    email_regex = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email):
        messagebox.showerror("Error", "Invalid email format")
        return

    hashed_password = sha256(password_value.encode()).hexdigest()

    with sqlite3.connect('groceria.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (email_id, first_name, last_name, pass_word) VALUES (?, ?, ?, ?)",
                           (email, first_name, last_name, hashed_password))
            messagebox.showinfo('Success', 'Successfully registered.')
            create_user_table(email)
            create_user_cart(email)
            login()
            send_registration_email(email, first_name)
        except sqlite3.IntegrityError:
            messagebox.showerror('Error', 'Email ID is already registered.')

def login_user():
    email = email_address_login.get().strip()
    password = password_entry.get().strip()

    if not all([email, password]):
        messagebox.showerror("Error", "All fields are required.")
        return

    email_regex = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email):
        messagebox.showerror("Error", "Invalid email format")
        return

    with sqlite3.connect('groceria.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE email_id = ?", (email,))
            user = cursor.fetchone()

            if user and sha256(password.encode()).hexdigest() == user[3]:
                messagebox.showinfo("Success", "Login successful!")
                checked()
                create_user_table(email)
                create_user_cart(email)
            else:
                messagebox.showerror("Error", "Invalid email or password")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")      
    	
    	              
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
    email=email_address.get()
    password=ctk.CTkButton(forgottab_frame,text=" Reset ",height=60,width=200,corner_radius=30,border_width=3,                            border_color='#0f969c',fg_color='#0c7075',command=send_forgot_password_email(email),font=('vivaldi italics', 20))
    
    #labels
    email_address_label=ctk.CTkLabel(email_address,text='Email',text_color='white',font=('vivaldi italics',10))
    email_address_label.place(x=20,y=4)

    #placing widgets
    email_address.place(x=20,y=140)
    password.place(x=130,y=260)
    
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
    global email_address_login, password_entry  # Declare as global to access in other functions
    
    # Hide other frames and show login frame
    for i in frame_list:
        i.place_forget()
    login_mainframe.place(x=30, y=30)
    
    # Background image for login frame
    login_backimage = ctk.CTkLabel(login_mainframe, text='', image=background_image1)
    login_backimage.place(x=575, y=30)
    
    # Return to signup page function
    def signup_return():
        login_mainframe.place_forget()   
        signup_mainframe.place(x=30, y=30)
    
    # Login frame setup
    loginframe = ctk.CTkFrame(login_mainframe, border_width=3, border_color='#093e44', height=520, width=480, bg_color='#05161a', fg_color='#072e33', corner_radius=30)
    loginframe.place(x=30, y=30)
    
    # Buttons and labels
    login_label = ctk.CTkLabel(loginframe, text='Log In', font=('vivaldi italics', 30), text_color='white')
    login_button = ctk.CTkButton(loginframe, text='Login', font=('vivaldi italics', 20), height=60, width=220, corner_radius=30, fg_color='#0c7075', hover_color='#0c7075', text_color='white', border_width=3, border_color='#0f969c', command=login_user)
    google_button = ctk.CTkButton(loginframe, text="", image=google, fg_color='#072e33', hover_color='white', width=50)
    phon_button = ctk.CTkButton(loginframe, text="", image=phon, width=50, fg_color='#072e33', hover_color='white')
    instagram_button = ctk.CTkButton(loginframe, text="", image=instagram, width=50, fg_color='#072e33', hover_color='white')
    forgot_password_btn = ctk.CTkButton(loginframe, text='Forgot password?', command=fgpass, fg_color='#072e33', text_color='white', hover_color='#072e33',height=30,width=60)
    signup_return = ctk.CTkButton(loginframe, text='Create Account', fg_color='#072e33', text_color='white', hover_color='#072e33', command=signup_return)
    
    # Entries
    email_address_login= ctk.CTkEntry(loginframe, height=80, width=440, corner_radius=30, border_width=3, fg_color='#0c7075', border_color='#0f969c')
    email_address_label = ctk.CTkLabel(email_address_login, text='Email', font=('vivaldi italics', 10), text_color='white')
    email_address_label.place(x=20, y=4)
    password_entry = ctk.CTkEntry(loginframe, height=80, width=210, corner_radius=30, border_width=3, fg_color='#0c7075', border_color='#0f969c')
    password_label = ctk.CTkLabel(password_entry, text='Password', font=('vivaldi italics', 10), text_color='white')
    password_label.place(x=20, y=4)
        
    # Email Validation
    feedback_label_login = ctk.CTkLabel(email_address_login, text="", font=("Helvetica", 16),bg_color='#0c7075',fg_color='#0c7075',width=30,height=30)
    feedback_label_login.place(x=380,y=20)
    
    def validate_email(event):
     global email_address_login
     email = email_address_login.get()
    # Regular expression to check the validity of the email including domain
     email_regex = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
     valid_length = 5 <= len(email) <= 254
     if re.match(email_regex, email) and valid_length:
     	feedback_label_login.configure(image=valid_image, compound='left', fg_color="#0c7075")
     else:
     	feedback_label_login.configure(image=invalid_image, compound='left', fg_color="#0c7075")

    #Binding valid email event
    email_address_login.bind("<KeyRelease>", validate_email)
    
    # Placing the widgets
    login_label.place(x=80, y=20)
    email_address_login.place(x=20, y=80)
    password_entry.place(x=20, y=180)
    forgot_password_btn.place(x=240, y=200)
    login_button.place(x=120, y=290)
    google_button.place(x=120, y=400)
    instagram_button.place(x=200, y=400)
    phon_button.place(x=280, y=400)
    signup_return.place(x=160, y=350)


def checked():
    
    load_animation()
    for i in frame_list:
        i.place_forget()   
           
    shop_mainframe.place(x=30, y=30)
    global searchbox,searchbox_menu    
    tabs_frame.propagate(0)
    shop_scrollframe=ctk.CTkScrollableFrame(shop_mainframe,height=380,width=960,corner_radius=30,fg_color='#294d61',bg_color='#05161a',border_width=0,border_color="#0f969c")
    shop_scrollframe.propagate(0)
            
    shop_scrollframe1.propagate(0)
    shop_scrollframe.place(x=25,y=110)

### PRODUCT DISPLAY FOR SALES ###    	    	    	
    def show_product_details_sales(product_id, product_name, price, discount, description, image_path,quantity):
    	       for frame in frame_list:
    	       	frame.place_forget()
    	       	product_frame.place(x=30, y=30)
    	       	pro_frame.place(x=30,y=110)
    	       
    	       def back():
    	       	for i in frame_list:
    	       		i.place_forget()
    	       		shop_mainframe.place(x=30,y=30)
    	       back_button = ctk.CTkButton(product_frame, text="", image=backpic, command=back,fg_color='#05161a', hover_color='#05161a', height=70, width=70, corner_radius=5)
    	       back_button.place(x=60, y=20)
    	       product_name_label = ctk.CTkLabel(pro_frame, text=product_name, font=('Helvetica', 45), text_color="black", fg_color="white")
    	       product_name_label.place(x=520, y=30)
    	       try:
    	       	img = Image.open(image_path)
    	       	product_image = ctk.CTkImage(img, size=(250, 250))
    	       	image_label = ctk.CTkButton(pro_frame, text='', image=product_image, height=280, width=280, fg_color="white", state=DISABLED,hover_color='white',corner_radius=30,border_width=3)
    	       	image_label.place(x=50, y=75)
    	       except FileNotFoundError:
    	        	image_label = ctk.CTkLabel(pro_frame, text="Image Not Available", height=220, width=220, fg_color="white")
    	        	image_label.place(x=50, y=50)    	       
    	       price_label = ctk.CTkLabel(pro_frame, text=f" ₹{price}", font=('Helvetica', 38), text_color="black")
    	       price_label.place(x=500, y=120)
    	       q_label = ctk.CTkLabel(pro_frame, text=f"Pack Of  {quantity}", font=('Helvetica', 20), text_color="black")
    	       q_label.place(x=500, y=170)
    	       discount_label = ctk.CTkLabel(pro_frame, text=f" -{discount}%   M.R.P", font=('Helvetica', 22), text_color="red")
    	       discount_label.place(x=500, y=200)
    	       ltdeal=ctk.CTkLabel(pro_frame,text="Limited time deal",font=('Helvetica',20),fg_color='red',corner_radius=10,height=20,width=80,text_color="white")
    	       ltdeal.place(x=500,y=90)
    	       description_label = ctk.CTkLabel(pro_frame, text=f"Product details:\n       {description}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black")
    	       description_label.place(x=500, y=230)
    	       add_to_cart_button = ctk.CTkButton(pro_frame, text="Add to Cart", command=lambda: add_to_cart(product_id, product_name, price), fg_color='#0c7075', font=('Helvetica', 28),corner_radius=20, height=50, width=200,text_color='white')
    	       add_to_cart_button.place(x=500, y=300)
    	
    	
### PRODUCT DISPLAY MINI ##    	
    def show_product_details_sales_mini(product_id, product_name, price, discount, description, image_path,quantity):
    	       for frame in frame_list:
    	       	frame.place_forget()
    	       	product_frame.place(x=30, y=30)
    	       	pro_frame.place(x=30,y=110)
    	       
    	       def back():
    	       	for i in frame_list:
    	       		i.place_forget()
    	       		shop_mainframe.place(x=30,y=30)
    	       	
    	       back_button = ctk.CTkButton(product_frame, text="", image=backpic, command=back,fg_color='#05161a', hover_color='#05161a', height=70, width=70, corner_radius=5)
    	       back_button.place(x=60, y=20)
    	       product_name_label = ctk.CTkLabel(pro_frame, text=product_name, font=('Helvetica', 45), text_color="black", fg_color="white")
    	       product_name_label.place(x=520, y=30)
    	       try:
    	       	img = Image.open(image_path)
    	       	product_image = ctk.CTkImage(img, size=(250, 250))
    	       	image_label = ctk.CTkButton(pro_frame, text='', image=product_image, height=280, width=280, fg_color="white", state=DISABLED,hover_color='white',corner_radius=30,border_width=3)
    	       	image_label.place(x=50, y=75)
    	       except FileNotFoundError:
    	        	image_label = ctk.CTkLabel(pro_frame, text="Image Not Available", height=220, width=220, fg_color="white")
    	        	image_label.place(x=50, y=50)    	       
    	       price_label = ctk.CTkLabel(pro_frame, text=f" ₹{price}", font=('Helvetica', 38), text_color="black")
    	       price_label.place(x=500, y=120)
    	       q_label = ctk.CTkLabel(pro_frame, text=f"Pack Of  {quantity}", font=('Helvetica', 20), text_color="black")
    	       q_label.place(x=500, y=170)
    	       discount_label = ctk.CTkLabel(pro_frame, text=f" -{discount}%   M.R.P", font=('Helvetica', 22), text_color="red")
    	       discount_label.place(x=500, y=200)
    	       ltdeal=ctk.CTkLabel(pro_frame,text="Limited time deal",font=('Helvetica',20),fg_color='red',corner_radius=10,height=20,width=80,text_color="white")
    	       ltdeal.place(x=500,y=90)
    	       description_label = ctk.CTkLabel(pro_frame, text=f"Product details:\n       {description}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black")
    	       description_label.place(x=500, y=230)
    	       add_to_cart_button = ctk.CTkButton(pro_frame, text="Add to Cart", command=lambda: add_to_cart(product_id, product_name, price), fg_color='#0c7075', font=('Helvetica', 28),corner_radius=20, height=50, width=200,text_color='white')
    	       add_to_cart_button.place(x=500, y=300)
         	   
    #PRODUCT PAGE 
    def product_page():
    	global product_frame
    	for i in frame_list:
    		i.place_forget()
    	product_frame.place(x=30, y=30)
    	tab_namelabel = ctk.CTkLabel(product_frame, text='Product Details', font=('Helvetica', 40), fg_color='#05161a', text_color='#FFFFFF')
    	tab_namelabel.place(x=220, y=10)
    	shop_mainframe.place(x=30, y=30)  # Return to main shop frame
    	shop_widgets.place(x=270, y=25)
    	bckbtn = ctk.CTkButton(product_frame, text="", command=back, image=backbutn, fg_color='#05161a', hover_color='#05161a', height=55, width=55, corner_radius=5)
    	bckbtn.place(x=40, y=10)
 
    	      	              	      	           
###   PRODUCT DISPLAY FOR SUPPLIES CATEGORY  ###
    
    def show_product_details_supplies(product_id, product_name, price, discount, description, image_path,quantity):
    # Hide other frames
        for frame in frame_list:
            frame.place_forget()
            product_frame.place(x=30, y=30)
            pro_frame.place(x=30,y=110)

  # Add a back button
        def back():
        	for i in frame_list:
        		i.place_forget()
        		supplies_frame.place(x=30, y=30)
        		
        back_button = ctk.CTkButton(product_frame, text="", image=backpic, command=back,fg_color='#05161a', hover_color='#05161a', height=70, width=70, corner_radius=5)
        back_button.place(x=60, y=20)

    # Display product name                           
        product_name_label = ctk.CTkLabel(pro_frame, text=product_name, font=('Helvetica', 45), text_color="black", fg_color="white")
        product_name_label.place(x=520, y=30)

    # Display product image
        try:
            img = Image.open(image_path)
            product_image = ctk.CTkImage(img, size=(250, 250))
            image_label = ctk.CTkButton(pro_frame, text='', image=product_image, height=280, width=280, fg_color="white", state=DISABLED,hover_color='white',corner_radius=30,border_width=3)
            image_label.place(x=50, y=75)
        except FileNotFoundError:
            image_label = ctk.CTkLabel(pro_frame, text="Image Not Available", height=220, width=220, fg_color="white")
            image_label.place(x=50, y=50)            
  
    # Display price and discount
        price_label = ctk.CTkLabel(pro_frame, text=f" ₹{price}", font=('Helvetica', 38), text_color="black")
        price_label.place(x=500, y=120)
        q_label = ctk.CTkLabel(pro_frame, text=f"Pack Of  {quantity}", font=('Helvetica', 20), text_color="black")
        q_label.place(x=500, y=170)
        discount_label = ctk.CTkLabel(pro_frame, text=f" -{discount}%   M.R.P", font=('Helvetica', 22), text_color="red")
        discount_label.place(x=500, y=200)
        ltdeal=ctk.CTkLabel(pro_frame,text="Limited time deal",font=('Helvetica',20),fg_color='red',corner_radius=10,height=20,width=80,text_color="white")
        ltdeal.place(x=500,y=90)

    # Display description
        description_label = ctk.CTkLabel(pro_frame, text=f"Product details:\n       {description}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black")
        description_label.place(x=500, y=230)

    # Add-to-cart button
        add_to_cart_button = ctk.CTkButton(pro_frame, text="Add to Cart", command=lambda: add_to_cart(product_id, product_name, price), fg_color='#0c7075', font=('Helvetica', 28),corner_radius=20, height=50, width=200,text_color='white')
        add_to_cart_button.place(x=500, y=300)
        
###   PRODUCT DISPLAY FOR FRUITS CATEGORY  ###
    
    def show_product_details_fruits(product_id, product_name, price, discount, description, image_path,quantity):
    # Hide other frames
        for frame in frame_list:
            frame.place_forget()
            product_frame.place(x=30, y=30)
            pro_frame.place(x=30,y=110)

  # Add a back button
        def back():
        	for i in frame_list:
        		i.place_forget()
        		fruits_frame.place(x=30, y=30)
        back_button = ctk.CTkButton(product_frame, text="", image=backpic, command=back,fg_color='#05161a', hover_color='#05161a', height=70, width=70, corner_radius=5)
        back_button.place(x=60, y=20)

    # Display product name                           
        product_name_label = ctk.CTkLabel(pro_frame, text=product_name, font=('Helvetica', 45), text_color="black", fg_color="white")
        product_name_label.place(x=520, y=30)

    # Display product image
        try:
            img = Image.open(image_path)
            product_image = ctk.CTkImage(img, size=(250, 250))
            image_label = ctk.CTkButton(pro_frame, text='', image=product_image, height=280, width=280, fg_color="white", state=DISABLED,hover_color='white',corner_radius=30,border_width=3)
            image_label.place(x=50, y=75)
        except FileNotFoundError:
            image_label = ctk.CTkLabel(pro_frame, text="Image Not Available", height=220, width=220, fg_color="white")
            image_label.place(x=50, y=50)            
  
    # Display price and discount
        price_label = ctk.CTkLabel(pro_frame, text=f" ₹{price}", font=('Helvetica', 38), text_color="black")
        price_label.place(x=500, y=120)
        q_label = ctk.CTkLabel(pro_frame, text=f"Pack Of  {quantity}", font=('Helvetica', 20), text_color="black")
        q_label.place(x=500, y=170)
        discount_label = ctk.CTkLabel(pro_frame, text=f" -{discount}%   M.R.P", font=('Helvetica', 22), text_color="red")
        discount_label.place(x=500, y=200)
        ltdeal=ctk.CTkLabel(pro_frame,text="Limited time deal",font=('Helvetica',20),fg_color='red',corner_radius=10,height=20,width=80,text_color="white")
        ltdeal.place(x=500,y=90)

    # Display description
        description_label = ctk.CTkLabel(pro_frame, text=f"Product details:\n       {description}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black")
        description_label.place(x=500, y=230)

    # Add-to-cart button
        add_to_cart_button = ctk.CTkButton(pro_frame, text="Add to Cart", command=lambda: add_to_cart(product_id, product_name, price), fg_color='#0c7075', font=('Helvetica', 28),corner_radius=20, height=50, width=200,text_color='white')
        add_to_cart_button.place(x=500, y=300)		
        
        
###   PRODUCT DISPLAY FOR VEGGIES CATEGORY  ###
    
    def show_product_details_veggies(product_id, product_name, price, discount, description, image_path,quantity):
    # Hide other frames
        for frame in frame_list:
            frame.place_forget()
            product_frame.place(x=30, y=30)
            pro_frame.place(x=30,y=110)

  # Add a back button
        def back():
        	for i in frame_list:
        		i.place_forget()
        		vegetable_frame.place(x=30, y=30)        		
        back_button = ctk.CTkButton(product_frame, text="", image=backpic, command=back,fg_color='#05161a', hover_color='#05161a', height=70, width=70, corner_radius=5)
        back_button.place(x=60, y=20)

    # Display product name                           
        product_name_label = ctk.CTkLabel(pro_frame, text=product_name, font=('Helvetica', 45), text_color="black", fg_color="white")
        product_name_label.place(x=520, y=30)

    # Display product image
        try:
            img = Image.open(image_path)
            product_image = ctk.CTkImage(img, size=(250, 250))
            image_label = ctk.CTkButton(pro_frame, text='', image=product_image, height=280, width=280, fg_color="white", state=DISABLED,hover_color='white',corner_radius=30,border_width=3)
            image_label.place(x=50, y=75)
        except FileNotFoundError:
            image_label = ctk.CTkLabel(pro_frame, text="Image Not Available", height=220, width=220, fg_color="white")
            image_label.place(x=50, y=50)            
  
    # Display price and discount
        price_label = ctk.CTkLabel(pro_frame, text=f" ₹{price}", font=('Helvetica', 38), text_color="black")
        price_label.place(x=500, y=120)
        q_label = ctk.CTkLabel(pro_frame, text=f"Pack Of  {quantity}", font=('Helvetica', 20), text_color="black")
        q_label.place(x=500, y=170)
        discount_label = ctk.CTkLabel(pro_frame, text=f" -{discount}%   M.R.P", font=('Helvetica', 22), text_color="red")
        discount_label.place(x=500, y=200)
        ltdeal=ctk.CTkLabel(pro_frame,text="Limited time deal",font=('Helvetica',20),fg_color='red',corner_radius=10,height=20,width=80,text_color="white")
        ltdeal.place(x=500,y=90)

    # Display description
        description_label = ctk.CTkLabel(pro_frame, text=f"Product details:\n       {description}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black")
        description_label.place(x=500, y=230)

    # Add-to-cart button
        add_to_cart_button = ctk.CTkButton(pro_frame, text="Add to Cart", command=lambda: add_to_cart(product_id, product_name, price), fg_color='#0c7075', font=('Helvetica', 28),corner_radius=20, height=50, width=200,text_color='white')
        add_to_cart_button.place(x=500, y=300)
        
###   PRODUCT DISPLAY FOR DAIRY CATEGORY  ###
    
    def show_product_details_dairy(product_id, product_name, price, discount, description, image_path,quantity):
    # Hide other frames
        for frame in frame_list:
            frame.place_forget()
            product_frame.place(x=30, y=30)
            pro_frame.place(x=30,y=110)

  # Add a back button
        def back():
        	for i in frame_list:
        		i.place_forget()
        		dairy_frame.place(x=30, y=30)
        		
        back_button = ctk.CTkButton(product_frame, text="", image=backpic, command=back,fg_color='#05161a', hover_color='#05161a', height=70, width=70, corner_radius=5)
        back_button.place(x=60, y=20)

    # Display product name                           
        product_name_label = ctk.CTkLabel(pro_frame, text=product_name, font=('Helvetica', 45), text_color="black", fg_color="white")
        product_name_label.place(x=520, y=30)

    # Display product image
        try:
            img = Image.open(image_path)
            product_image = ctk.CTkImage(img, size=(250, 250))
            image_label = ctk.CTkButton(pro_frame, text='', image=product_image, height=280, width=280, fg_color="white", state=DISABLED,hover_color='white',corner_radius=30,border_width=3)
            image_label.place(x=50, y=75)
        except FileNotFoundError:
            image_label = ctk.CTkLabel(pro_frame, text="Image Not Available", height=220, width=220, fg_color="white")
            image_label.place(x=50, y=50)            
  
    # Display price and discount
        price_label = ctk.CTkLabel(pro_frame, text=f" ₹{price}", font=('Helvetica', 38), text_color="black")
        price_label.place(x=500, y=120)
        q_label = ctk.CTkLabel(pro_frame, text=f"Pack Of  {quantity}", font=('Helvetica', 20), text_color="black")
        q_label.place(x=500, y=170)
        discount_label = ctk.CTkLabel(pro_frame, text=f" -{discount}%   M.R.P", font=('Helvetica', 22), text_color="red")
        discount_label.place(x=500, y=200)
        ltdeal=ctk.CTkLabel(pro_frame,text="Limited time deal",font=('Helvetica',20),fg_color='red',corner_radius=10,height=20,width=80,text_color="white")
        ltdeal.place(x=500,y=90)

    # Display description
        description_label = ctk.CTkLabel(pro_frame, text=f"Product details:\n       {description}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black")
        description_label.place(x=500, y=230)

    # Add-to-cart button
        add_to_cart_button = ctk.CTkButton(pro_frame, text="Add to Cart", command=lambda: add_to_cart(product_id, product_name, price), fg_color='#0c7075', font=('Helvetica', 28),corner_radius=20, height=50, width=200,text_color='white')
        add_to_cart_button.place(x=500, y=300)
                
    def supplie_products():
    # Hide other frames
        for frame in frame_list:
            frame.place_forget()

    # Display the supplies_frame for the Supplies tab
        supplies_frame.place(x=30, y=30)
        tab_namelabel = ctk.CTkLabel(supplies_frame, text='Supplies', font=('Helvetica', 40), fg_color='#05161a', text_color='#FFFFFF')
        tab_namelabel.place(x=220, y=10)

    # Back button setup
        def back():
            for frame in frame_list:
                frame.place_forget()
                shop_mainframe.place(x=30, y=30)
                shop_widgets.place(x=270, y=25)

        bckbtn = ctk.CTkButton(supplies_frame, text="", command=back, image=backbutn, fg_color='#05161a', hover_color='#05161a', height=55, width=55, corner_radius=5)
        logo = ctk.CTkButton(supplies_frame, image=logo_image_one, text='', fg_color='#05161a', bg_color='#05161a', hover_color='#05161a', command=checked, height=60, width=70)
        logo.place(x=120, y=3)
        bckbtn.place(x=40, y=10)

    # Scrollable frame for displaying products with dynamically adjusted height
        
        with sqlite3.connect('groceria.db') as conn:
        	cursor = conn.cursor()
        	try:
        	       cursor.execute("SELECT product_id, product_name, price, discount,description,quantity FROM supplies")
        	       products = cursor.fetchall()
        	       positions = [(10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),(10, 610), (480, 610), (10, 810), (480, 810)][:len(products)]
        	       product_height = 180  # Height of each product frame
        	       scroll_frame_height =   ((product_height )*2)+40  # Adjust height with padding
        	       scroll_frame = ctk.CTkScrollableFrame(supplies_frame, width=960, height=scroll_frame_height, fg_color='#05161a', corner_radius=40, border_width=0)
        	       scroll_frame.place(x=20, y=70)
        	       backlbl= ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=900, height=1000, fg_color='#05161a', corner_radius=20)
        	       backlbl.pack()
        	       
        	       for i, product in enumerate(products):
        	           product_id, product_name, price, discount,description,quantity = product
        	           # Product display frame                          
        	           product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
        	           product_label.place(x=positions[i][0], y=positions[i][1])
        	           try:
        	               image_path = f"images/{product_id}.png"  # Assuming each image is named by product_id
        	               img = Image.open(image_path)
        	               ctk_image = ctk.CTkImage(img, size=(100, 100))
        	               image_button = ctk.CTkButton(product_label, text='', image=ctk_image, height=140, width=140, corner_radius=20, fg_color='white',border_width=3,bg_color='white',hover_color='white',command=lambda p_id=product_id, p_name=product_name, p_price=price, p_discount=discount, p_desc=description,p_quant=quantity: show_product_details_supplies(p_id, p_name, p_price, p_discount, p_desc, f"images/{p_id}.png",p_quant))
        	               image_button.place(x=20, y=20)       	           	        	           	
        	           except FileNotFoundError:
        	               print("Image file not found:", image_path)
        	               
        	               image_button = ctk.CTkButton(product_label, text='No Image', height=140, width=140, corner_radius=20, fg_color='white',border_width=3,bg_color='white',hover_color='white')
        	               image_button.place(x=20, y=20)        	       
        	       
        	       info_label = ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff', border_width=3)
        	       info_label.place(x=180, y=20)
        	       product_name_label = ctk.CTkLabel(info_label, text=f"{product_name}", font=('Helvetica', 22))
        	       product_name_label.place(x=10, y=10)
        	       price_label = ctk.CTkLabel(info_label, text=f"₹{price}", font=('Helvetica', 22))
        	       price_label.place(x=20, y=40)
        	       discount_label = ctk.CTkLabel(info_label, text=f"{discount}% Off", font=('Helvetica', 22),text_color='red')
        	       discount_label.place(x=20, y=70)        		
        	except sqlite3.Error as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")
            	
    def fruit_products():
    # Hide other frames
        for frame in frame_list:
            frame.place_forget()
            
        fruits_frame.place(x=30, y=30)
        tab_namelabel = ctk.CTkLabel(fruits_frame, text='Fruits', font=('Helvetica', 40), fg_color='#05161a', text_color='#FFFFFF')
        tab_namelabel.place(x=220, y=10)

    # Back button setup
        def back():
            for frame in frame_list:
                frame.place_forget()
                shop_mainframe.place(x=30, y=30)
                shop_widgets.place(x=270, y=25)

        bckbtn = ctk.CTkButton(fruits_frame, text="", command=back, image=backbutn, fg_color='#05161a', hover_color='#05161a', height=55, width=55, corner_radius=5)
        logo = ctk.CTkButton(fruits_frame, image=logo_image_one, text='', fg_color='#05161a', bg_color='#05161a', hover_color='#05161a', command=checked, height=60, width=70)
        logo.place(x=120, y=3)
        bckbtn.place(x=40, y=10)
        
        with sqlite3.connect('groceria.db') as conn:
        	cursor = conn.cursor()
        	try:
        	       cursor.execute("SELECT product_id, product_name, price, discount,description,quantity FROM fruits")
        	       products = cursor.fetchall()
        	       positions = [(10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),(10, 610), (480, 610), (10, 810), (480, 810)][:len(products)]
        	       product_height = 180  # Height of each product frame
        	       scroll_frame_height =   ((product_height )*2)+40  # Adjust height with padding
        	       scroll_frame = ctk.CTkScrollableFrame(fruits_frame, width=960, height=scroll_frame_height, fg_color='#05161a', corner_radius=40, border_width=0)
        	       scroll_frame.place(x=20, y=70)
        	       backlbl= ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=900, height=1000, fg_color='#05161a', corner_radius=20)
        	       backlbl.pack()
        	       
        	       for i, product in enumerate(products):
        	           product_id, product_name, price, discount,description,quantity = product
        	           # Product display frame                          
        	           product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
        	           product_label.place(x=positions[i][0], y=positions[i][1])
        	           try:
        	               image_path = f"images/{product_id}.png"  # Assuming each image is named by product_id
        	               img = Image.open(image_path)
        	               ctk_image = ctk.CTkImage(img, size=(100, 100))
        	               image_button = ctk.CTkButton(product_label, text='', image=ctk_image, height=140, width=140, corner_radius=20, fg_color='white',border_width=3,bg_color='white',hover_color='white',command=lambda p_id=product_id, p_name=product_name, p_price=price, p_discount=discount, p_desc=description,p_quant=quantity: show_product_details_fruits(p_id, p_name, p_price, p_discount, p_desc, f"images/{p_id}.png",p_quant))
        	               image_button.place(x=20, y=20)       	           	        	           	
        	           except FileNotFoundError:
        	               print("Image file not found:", image_path)
        	               
        	               image_button = ctk.CTkButton(product_label, text='No Image', height=140, width=140, corner_radius=20, fg_color='white',border_width=3,bg_color='white',hover_color='white')
        	               image_button.place(x=20, y=20)        	       
        	       
        	       info_label = ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff', border_width=3)
        	       info_label.place(x=180, y=20)
        	       product_name_label = ctk.CTkLabel(info_label, text=f"{product_name}", font=('Helvetica', 22))
        	       product_name_label.place(x=10, y=10)
        	       price_label = ctk.CTkLabel(info_label, text=f"₹{price}", font=('Helvetica', 22))
        	       price_label.place(x=20, y=40)
        	       discount_label = ctk.CTkLabel(info_label, text=f"{discount}% Off", font=('Helvetica', 22),text_color='red')
        	       discount_label.place(x=20, y=70)        		
        	except sqlite3.Error as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")

                                                            
    def dairy_products():
    # Hide other frames
        for frame in frame_list:
            frame.place_forget()

    # Display the supplies_frame for the Supplies tab
        dairy_frame.place(x=30, y=30)
        tab_namelabel = ctk.CTkLabel(dairy_frame, text='Dairy', font=('Helvetica', 40), fg_color='#05161a', text_color='#FFFFFF')
        tab_namelabel.place(x=220, y=10)

    # Back button setup
        def back():
            for frame in frame_list:
                frame.place_forget()
                shop_mainframe.place(x=30, y=30)
                shop_widgets.place(x=270, y=25)

        bckbtn = ctk.CTkButton(dairy_frame, text="", command=back, image=backbutn, fg_color='#05161a', hover_color='#05161a', height=55, width=55, corner_radius=5)
        logo = ctk.CTkButton(dairy_frame, image=logo_image_one, text='', fg_color='#05161a', bg_color='#05161a', hover_color='#05161a', command=checked, height=60, width=70)
        logo.place(x=120, y=3)
        bckbtn.place(x=40, y=10)
        
        with sqlite3.connect('groceria.db') as conn:
        	cursor = conn.cursor()
        	try:
        	       cursor.execute("SELECT product_id, product_name, price, discount,description,quantity FROM dairy")
        	       products = cursor.fetchall()
        	       positions = [(10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),(10, 610), (480, 610), (10, 810), (480, 810)][:len(products)]
        	       product_height = 180  # Height of each product frame
        	       scroll_frame_height =   ((product_height )*2)+40  # Adjust height with padding
        	       scroll_frame = ctk.CTkScrollableFrame(dairy_frame, width=960, height=scroll_frame_height, fg_color='#05161a', corner_radius=40, border_width=0)
        	       scroll_frame.place(x=20, y=70)
        	       backlbl= ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=900, height=1000, fg_color='#05161a', corner_radius=20)
        	       backlbl.pack()
        	       
        	       for i, product in enumerate(products):
        	           product_id, product_name, price, discount,description,quantity = product
        	           # Product display frame                          
        	           product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
        	           product_label.place(x=positions[i][0], y=positions[i][1])
        	           info_label = ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff', border_width=3)
        	           info_label.place(x=180, y=20)
        	           try:
        	               image_path = f"images/{product_id}.png"  # Assuming each image is named by product_id
        	               img = Image.open(image_path)
        	               ctk_image = ctk.CTkImage(img, size=(100, 100))
        	               image_button = ctk.CTkButton(product_label, text='', image=ctk_image, height=140, width=140, corner_radius=20, fg_color='white',border_width=3,bg_color='white',hover_color='white',command=lambda p_id=product_id, p_name=product_name, p_price=price, p_discount=discount, p_desc=description,p_quant=quantity: show_product_details_dairy(p_id, p_name, p_price, p_discount, p_desc, f"images/{p_id}.png",p_quant))
        	               image_button.place(x=20, y=20)       	           	        	           	
        	           except FileNotFoundError:
        	               print("Image file not found:", image_path)
        	               
        	               image_button = ctk.CTkButton(product_label, text='No Image', height=140, width=140, corner_radius=20, fg_color='white',border_width=3,bg_color='white',hover_color='white')
        	               image_button.place(x=20, y=20)        	               
        	               product_name_label = ctk.CTkLabel(info_label, text=f"{product_name}", font=('Helvetica', 22))
        	               product_name_label.place(x=10, y=10)
        	               price_label = ctk.CTkLabel(info_label, text=f"₹{price}", font=('Helvetica', 22))
        	               price_label.place(x=20, y=40)
        	               discount_label = ctk.CTkLabel(info_label, text=f"{discount}% Off", font=('Helvetica', 22),text_color='red')
        	               discount_label.place(x=20, y=70)        		
        	except sqlite3.Error as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")

        	
    def vegetable_products():
    # Hide other frames
        for frame in frame_list:
            frame.place_forget()

    # Display the supplies_frame for the Supplies tab
        vegetable_frame.place(x=30, y=30)
        tab_namelabel = ctk.CTkLabel(vegetable_frame, text='Vegetables', font=('Helvetica', 40), fg_color='#05161a', text_color='#FFFFFF')
        tab_namelabel.place(x=220, y=10)

    # Back button setup
        def back():
            for frame in frame_list:
                frame.place_forget()
                shop_mainframe.place(x=30, y=30)
                shop_widgets.place(x=270, y=25)

        bckbtn = ctk.CTkButton(vegetable_frame, text="", command=back, image=backbutn, fg_color='#05161a', hover_color='#05161a', height=55, width=55, corner_radius=5)
        logo = ctk.CTkButton(vegetable_frame, image=logo_image_one, text='', fg_color='#05161a', bg_color='#05161a', hover_color='#05161a', command=checked, height=60, width=70)
        logo.place(x=120, y=3)
        bckbtn.place(x=40, y=10)
        
        with sqlite3.connect('groceria.db') as conn:
        	cursor = conn.cursor()
        	try:
        	       cursor.execute("SELECT product_id, product_name, price, discount,description,quantity FROM veges")
        	       products = cursor.fetchall()
        	       positions = [(10, 10), (480, 10), (10, 210), (480, 210), (10, 410), (480, 410),(10, 610), (480, 610), (10, 810), (480, 810)][:len(products)]
        	       product_height = 180  # Height of each product frame
        	       scroll_frame_height =   ((product_height )*2)+40  # Adjust height with padding
        	       scroll_frame = ctk.CTkScrollableFrame(vegetable_frame, width=960, height=scroll_frame_height, fg_color='#05161a', corner_radius=40, border_width=0)
        	       scroll_frame.place(x=20, y=70)
        	       backlbl= ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=900, height=1000, fg_color='#05161a', corner_radius=20)
        	       backlbl.pack()
        	       
        	       for i, product in enumerate(products):
        	           product_id, product_name, price, discount,description,quantity = product
        	           # Product display frame                          
        	           product_label = ctk.CTkLabel(scroll_frame, text='', font=('Helvetica', 40), width=440, height=180, fg_color='white', corner_radius=20)
        	           product_label.place(x=positions[i][0], y=positions[i][1])
        	           try:
        	               image_path = f"images/{product_id}.png"  # Assuming each image is named by product_id
        	               img = Image.open(image_path)
        	               ctk_image = ctk.CTkImage(img, size=(100, 100))
        	               image_button = ctk.CTkButton(product_label, text='', image=ctk_image, height=140, width=140, corner_radius=20, fg_color='white',border_width=3,bg_color='white',hover_color='white',command=lambda p_id=product_id, p_name=product_name, p_price=price, p_discount=discount, p_desc=description,p_quant=quantity: show_product_details_veggies(p_id, p_name, p_price, p_discount, p_desc, f"images/{p_id}.png",p_quant))
        	               image_button.place(x=20, y=20)       	           	        	           	
        	           except FileNotFoundError:
        	               print("Image file not found:", image_path)
        	               
        	               image_button = ctk.CTkButton(product_label, text='No Image', height=140, width=140, corner_radius=20, fg_color='white',border_width=3,bg_color='white',hover_color='white')
        	               image_button.place(x=20, y=20)        	       
        	       
        	       info_label = ctk.CTkFrame(product_label, height=140, width=240, corner_radius=20, fg_color='#ffffff', border_width=3)
        	       info_label.place(x=180, y=20)
        	       product_name_label = ctk.CTkLabel(info_label, text=f"{product_name}", font=('Helvetica', 22))
        	       product_name_label.place(x=10, y=10)
        	       price_label = ctk.CTkLabel(info_label, text=f"₹{price}", font=('Helvetica', 22))
        	       price_label.place(x=20, y=40)
        	       discount_label = ctk.CTkLabel(info_label, text=f"{discount}% Off", font=('Helvetica', 22),text_color='red')
        	       discount_label.place(x=20, y=70)        		
        	except sqlite3.Error as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")
                                                                                                                                                                                                                                                                                                                       
    #widgets in scrollable frame   
    # Advertisement Frame
    show = ctk.CTkLabel(shop_scrollframe, width=960, height=700, fg_color='#294d61',text='')
    show.grid(column=0,row=0)
    advertisement = ctk.CTkLabel(shop_scrollframe, width=960, height=200, fg_color='#294d61',text='')
    advertisement.place(x=-10,y=0)
    
#CATEGORY TABS    
    category_frame=ctk.CTkFrame(shop_scrollframe,height=160,width=850,corner_radius=30,fg_color='#05161a',border_width=3,border_color='#0f969c') 
    products_frame=ctk.CTkFrame(shop_scrollframe,height=340,width=920,corner_radius=30,fg_color='#05161a',border_width=3,border_color='#0f969c')  
    category_label= ctk.CTkLabel(category_frame,text_color='white', width=100, height=60, fg_color='#05161a',text='Categories:',font=fnt1)
    sale_label= ctk.CTkLabel(shop_scrollframe,text_color='white', width=100, height=60, fg_color='#05161a',text='Grab the Trending Deals now !!',font=fnt1)  
    vegetables=ctk.CTkButton(category_frame,text='Veges',image=vegtab,height=70,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=vegetable_products)   
    fruits=ctk.CTkButton(category_frame,text='Fruits',image=fru,height=70,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=fruit_products)
    dairy=ctk.CTkButton(category_frame,text='Dairy',height=70,image=dair,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=dairy_products)   
    essentials=ctk.CTkButton(category_frame,text='Supplies',image=essen,height=70,width=200,fg_color='#0c7075',corner_radius=20,font=fnt1,border_width=3,border_color='#0f969c',command=supplie_products)
    
    product_labels = []
    x_positions = [25, 203, 381, 559, 737]

# Create product labels
    for x_pos in x_positions:
        product_label = ctk.CTkLabel(products_frame, text='', height=240, width=158, fg_color='white', corner_radius=20)
        product_label.place(x=x_pos, y=80)
        product_labels.append(product_label)

# Fetch product data from the database
    try:
        with sqlite3.connect('groceria.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT product_id, product_name, price, discount, description, quantity FROM sales LIMIT 5")
            products = cursor.fetchall()

            for index, (product_label, product) in enumerate(zip(product_labels, products)):
                product_id, product_name, price, discount, description, quantity = product

            # Load product image
                try:
                    image_path = f"images/{product_id}.png"
                    img = Image.open(image_path)
                    ctk_image = ctk.CTkImage(img, size=(100, 100))
                    image_button = ctk.CTkButton(product_label,text='',height=120,width=120,corner_radius=20,fg_color='white',font=('Helvetica', 50),border_width=3,image=ctk_image,command=lambda p_id=product_id, p_name=product_name, p_price=price, p_discount=discount, p_desc=description, p_quant=quantity: show_product_details_sales(p_id, p_name, p_price, p_discount, p_desc, image_path, p_quant))
                    image_button.place(x=10, y=10)  # Positioning inside product label
                except FileNotFoundError:
                    print(f"Image not found: {image_path}")
                    image_button = ctk.CTkButton(product_label,text='No Image',height=120,width=120,corner_radius=20,fg_color='white',border_width=3)
                    image_button.place(x=10, y=10)

            # Create info label for price and discount
                info_label = ctk.CTkFrame(product_label, height=90, width=140, corner_radius=20, fg_color='#ffffff', border_width=3)
                info_label.place(x=10, y=140)  # Positioning inside product label

            # Add price and discount text
                price_label = ctk.CTkLabel(info_label, text=f"₹{price}", font=('Helvetica', 16))
                price_label.pack(padx=10, pady=5)

                if discount:
                    discount_label = ctk.CTkLabel(info_label, text=f"{discount}% Off", font=('Helvetica', 14), text_color='red')
                    discount_label.pack(padx=10, pady=5)

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
                        
      #placing of tabs
    category_frame.place(x=50,y=180)
    sale_label.place(x=50,y=375)
    products_frame.place(x=10,y=360)
    category_label.place(x=30,y=10)
    dairy.place(x=430,y=70)
    fruits.place(x=220,y=70)
    vegetables.place(x=10,y=70)    
    essentials.place(x=640,y=70)      
    
    #scrollable frame with menu button on screen
    advertisement_menu= ctk.CTkLabel(shop_scrollframe1, width=700, height=300, fg_color='#294d61',text='')
    advertisement_menu.place(x=20,y=20)
    category_frame_menu=ctk.CTkFrame(tabs_frame,height=150,width=210,corner_radius=30,fg_color='#05161a',border_width=3,border_color='#0f969c')
    products_frame_menu=ctk.CTkFrame(shop_scrollframe1,height=210,width=675,corner_radius=30,fg_color='#05161a',border_width=3,border_color='#0f969c')
    
#CATEGORY TABS
    vegetables=ctk.CTkButton(category_frame_menu,text='',image=vegtab2,height=50,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=vegetable_products)    
    fruits=ctk.CTkButton(category_frame_menu,text='',image=fru2,height=50,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=fruit_products)    
    dairy=ctk.CTkButton(category_frame_menu,text='',height=50,image=dair2,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=dairy_products)    
    essentials=ctk.CTkButton(category_frame_menu,text='',image=essen2,height=50,width=50,fg_color='#0c7075',corner_radius=20,font=fnt,border_width=3,border_color='#0f969c',command=supplie_products)
    
    product_labels = []
    x_positions = [25, 185, 345, 505]

    for x_pos in x_positions:
        product_label = ctk.CTkLabel(products_frame_menu, text='', height=190, width=140, fg_color='white', corner_radius=20)
        product_label.place(x=x_pos, y=10)
        product_labels.append(product_label)

# Fetch product data from the database
    try:
        with sqlite3.connect('groceria.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT product_id, product_name, price, discount, description, quantity FROM sales LIMIT 5")
            products = cursor.fetchall()

            for index, (product_label, product) in enumerate(zip(product_labels, products)):
                product_id, product_name, price, discount, description, quantity = product

            # Load product image
                try:
                    image_path = f"images/{product_id}.png"
                    img = Image.open(image_path)
                    ctk_image = ctk.CTkImage(img, size=(80, 80))
                    image_button = ctk.CTkButton(product_label,text='',height=90,width=90,corner_radius=20,fg_color='white',font=('Helvetica', 50),border_width=3,image=ctk_image,command=lambda p_id=product_id, p_name=product_name, p_price=price, p_discount=discount, p_desc=description, p_quant=quantity: show_product_details_sales_mini(p_id, p_name, p_price, p_discount, p_desc, image_path, p_quant))
                    image_button.place(x=10, y=10)  # Positioning inside product label
                except FileNotFoundError:
                    print(f"Image not found: {image_path}")
                    image_button = ctk.CTkButton(product_label,text='No Image',height=120,width=120,corner_radius=20,fg_color='white',border_width=3)
                    image_button.place(x=10, y=10)

            # Create info label for price and discount
                info_label = ctk.CTkFrame(product_label, height=90, width=140, corner_radius=20, fg_color='#ffffff', border_width=3)
                info_label.place(x=10, y=105)  # Positioning inside product label

            # Add price and discount text
                price_label = ctk.CTkLabel(info_label, text=f"₹{price}", font=('Helvetica', 16))
                price_label.pack(padx=10, pady=5)

                if discount:
                    discount_label = ctk.CTkLabel(info_label, text=f"{discount}% Off", font=('Helvetica', 14), text_color='red')
                    discount_label.pack(padx=10, pady=5)

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        
    
    #placing tabs and widgets  
   # category_frame_menu.place(x=20,y=280)
    fruits.place(x=110,y=10)
    dairy.place(x=10,y=80)
    vegetables.place(x=10,y=10)
    essentials.place(x=110,y=80)
    
    
    def confirm_order(order_details):
        try:
            with sqlite3.connect('groceria.db') as conn:
            	cursor = conn.cursor()
            	s_mail = email_address_login.get()
            	sanitized_table_name = sanitize_email(s_mail) + "_orders"
            	order_id = random.randint(10000, 99999)
            	cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {sanitized_table_name} (
                    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id TEXT NOT NULL,
                    product_name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL,
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    order_status TEXT NOT NULL,
                    payment_status TEXT NOT NULL)''')
            	cursor.execute(f'''
INSERT INTO {sanitized_table_name} (order_id, product_id, product_name, quantity, price, order_status, payment_status)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    order_id,
    order_details['product_id'],            
    order_details['product_name'],
    order_details['quantity'],
    order_details['total'],  # Total price as `price`
    "To be Shipped",
    "Due"
))
            	
            conn.commit()
            messagebox.showinfo(
            "Order Confirmation",
            f"Your order for {order_details['quantity']} units of {order_details['product_name']} "
            f"has been placed successfully!\n\nOrder Status: To be Shipped soon")
            cart_tab()
            send_order_email(email, order_details)
        except sqlite3.Error as e:
        	messagebox.showerror("Database Error", str(e))
        	messagebox.showerroe("Debug",sanitized_email_name)
     
    def payments_page(order_details):
        for i in frame_list:
        	i.place_forget()  # Hide all frames        
        payment_frame.place(x=30, y=30)
        heading_label = ctk.CTkLabel(payment_frame,text="Payment",font=("Helvetica", 40),fg_color='#05161a',text_color="#FFFFFF")
        heading_label.place(x=440, y=10)
        bill=ctk.CTkLabel(details_frame_pay,text="Bill",font=('Helvetica',28),fg_color='white')
        bill.place(x=180,y=20)
        div=ctk.CTkFrame(details_frame_pay,width=340,height=2,border_color='black',border_width=2,fg_color='black',bg_color='black')
        div.place(x=30,y=60)
        divl=ctk.CTkFrame(details_frame_pay,width=340,height=2,border_color='black',border_width=2,fg_color='black',bg_color='black')
        divl.place(x=30,y=360)
        back_button = ctk.CTkButton(payment_frame,text="",command=lambda: transit_tab(order_details), image=backbutn,fg_color='#05161a',hover_color='#05161a',height=55,width=55,corner_radius=5)
        back_button.place(x=40, y=10)
        logo = ctk.CTkButton(payment_frame,image=logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
        qr=ctk.CTkImage(Image.open(r"qr.png"),size=(280,280))
        qr_label=ctk.CTkLabel(payment_frame,text="",image=qr,corner_radius=20,fg_color='white')
        qr_label.place(x=650,y=150)        
        logo.place(x=120, y=3)        
        details_frame_pay.place(x=80, y=80)
        product_name = order_details["product_name"]
        price = order_details["price"]
        quantity = order_details["quantity"]
        total= order_details["total"]     
          
        price_label = ctk.CTkLabel(details_frame_pay, text=f"{quantity} × {product_name}    ₹{price}", font=('Helvetica', 20), text_color="black",fg_color="white")
        price_label.place(x=100, y=80)
        gst = round((total * 12) / 100, 2)  # Using round for better precision
        net = total + gst
        gst_label = ctk.CTkLabel(details_frame_pay, text=f"Gst    -     ₹{gst}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black",fg_color="white")
        gst_label.place(x=100, y=120)
        net_label = ctk.CTkLabel(details_frame_pay, text=f"Total   -     {net}", font=('Helvetica', 24), wraplength=500, justify="left", text_color="black",fg_color="white")
        net_label.place(x=100, y=370)
        print(f"pid:{product_id}")
        order_detail= {"product_id":product_id,"product_name": product_name,"price": price,"quantity": quantity,"total": net}       
        confirm_button = ctk.CTkButton(payment_frame,text="Confirm Order",font=("Helvetica", 22),corner_radius=20,fg_color="#0c7075",text_color="#FFFFFF",command=lambda: confirm_order(order_detail),height=50,width=80)
        confirm_button.place(x=720, y=450)
    
    def transit_tab(product):
        for i in frame_list:
        	i.place_forget()  # Hide all frames    
        transit_frame.place(x=30, y=30)
        print(ui)
        product_frame_exe=ctk.CTkFrame(transit_frame,border_width=3,fg_color='white',corner_radius=60,height=450,width=1000)
        product_frame_exe.place(x=32, y=90)
        tab_namelabel = ctk.CTkLabel(transit_frame,text='Order Summary',font=('Helvetica', 40),fg_color='#05161a',text_color='#FFFFFF')
        tab_namelabel.place(x=300, y=10)
        bckbtn = ctk.CTkButton(transit_frame,text="",command=cart_tab,image=backbutn,fg_color='#05161a',hover_color='#05161a',height=55,width=55,corner_radius=5)
        bckbtn.place(x=40, y=10)
        logo = ctk.CTkButton(transit_frame,image=logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
        logo.place(x=120, y=3)
        try:
        	   	       image_path = f"images/{product_id}.png"
        	   	       img = Image.open(image_path)
        	   	       product_image = ctk.CTkImage(img, size=(100, 100))
        	   	       image_label = ctk.CTkButton(product_frame_exe, image=product_image, text="",corner_radius=30,border_width=3,state=DISABLED,height=280,width=280,hover_color='white',fg_color='white')
        	   	       image_label.image = product_image
        	   	       image_label.place(x=30, y=50)  
        	   	       print(f"ni{product_id}")
        	 
        except FileNotFoundError:
        	   	       image_button = ctk.CTkButton(product_label,text='No Image',height=140,width=140,corner_radius=20,fg_color='white',border_width=3,bg_color='white',hover_color='white')
        	   	       image_button.place(x=20, y=20)
        
        
        product_name = product["product_name"]
        price = product["price"]
        available_quantity = product["quantity"]
        description = product["description"]
        discount = product.get("discount", None)
        product_name_label = ctk.CTkLabel(product_frame_exe, text=product_name, font=('Helvetica', 45), text_color="black", fg_color="white")
        product_name_label.place(x=520, y=30)
        price_label = ctk.CTkLabel(product_frame_exe, text=f" ₹{price}", font=('Helvetica', 38), text_color="black",fg_color="white")
        price_label.place(x=500, y=120)
        q_label = ctk.CTkLabel(product_frame_exe, text=f"Pack Of  {quantity}", font=('Helvetica', 20), text_color="black",fg_color="white")
        q_label.place(x=500, y=170)        
        ltdeal=ctk.CTkLabel(product_frame_exe,text="Limited time deal",font=('Helvetica',20),fg_color='red',corner_radius=10,height=20,width=80,text_color="white")
        ltdeal.place(x=500,y=90)
        description_label = ctk.CTkLabel(product_frame_exe, text=f"Product details:\n       {description}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black",fg_color="white")
        description_label.place(x=500, y=230)
        if discount:
        	discount_label = ctk.CTkLabel(product_frame_exe, text=f" -{discount}%   M.R.P", font=('Helvetica', 22), text_color="red",fg_color="white")
        	discount_label.place(x=500, y=200)
        quantity_input = ctk.CTkEntry(product_frame_exe, placeholder_text="Enter Quantity", width=120,height=50,corner_radius=20,border_width=3)
        quantity_input.place(x=500, y=300)
        
        def proceed_to_payment():
            try:
            	quantity = quantity_input.get().strip()  # Get and strip any extra spaces
            	if not quantity.isdigit():
            		messagebox.showerror("Error" ,"Please enter a valid numeric quantity.")
            	quantity = int(quantity_input.get())
            	order_details= {"product_id":product_id,"product_name": product_name,"price": price,"quantity": quantity,"total": price * quantity}
            	payments_page(order_details)
            	
            except ValueError as e:
            	messagebox.showerror("Input Error", str(e))
        order_now_button = ctk.CTkButton(product_frame_exe,text="Order Now", command=proceed_to_payment,font=("Helvetica", 28),corner_radius=20,fg_color="#0c7075",text_color="#FFFFFF",height=50)
        order_now_button.place(x=640, y=300)     
        
          
#DEFINING THE TABS

## NESTED SEARCH BOX ##

    def search_box(nested_searchbox, search_frame, email_id):
        search_term = nested_searchbox.get().strip()
        for i in frame_list:
                i.place_forget()            
        search_frame.place(x=30,y=30)

    # Clear previous results

        tables = ["veges", "fruits", "dairy", "supplies"]
        found_products = []

    # Connect to the database
        connection = sqlite3.connect("groceria.db")
        cursor = connection.cursor()

        try:
            for table in tables:
                cursor.execute(f"SELECT * FROM {table} WHERE product_name LIKE ?", ('%' + search_term + '%',))
                products = cursor.fetchall()
                found_products.extend(products)

            if found_products:
                for product in found_products:
                    product_id, exp_date, price, quantity, discount, product_name, description = product

                # Display product information
                    product_frame = ctk.CTkFrame(search_frame, fg_color="white", width=980, height=430,corner_radius=30)
                    product_frame.place(x=40,y=90)
                    logo=ctk.CTkButton(search_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
                    logo.place(x=120,y=3)    

                # Display image if available
                    try:
                        image_path = f"images/{product_id}.png"
                        img = Image.open(image_path)      
                        product_image =ctk.CTkImage(img, size=(250, 250))
                        image_label = ctk.CTkButton(product_frame, image=product_image, text="",corner_radius=30,border_width=3,state=DISABLED,height=280,width=280,hover_color='white',fg_color='white')
                        image_label.image = product_image
                        image_label.place(x=30, y=50)
                    except FileNotFoundError:
                        print(f"Image for {product_name} not found at {image_path}")
                # Display details
                    product_name_label = ctk.CTkLabel(product_frame, text=product_name, font=('Helvetica', 45), text_color="black", fg_color="white")
                    product_name_label.place(x=520, y=30)
                    price_label = ctk.CTkLabel(product_frame, text=f" ₹{price}", font=('Helvetica', 38), text_color="black",fg_color="white")
                    price_label.place(x=500, y=120)
                    q_label = ctk.CTkLabel(product_frame, text=f"Pack Of  {quantity}", font=('Helvetica', 20), text_color="black",fg_color="white")
                    q_label.place(x=500, y=170)
                    discount_label = ctk.CTkLabel(product_frame, text=f" -{discount}%   M.R.P", font=('Helvetica', 22), text_color="red",fg_color="white")
                    discount_label.place(x=500, y=200)
                    ltdeal=ctk.CTkLabel(product_frame,text="Limited time deal",font=('Helvetica',20),fg_color='red',corner_radius=10,height=20,width=80,text_color="white")
                    ltdeal.place(x=500,y=90)
                    description_label = ctk.CTkLabel(product_frame, text=f"Product details:\n       {description}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black",fg_color="white")
                    description_label.place(x=500, y=230)
                    add_to_cart_button = ctk.CTkButton(product_frame, text="Add to Cart", command=lambda: add_to_cart(product_id, product_name, price), fg_color='#0c7075', font=('Helvetica', 28),corner_radius=20, height=50, width=200,text_color='white')
                    add_to_cart_button.place(x=500, y=300)
                    
            else:
                no_product_label = ctk.CTkLabel(search_frame, text="Product not found", font=("Helvetica", 16))
                no_product_label.pack(pady=10)

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        	
    def add_to_cart( product_id,product_name,price):
        try:
        	conn= sqlite3.connect("groceria.db")
        	cursor = conn.cursor()
        	s_mail=email_address_login.get()
        	user_id=sanitize_email(s_mail)
        	table_name = f"{user_id}_cart"
        	cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                price REAL
            )
        """) 	
        	try:
        		with sqlite3.connect('groceria.db') as conn:
        		  	cursor = conn.cursor()
        		  	cursor.execute(f'''
                INSERT INTO {table_name} (product_id, product_name, price)
                VALUES (?, ?, ?)
            ''', (product_id, product_name, price))
        		  	messagebox.showinfo("Cart", f"{product_name} added to cart!")
        	except sqlite3.Error as e:
        		messagebox.showerror("Database Error", f"Could not add to cart: {e}")
 
        except sqlite3.Error as e:
        	messagebox.showerroe("Error",f"Database Error: {e}")
        	return f"An error occurred: {e}"    	
    
   
#SEARCH TAB
    def search_tab(searchbox, search_frame, email_id):
        global nested_searchbox
        search_term = searchbox.get().strip()
        for i in frame_list:
                i.place_forget()            
        search_frame.place(x=30,y=30)
        
        def back():
            for frame in frame_list:
                search_frame.place_forget()
                shop_mainframe.place(x=30, y=30)
                shop_widgets.place(x=270, y=25)

    # Clear previous results

        tables = ["veges", "fruits", "dairy", "supplies"]
        found_products = []

    # Connect to the database
        connection = sqlite3.connect("groceria.db")
        cursor = connection.cursor()

        try:
            for table in tables:
                cursor.execute(f"SELECT * FROM {table} WHERE product_name LIKE ?", ('%' + search_term + '%',))
                products = cursor.fetchall()
                found_products.extend(products)

            if found_products:
                for product in found_products:
                    product_id, exp_date, price, quantity, discount, product_name, description = product

                # Display product information
                    product_frame = ctk.CTkFrame(search_frame, fg_color="white", width=980, height=430,corner_radius=30)
                    product_frame.place(x=40,y=90)
                    logo=ctk.CTkButton(search_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
                    logo.place(x=120,y=8) 
                    bckbtn = ctk.CTkButton(search_frame, text="", command=back, image=backbutn, fg_color='#05161a', hover_color='#05161a', height=55, width=55, corner_radius=5)
                    bckbtn.place(x=40,y=15)
                    nested_searchbox=ctk.CTkEntry(search_frame,fg_color='white',width=500,height=60,corner_radius=20,border_width=3,bg_color='#05161a',border_color='#0f969c')
                    nested_searchbox.place(x=240,y=10)
                    search_button=ctk.CTkButton(nested_searchbox,text='',image=seac,fg_color='#05161a',width=50,height=30,corner_radius=20,border_width=3,bg_color='#ffffff',border_color='#0f969c',command=lambda: search_box(nested_searchbox, search_frame, email_id))
                    search_button.place(x=415,y=5)
                    

                # Display image if available
                    try:
                        image_path = f"images/{product_id}.png"
                        img = Image.open(image_path)      
                        product_image =ctk.CTkImage(img, size=(250, 250))
                        image_label = ctk.CTkButton(product_frame, image=product_image, text="",corner_radius=30,border_width=3,state=DISABLED,height=280,width=280,hover_color='white',fg_color='white')
                        image_label.image = product_image
                        image_label.place(x=30, y=50)
                    except FileNotFoundError:
                        print(f"Image for {product_name} not found at {image_path}")

                # Display details
                    product_name_label = ctk.CTkLabel(product_frame, text=product_name, font=('Helvetica', 45), text_color="black", fg_color="white")
                    product_name_label.place(x=520, y=30)
                    price_label = ctk.CTkLabel(product_frame, text=f" ₹{price}", font=('Helvetica', 38), text_color="black",bg_color='white',fg_color='white')
                    price_label.place(x=500, y=120)
                    q_label = ctk.CTkLabel(product_frame, text=f"Pack Of  {quantity}", font=('Helvetica', 20), text_color="black",bg_color='white',fg_color='white')
                    q_label.place(x=500, y=170)
                    discount_label = ctk.CTkLabel(product_frame, text=f" -{discount}%   M.R.P", font=('Helvetica', 22), text_color="red",bg_color='white',fg_color='white')
                    discount_label.place(x=500, y=200)
                    ltdeal=ctk.CTkLabel(product_frame,text="Limited time deal",font=('Helvetica',20),fg_color='red',corner_radius=10,height=20,width=80,text_color="white",bg_color='white')
                    ltdeal.place(x=500,y=90)
                    description_label = ctk.CTkLabel(product_frame, text=f"Product details:\n       {description}", font=('Helvetica', 20), wraplength=500, justify="left", text_color="black",bg_color='white',fg_color='white')
                    description_label.place(x=500, y=230)
                    add_to_cart_button = ctk.CTkButton(product_frame, text="Add to Cart", command=lambda: add_to_cart(product_id, product_name, price), fg_color='#0c7075', font=('Helvetica', 28),corner_radius=20, height=50, width=200,text_color='white',bg_color='white')
                    add_to_cart_button.place(x=500, y=300)

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        	

    def order(product, email_id):
        product_id, exp_date, price, quantity, discount, product_name, description = product
        
	
        connection = sqlite3.connect("groceria.db")
        cursor = connection.cursor()

        sanitized_table_name = email.id.replace('@', '_at_').replace('.', '_dot_')
    
        try:
            cursor.execute(f"INSERT INTO {sanitized_table_name} (order_id, product_name, quantity, price) VALUES (?, ?, ?, ?)",
                       (order_id, product_name, quantity, price))
            connection.commit()
            messagebox.showinfo("Order Placed Successfully")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        finally:
        	connection.close()     
        	   
#PROFILE TAB
    
    
    
   
    def profile_tab():            
            for i in frame_list:
                i.place_forget()          
            profile_frame.place(x=30,y=30)
            try:
             	connection = sqlite3.connect("groceria.db")
             	cursor = connection.cursor()
             	user_id = email_address_login.get()  # Example: Replace with the logged-in user# SQL query to fetch user de
             	query = """SELECT first_name, last_name, email_id, address, pincode 
                   FROM users 
                   WHERE email_id = ?"""
             	cursor.execute(query, (user_id,))
             	user_data = cursor.fetchone()
             	if user_data:
                 	  first_name, last_name, email, address, pincode = user_data
            except sqlite3.Error as e:
            	print(f"An error occurred: {e}")
            	
            #widgets in profile tab     
            logo=ctk.CTkButton(profile_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)       
            tab_namelabel=ctk.CTkLabel(profile_frame,text='Profile',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')        
            profile_tab_one=ctk.CTkFrame(profile_frame,fg_color='#294d61',height=480,width=600,corner_radius=50,border_width=3,border_color="#0f969c") 
            profile_tab_two=ctk.CTkFrame(profile_frame,fg_color='#294d61',height=480,width=380,corner_radius=50,border_width=3,border_color="#0f969c")      
                
            prof_image=ctk.CTkButton(profile_tab_one,text='',corner_radius=50,image=prof,fg_color='#ffffff',border_width=3,width=200,height=200)
            edit_profile=ctk.CTkButton(profile_tab_one,text='Edit Profile',corner_radius=50,fg_color='#0c7075',border_width=3,width=400,height=60,font=fnt1)
            delete_button=ctk.CTkButton(profile_tab_two,text='Delete Acoount',font=fnt1,border_width=4,border_color='#811331',fg_color='#0c7075',height=60,width=280,corner_radius=30)
            terms_button=ctk.CTkButton(profile_tab_two,text='Terms & Conditions ',font=fnt1,border_width=3,fg_color='#0c7075',height=60,width=280,corner_radius=30)
            about_button=ctk.CTkButton(profile_tab_two,text='About Us',font=fnt1,border_width=3,fg_color='#0c7075',height=60,width=280,corner_radius=30)
            payments=ctk.CTkButton(profile_tab_two,text='Payments',font=fnt1,border_width=3,fg_color='#0c7075',height=60,width=280,corner_radius=30)
            payments.place(x=20,y=180)
            
            #Labels
            fullname_label=ctk.CTkLabel(profile_tab_one,text=first_name,text_color='white',font=('vivaldi italics',20))         
            lastname_label=ctk.CTkLabel(profile_tab_one,text=last_name,text_color='white',font=('vivaldi italics',20))            
            email_address_label=ctk.CTkLabel(profile_tab_one,text=email,text_color='white',font=('vivaldi italics',20))
            address=ctk.CTkLabel(profile_tab_one,text=address,text_color='white',font=('vivaldi italics',20))
            pincode=ctk.CTkLabel(profile_tab_one,text=pincode,text_color='white',font=('vivaldi italics',20))
            
            features=ctk.CTkLabel(profile_tab_two,text="Options",font=("Helvetica",30))
            features.place(x=60,y=30)
            divider=ctk.CTkFrame(profile_tab_two,height=1,width=300,border_width=4)
            divider.place(x=40,y=80)                                                   
            bckbtn = ctk.CTkButton(profile_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5)
            
            #placing widgets           
            profile_tab_one.place(x=30,y=70)
            profile_tab_two.place(x=650,y=70)
            tab_namelabel.place(x=220, y=10)
            delete_button.place(x=20,y=360)
            terms_button.place(x=20,y=100)
            about_button.place(x=20,y=260)
            prof_image.place(x=40,y=40)
            edit_profile.place(x=100,y=400)
            bckbtn.place(x=40, y=10)
            
            lastname_label.place(x=450,y=40)
            email_address_label.place(x=300,y=120)
            fullname_label.place(x=300,y=40)
            address.place(x=300,y=200)
            pincode.place(x=300,y=280)
            

#  ORDERS TAB 

    def orders_tab():
                        
            for i in frame_list:
                i.place_forget()
            
            orders_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(orders_frame,text='Orders',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)
            
            bckbtn = ctk.CTkButton(orders_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5) 
            logo=ctk.CTkButton(orders_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)
            with sqlite3.connect('groceria.db') as conn:
        	    cursor = conn.cursor()
        	    try:
        	       s_mail = email_address_login.get()
        	       user_id = sanitize_email(s_mail)
        	       table_name = f"{user_id}"+"_orders"
        	       query = f"SELECT * FROM {table_name}"
        	       cursor.execute(query)
        	       orders = cursor.fetchall()
        	       for i, order in enumerate(orders):
        	       	order_id, product_id,product_name, quantity, price, order_date, order_status,payment_status = order        	      
        	       	print(f"Order ID: {order_id}, Product: {product_id}, Price: {price}, Order Date: {order_date}")
        	       if not products:
        	           ctk.CTkLabel(cart_frame,text="Your cart is empty!",font=('Helvetica', 22),text_color='#FFFFFF').place(x=50, y=100)
        	           return
        	       product_height = 180  # Height of each product frame
        	       scroll_frame_height = ((product_height) * 2) + 40  # Adjust height with padd
        	       scroll_frame = ctk.CTkScrollableFrame(orders_frame,width=960,height=scroll_frame_height,fg_color='#05161a',corner_radius=40,border_width=3)
        	       scroll_frame.place(x=20, y=70)
        	       positions = [(10, 10), (10, 210), (10, 410),(10, 610), (10, 810), (10, 1010), (10, 1210), (10, 1410), (10, 1610), (10, 1810), (10, 2010), (10, 2210), (10, 2410), (10, 2610), (10, 2810), (10, 3010), (10, 3210), (10, 3410), (10, 3610), (10, 3810)][:len(products)]
        	       backlbl = ctk.CTkLabel(scroll_frame,text='',font=('Helvetica', 40),width=900,height=4000,fg_color='#05161a',corner_radius=20)
        	       backlbl.pack()
        	       product_label = ctk.CTkLabel(scroll_frame,text='',font=('Helvetica', 40),width=900,height=180,fg_color='white',corner_radius=20)
        	       product_label.place(x=positions[i][0], y=positions[i][1])
        	       image_path = f"images/{product_id}.png"
        	       img = Image.open(image_path)
        	       ctk_image = ctk.CTkImage(img, size=(100, 100))
        	       image_button = ctk.CTkButton(product_label,text='',image=ctk_image,height=140,width=140,corner_radius=20,fg_color='white',border_width=3,bg_color='white',hover_color='white')
        	       image_button.place(x=20, y=20)
        	       info_label = ctk.CTkFrame(product_label,height=140,width=620,corner_radius=20,fg_color='#ffffff',border_width=3)
        	       info_label.place(x=180, y=20)
        	       product_name_label = ctk.CTkLabel(info_label,text=f"Name: {product_name}",font=('Helvetica', 22))
        	       product_name_label.place(x=10, y=10)
        	       price_label = ctk.CTkLabel(info_label,text=f"Price: ₹{price}",font=('Helvetica', 22))
        	       price_label.place(x=10, y=40)
        	       quantity_label = ctk.CTkLabel(info_label,text=f"Quantity: {quantity}",font=('Helvetica', 22))
        	       quantity_label.place(x=10, y=70)
        	       description_label = ctk.CTkLabel(info_label,text=f"Ordered On: {order_date}",font=('Helvetica', 16),wraplength=550,justify='left')
        	       description_label.place(x=10, y=100)
        	       if discount:
        	   	           discount_label = ctk.CTkLabel(info_label,text=f"Discount: {discount}%",font=('Helvetica', 22),text_color='red')
        	   	           discount_label.place(x=400, y=10)
        	    except sqlite3.Error as e:
        	       		messagebox.showerror("Database Error", str(e))
          

#CATEGORIES BUTTON
  
            
    def cat_function_one():
        category_frame_menu.place(x=20,y=280) 
                
    def cat_function_two():
                     category_frame_menu.place_forget()
                     
    def category_button():
        global cat_click_count
        cat_click_count += 1
        if cat_click_count == 1:
            cat_function_one()
        elif cat_click_count == 2:
            cat_function_two()
            cat_click_count = 0
            
            
 
 #SUPPORTS TAB  
                     
    def supports_tab():
                        
            for i in frame_list:
                i.place_forget()
            
            supports_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(supports_frame,text='Contact Us',font=('Helvetica',40),fg_color='#05161a',text_color='#FFFFFF')
            tab_namelabel.place(x=430, y=20)
                
            bckbtn = ctk.CTkButton(supports_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5)
            logo=ctk.CTkButton(supports_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            help_namelabel=ctk.CTkLabel(supports_frame,text="We're here to help.",font=('Helvetica',35),fg_color='#05161a',text_color='grey')
            help_namelabel.place(x=390, y=100)
            query_namelabel=ctk.CTkLabel(supports_frame,text="Have any queries ?",font=('Helvetica',20),fg_color='#05161a',text_color='grey')
            query_namelabel.place(x=450, y=80)
            divider=ctk.CTkFrame(supports_frame,width=700,height=3,border_width=0,border_color='grey',fg_color='grey',corner_radius=20)
            divider.place(x=215,y=145)
            help_sales=ctk.CTkLabel(supports_frame,text='Sales',fg_color='#0c7075',bg_color='#05161a',height=150,width=240,corner_radius=20,text_color='white',font=fnt1)
            help_returns=ctk.CTkLabel(supports_frame,text='Returns',fg_color='#0c7075',bg_color='#05161a',height=150,width=240,corner_radius=20,text_color='white',font=fnt1)
            help_complaints=ctk.CTkLabel(supports_frame,text='Complaints',fg_color='#0c7075',bg_color='#05161a',height=150,width=240,corner_radius=20,text_color='white',font=fnt1)
            help_marketing=ctk.CTkLabel(supports_frame,text='Marketing',fg_color='#0c7075',bg_color='#05161a',height=150,width=240,corner_radius=20,text_color='white',font=fnt1)
            help_sales.place(x=35,y=180)
            help_returns.place(x=285,y=180)
            help_complaints.place(x=535,y=180)
            help_marketing.place(x=785,y=180)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)
  
 #NOTIFICATION TAB   
       
    def notification_tab():          
            
            for i in frame_list:
                i.place_forget()
            
            notification_frame.place(x=30,y=30)
            tab_namelabel=ctk.CTkLabel(notification_frame,text='Notifications',font=('Helvetica',40),fg_color='#072e33',text_color='#FFFFFF')
            tab_namelabel.place(x=220, y=10)            
    
            bckbtn = ctk.CTkButton(notification_frame, text="", command=back, image=backbutn, fg_color='#05161a',                    hover_color='#05161a', height=55, width=55, corner_radius=5) 
            logo=ctk.CTkButton(notification_frame,image= logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
            logo.place(x=120,y=3)      
            bckbtn.place(x=40, y=10)      
            scroll_frame = ctk.CTkScrollableFrame(notification_frame, height=400, width=960, fg_color='#05161a',                               corner_radius=40, border_width=3)
            scroll_frame.place(x=20, y=70)
            shop_scrollframe1=ctk.CTkLabel(scroll_frame,text='',width=100,height=1200)
            shop_scrollframe1.pack()

            
#CART TAB      
    def cart_tab():
        global ui
        for i in frame_list:
        	i.place_forget()
        	
        cart_frame.place(x=30, y=30)
        tab_namelabel = ctk.CTkLabel(cart_frame, text='Cart',  font=('Helvetica', 40),fg_color='#05161a',text_color='#FFFFFF' )
        tab_namelabel.place(x=220, y=10)
        bckbtn = ctk.CTkButton(cart_frame,text="",command=back,image=backbutn,fg_color='#05161a',hover_color='#05161a',height=55,width=55,corner_radius=5)
        logo = ctk.CTkButton(cart_frame,image=logo_image_one,text='',fg_color='#05161a',bg_color='#05161a',hover_color='#05161a',command=checked,height=60,width=70)
        logo.place(x=120, y=3)
        bckbtn.place(x=40, y=10)
        with sqlite3.connect('groceria.db') as conn:
        	cursor = conn.cursor()
        	try:
        	   s_mail = email_address_login.get()
        	   user_id = sanitize_email(s_mail)
        	   table_name = f"{user_id}_cart"
        	   query = f"SELECT product_id, product_name, price FROM {table_name}"
        	   cursor.execute(query)
        	   products = cursor.fetchall()
        	   if not products:
        	           ctk.CTkLabel(cart_frame,text="Your cart is empty!",font=('Helvetica', 22),text_color='#FFFFFF').place(x=50, y=100)
        	           return
        	   product_height = 180  # Height of each product frame
        	   scroll_frame_height = ((product_height) * 2) + 40  # Adjust height with padd
        	   scroll_frame = ctk.CTkScrollableFrame(cart_frame,width=960,height=scroll_frame_height,fg_color='#05161a',corner_radius=40,border_width=0)
        	   scroll_frame.place(x=20, y=70)
        	   positions = [(10, 10), (10, 210), (10, 410),(10, 610), (10, 810), (10, 1010), (10, 1210), (10, 1410), (10, 1610), (10, 1810), (10, 2010), (10, 2210), (10, 2410), (10, 2610), (10, 2810), (10, 3010), (10, 3210), (10, 3410), (10, 3610), (10, 3810)][:len(products)]
        	   backlbl = ctk.CTkLabel(scroll_frame,text='',font=('Helvetica', 40),width=900,height=4000,fg_color='#05161a',corner_radius=20)
        	   backlbl.pack()
        	   
        	   tables = ["veges", "fruits", "dairy", "supplies"]
        	   for i, product in enumerate(products):
        	   	product_id, product_name, price = product
        	   	product_details = None
        	   	for table in tables:
        	   	           cursor.execute(f"SELECT description, quantity, discount FROM {table} WHERE product_id = ?",(product_id,))
        	   	           product_details = cursor.fetchone()
        	   	           if product_details:
        	   	            	break 
        	   	            	 
        	   	if not product_details:
        	   		continue  # Skip products not found in any category table
        	   	description, db_quantity, discount = product_details
        	   	product_label = ctk.CTkLabel(scroll_frame,text='',font=('Helvetica', 40),width=900,height=180,fg_color='white',corner_radius=20)
        	   	product_label.place(x=positions[i][0], y=positions[i][1])
        	   	try:
        	   	       image_path = f"images/{product_id}.png"
        	   	       img = Image.open(image_path)
        	   	       ctk_image = ctk.CTkImage(img, size=(100, 100))
        	   	       image_button = ctk.CTkButton(product_label,text='',image=ctk_image,height=140,width=140,corner_radius=20,fg_color='white',border_width=3,bg_color='white',hover_color='white',command=lambda product_id=product_id, product_name=product_name, price=price, quantity=quantity, description=description, discount=discount: transit_tab({
    "product_id": product_id,
    "product_name": product_name,
    "price": price,
    "quantity": quantity,
    "description": description,
    "discount": discount
}))
        	   	       image_button.place(x=20, y=20)
        	   	       print(f"ui{product_id}")
        	   	       ui=product_id
        	   	except FileNotFoundError:
        	   	       image_button = ctk.CTkButton(product_label,text='No Image',height=140,width=140,corner_radius=20,fg_color='white',border_width=3,bg_color='white',hover_color='white')
        	   	       image_button.place(x=20, y=20)        	   	
        	   	
        	   	info_label = ctk.CTkFrame(product_label,height=140,width=620,corner_radius=20,fg_color='#ffffff',border_width=3)
        	   	info_label.place(x=180, y=20)
        	   	product_name_label = ctk.CTkLabel(info_label,text=f"Name: {product_name}",font=('Helvetica', 22))
        	   	product_name_label.place(x=10, y=10)
        	   	price_label = ctk.CTkLabel(info_label,text=f"Price: ₹{price}",font=('Helvetica', 22))
        	   	price_label.place(x=10, y=40)
        	   	quantity_label = ctk.CTkLabel(info_label,text=f"Quantity: {quantity}",font=('Helvetica', 22))
        	   	quantity_label.place(x=10, y=70)
        	   	description_label = ctk.CTkLabel(info_label,text=f"Description: {description}",font=('Helvetica', 16),wraplength=550,justify='left')
        	   	print(f"cid:{product_id}")
        	   	if discount:
        	   	           discount_label = ctk.CTkLabel(info_label,text=f"Discount: {discount}%",font=('Helvetica', 22),text_color='red')
        	   	           discount_label.place(x=10, y=100)

        	except sqlite3.Error as e:
        	 	messagebox.showerror("Database Error", str(e))
          	
                 
    #widgets on shop without menu
    searchbox=ctk.CTkEntry(shop_widgets,fg_color='white',width=500,height=60,corner_radius=20,border_width=3,bg_color='#05161a',border_color='#0f969c')
    notification_button=ctk.CTkButton(shop_widgets,text='',image=notify,fg_color='#05161a',width=50,height=50,corner_radius=20,border_width=0,bg_color='#05161a',command=notification_tab)
    cart_button=ctk.CTkButton(shop_widgets,text='',image=cartt,fg_color='#0c7075',width=50,height=50,corner_radius=20,border_width=3,bg_color='#05161a',command=cart_tab)
    search_button=ctk.CTkButton(shop_widgets,text='',image=seac,fg_color='#05161a',width=50,height=30,corner_radius=20,border_width=3,bg_color='#ffffff',border_color='#0f969c',command=lambda: search_tab(searchbox, search_frame, email_id))    
    #placing the widgets without menu
    shop_widgets.place(x=270,y=25)
    notification_button.place(x=630,y=5)
    cart_button.place(x=520,y=5)
    search_button.place(x=420,y=10)
    searchbox.place(x=5,y=5)
            
            
    #widgets in the menu
    orders = ctk.CTkButton(tabs_frame, text="Orders          ",image=open, fg_color="#05161a", font=fnt1, corner_radius=20, width=210, height=40,border_width=3,compound='right',text_color='white',command=orders_tab,border_color="#0f969c")
    profile = ctk.CTkButton(tabs_frame, text="   Hi user ", fg_color="#ffffff", font=fnt1, corner_radius=20, width=210, height=100,border_width=3,compound='left',text_color='black',image=prof,command=profile_tab)
    hpc = ctk.CTkButton(tabs_frame, text="Contact Us      ", fg_color="#05161a", font=fnt1, corner_radius=20, width=210, height=40,image=open,border_width=3,text_color='white',compound='right',command=supports_tab,border_color="#0f969c")
    category= ctk.CTkButton(tabs_frame, text="Categories     ", fg_color="#05161a", font=fnt1, corner_radius=20, width=210, height=40,image=open,border_width=3,text_color='white',compound='right',command=category_button,border_color="#0f969c")
    logout= ctk.CTkButton(tabs_frame, text="", fg_color="#0f969c", font=fnt1, corner_radius=20, width=210, height=40, command=login,border_width=3,image=logoutimg,text_color='black')
    
    # placing tab buttons    
    profile.place(x=20, y=20)
    orders.place(x=20, y=130)
    hpc.place(x=20, y=180)
    category.place(x=20, y=230)
    logout.place(x=20,y=450)
    
    #widgets with menu
    menu_searchbox=ctk.CTkEntry(shop_widgets_menu,fg_color='white',width=420,height=60,corner_radius=20,border_width=3,bg_color='#05161a',border_color="#0f969c")
    menu_notification_button=ctk.CTkButton(shop_widgets_menu,text='',image=notify,fg_color='#05161a',width=50,height=50,corner_radius=20,border_width=0,bg_color='#05161a',command=notification_tab)
    menu_cart_button=ctk.CTkButton(shop_widgets_menu,text='',image=cartt,fg_color='#0c7075',width=50,height=50,corner_radius=20,border_width=3,bg_color='#05161a',command=cart_tab)
    menu_search_button=ctk.CTkButton(shop_widgets_menu,text='',image=seac,fg_color='#05161a',width=50,height=30,corner_radius=20,border_width=3,bg_color='#ffffff',border_color='#0f969c',command=search_tab)
    
    #placing widgets with menu
    menu_notification_button.place(x=630,y=5)
    menu_cart_button.place(x=530,y=5)  
    menu_search_button.place(x=435,y=10)
    menu_searchbox.place(x=100,y=5)
        
#MENU BUTTON FUNCTIONING AND DEFINING
    def function_one():
        shop_scrollframe.place_forget()
        shop_scrollframe1.place(x=290,y=110)            
        tabs_frame.place(x=25,y=25)
        products_frame_menu.place(x=35,y=205)
                
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
    menubtn=ctk.CTkButton(shop_mainframe,text='',image=menu,fg_color='#05161a',command=click,corner_radius=20,height=40,    width=40,hover_color='#05161a',border_width=0,bg_color='#05161a')
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
email_id = email_address.get()
email=email_address.get()

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
signup_button=ctk.CTkButton(widgetframe_su,text='Sign Up',font=('vivaldi italics',20),height=60,width=220,corner_radius=30,fg_color='#0c7075',hover_color='white',border_color='#0f969c',border_width=3,command=signup_user)
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
    global email_address
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