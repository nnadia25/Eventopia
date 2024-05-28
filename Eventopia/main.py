import tkinter as tk
from tkinter import ttk, Label, Button, Radiobutton, messagebox, Entry
import csv
from PIL import Image, ImageTk, ImageDraw, ImageFont

root = tk.Tk()
root.title("Yuk Cari Tiketmu Disini!")
root.geometry("1204x670")
root.resizable(False, False)

# Stack untuk melacak riwayat halaman
history_stack = []

def starter():
    root1 = tk.Toplevel(root)
    root1.title("Pilih Event")
    root1.geometry("300x200")
    root1.resizable(False, False)
    history_stack.append(root1)  # Tambahkan halaman ke stack

    def show():
        root1.destroy()
        root2 = tk.Toplevel(root)
        root2.title("Pilih Event")
        root2.geometry("300x200")
        root2.resizable(False, False)
        history_stack.append(root2)  # Tambahkan halaman ke stack

        def event1():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Blooms and Crafts")
            root3.geometry("300x200")
            root3.resizable(False, False)
            history_stack.append(root3)  # Tambahkan halaman ke stack

            def harga(harga_tiket, nama_event):
                root3.destroy()
                tagihan(nama_event, harga_tiket)

            l = Label(root3, text="EVENT YANG TERSEDIA :")
            l.pack(pady=10)
            Radiobutton(root3, text="Bouquet Crafting Workshop", command=lambda: harga(150000, "Bouquet Crafting Workshop")).pack()
            Radiobutton(root3, text="Clay Painting Class", command=lambda: harga(75000, "Clay Painting Class")).pack()
            Radiobutton(root3, text="Beads Crafting Session", command=lambda: harga(50000, "Beads Crafting Session")).pack()
            Button(root3, text="Back", command=navigate_back).pack(pady=10)

        def event2():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Flavor Fusion Kitchen")
            root3.geometry("300x200")
            root3.resizable(False, False)
            history_stack.append(root3)  # Tambahkan halaman ke stack

            def harga(harga_tiket, nama_event):
                root3.destroy()
                tagihan(nama_event, harga_tiket)

            l = Label(root3, text="EVENT YANG TERSEDIA:")
            l.pack(pady=10)
            Radiobutton(root3, text="Pizza Palooza", command=lambda: harga(150000, "Pizza Palooza")).pack()
            Radiobutton(root3, text="SweetBake Cup", command=lambda: harga(150000, "SweetBake Cup")).pack()
            Radiobutton(root3, text="CakeCraft Bento", command=lambda: harga(150000, "CakeCraft Bento")).pack()
            Button(root3, text="Back", command=navigate_back).pack(pady=10)

        def event3():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Suara Sejuta Rasa")
            root3.geometry("300x200")
            root3.resizable(False, False)
            history_stack.append(root3)  # Tambahkan halaman ke stack

            def harga(harga_tiket, nama_event):
                root3.destroy()
                tagihan(nama_event, harga_tiket)

            l = Label(root3, text="EVENT YANG TERSEDIA:")
            l.pack(pady=10)
            Radiobutton(root3, text="Day 1 (Yura Yunita, Raisa Anggiani, Arash Buana)", command=lambda: harga(200000, "Day 1 (Yura Yunita, Raisa Anggiani, Arash Buana)")).pack()
            Radiobutton(root3, text="Day 2 (Gangga, Nadhif Basalamah, Tulus)", command=lambda: harga(200000, "Day 2 (Gangga, Nadhif Basalamah, Tulus)")).pack()
            Button(root3, text="Back", command=navigate_back).pack(pady=10)

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
    root5.geometry("300x350")
    root5.resizable(False, False)
    history_stack.append(root5)  # Tambahkan halaman ke stack

    def calculate_total():
        try:
            jumlah_tiket = int(jumlah_entry.get())
            total_harga = jumlah_tiket * harga_tiket
            l4.config(text=f"Total Harga: Rp. {total_harga}")
            proceed_button.config(state='normal')  # Aktifkan tombol setelah perhitungan berhasil
        except ValueError:
            messagebox.showerror("Error", "Jumlah tiket harus berupa angka!")

    def proceed_to_payment():
        try:
            jumlah_tiket = int(jumlah_entry.get())
            pembayaran(nama_event, harga_tiket, jumlah_tiket)
        except ValueError:
            messagebox.showerror("Error", "Jumlah tiket harus valid sebelum melanjutkan!")

    l1 = Label(root5, text="Detail Tagihan")
    l1.pack(pady=10)
    l2 = Label(root5, text=f"Event: {nama_event}")
    l2.pack(pady=5)
    l3 = Label(root5, text=f"Harga Tiket: Rp. {harga_tiket}")
    l3.pack(pady=5)

    Label(root5, text="Jumlah Tiket:").pack(pady=5)
    jumlah_entry = Entry(root5)
    jumlah_entry.pack(pady=5)

    l4 = Label(root5, text="Total Harga: Rp. 0")
    l4.pack(pady=5)

    b1 = Button(root5, text="Hitung Total", command=calculate_total)
    b1.pack(pady=10)
    proceed_button = Button(root5, text="Lanjut ke Pembayaran", command=proceed_to_payment, state='disabled')
    proceed_button.pack(pady=10)
    b3 = Button(root5, text="Back", command=navigate_back)
    b3.pack()

def pembayaran(nama_event, harga_tiket, jumlah_tiket):
    def submit_form():
        nama = name_entry.get().strip()
        email = email_entry.get().strip()
        tipe_kartu = card_type_combobox.get().strip()
        nomor_rekening = card_no_entry.get().strip()
        nomor_hp = phone_no_entry.get().strip()
        total_pembayaran = harga_tiket * jumlah_tiket

        if not (nama and email and tipe_kartu and nomor_rekening and nomor_hp):
            messagebox.showerror("Error", "Harap isi semua kolom yang diperlukan!")
            return

        if not (nomor_rekening.isdigit() and nomor_hp.isdigit()):
            messagebox.showerror("Error", "Nomor Rekening dan nomor HP hanya boleh berisi angka!")
            return

        with open('database_pembayaran.csv', mode='a', newline='') as file:  # Menggunakan mode 'a' untuk menambahkan data
            writer = csv.writer(file)
            writer.writerow(["Nama", "Email", "Tipe Kartu", "Nomor Rekening", "Nomor HP", "Jumlah Tiket", "Total Pembayaran"])
            writer.writerow([nama, email, tipe_kartu, nomor_rekening, nomor_hp, jumlah_tiket, total_pembayaran])
        
        messagebox.showinfo("Sukses", "Pembayaran sudah berhasil dan telah disimpan!")
        generate_e_ticket(nama, email, nama_event, harga_tiket, jumlah_tiket)

    def generate_e_ticket(nama, email, nama_event, harga_tiket, jumlah_tiket):
        filename = "e_ticket.png"
        ticket_img = Image.new('RGB', (600, 300), color='white')
        draw = ImageDraw.Draw(ticket_img)

        font_path = "arial.ttf"  # Sesuaikan path font yang diinginkan
        font = ImageFont.truetype(font_path, 16)

        draw.text((10, 10), "E-Ticket", font=font, fill=(0, 0, 0))
        draw.text((10, 30), f"Nama: {nama}", font=font, fill=(0, 0, 0))
        draw.text((10, 50), f"Event: {nama_event}", font=font, fill=(0, 0, 0))
        draw.text((10, 70), f"Harga Tiket: {harga_tiket}", font=font, fill=(0, 0, 0))
        draw.text((10, 90), f"Jumlah Tiket: {jumlah_tiket}", font=font, fill=(0, 0, 0))
        draw.text((10, 110), f"Total Pembayaran: {harga_tiket * jumlah_tiket}", font=font, fill=(0, 0, 0))

        ticket_img.save(filename)

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
    root_pembayaran.geometry("400x400")
    root_pembayaran.resizable(False, False)
    history_stack.append(root_pembayaran)  # Tambahkan halaman ke stack

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
    total_pembayaran = harga_tiket * jumlah_tiket
    total_pembayaran_entry = ttk.Entry(main_frame)
    total_pembayaran_entry.grid(row=6, column=1, sticky="w")
    total_pembayaran_entry.insert(0, str(total_pembayaran))
    total_pembayaran_entry.config(state='readonly')

    submit_button = ttk.Button(main_frame, text="Bayar", command=submit_form)
    submit_button.grid(row=7, column=0, columnspan=2, pady=(20, 0))

    back_button = ttk.Button(main_frame, text="Back", command=navigate_back)
    back_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))

image_path = r'/Users/cendikiawisnuputranto/Eventopia/Eventopia/Home.jpeg'
original_image = Image.open(image_path)
resized_image = original_image.resize((1200, 600), Image.LANCZOS)
im = ImageTk.PhotoImage(resized_image)

i = Label(root, image=im)
i.image = im  
i.place(x=0, y=50) 

# Button
b1 = Button(root, text="Beli Tiket", bg='light blue', font=("Perpetua", 12), compound="left", command=starter)
b1.place(x=530, y=440, width=150, height=50)  

def navigate_back():
    if history_stack:
        current_window = history_stack.pop()
        current_window.destroy()
        if history_stack:
            previous_window = history_stack[-1]
            previous_window.deiconify()

root.mainloop()