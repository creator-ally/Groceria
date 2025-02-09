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
    forgot_password_btn = ctk.CTkButton(loginframe, text='Forgot password?', command=fgpass, fg_color='#072e33', text_color='white', hover_color='#072e33')
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
    forgot_password_btn.place(x=30, y=260)
    login_button.place(x=120, y=290)
    google_button.place(x=120, y=400)
    instagram_button.place(x=200, y=400)
    phon_button.place(x=280, y=400)
    signup_return.place(x=160, y=350)    