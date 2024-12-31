import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # This is needed for the Treeview widget
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

# Function to view treatments
def view_treatment():
    # Connect to the database
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Query to retrieve all treatments
            cursor.execute("SELECT Treatment_ID, Appointment_ID, Treatment_Description, TreatmentDate, Cost FROM treatment")
            treatments = cursor.fetchall()

            # Create the main window for viewing treatments
            view_window = tk.Tk()  # Use the main window for viewing data
            view_window.title("View Treatments")
            # view_window = Frame(self.master, bg = "cadet blue")

            # Create a treeview widget to display treatments in a table format
            treeview = ttk.Treeview(view_window, columns=("Treatment_ID", "Appointment_ID", "Treatment_Description", "TreatmentDate", "Cost"), show="headings")
            treeview.pack(fill=tk.BOTH, expand=True)

            # Define column headings
            treeview.heading("Treatment_ID", text="Treatment ID")
            treeview.heading("Appointment_ID", text="Appointment ID")
            treeview.heading("Treatment_Description", text="Treatment Description")
            treeview.heading("TreatmentDate", text="Treatment Date")
            treeview.heading("Cost", text="Cost")

            # Insert data into the treeview
            for row in treatments:
                treeview.insert("", tk.END, values=row)

            # Start the GUI event loop for the new window
            view_window.mainloop()

        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

# Call the view_treatment function immediately after the main window is created
view_treatment()
