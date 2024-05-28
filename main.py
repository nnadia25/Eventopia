import tkinter as tk
from tkinter import ttk, Label, Button, Radiobutton, messagebox
import csv
from PIL import Image, ImageTk, ImageDraw, ImageFont

root = tk.Tk()
root.title("Yuk Cari Tiketmu Disini!")
root.geometry("1204x670")
root.resizable(False, False)

def starter():
    root1 = tk.Toplevel(root)
    root1.title("Pilih Event")
    root1.geometry("300x200")
    root1.resizable(False, False)
    
    def show():
        root1.destroy()
        root2 = tk.Toplevel(root)
        root2.title("Pilih Event")
        root2.geometry("300x200")
        root2.resizable(False, False)
        
        def event1():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Blooms and Crafts")
            root3.geometry("300x200")
            root3.resizable(False, False)
            
            def harga(harga_tiket, nama_event):
                root3.destroy()
                tagihan(nama_event, harga_tiket)
            
            l = Label(root3, text="EVENT YANG TERSEDIA :")
            l.pack(pady=10)
            Radiobutton(root3, text="Bouquet Crafting Workshop", command=lambda: harga(150000, "Bouquet Crafting Workshop")).pack()
            Radiobutton(root3, text="Clay Painting Class", command=lambda: harga(75000, "Clay Painting Class")).pack()
            Radiobutton(root3, text="Beads Crafting Session", command=lambda: harga(50000, "Beads Crafting Session")).pack()
            Button(root3, text="Back", command=lambda: (root3.destroy(), show())).pack(pady=10)
        
        def event2():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Flavor Fusion Kitchen")
            root3.geometry("300x200")
            root3.resizable(False, False)
            
            def harga(harga_tiket, nama_event):
                root3.destroy()
                tagihan(nama_event, harga_tiket)
            
            l = Label(root3, text="EVENT YANG TERSEDIA:")
            l.pack(pady=10)
            Radiobutton(root3, text="Pizza Palooza", command=lambda: harga(150000, "Pizza Palooza")).pack()
            Radiobutton(root3, text="SweetBake Cup", command=lambda: harga(150000, "SweetBake Cup")).pack()
            Radiobutton(root3, text="CakeCraft Bento", command=lambda: harga(150000, "CakeCraft Bento")).pack()
            Button(root3, text="Back", command=lambda: (root3.destroy(), show())).pack(pady=10)
        
        def event3():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Suara Sejuta Rasa")
            root3.geometry("300x200")
            root3.resizable(False, False)
            
            def harga(harga_tiket, nama_event):
                root3.destroy()
                tagihan(nama_event, harga_tiket)
            
            l = Label(root3, text="EVENT YANG TERSEDIA:")
            l.pack(pady=10)
            Radiobutton(root3, text="Day 1 (Yura Yunita, Raisa Anggiani, Arash Buana)", command=lambda: harga(200000, "Day 1 (Yura Yunita, Raisa Anggiani, Arash Buana)")).pack()
            Radiobutton(root3, text="Day 2 (Gangga, Nadhif Basalamah, Tulus)", command=lambda: harga(200000, "Day 2 (Gangga, Nadhif Basalamah, Tulus)")).pack()
            Button(root3, text="Back", command=lambda: (root3.destroy(), show())).pack(pady=10)

        l3 = Label(root2, text="PILIH EVENT:")
        l3.pack(pady=10)
        Button(root2, text="Blooms and Crafts", command=event1).pack(pady=5)
        Button(root2, text="Flavor Fusion Kitchen", command=event2).pack(pady=5)
        Button(root2, text="Suara Sejuta Rasa", command=event3).pack(pady=5)
        Button(root2, text='EXIT', bg='sky blue', command=root2.destroy).pack(pady=15)

    show()

def tagihan(nama_event, harga_tiket):
    root5 = tk.Toplevel(root)
    root5.title("Tagihan Tiket")
    root5.geometry("300x200")
    root5.resizable(False, False)

    l1 = Label(root5, text="Detail Tagihan")
    l1.pack(pady=10)
    l2 = Label(root5, text=f"Event: {nama_event}")
    l2.pack(pady=5)
    l3 = Label(root5, text=f"Harga Tiket: Rp. {harga_tiket}")
    l3.pack(pady=5)
    b1 = Button(root5, text="Lanjut ke Pembayaran", command=lambda: (root5.destroy(), pembayaran(nama_event, harga_tiket)))
    b1.pack(pady=20)

def pembayaran(nama_event, harga_tiket):
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

        with open('database_pembayaran.csv', mode='a', newline='') as file:  # Menggunakan mode 'a' untuk menambahkan data
            writer = csv.writer(file)
            writer.writerow(["Nama", "Email", "Tipe Kartu", "Nomor Rekening", "Nomor HP", "Jumlah Pembayaran"])
            writer.writerow([nama, email, tipe_kartu, nomor_rekening, nomor_hp, jumlah_pembayaran])
        
        messagebox.showinfo("Sukses", "Pembayaran sudah berhasil dan telah disimpan!")
        generate_e_ticket(nama, email, nama_event, harga_tiket)

        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        card_no_entry.delete(0, tk.END)
        phone_no_entry.delete(0, tk.END)
        jml_pembayaran_entry.delete(0, tk.END)
        card_type_combobox.set("Pilih Tipe Kartu")

    def generate_e_ticket(nama, email, nama_event, harga_tiket):
        filename = f"Tiket_{nama_event.replace(' ', '_')}.jpeg"

        ticket_img = Image.new("RGB", (400, 200), (255, 255, 255))
        draw = ImageDraw.Draw(ticket_img)
        font = ImageFont.load_default()

        draw.text((10, 10), f"Nama: {nama}", font=font, fill=(0, 0, 0))
        draw.text((10, 30), f"Email: {email}", font=font, fill=(0, 0, 0))
        draw.text((10, 50), f"Event: {nama_event}", font=font, fill=(0, 0, 0))
        draw.text((10, 70), f"Harga Tiket: Rp. {harga_tiket}", font=font, fill=(0, 0, 0))

        ticket_img.save(filename)

        show_ticket(filename)

    def show_ticket(filename):
        ticket_window = tk.Toplevel(root)
        ticket_window.title("E-Ticket")
        ticket_frame = ttk.Frame(ticket_window, padding="20")
        ticket_frame.grid(row=0, column=0)

        ticket_img = Image.open(filename)
        ticket_img_resized = ticket_img.resize((600, 400), Image.LANCZOS)
        ticket_image = ImageTk.PhotoImage(ticket_img_resized)

        image_label = ttk.Label(ticket_frame, image=ticket_image)
        image_label.image = ticket_image
        image_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        ttk.Button(ticket_frame, text="Tutup", command=ticket_window.destroy).grid(row=1, column=0, columnspan=2, pady=(10, 0))

    root_pembayaran = tk.Toplevel(root)
    root_pembayaran.title("Formulir Pembayaran")
    root_pembayaran.geometry("400x300")
    root_pembayaran.resizable(False, False)

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

    jml_pembayaran_entry.insert(0, str(harga_tiket))

    submit_button = ttk.Button(main_frame, text="Bayar", command=submit_form)
    submit_button.grid(row=7, column=0, columnspan=2, pady=(20, 0))

image_path = r'C:\Users\DELL\.vscode\EVENTOPIA\Eventopia\Home.jpeg'
original_image = Image.open(image_path)
resized_image = original_image.resize((1200, 600), Image.LANCZOS)
im = ImageTk.PhotoImage(resized_image)

i = Label(root, image=im)
i.image = im  
i.place(x=0, y=50) 

# Button

b1 = Button(root, text="Beli Tiket", bg='light blue', font=("Perpetua", 12), compound="left", command=starter)
b1.place(x=530, y=440, width=150, height=50)  

root.mainloop()

