import tkinter as tk
import tkinter.messagebox
from tkinter import *
from try3 import HospitalManagementSystem  
from PIL import Image, ImageTk

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")

        self.master.attributes('-fullscreen', True)

        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.bg_image = Image.open(r"C:\\Users\\hanal\\Desktop\\dbms\\bg1.jpeg")  # Make sure to have this image in the same directory
        self.bg_image = self.bg_image.resize((self.screen_width, self.screen_height), Image.LANCZOS)  # Resize image to fit the window
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = Label(self.master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Make it cover the entire window

        self.frame = Frame(self.master, bg="powder blue", bd=10)  # Change frame background to white for contrast
        self.frame.place(relx=0.5, rely=0.5, anchor='center',width=500, height=400) 

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text="HOSPITAL MANAGEMENT SYSTEM", font="Helvetica 20 bold", bg="powder blue", fg="black")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblUsername = Label(self.LoginFrame1, text="Username", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.entUsername = Entry(self.LoginFrame1, font="Helvetica 14 bold", textvariable=self.Username, bd=2)
        self.entUsername.grid(row=0, column=1)
        
        self.lblPassword = Label(self.LoginFrame1, text="Password", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.entPassword = Entry(self.LoginFrame1, font="Helvetica 14 bold", show="*", textvariable=self.Password, bd=2)
        self.entPassword.grid(row=1, column=1)

        self.btnLogin = Button(self.LoginFrame2, text="Login", font="Helvetica 10 bold", width=10, bg="powder blue", command=self.Login_system)
        self.btnLogin.grid(row=3, column=0)
        
        self.btnExit = Button(self.LoginFrame2, text="Exit", font="Helvetica 10 bold", width=10, bg="powder blue", command=self.Exit)
        self.btnExit.grid(row=3, column=1)

    def Login_system(self):
        """Handles login verification."""
        S1 = self.Username.get()
        S2 = self.Password.get()

        if S1 == 'admin' and S2 == '1234':  
            self.newWindow = Toplevel(self.master)  
            self.app = HospitalManagementSystem(self.newWindow)  
            self.master.withdraw()  
        elif S1 == 'root' and S2 == '4321':  
            self.newWindow = Toplevel(self.master)  
            self.app = HospitalManagementSystem(self.newWindow)  
            self.master.withdraw()  
        elif S1 == 'doctor' and S2 == 'doctor':
            self.newWindow = Toplevel(self.master)
            self.app = HospitalManagementSystem(self.newWindow)
            self.master.withdraw()  
        else:
            tkinter.messagebox.askretrycancel("HOSPITAL MANAGEMENT SYSTEM", "PLEASE ENTER VALID USERNAME AND PASSWORD")

    def Exit(self):
        """Exit the application."""
        self.master.quit() 

def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
