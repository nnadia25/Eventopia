import tkinter as tk
from tkinter import ttk, Label, Button, Radiobutton, messagebox, Radiobutton
import csv
from PIL import Image, ImageTk
import qrcode

root = tk.Tk()
root.title("Yuk Cari Tiket mu Disini!")
root.geometry("1200x670")
root.resizable(False, False)

l1 = Label(root, text="Your Gateway to Unforgettable Events", font=("Perpetua", 16, "bold"), bg='sky blue')
l1.pack(pady=10)

def starter():
    root1 = tk.Toplevel(root)
    root1.title("Pilih Event")
    
    def show():
        root1.destroy()
        root2 = tk.Toplevel(root)
        root2.title("Pilih Event")
        
        def event1():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Blooms and Crafts")
            
            def harga(harga_tiket):
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                
                def konfirmasi():
                    if messagebox.askyesno("Konfirmasi", "Apakah Anda ingin membeli tiket?"):
                        messagebox.showinfo("Lanjut", "Silakan lanjut ke pembayaran.")
                        messagebox.showinfo("SELAMAT", "TIKET ANDA TELAH DIPESAN")
                    else:
                        root4.destroy()
                        starter()
                
                l = Label(root4, text=f"Harga Tiket Anda adalah : Rp. {harga_tiket}")
                l.pack()
                b1 = Button(root4, text="YA", command=konfirmasi)
                b1.pack(side=tk.LEFT, padx=20)
                b2 = Button(root4, text="TIDAK", command=lambda: (root4.destroy(), starter()))
                b2.pack(side=tk.RIGHT, padx=20)
            
            l = Label(root3, text="EVENT YANG TERSEDIA :")
            l.pack()
            Radiobutton(root3, text="Bouquet Crafting Workshop", command=lambda: harga(150000)).pack()
            Radiobutton(root3, text="Clay Painting Class", command=lambda: harga(75000)).pack()
            Radiobutton(root3, text="Beads Crafting Session", command=lambda: harga(50000)).pack()
            Button(root3, text="Back", command=lambda: (root3.destroy(), show())).pack(pady=5)
        
        def event2():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Flavor Fusion Kitchen")
            
            def harga(harga_tiket):
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                
                def konfirmasi():
                    if messagebox.askyesno("Konfirmasi", "Apakah Anda ingin membeli tiket?"):
                        messagebox.showinfo("Lanjut", "Silakan lanjut ke pembayaran.")
                        messagebox.showinfo("SELAMAT", "TIKET ANDA TELAH DIPESAN")
                    else:
                        root4.destroy()
                        starter()
                
                l = Label(root4, text=f"Harga Tiket Anda adalah : Rp. {harga_tiket}")
                l.pack()
                b1 = Button(root4, text="YA", command=konfirmasi)
                b1.pack(side=tk.LEFT, padx=20)
                b2 = Button(root4, text="TIDAK", command=lambda: (root4.destroy(), starter()))
                b2.pack(side=tk.RIGHT, padx=20)
            
            l = Label(root3, text="EVENT YANG TERSEDIA:")
            l.pack()
            Radiobutton(root3, text="Pizza Palooza", command=lambda: harga(150000)).pack()
            Radiobutton(root3, text="SweetBake Cup", command=lambda: harga(150000)).pack()
            Radiobutton(root3, text="CakeCraft Bento", command=lambda: harga(150000)).pack()
            Button(root3, text="Back", command=lambda: (root3.destroy(), event1())).pack(pady=5)
            
        
        def event3():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Suara Sejuta Rasa")
            
            def harga(harga_tiket):
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                
                def konfirmasi():
                    if messagebox.askyesno("Konfirmasi", "Apakah Anda ingin membeli tiket?"):
                        messagebox.showinfo("Lanjut", "Silakan lanjut ke pembayaran.")
                        messagebox.showinfo("SELAMAT", "TIKET ANDA TELAH DIPESAN")
                    else:
                        root4.destroy()
                        starter()
                
                l = Label(root4, text=f"Harga Tiket Anda adalah : Rp. {harga_tiket}")
                l.pack()
                b1 = Button(root4, text="YA", command=konfirmasi)
                b1.pack(side=tk.LEFT, padx=20)
                b2 = Button(root4, text="TIDAK", command=lambda: (root4.destroy(), starter()))
                b2.pack(side=tk.RIGHT, padx=20)
               
            l = Label(root3, text="EVENT YANG TERSEDIA:")
            l.pack()
            Radiobutton(root3, text="Day 1 (Yura Yunita, Raisa Anggiani, Arash Buana)", command=lambda: harga(200000)).pack()
            Radiobutton(root3, text="Day 2 (Gangga, Nadhif Basalamah, Tulus)", command=lambda: harga(200000)).pack()
            Button(root3, text="Back", command=lambda: (root3.destroy(), event1())).pack(pady=5)

        l3 = Label(root2, text="PILIH EVENT:")
        l3.pack()
        Button(root2, text="Blooms and Crafts", command=event1).pack()
        Button(root2, text="Flavor Fusion Kitchen", command=event2).pack()
        Button(root2, text="Suara Sejuta Rasa", command=event3).pack()
        Button(root2, text='EXIT', bg='sky blue', command=root2.destroy).pack()

    show()

def pembayaran():
    def submit_form():
        nama = name_entry.get().strip()
        email = email_entry.get().strip()
        tipe_kartu = card_type_combobox.get().strip()
        nomor_rekening = card_no_entry.get().strip()
        nomor_hp = phone_no_entry.get().strip()
        jumlah_pembayaran = jml_pembayaran_entry.get().strip()  

        if not (nama and email and tipe_kartu and nomor_rekening and nomor_hp and jumlah_pembayaran):
            messagebox.showerror("Error", "Harap isi semua kolom yang diperlukan!")
            return

        if not (nomor_rekening.isdigit() and nomor_hp.isdigit() and jumlah_pembayaran.isdigit()):
            messagebox.showerror("Error", "Nomor Rekening, nomor HP, dan jumlah pembayaran hanya boleh berisi angka!")
            return

        with open('database_pembayaran.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nama", "Email", "Tipe Kartu", "Nomor Rekening", "Nomor HP", "Jumlah Pembayaran"])
            writer.writerow([nama, email, tipe_kartu, nomor_rekening, nomor_hp, jumlah_pembayaran])
        
        messagebox.showinfo("Sukses", "Pembayaran sudah berhasil dan telah disimpan!")
        generate_qr_code(nama, email, tipe_kartu, nomor_rekening, nomor_hp, jumlah_pembayaran)

        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        card_no_entry.delete(0, tk.END)
        phone_no_entry.delete(0, tk.END)
        jml_pembayaran_entry.delete(0, tk.END)
        card_type_combobox.set("Pilih Tipe Kartu")

    def generate_qr_code(nama, email, tipe_kartu, nomor_rekening, nomor_hp, jumlah_pembayaran):
        data = f"Nama: {nama}\nEmail: {email}\nTipe Kartu: {tipe_kartu}\nNomor Rekening: {nomor_rekening}\nNomor HP: {nomor_hp}\nJumlah Pembayaran: {jumlah_pembayaran}"
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("tiket_qr_code.png")

    root_pembayaran = tk.Toplevel(root)
    root_pembayaran.title("Formulir Pembayaran")

    main_frame = ttk.Frame(root_pembayaran, padding="20")
    main_frame.grid(row=0, column=0)

    ttk.Label(main_frame, text="Data Pribadi", font=("Perpetua", 12)).grid(row=0, column=0, columnspan=2, pady=(0, 5), sticky="")

    ttk.Label(main_frame, text="Nama").grid(row=1, column=0, sticky="e")
    name_entry = ttk.Entry(main_frame)
    name_entry.grid(row=1, column=1, sticky="w")

    ttk.Label(main_frame, text="Email ").grid(row=2, column=0, sticky="e")
    email_entry = ttk.Entry(main_frame)
    email_entry.grid(row=2, column=1, sticky="w")

    ttk.Label(main_frame, text="Tipe Kartu").grid(row=3, column=0, sticky="e")
    card_types = ["Mandiri", "BNI", "BCA", "BRI", "Bank Jateng"]
    card_type_combobox = ttk.Combobox(main_frame, values=card_types)
    card_type_combobox.grid(row=3, column=1, sticky="w")

    ttk.Label(main_frame, text="Nomor Rekening *").grid(row=4, column=0, sticky="e")
    card_no_entry = ttk.Entry(main_frame)
    card_no_entry.grid(row=4, column=1, sticky="w")

    ttk.Label(main_frame, text="Nomor HP").grid(row=5, column=0, sticky="e")
    phone_no_entry = ttk.Entry(main_frame)
    phone_no_entry.grid(row=5, column=1, sticky="w")

    ttk.Label(main_frame, text="Total Pembayaran").grid(row=6, column=0, sticky="e")
    jml_pembayaran_entry = ttk.Entry(main_frame)
    jml_pembayaran_entry.grid(row=6, column=1, sticky="w")

    submit_button = ttk.Button(main_frame, text="Bayar", command=submit_form)
    submit_button.grid(row=7, column=0, columnspan=2, pady=(20, 0))

image_path = r'C:\Users\ASUS\Documents\21 Prokom\Home.jpeg'
original_image = Image.open(image_path)
resized_image = original_image.resize((1200, 600), Image.LANCZOS)
im = ImageTk.PhotoImage(resized_image)

i = Label(root, image=im)
i.image = im  
i.place(x=0, y=50) 

#Button
button_continue = Button(root, text="Beli Tiket", bg='White', font=("Perpetua", 12), compound="left", command=starter)
button_continue.place(x=330, y=440, width=150, height=50) 

b1 = Button(root, text="Pembayaran", bg='light blue', font=("Perpetua", 12), compound="left", command=pembayaran)
b1.place(x=530, y=440, width=150, height=50)  

button_quit = Button(root, text='EXIT', bg='white', font=("Perpetua", 12), compound="left", command=root.quit)
button_quit.place(x=730, y=440, width=150, height=50)  

root.mainloop()

