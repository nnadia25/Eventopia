import tkinter as tk
from tkinter import messagebox
import csv
import os
from PIL import Image, ImageTk

class EventopiaApp(tk.Tk):
   """
   Aplikasi Eventopia untuk melihat dan membeli tiket untuk berbagai acara.
   """

   def __init__(self):
       super().__init__()
       self.title("Eventopia - Your Gateway to Unforgettable Events")
       self.geometry("800x600")
       self.current_frame = None
       self.frames = []
       self.users_file = 'users.csv'
       self.create_login_screen()

   def create_login_screen(self):
       """
       Membuat frame login.
       """
       login_screen = tk.Frame(self)
       self.current_frame = login_screen
       login_screen.pack(fill="both", expand=True)

       # Load logo image
       logo_image = Image.open("logo.png")
       logo_photo = ImageTk.PhotoImage(logo_image)
       logo_label = tk.Label(login_screen, image=logo_photo)
       logo_label.image = logo_photo  # Keep a reference to prevent garbage collection
       logo_label.pack(pady=20)

       tk.Label(login_screen, text="Login", font=("Times New Roman", 16)).pack(pady=10)

       tk.Label(login_screen, text="Username:").pack(pady=5)
       self.username_input = tk.Entry(login_screen)
       self.username_input.pack(pady=5)

       tk.Label(login_screen, text="Password:").pack(pady=5)
       self.password_input = tk.Entry(login_screen, show="*")
       self.password_input.pack(pady=5)

       login_button = tk.Button(login_screen, text="Login", command=self.verify_login)
       login_button.pack(pady=10)

       register_button = tk.Button(login_screen, text="Create Account", command=self.create_register_screen)
       register_button.pack(pady=10)

       self.frames.append(login_screen)

   def create_register_screen(self):
       """
       Membuat frame registrasi.
       """
       if self.current_frame:
           self.current_frame.pack_forget()

       register_screen = tk.Frame(self)
       self.current_frame = register_screen
       register_screen.pack(fill="both", expand=True)

       # Load logo image
       logo_image = Image.open("Modern Initial E Logo.png")
       logo_photo = ImageTk.PhotoImage(logo_image)
       logo_label = tk.Label(register_screen, image=logo_photo)
       logo_label.image = logo_photo  # Keep a reference to prevent garbage collection
       logo_label.pack(pady=20)

       tk.Label(register_screen, text="Register", font=("Times New Roman", 16)).pack(pady=10)

       tk.Label(register_screen, text="Username:").pack(pady=5)
       self.new_username_input = tk.Entry(register_screen)
       self.new_username_input.pack(pady=5)

       tk.Label(register_screen, text="Password:").pack(pady=5)
       self.new_password_input = tk.Entry(register_screen, show="*")
       self.new_password_input.pack(pady=5)

       register_button = tk.Button(register_screen, text="Register", command=self.register_user)
       register_button.pack(pady=10)

       back_button = tk.Button(register_screen, text="Back", command=self.go_back)
       back_button.pack(pady=10)

       self.frames.append(register_screen)

   # Existing methods remain unchanged

   def create_main_screen(self):
       """
       Membuat frame utama aplikasi.
       """
       if self.current_frame:
           self.current_frame.pack_forget()

       main_screen = tk.Frame(self)
       self.current_frame = main_screen
       main_screen.pack(fill="both", expand=True)

       # Load logo image
       logo_image = Image.open("logo.png")
       logo_photo = ImageTk.PhotoImage(logo_image)
       logo_label = tk.Label(main_screen, image=logo_photo)
       logo_label.image = logo_photo  # Keep a reference to prevent garbage collection
       logo_label.pack(pady=20)

       welcome_label = tk.Label(main_screen, text="Welcome To Eventopia!", font=("Times New Roman", 16))
       welcome_label.pack(pady=10)

       description_label = tk.Label(main_screen, text=(
           "Our user-friendly platform offers a wide range of events, from music concerts and art festivals "
           "to creative workshops and culinary experiences.\nWith advanced search features and secure payment "
           "options, finding and purchasing tickets has never been easier.\nDiscover detailed information about "
           "each event, including descriptions, schedules, and prices, all in one place.\nUse Eventopia today "
           "and unlock a world of exciting experiences at your fingertips!"
       ), wraplength=400, justify="center")
       description_label.pack(pady=10)

       fun_art_button = tk.Button(main_screen, text="Fun Art", command=self.show_fun_art_event)
       fun_art_button.pack(pady=5)

       cooking_class_button = tk.Button(main_screen, text="Cooking Class", command=self.show_cooking_class_event)
       cooking_class_button.pack(pady=5)

       concert_button = tk.Button(main_screen, text="Konser", command=self.show_concert_event)
       concert_button.pack(pady=5)

       exit_button = tk.Button(main_screen, text="Keluar", command=self.quit)
       exit_button.pack(pady=20)

       self.frames.append(main_screen)

   # Remaining methods remain unchanged

if __name__ == "__main__":
   app = EventopiaApp()
   app.mainloop()