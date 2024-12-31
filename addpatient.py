import tkinter as tk
from tkinter import messagebox
import cx_Oracle
from datetime import datetime
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

# Function to add a new patient
def add_patient():
    patientid = patientid_entry.get()
    pname = pname_entry.get()
    dob = dob_entry.get()
    gender = gender_entry.get()
    pphonenumber = pphonenumber_entry.get()
    address = address_entry.get()
    bloodgroup = bloodgroup_entry.get()

    if not patientid or not pname or not dob or not gender or not pphonenumber or not address or not bloodgroup:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    # Convert DOB to date format
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter DOB in YYYY-MM-DD format.")
        return

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO patients (patient_id, pname, dob, gender, pphonenumber, address, blood_group) "
                "VALUES (:1, :2, :3, :4, :5, :6, :7)",
                (patientid, pname, dob_date, gender, pphonenumber, address, bloodgroup)
            )
            connection.commit()
            messagebox.showinfo("Success", "Patient added successfully!")
            clear_fields()  # Clear input fields after successful addition
        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Function to clear input fields
def clear_fields():
    patientid_entry.delete(0, tk.END)
    pname_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    pphonenumber_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    bloodgroup_entry.delete(0, tk.END)



# Create the main window
root = tk.Tk()
root.title("Hospital Management System")

# Frame for adding patient details
add_frame = tk.LabelFrame(root, text="Add Patient Details", padx=10, pady=10)
add_frame.grid(row=0, column=0, padx=20, pady=10)

# Create input fields
tk.Label(add_frame, text="Patient ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
patientid_entry = tk.Entry(add_frame)
patientid_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(add_frame, text="Patient Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
pname_entry = tk.Entry(add_frame)
pname_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(add_frame, text="Date of Birth (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
dob_entry = tk.Entry(add_frame)
dob_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(add_frame, text="Gender:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_entry = tk.Entry(add_frame)
gender_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(add_frame, text="Phone Number:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
pphonenumber_entry = tk.Entry(add_frame)
pphonenumber_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(add_frame, text="Address:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
address_entry = tk.Entry(add_frame)
address_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(add_frame, text="Blood Group:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
bloodgroup_entry = tk.Entry(add_frame)
bloodgroup_entry.grid(row=6, column=1, padx=10, pady=5)

# Create Add Patient button below input fields
add_button = tk.Button(add_frame, text="Add Patient", command=add_patient)
add_button.grid(row=7, column=0, columnspan=2, pady=10)


   

# Start the GUI event loop
root.mainloop()
