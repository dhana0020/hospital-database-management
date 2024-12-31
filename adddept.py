import tkinter as tk
from tkinter import messagebox
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

# Function to add a new department
def add_department():
    department_id = department_id_entry.get()
    department_name = department_name_entry.get()
    specialized_doctor = specialized_doctor_entry.get()

    if not department_id or not department_name or not specialized_doctor:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO departments (Department_ID, Department_Name, SpecializedDoctor) VALUES (:1, :2, :3)",
                (department_id, department_name, specialized_doctor)
            )
            connection.commit()
            messagebox.showinfo("Success", "Department added successfully!")
            clear_fields()  # Clear input fields after successful addition
        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Function to clear input fields
def clear_fields():
    department_id_entry.delete(0, tk.END)
    department_name_entry.delete(0, tk.END)
    specialized_doctor_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Add Department")

# Create input fields
tk.Label(root, text="Department ID:").grid(row=0, column=0)
department_id_entry = tk.Entry(root)
department_id_entry.grid(row=0, column=1)

tk.Label(root, text="Department Name:").grid(row=1, column=0)
department_name_entry = tk.Entry(root)
department_name_entry.grid(row=1, column=1)

tk.Label(root, text="Specialized Doctor:").grid(row=2, column=0)
specialized_doctor_entry = tk.Entry(root)
specialized_doctor_entry.grid(row=2, column=1)

# Create Add Department button
add_button = tk.Button(root, text="Add Department", command=add_department)
add_button.grid(row=3, columnspan=2)

# Start the GUI event loop
root.mainloop()
