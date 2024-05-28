from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Membuat jendela utama
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    if username == "admin" and password == "1234":
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg='white')

        Label(screen, text='Hello, Everyone!', bg="#fff", font=('Perpetua', 50, 'bold')).pack(expand=True)

    elif username != "admin" and password != "1234":
        messagebox.showerror('Invalid', 'Invalid username and password')
    elif password != "1234":
        messagebox.showerror('Invalid', 'Invalid password')
    elif username != "admin":
        messagebox.showerror('Invalid', 'Invalid username')


# Memuat gambar menggunakan PIL
image_path = r"C:\Users\ASUS\Documents\21 Prokom\Halaman Login.jpeg"
pil_image = Image.open(image_path)

# Mengubah ukuran gambar agar sesuai dengan jendela
pil_image = pil_image.resize((1000, 580), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(pil_image)

# Menampilkan gambar latar belakang di tkinter
bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Membuat frame untuk form login dengan latar belakang transparan
frame = Frame(root, bg="white", bd=0)
frame.place(x=550, y=70, width=350, height=350)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Perpetua', 23, 'bold'))
heading.place(x=125, y=17)

def on_enter_user(e):
    user.delete(0, 'end')

def on_leave_user(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_user)
user.bind('<FocusOut>', on_leave_user)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter_code(e):
    code.delete(0, 'end')

def on_leave_code(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11), show='*')
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_code)
code.bind('<FocusOut>', on_leave_code)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign In', bg="#57a1f8", fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Perpetua', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text="Sign Up", border=0, cursor="hand2", fg='#57a1f8', bg='white')
sign_up.place(x=200, y=269)

root.mainloop()
