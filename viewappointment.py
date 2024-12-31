import tkinter as tk
from tkinter import messagebox
import cx_Oracle
from tkinter import ttk
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

# Function to view appointments and update the Treeview
def view_appointments():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Query to select all appointments
            cursor.execute("SELECT Appointment_ID, Patient_ID, Doctor_ID, AppointmentDate, AppointmentTime, Status FROM appointments")
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
root.title("Appointment Management")

# Create a Treeview to display appointments
tree = ttk.Treeview(root, columns=("Appointment_ID", "Patient_ID", "Doctor_ID", "AppointmentDate", "AppointmentTime", "Status"), show='headings')
tree.grid(row=0, column=0, columnspan=2, pady=10)

# Define column headings
tree.heading("Appointment_ID", text="Appointment ID")
tree.heading("Patient_ID", text="Patient ID")
tree.heading("Doctor_ID", text="Doctor ID")
tree.heading("AppointmentDate", text="Appointment Date")
tree.heading("AppointmentTime", text="Appointment Time")
tree.heading("Status", text="Status")

# Call view_appointments to fetch and display data immediately
view_appointments()

# Start the GUI event loop
root.mainloop()
