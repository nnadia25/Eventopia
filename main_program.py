import tkinter as tk
from tkinter import ttk, Label, Button, Radiobutton, messagebox, Entry
from PIL import Image, ImageTk, ImageDraw
from PIL import ImageFont

root = tk.Tk()
root.title("Yuk Cari Tiketmu Disini!")
root.geometry("1204x670")
root.resizable(False, False)

# Stack untuk melacak riwayat halaman
history_stack = []

def start_main_program():
    root1 = tk.Toplevel(root)
    root1.title("Pilih Event")
    root1.geometry("300x200")
    root1.resizable(False, False)
    history_stack.append(root1)

    def show():
        root1.destroy()
        root2 = tk.Toplevel(root)
        root2.title("Pilih Event")
        root2.geometry("300x200")
        root2.resizable(False, False)
        history_stack.append(root2)

        def event1():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Blooms and Crafts")
            root3.geometry("300x200")
            root3.resizable(False, False)
            history_stack.append(root3)

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
            history_stack.append(root3)

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
            history_stack.append(root3)

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
    history_stack.append(root5)

    def calculate_total():
        try:
            jumlah_tiket = int(jumlah_entry.get())
            total_harga = jumlah_tiket * harga_tiket
            l4.config(text=f"Total Harga: Rp. {total_harga}")
            proceed_button.config(state='normal')
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

class PaymentApp:
    def __init__(self, root, nama_event, harga_tiket, jumlah_tiket):
        self.root = root
        self.root.title("Metode Pembayaran")
        self.nama_event = nama_event
        self.harga_tiket = harga_tiket
        self.jumlah_tiket = jumlah_tiket

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 320
        window_height = 320
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.setup_payment_page()

    def setup_payment_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label_data_pembayaran = tk.Label(self.root, text="Data Pembayaran", font=("Perpetua", 15))
        self.label_data_pembayaran.pack(pady=10)

        self.label_nama = tk.Label(self.root, text="Nama Pembeli :", font=("Perpetua", 12))
        self.label_nama.pack(anchor="w", padx=10)

        self.entry_nama = tk.Entry(self.root, font=("Perpetua", 12))
        self.entry_nama.pack(padx=10, pady=5)

        self.label_email = tk.Label(self.root, text="Email :", font=("Perpetua", 12))
        self.label_email.pack(anchor="w", padx=10)

        self.entry_email = tk.Entry(self.root, font=("Perpetua", 12))
        self.entry_email.pack(padx=10, pady=5)

        self.label_total = tk.Label(self.root, text="Total Pembelian :", font=("Perpetua", 12))
        self.label_total.pack(anchor="w", padx=10)

        self.entry_total = tk.Entry(self.root, font=("Perpetua", 12))
        self.entry_total.insert(0, f"{self.harga_tiket * self.jumlah_tiket}")
        self.entry_total.config(state='readonly')
        self.entry_total.pack(padx=10, pady=5)

        self.label_bank = tk.Label(self.root, text="Nama Bank :", font=("Perpetua", 12))
        self.label_bank.pack(anchor="w", padx=10)

        self.bank_var = tk.StringVar(self.root)
        self.bank_var.set("Pilih Bank :")
        self.bank_options = ["BCA", "Mandiri", "BNI", "BRI", "Bank Jateng"]
        self.bank_menu = tk.OptionMenu(self.root, self.bank_var, *self.bank_options)
        self.bank_menu.config(font=("Perpetua", 12))
        self.bank_menu.pack(padx=10, pady=5)

        self.finish_button = tk.Button(self.root, text="Selesai", command=self.finish_payment, bg="light blue", fg="black", font=("Perpetua", 12))
        self.finish_button.pack(padx=10, pady=5)

    def finish_payment(self):
        total_pembelian = self.entry_total.get()
        nama_bank = self.bank_var.get()
        nama_pembeli = self.entry_nama.get()
        email_pembeli = self.entry_email.get()

        if not nama_pembeli:
            messagebox.showerror("Input Error", "Nama pembeli tidak boleh kosong.")
            return

        if not email_pembeli:
            messagebox.showerror("Input Error", "Email tidak boleh kosong.")
            return

        if not total_pembelian:
            messagebox.showerror("Input Error", "Total pembelian tidak boleh kosong.")
            return

        if nama_bank == "Pilih Bank":
            messagebox.showerror("Input Error", "Silakan pilih nama bank.")
            return

        try:
            total_pembelian = float(total_pembelian)
            self.show_success_page(total_pembelian, nama_bank, nama_pembeli, email_pembeli)
        except ValueError:
            messagebox.showerror("Input Error", "Total pembelian harus berupa angka.")

    def show_success_page(self, total_pembelian, nama_bank, nama_pembeli, email_pembeli):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label_success = tk.Label(self.root, text="Pembayaran Berhasil", font=("Perpetua", 15))
        self.label_success.pack(pady=20)

        info_text = f"Total Pembelian: Rp. {total_pembelian}\nBank: {nama_bank}\nNama: {nama_pembeli}\nEmail: {email_pembeli}"
        self.label_info = tk.Label(self.root, text=info_text, font=("Perpetua", 12))
        self.label_info.pack(pady=10)

        self.print_button = tk.Button(self.root, text="Cetak E-Ticket", command=lambda: self.print_eticket(nama_pembeli, email_pembeli), bg="light blue", fg="black", font=("Perpetua", 12))
        self.print_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="light blue", fg="black", font=("Perpetua", 12))
        self.exit_button.pack(pady=5)

    def print_eticket(self, nama_pembeli, email_pembeli):
        event_images = {
            "Bouquet Crafting Workshop": r"C:\Users\ASUS\Documents\21 Prokom\Tiket_Fun.jpeg",
            "Clay Painting Class": r"C:\Users\ASUS\Documents\21 Prokom\Tiket_Fun.jpeg",
            "Beads Crafting Session": r"C:\Users\ASUS\Documents\21 Prokom\Tiket_Fun.jpeg",
            "Pizza Palooza": r"C:\Users\ASUS\Documents\21 Prokom\Tiket_Cooking.jpeg",
            "SweetBake Cup": r"C:\Users\ASUS\Documents\21 Prokom\Tiket_Cooking.jpeg",
            "CakeCraft Bento": r"C:\Users\ASUS\Documents\21 Prokom\Tiket_Cooking.jpeg",
            "Day 1 (Yura Yunita, Raisa Anggiani, Arash Buana)": r"C:\Users\ASUS\Documents\21 Prokom\Tiket_Konser.jpeg",
            "Day 2 (Gangga, Nadhif Basalamah, Tulus)": r"C:\Users\ASUS\Documents\21 Prokom\Tiket_Konser.jpeg",
        }

        image_path = event_images.get(self.nama_event, "default_image.png")

        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
    
        font_path = "Perpetua.ttf"  
        font = ImageFont.truetype("PER_____.TTF", 48)

    # Menyesuaikan posisi teks pada gambar
        draw.text((300, 300), f"Nama Event: {self.nama_event}", font=font, fill="brown")
        draw.text((300, 380), f"Nama: {nama_pembeli}", font=font, fill="brown")
        draw.text((300, 460), f"Email: {email_pembeli}", font=font, fill="brown")
        draw.text((300, 540), f"Jumlah Tiket: {self.jumlah_tiket}", font=font, fill="brown")
        draw.text((300, 620), f"Total Pembelian: Rp. {self.harga_tiket * self.jumlah_tiket}", font=font, fill="brown")

        img.save(f"e_ticket_{self.nama_event.replace(' ', '_')}.png")
        messagebox.showinfo("Cetak E-Ticket", f"E-Ticket berhasil dicetak sebagai e_ticket_{self.nama_event.replace(' ', '_')}.png")

def pembayaran(nama_event, harga_tiket, jumlah_tiket):
    payment_root = tk.Toplevel(root)
    app = PaymentApp(payment_root, nama_event, harga_tiket, jumlah_tiket)
    payment_root.mainloop()

def navigate_back():
    if history_stack:
        current_window = history_stack.pop()
        current_window.destroy()
        if history_stack:
            history_stack[-1].deiconify()

image_path = r'C:\Users\ASUS\Documents\21 Prokom\Home.jpeg'
original_image = Image.open(image_path)
resized_image = original_image.resize((1200, 600), Image.LANCZOS)
im = ImageTk.PhotoImage(resized_image)

i = Label(root, image=im)
i.image = im
i.place(x=0, y=50)

b1 = Button(root, text="Beli Tiket", bg='light blue', font=("Perpetua", 12), compound="left", command=start_main_program)
b1.place(x=530, y=440, width=150, height=50)

root.mainloop()
