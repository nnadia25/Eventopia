from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("Sign Up")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False, False)

def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            with open('datasheet.txt', 'r+') as file:
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.seek(0)
                file.truncate(0)
                file.write(str(r))
                messagebox.showinfo('Signup', 'Successfully signed up')

        except (FileNotFoundError, SyntaxError):
            with open('datasheet.txt', 'w') as file:
                pp = str({username: password})
                file.write(pp)
                messagebox.showinfo('Signup', 'Successfully signed up')
    else:
        messagebox.showerror('Invalid', 'Both Passwords should match')

def on_enter_user(e):
    if user.get() == 'Username':
        user.delete(0, 'end')
def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'Username')

def on_enter_code(e):
    if code.get() == 'password':
        code.delete(0, 'end')
def on_leave_code(e):
    if code.get() == '':
        code.insert(0, 'password')

def on_enter_confirm_code(e):
    if confirm_code.get() == 'confirm password':
        confirm_code.delete(0, 'end')
def on_leave_confirm_code(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'confirm password')

img = PhotoImage(file=r'C:\Users\ASUS\Documents\21 Prokom\Halaman Login.jpeg')
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg="white")
frame.place(x=480, y=50)

heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Perpetua', 23, 'bold'))
heading.place(x=125, y=17)

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11))
code.place(x=30, y=150)
code.insert(0, 'password')
code.bind("<FocusIn>", on_enter_code)
code.bind("<FocusOut>", on_leave_code)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

confirm_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Perpetua', 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'confirm password')
confirm_code.bind("<FocusIn>", on_enter_confirm_code)
confirm_code.bind("<FocusOut>", on_leave_confirm_code)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
Label(frame, text='I have an account', fg='black', bg='white', font=('Perpetua', 9)).place(x=90, y=340)

signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8')
signin.place(x=200, y=340)

window.mainloop()
