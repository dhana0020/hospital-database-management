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

# Function to view patients and update the Treeview
def view_patients():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM patients")
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

view_frame = tk.LabelFrame(root, text="View Patients", padx=10, pady=10)
view_frame.grid(row=1, column=0, padx=20, pady=10)

# Create Treeview to display patients
tree = ttk.Treeview(view_frame, columns=("Patient ID", "Name", "DOB", "Gender", "Contact Number", "Address", "Blood Group"), show='headings')
tree.pack()

# Define column headings
tree.heading("Patient ID", text="Patient ID")
tree.heading("Name", text="Name")
tree.heading("DOB", text="DOB")
tree.heading("Gender", text="Gender")
tree.heading("Contact Number", text="Contact Number")
tree.heading("Address", text="Address")
tree.heading("Blood Group", text="Blood Group")

# Call view_patients function to populate the Treeview when the application starts
view_patients()

# Start the GUI event loop
root.mainloop()
