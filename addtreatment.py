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

# Function to add a new treatment
def add_treatment():
    treatment_id = treatment_id_entry.get()
    appointment_id = appointment_id_entry.get()
    treatment_description = treatment_description_entry.get()
    treatment_date = treatment_date_entry.get()
    cost = cost_entry.get()

    if not treatment_id or not appointment_id or not treatment_description or not treatment_date or not cost:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    # Convert treatment date to proper format
    try:
        treatment_date_obj = datetime.strptime(treatment_date, "%Y-%m-%d").date()
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter date in YYYY-MM-DD format.")
        return

    # Convert cost to float
    try:
        cost_value = float(cost)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid cost.")
        return

    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """INSERT INTO treatment(Treatment_ID, Appointment_ID, Treatment_Description, 
                TreatmentDate, Cost) 
                VALUES (:1, :2, :3, :4, :5)""",
                (treatment_id, appointment_id, treatment_description, treatment_date_obj, cost_value)
            )
            connection.commit()
            messagebox.showinfo("Success", "Treatment added successfully!")
            clear_fields()  # Clear input fields after successful addition
        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Function to clear input fields
def clear_fields():
    treatment_id_entry.delete(0, tk.END)
    appointment_id_entry.delete(0, tk.END)
    treatment_description_entry.delete(0, tk.END)
    treatment_date_entry.delete(0, tk.END)
    cost_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Add Treatment")

# Create input fields
tk.Label(root, text="Treatment ID:").grid(row=0, column=0)
treatment_id_entry = tk.Entry(root)
treatment_id_entry.grid(row=0, column=1)

tk.Label(root, text="Appointment ID:").grid(row=1, column=0)
appointment_id_entry = tk.Entry(root)
appointment_id_entry.grid(row=1, column=1)

tk.Label(root, text="Treatment Description:").grid(row=2, column=0)
treatment_description_entry = tk.Entry(root)
treatment_description_entry.grid(row=2, column=1)

tk.Label(root, text="Treatment Date (YYYY-MM-DD):").grid(row=3, column=0)
treatment_date_entry = tk.Entry(root)
treatment_date_entry.grid(row=3, column=1)

tk.Label(root, text="Cost:").grid(row=4, column=0)
cost_entry = tk.Entry(root)
cost_entry.grid(row=4, column=1)

# Create Add Treatment button
add_button = tk.Button(root, text="Add Treatment", command=add_treatment)
add_button.grid(row=5, columnspan=2)

# Start the GUI event loop
root.mainloop()
