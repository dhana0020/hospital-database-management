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

# Function to view bills for a specific patient ID and update the Treeview
def view_bills(patient_id):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
           
            # Query to select bills for the specified patient ID
            #print(f"Querying for Patient ID: {patient_id}")
            cursor.execute("SELECT * FROM bills WHERE Patient_ID = :1", (patient_id,))
            rows = cursor.fetchall()
            # Clear previous entries in the Treeview
            for row in tree.get_children():
                tree.delete(row)
            # Insert new rows into the Treeview
            if rows:
                for row in rows:
                    tree.insert("", "end", values=row)
            else:
                messagebox.showinfo("No Records", f"No bills found for Patient ID: {patient_id}")
        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Function to fetch and display bills for the entered Patient ID
def fetch_bills():
    patient_id = patient_id_entry.get()
    if patient_id:
        view_bills(patient_id)
    else:
        messagebox.showwarning("Input Error", "Please enter a Patient ID.")

# Create the main window
root = tk.Tk()
root.title("View Bills for Patient")

# Create input field for Patient ID
tk.Label(root, text="Enter Patient ID:").pack(pady=10)
patient_id_entry = tk.Entry(root)
patient_id_entry.pack(pady=5)

# Create a Treeview to display bills
tree = ttk.Treeview(root, columns=("Bill ID", "Medicine ID", "Bill Date", "Total Amount", "Payment Status"), show='headings')
tree.pack()

# Define column headings
tree.heading("Bill ID", text="Bill ID")
tree.heading("Medicine ID", text="Medicine ID")
tree.heading("Bill Date", text="Bill Date")
tree.heading("Total Amount", text="Total Amount")
tree.heading("Payment Status", text="Payment Status")

# Create a button to fetch bills for the entered Patient ID
fetch_button = tk.Button(root, text="Fetch Bills", command=fetch_bills)
fetch_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
