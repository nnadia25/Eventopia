import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ast

# Fungsi untuk beralih ke jendela login
def switch_to_login():
    login_frame.tkraise()

# Fungsi untuk beralih ke jendela sign up
def switch_to_signup():
    signup_frame.tkraise()

# Jendela utama
root = tk.Tk()
root.title('Login & Signup')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Fungsi untuk login
def signin():
    username = user.get()
    password = code.get()

    try:
        with open('datasheet.txt', 'r') as file:
            data = file.read()
            users = ast.literal_eval(data)

        if username in users and users[username] == password:
            screen = tk.Toplevel(root)
            screen.title("Aplikasi")
            screen.geometry("925x500+300+200")
            screen.config(bg='white')
            tk.Label(screen, text='Hello, Everyone!', bg="#fff", font=('Perpetua', 50, 'bold')).pack(expand=True)
        else:
            messagebox.showerror('Invalid', 'Username atau password salah')
    except FileNotFoundError:
        messagebox.showerror('Invalid', 'Data pengguna tidak ditemukan')

# Fungsi untuk signup
def signup():
    username = user_signup.get()
    password = code_signup.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            with open('datasheet.txt', 'r+') as file:
                data = file.read()
                try:
                    users = ast.literal_eval(data)
                except:
                    users = {}

                if username in users:
                    messagebox.showerror('Invalid', 'Username sudah ada')
                else:
                    users[username] = password
                    file.seek(0)
                    file.truncate()
                    file.write(str(users))
                    messagebox.showinfo('Signup', 'Berhasil mendaftar')
                    switch_to_login()

        except FileNotFoundError:
            with open('datasheet.txt', 'w') as file:
                users = {username: password}
                file.write(str(users))
                messagebox.showinfo('Signup', 'Berhasil mendaftar')
                switch_to_login()
    else:
        messagebox.showerror('Invalid', 'Password tidak cocok')

# Fungsi untuk mengubah visibilitas password
def toggle_password(entry, var):
    if var.get():
        entry.config(show='')
    else:
        entry.config(show='*')

# Memuat gambar menggunakan PIL
image_path = r"C:\Users\DELL\.vscode\EVENTOPIA\Eventopia\Halaman Login.jpeg"
try:
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((925, 500), Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(pil_image)
except Exception as e:
    messagebox.showerror("Error", f"Gambar tidak ditemukan: {e}")
    root.destroy()

# Label Latar Belakang
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame Login
login_frame = tk.Frame(root, bg="white")

heading = tk.Label(login_frame, text='Sign in', fg='#57a1f8', bg='white', font=('Perpetua', 23, 'bold'))
heading.place(x=125, y=17)

user = tk.Entry(login_frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', lambda e: user.delete(0, 'end') if user.get() == 'Username' else None)
user.bind('<FocusOut>', lambda e: user.insert(0, 'Username') if user.get() == '' else None)

tk.Frame(login_frame, width=295, height=2, bg='black').place(x=25, y=107)

code = tk.Entry(login_frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11), show='*')
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', lambda e: code.delete(0, 'end') if code.get() == 'Password' else None)
code.bind('<FocusOut>', lambda e: code.insert(0, 'Password') if code.get() == '' else None)

tk.Frame(login_frame, width=295, height=2, bg='black').place(x=25, y=177)

show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(login_frame, text='Show Password', bg='white', fg='black', font=('Perpetua', 9), variable=show_password_var, command=lambda: toggle_password(code, show_password_var))
show_password_check.place(x=30, y=180)

tk.Button(login_frame, width=39, pady=7, text='Sign In', bg="#57a1f8", fg='white', border=0, command=signin).place(x=35, y=220)
tk.Label(login_frame, text="Belum punya akun?", fg='black', bg='white', font=('Perpetua', 9)).place(x=75, y=270)
tk.Button(login_frame, width=6, text="Sign Up", border=0, cursor="hand2", fg='#57a1f8', bg='white', command=switch_to_signup).place(x=200, y=269)

# Frame Signup
signup_frame = tk.Frame(root, bg="white")

heading = tk.Label(signup_frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Perpetua', 23, 'bold'))
heading.place(x=125, y=17)

user_signup = tk.Entry(signup_frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11))
user_signup.place(x=30, y=80)
user_signup.insert(0, 'Username')
user_signup.bind('<FocusIn>', lambda e: user_signup.delete(0, 'end') if user_signup.get() == 'Username' else None)
user_signup.bind('<FocusOut>', lambda e: user_signup.insert(0, 'Username') if user_signup.get() == '' else None)

tk.Frame(signup_frame, width=295, height=2, bg='black').place(x=25, y=107)

code_signup = tk.Entry(signup_frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11), show='*')
code_signup.place(x=30, y=150)
code_signup.insert(0, 'password')
code_signup.bind('<FocusIn>', lambda e: code_signup.delete(0, 'end') if code_signup.get() == 'password' else None)
code_signup.bind('<FocusOut>', lambda e: code_signup.insert(0, 'password') if code_signup.get() == '' else None)

tk.Frame(signup_frame, width=295, height=2, bg='black').place(x=25, y=177)

confirm_code = tk.Entry(signup_frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11), show='*')
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'confirm password')
confirm_code.bind('<FocusIn>', lambda e: confirm_code.delete(0, 'end') if confirm_code.get() == 'confirm password' else None)
confirm_code.bind('<FocusOut>', lambda e: confirm_code.insert(0, 'confirm password') if confirm_code.get() == '' else None)

tk.Frame(signup_frame, width=295, height=2, bg='black').place(x=25, y=247)

show_signup_password_var = tk.BooleanVar()
show_signup_password_check = tk.Checkbutton(signup_frame, text='Show Password', bg='white', fg='black', font=('Perpetua', 9), variable=show_signup_password_var, command=lambda: toggle_password(code_signup, show_signup_password_var))
show_signup_password_check.place(x=30, y=250)

show_confirm_password_var = tk.BooleanVar()
show_confirm_password_check = tk.Checkbutton(signup_frame, text='Show Confirm Password', bg='white', fg='black', font=('Perpetua', 9), variable=show_confirm_password_var, command=lambda: toggle_password(confirm_code, show_confirm_password_var))
show_confirm_password_check.place(x=160, y=250)

tk.Button(signup_frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=290)
tk.Label(signup_frame, text='Sudah punya akun?', fg='black', bg='white', font=('Perpetua', 10)).place(x=90, y=340)
tk.Button(signup_frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=switch_to_login).place(x=200, y=340)

# Tempatkan frame login dan signup pada posisi yang sama
login_frame.place(x=550, y=85, width=350, height=350)
signup_frame.place(x=550, y=65, width=350, height=400)

# Tampilkan frame login pada awal
login_frame.tkraise()

root.mainloop()
