import tkinter as tk
from tkinter import messagebox, ttk
import cx_Oracle

# Function to connect to the Oracle database
def connect_to_db():
    try:
        # Replace with your actual connection details
        dsn = cx_Oracle.makedsn("dhans", 1521, service_name="XE")
        connection = cx_Oracle.connect(user="system", password="system", dsn=dsn)
        return connection
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Database Error", str(e))
        return None

# Function to fetch categories and populate the combobox
def fetch_categories():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT DISTINCT Category FROM medicines")  # Adjust the query as needed
            categories = cursor.fetchall()
            category_combobox['values'] = [cat[0] for cat in categories]  # Assuming cat[0] is the category name
        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Function to view medicines by selected category
def view_medicines_by_category():
    selected_category = category_combobox.get()
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Query to select medicines by category
            cursor.execute("""
                SELECT Medicine_ID, MName, Category, Treatment_ID, Dosage, Price 
                FROM medicines 
                WHERE Category = :category
            """, category=selected_category)
            rows = cursor.fetchall()
            # Clear previous entries in the Treeview
            for row in tree.get_children():
                tree.delete(row)
            # Insert new rows into the Treeview
            for row in rows:
                tree.insert("", "end", values=row)
        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Create the main window
root = tk.Tk()
root.title("Medicine Management by Category")

# Create a combobox for selecting category
tk.Label(root, text="Select Category:").grid(row=0, column=0)
category_combobox = ttk.Combobox(root, state="readonly")
category_combobox.grid(row=0, column=1)
category_combobox.bind("<<ComboboxSelected>>", lambda e: view_medicines_by_category())

# Create a Treeview to display medicines
tree = ttk.Treeview(root, columns=("Medicine_ID", "MName", "Category", "Treatment_ID", "Dosage", "Price"), show='headings')
tree.grid(row=1, column=0, columnspan=2, pady=10)

# Define column headings
tree.heading("Medicine_ID", text="Medicine ID")
tree.heading("MName", text="Medicine Name")
tree.heading("Category", text="Category")
tree.heading("Treatment_ID", text="Treatment ID")
tree.heading("Dosage", text="Dosage")
tree.heading("Price", text="Price")

# Fetch categories to populate the combobox
fetch_categories()

# Start the GUI event loop
root.mainloop()
