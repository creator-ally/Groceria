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

#Sign Up Mainframe
signup_mainframe=ctk.CTkFrame(window,border_width=3,fg_color='#05161a',corner_radius=60,height=580,width=1060,border_color='white')
signup_mainframe.place(x=30,y=30)
signup_backimage=ctk.CTkLabel(signup_mainframe,text='',image=background_image1)
signup_backimage.place(x=575,y=30)

#SIGNUP PAGE EMAIL VALIDATOR

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

#### USER DATABASE  [SERVER] ####

# Create a cursor object
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   email_id TEXT PRIMARY KEY,
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   pass_word TEXT NOT NULL,
                   address TEXT,
                   pincode TEXT)''')

# Commit the changes and close the connection
connection.commit()


def insert_user():
    email_id = email_address.get()
    first_name = fullname_entry.get()
    last_name = lastname_entry.get()
    pass_word = password.get()

    # Hash the password before storing it
    hashed_password = sha256(pass_word.encode()).hexdigest()

    conn = sqlite3.connect('groceria.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (email_id, first_name, last_name, pass_word) VALUES (?, ?, ?, ?)",
                       (email_id, first_name, last_name, hashed_password))
        conn.commit()
        messagebox.showinfo('Success','Successfully registered.')
    except sqlite3.IntegrityError:
        messagebox.showinfo('Error','Registered Email Id .')
        print("Error: Email ID already exists.")
    finally:
        conn.close()
