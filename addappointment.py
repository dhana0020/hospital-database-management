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

# Function to add a new appointment
def add_appointment():
    appointment_id = appointment_id_entry.get()
    patient_id = patient_id_entry.get()
    doctor_id = doctor_id_entry.get()
    appointment_date = appointment_date_entry.get()
    appointment_time = appointment_time_entry.get()
    status = status_entry.get()

    if not appointment_id or not patient_id or not doctor_id or not appointment_date or not appointment_time or not status:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    # Convert appointment date and time to proper format
    try:
        appointment_date_obj = datetime.strptime(appointment_date, "%Y-%m-%d").date()
       # appointment_time_obj = datetime.strptime(appointment_time, "%H:%M").time()
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter date in YYYY-MM-DD format and time in HH:MM format.")
        return

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO appointments (Appointment_ID, Patient_ID, Doctor_ID, AppointmentDate, AppointmentTime, Status) VALUES (:1, :2, :3, :4, :5, :6)",
                (appointment_id, patient_id, doctor_id, appointment_date_obj, appointment_time, status)
            )
            connection.commit()
            messagebox.showinfo("Success", "Appointment added successfully!")
            clear_fields()  # Clear input fields after successful addition
        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Function to clear input fields
def clear_fields():
    appointment_id_entry.delete(0, tk.END)
    patient_id_entry.delete(0, tk.END)
    doctor_id_entry.delete(0, tk.END)
    appointment_date_entry.delete(0, tk.END)
    appointment_time_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Add Appointment")

# Create input fields
tk.Label(root, text="Appointment ID:").grid(row=0, column=0)
appointment_id_entry = tk.Entry(root)
appointment_id_entry.grid(row=0, column=1)

tk.Label(root, text="Patient ID:").grid(row=1, column=0)
patient_id_entry = tk.Entry(root)
patient_id_entry.grid(row=1, column=1)

tk.Label(root, text="Doctor ID:").grid(row=2, column=0)
doctor_id_entry = tk.Entry(root)
doctor_id_entry.grid(row=2, column=1)

tk.Label(root, text="Appointment Date (YYYY-MM-DD):").grid(row=3, column=0)
appointment_date_entry = tk.Entry(root)
appointment_date_entry.grid(row=3, column=1)

tk.Label(root, text="Appointment Time (HH:MM):").grid(row=4, column=0)
appointment_time_entry = tk.Entry(root)
appointment_time_entry.grid(row=4, column=1)

tk.Label(root, text="Status:").grid(row=5, column=0)
status_entry = tk.Entry(root)
status_entry.grid(row=5, column=1)

# Create Add Appointment button
add_button = tk.Button(root, text="Add Appointment", command=add_appointment)
add_button.grid(row=6, columnspan=2)

# Start the GUI event loop
root.mainloop()
