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


# Function to view medicines and update the Treeview
def view_medicines():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Query to select all medicines
            cursor.execute("SELECT Medicine_ID, MName, Category, Treatment_ID, Dosage, Price FROM medicines")
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
root.title("Medicine Management")



# Create a Treeview to display medicines
tree = ttk.Treeview(root, columns=("Medicine_ID", "MName", "Category", "Treatment_ID", "Dosage", "Price"), show='headings')
tree.grid(row=7, column=0, columnspan=2, pady=10)

# Define column headings
tree.heading("Medicine_ID", text="Medicine ID")
tree.heading("MName", text="Medicine Name")
tree.heading("Category", text="Category")
tree.heading("Treatment_ID", text="Treatment ID")
tree.heading("Dosage", text="Dosage")
tree.heading("Price", text="Price")

# Call view_medicines to fetch and display data immediately
view_medicines()

# Start the GUI event loop
root.mainloop()
