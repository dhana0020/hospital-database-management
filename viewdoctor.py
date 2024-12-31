import tkinter as tk
from tkinter import messagebox
import cx_Oracle
from tkinter import ttk

# Function to connect to the Oracle database
def connect_to_db():
    try:
        dsn = cx_Oracle.makedsn("dhans", 1521, service_name="XE")
        connection = cx_Oracle.connect(user="system", password="system", dsn=dsn)
        return connection
    except cx_Oracle.DatabaseError as e:
        messagebox.showerror("Database Error", str(e))
        return None

# Function to view doctors and update the Treeview
def view_doctors():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM doctors")
            rows = cursor.fetchall()
            # Clear previous entries in the Treeview
            for row in tree.get_children():
                tree.delete(row)  # Clear previous entries
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
root.title("Hospital Management System")

view_frame = tk.LabelFrame(root, text="View Doctors", padx=10, pady=10)
view_frame.grid(row=1, column=0, padx=20, pady=10)

# Create Treeview to display doctors
tree = ttk.Treeview(view_frame, columns=("Doctor ID", "Name", "Specialization", "Phone", "Email", "Dept ID"), show='headings')
tree.pack()

# Define column headings
tree.heading("Doctor ID", text=" Doctor ID")
tree.heading("Name", text="Name")
tree.heading("Specialization", text="Specialization")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Dept ID", text="Dept ID")

# Call view_doctors function to populate the Treeview when the application starts
view_doctors()

# Start the GUI event loop
root.mainloop()
