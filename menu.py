import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.config(bg="#5F9EA0")

        self.create_main_menu()


    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=20)

        self.create_button(menu_frame, "Patient", self.open_patient_window)
        self.create_button(menu_frame, "Department", self.open_department_window)
        self.create_button(menu_frame, "Appointment", self.open_appointment_window)
        self.create_button(menu_frame, "Medicine", self.open_medicine_window)
        self.create_button(menu_frame, "Treatment", self.open_treatment_window)
        self.create_button(menu_frame, "Exit", self.exit)

    def create_button(self, parent, text, command):
        """Creates a large blue, interactive button"""
        button = tk.Button(parent, text=text, command=command, 
                           font=("Algerian", 16, "bold"), 
                           bg="#5F9EA0", fg="Black", 
                           activebackground="#DA70D6", activeforeground="black",
                           relief="raised", bd=10, height=2)
        button.pack(pady=15, padx=20, fill=tk.X)

        button.bind("<Enter>", lambda e: button.config(bg="#0056b3"))
        button.bind("<Leave>", lambda e: button.config(bg="#5F9EA0"))
    
    def open_patient_window(self):
        self.root.withdraw()  
        patient_window = tk.Toplevel(self.root)
        patient_window.title("Patient Management")
        
        self.create_button(patient_window, "Add Patient", self.add_patient)
        self.create_button(patient_window, "View Patient", self.view_patient)
        self.create_button(patient_window, "Patient Bill", self.patient_bill)

        self.create_button(patient_window, "Back to Main Menu", lambda: self.show_main_menu(patient_window))

    def add_patient(self):
        messagebox.showinfo("Add Patient", "Click OK to add patient!")
        from patient import add_patient        

    def view_patient(self):
        messagebox.showinfo("View Patient", "Click OK to view patient details.")
        from pat2 import  view_patients

    def patient_bill(self):
        messagebox.showinfo("Patient Bill", "Patient Bill functionality goes here.")
        from bill2 import view_bills


    def open_department_window(self):
        self.root.withdraw()  
        department_window = tk.Toplevel(self.root)
        department_window.title("Department Management")
        
        self.create_button(department_window, "Add Department", self.add_department)
        self.create_button(department_window, "View Department", self.view_department)

        self.create_button(department_window, "add doctors", self.add_doctor)
        self.create_button(department_window, "view doctors", self.view_doctors)

        self.create_button(department_window, "Back to Main Menu", lambda: self.show_main_menu(department_window))

    def add_department(self):
        messagebox.showinfo("Add Department", "Add Department functionality goes here.")
        from dept import add_department

    def view_department(self):
        messagebox.showinfo("View Department", "View Department functionality goes here.")
        from dept2 import view_departments
    
    def add_doctor(self):
        messagebox.showinfo("Add Doctors", "Add Doctors functionality goes here.")
        from doctor import add_doctor

    def view_doctors(self):
        messagebox.showinfo("View Doctors", "view Doctors functionality goes here.")
        from doc2 import view_doctors
    

    def open_appointment_window(self):
        self.root.withdraw()  # Hide the main window
        appointment_window = tk.Toplevel(self.root)
        appointment_window.title("Appointment Management")
        
        self.create_button(appointment_window, "Add Appointment", self.add_appointment)
        self.create_button(appointment_window, "View Appointment", self.view_appointment)

        
        self.create_button(appointment_window, "Back to Main Menu", lambda: self.show_main_menu(appointment_window))

    def add_appointment(self):
        messagebox.showinfo("Add Appointment", "Add Appointment functionality goes here.")
        from app import add_appointment

    def view_appointment(self):
        messagebox.showinfo("View Appointment", "View Appointment functionality goes here.")
        from app2 import view_appointments


    def open_medicine_window(self):
        self.root.withdraw()  
        medicine_window = tk.Toplevel(self.root)
        medicine_window.title("Medicine Management")
        
        self.create_button(medicine_window, "Medicines Available", self.view_medicines)
        self.create_button(medicine_window, "Add Medicine", self.add_medicine)
        self.create_button(medicine_window, "Medicines by Department", self.medicines_by_department)

        self.create_button(medicine_window, "Back to Main Menu", lambda: self.show_main_menu(medicine_window))

    def view_medicines(self):
        messagebox.showinfo("Medicines Available", "View Medicines functionality goes here.")
        from med2 import view_medicines

    def add_medicine(self):
        messagebox.showinfo("Add Medicine", "Add Medicine functionality goes here.")
        from med import add_medicines
    def medicines_by_department(self):
        messagebox.showinfo("Medicines by Department", "Medicines by Department functionality goes here.")
        from med3 import view_medicines_by_category
        
    def open_treatment_window(self):
        self.root.withdraw()  
        treatment_window = tk.Toplevel(self.root)
        treatment_window.title("Treatment Management")
        
        self.create_button(treatment_window, "Add Treatment", self.add_treatment)
        self.create_button(treatment_window, "View Treatment", self.view_treatment)

        self.create_button(treatment_window, "Back to Main Menu", lambda: self.show_main_menu(treatment_window))

    def add_treatment(self):
        messagebox.showinfo("Add Treatment", "Click OK/Enter to add Treatment ")
        from treat import add_treatment

    def view_treatment(self):
        messagebox.showinfo("View Treatment", "Click OK/Enter to view Treatment details")
        from treat2 import view_treatment

    def show_main_menu(self, window):
        window.destroy()  
        self.root.deiconify()  
        self.create_main_menu()  

    def exit(self):
        """Closes the application"""
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()
