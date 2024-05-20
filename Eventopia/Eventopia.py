import tkinter as tk
from tkinter import messagebox
import csv
import os

class EventopiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eventopia - Your Gateway to Unforgettable Events")
        self.current_frame = None
        self.frames = []
        self.users_file = 'users.csv'
        self.create_login_screen()

    def create_login_screen(self):
        login_screen = tk.Frame(self.root)
        self.current_frame = login_screen
        login_screen.pack(fill="both", expand=True)

        tk.Label(login_screen, text="Login", font=("Times New Roman", 16)).pack(pady=10)

        tk.Label(login_screen, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(login_screen)
        self.username_entry.pack(pady=5)

        tk.Label(login_screen, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(login_screen, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(login_screen, text="Login", command=self.verify_login)
        login_button.pack(pady=10)

        register_button = tk.Button(login_screen, text="Create Account", command=self.create_register_screen)
        register_button.pack(pady=10)

        self.frames.append(login_screen)

    def verify_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.check_credentials(username, password):
            messagebox.showinfo("Login Successful", "Welcome to Eventopia!")
            self.create_main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def check_credentials(self, username, password):
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username and row[1] == password:
                        return True
        return False

    def create_register_screen(self):
        if self.current_frame:
            self.current_frame.pack_forget()

        register_screen = tk.Frame(self.root)
        self.current_frame = register_screen
        register_screen.pack(fill="both", expand=True)

        tk.Label(register_screen, text="Register", font=("Times New Roman", 16)).pack(pady=10)

        tk.Label(register_screen, text="Username:").pack(pady=5)
        self.new_username_entry = tk.Entry(register_screen)
        self.new_username_entry.pack(pady=5)

        tk.Label(register_screen, text="Password:").pack(pady=5)
        self.new_password_entry = tk.Entry(register_screen, show="*")
        self.new_password_entry.pack(pady=5)

        register_button = tk.Button(register_screen, text="Register", command=self.register_user)
        register_button.pack(pady=10)

        back_button = tk.Button(register_screen, text="Back", command=self.go_back)
        back_button.pack(pady=10)

        self.frames.append(register_screen)

    def register_user(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()

        if new_username and new_password:
            if not self.check_username_exists(new_username):
                with open(self.users_file, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([new_username, new_password])
                messagebox.showinfo("Registration Successful", "Account created successfully!")
                self.go_back()
            else:
                messagebox.showerror("Registration Failed", "Username already exists")
        else:
            messagebox.showerror("Registration Failed", "All fields are required")

    def check_username_exists(self, username):
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username:
                        return True
        return False

    # Existing methods remain unchanged

if __name__ == "__main__":
    root = tk.Tk()
    app = EventopiaApp(root)
    root.mainloop()
