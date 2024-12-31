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

# Function to add a new doctor
def add_doctor():
    doctor_id = doctor_id_entry.get()
    dname = dname_entry.get()
    specialization = specialization_entry.get()
    dphonenumber = dphonenumber_entry.get()
    email = email_entry.get()
    department_id = department_id_entry.get()

    if not doctor_id or not dname or not specialization or not dphonenumber or not email or not department_id:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO doctors (Doctor_ID, DName, Specialization, DPhoneNumber, Email, Department_ID) VALUES (:1, :2, :3, :4, :5, :6)",
                (doctor_id, dname, specialization, dphonenumber, email, department_id)
            )
            connection.commit()
            messagebox.showinfo("Success", "Doctor added successfully!")
            clear_fields()  # Clear input fields after successful addition
        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Function to clear input fields
def clear_fields():
    doctor_id_entry.delete(0, tk.END)
    dname_entry.delete(0, tk.END)
    specialization_entry.delete(0, tk.END)
    dphonenumber_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    department_id_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Add Doctor")

# Create input fields
tk.Label(root, text="Doctor ID:").grid(row=0, column=0)
doctor_id_entry = tk.Entry(root)
doctor_id_entry.grid(row=0, column=1)

tk.Label(root, text="Doctor Name:").grid(row=1, column=0)
dname_entry = tk.Entry(root)
dname_entry.grid(row=1, column=1)

tk.Label(root, text="Specialization:").grid(row=2, column=0)
specialization_entry = tk.Entry(root)
specialization_entry.grid(row=2, column=1)

tk.Label(root, text="Phone Number:").grid(row=3, column=0)
dphonenumber_entry = tk.Entry(root)
dphonenumber_entry.grid(row=3, column=1)

tk.Label(root, text="Email:").grid(row=4, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1)

tk.Label(root, text="Department ID:").grid(row=5, column=0)
department_id_entry = tk.Entry(root)
department_id_entry.grid(row=5, column=1)

# Create Add Doctor button
add_button = tk.Button(root, text="Add Doctor", command=add_doctor)
add_button.grid(row=6, columnspan=2)

# Start the GUI event loop
root.mainloop()
