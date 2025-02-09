import tkinter
import customtkinter as ctk
from PIL import Image, ImageTk

# Create the main window
window = ctk.CTk()
window.title("Product Display Page")
window.geometry("800x600")

# Product information
product_name = "Apple Watch"
product_price = "$399"
product_description = "A sleek and stylish smartwatch with fitness tracking and notification features."

# Load the product image
image = Image.open("product_image.jpg")
image = image.resize((300, 300))
photo = ImageTk.PhotoImage(image)

# Create the product frame
product_frame = ctk.CTkFrame(window, corner_radius=10, fg_color="#f2f2f2")
product_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Create the product image label
image_label = ctk.CTkLabel(product_frame, image=photo, text="", corner_radius=10, fg_color="#f2f2f2")
image_label.pack(pady=20, padx=20, side="left")

# Create the product information frame
info_frame = ctk.CTkFrame(product_frame, corner_radius=10, fg_color="#f2f2f2")
info_frame.pack(pady=20, padx=20, side="right", fill="both", expand=True)

# Create the product name label
name_label = ctk.CTkLabel(info_frame, text=product_name, font=("Arial", 24), corner_radius=10, fg_color="#f2f2f2")
name_label.pack(pady=10, padx=10)

# Create the product price label
price_label = ctk.CTkLabel(info_frame, text=product_price, font=("Arial", 18), corner_radius=10, fg_color="#f2f2f2")
price_label.pack(pady=10, padx=10)

# Create the product description label
description_label = ctk.CTkLabel(info_frame, text=product_description, font=("Arial", 14), corner_radius=10, fg_color="#f2f2f2", wraplength=400, justify="left")
description_label.pack(pady=10, padx=10)

window.mainloop()