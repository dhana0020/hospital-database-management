
import tkinter as tk
from tkinter import messagebox
import cx_Oracle
from datetime import datetime

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

# Function to add a new medicine
def add_medicine():
    medicine_id = medicine_id_entry.get()
    mname = mname_entry.get()
    category = category_entry.get()
    treatment_id = treatment_id_entry.get()
    dosage = dosage_entry.get()
    price = price_entry.get()

    if not medicine_id or not mname or not category or not treatment_id or not dosage or not price:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    # Convert price to float
    try:
        price_value = float(price)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid price.")
        return

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """INSERT INTO medicines (Medicine_ID, MName, Category, Treatment_ID, Dosage, Price) 
                VALUES (:1, :2, :3, :4, :5, :6)""",
                (medicine_id, mname, category, treatment_id, dosage, price_value)
            )
            connection.commit()
            messagebox.showinfo("Success", "Medicine added successfully!")
            clear_fields()  # Clear input fields after successful addition
        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Function to clear input fields
def clear_fields():
    medicine_id_entry.delete(0, tk.END)
    mname_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    treatment_id_entry.delete(0, tk.END)
    dosage_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Add Medicine")

# Create input fields
tk.Label(root, text="Medicine ID:").grid(row=0, column=0)
medicine_id_entry = tk.Entry(root)
medicine_id_entry.grid(row=0, column=1)

tk.Label(root, text="Medicine Name:").grid(row=1, column=0)
mname_entry = tk.Entry(root)
mname_entry.grid(row=1, column=1)

tk.Label(root, text="Category:").grid(row=2, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=2, column=1)

tk.Label(root, text="Treatment ID:").grid(row=3, column=0)
treatment_id_entry = tk.Entry(root)
treatment_id_entry.grid(row=3, column=1)

tk.Label(root, text="Dosage:").grid(row=4, column=0)
dosage_entry = tk.Entry(root)
dosage_entry.grid(row=4, column=1)

tk.Label(root, text="Price:").grid(row=5, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=5, column=1)

# Create Add Medicine button
add_button = tk.Button(root, text="Add Medicine", command=add_medicine)
add_button.grid(row=6, columnspan=2)

# Start the GUI event loop
root.mainloop()
