import sqlite3
from tkinter import messagebox, Tk, Label, Frame
from PIL import Image, ImageTk  # Make sure Pillow is installed

def display_category_products(category_table_name):
    conn = sqlite3.connect('groceria.db')
    cursor = conn.cursor()

    try:
        # Fetch product data from the specified category table
        cursor.execute(f"SELECT product_id, product_name, price, discount_percent, quantity_available, expiry_date, description FROM {category_table_name}")
        products = cursor.fetchall()

        # Check if the table has data
        if not products:
            messagebox.showinfo("Information", f"No products available in {category_table_name.capitalize()}.")
            return

        # Initialize a window to display the products
        window = Tk()
        window.title(f"{category_table_name.capitalize()} Products")

        # Display products systematically
        row = 0
        for product in products:
            product_id, product_name, price, discount_percent, quantity, expiry_date, description = product
            discount_price = price - (price * discount_percent / 100)

            # Create a frame for each product
            product_frame = Frame(window, padx=10, pady=10, relief="solid", borderwidth=1)
            product_frame.grid(row=row, column=0, padx=10, pady=5, sticky='w')

            # Product details
            Label(product_frame, text=f"Product Name: {product_name}", font=("Arial", 12)).grid(row=0, column=0, sticky='w')
            Label(product_frame, text=f"Price: ₹{price}", font=("Arial", 12)).grid(row=1, column=0, sticky='w')
            Label(product_frame, text=f"Discount: {discount_percent}%", font=("Arial", 12)).grid(row=2, column=0, sticky='w')
            Label(product_frame, text=f"Discounted Price: ₹{discount_price:.2f}", font=("Arial", 12)).grid(row=3, column=0, sticky='w')
            Label(product_frame, text=f"Quantity Available: {quantity}", font=("Arial", 12)).grid(row=4, column=0, sticky='w')
            Label(product_frame, text=f"Expiry Date: {expiry_date}", font=("Arial", 12)).grid(row=5, column=0, sticky='w')
            Label(product_frame, text=f"Description: {description}", font=("Arial", 12), wraplength=200).grid(row=6, column=0, sticky='w')

            # Load and display product image
            try:
                image_path = f"images/{product_id}.png"
                img = Image.open(image_path)
                img = img.resize((100, 100))  # Resize for display
                photo = ImageTk.PhotoImage(img)
                image_label = Label(product_frame, image=photo)
                image_label.image = photo  # Keep reference to avoid garbage collection
                image_label.grid(row=0, column=1, rowspan=7, padx=10)
            except FileNotFoundError:
                Label(product_frame, text="Image not found", font=("Arial", 10), fg="red").grid(row=0, column=1, rowspan=7, padx=10)

            row += 1  # Move to the next row for the next product

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        conn.close()

# Example usage for different categories:
display_category_products('fruits')        # Display products in the 'fruits' category
display_category_products('vegetables')     # Display products in the 'vegetables' category
display_category_products('dairy')          # Display products in the 'dairy' category