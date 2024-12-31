import tkinter as tk
from tkinter import messagebox
import cx_Oracle
from tkinter import ttk

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

# Function to view departments and update the Treeview
def view_departments():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Query to select all departments
            cursor.execute("SELECT * FROM departments")
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
root.title("Department Management")



# Create a Treeview to display departments
tree = ttk.Treeview(root, columns=("Department_ID", "DepartmentName", "SpecializedDoctor"), show='headings')
tree.grid(row=4, column=0, columnspan=2, pady=10)

# Define column headings
tree.heading("Department_ID", text="Department ID")
tree.heading("DepartmentName", text="Department Name")
tree.heading("SpecializedDoctor", text="Specialized Doctor")

# Call view_departments to fetch and display data immediately
view_departments()

# Start the GUI event loop
root.mainloop()
