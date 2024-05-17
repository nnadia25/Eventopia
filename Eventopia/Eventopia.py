import tkinter as tk
from tkinter import messagebox
import csv

class EventopiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eventopia - Your Gateway to Unforgettable Events")
        self.create_widgets()

    def create_widgets(self):
        # Welcome message
        welcome_label = tk.Label(self.root, text="Welcome To Eventopia!", font=("Helvetica", 16))
        welcome_label.pack(pady=10)

        description_label = tk.Label(self.root, text=(
            "Our user-friendly platform offers a wide range of events, from music concerts and art festivals "
            "to creative workshops and culinary experiences.\nWith advanced search features and secure payment "
            "options, finding and purchasing tickets has never been easier.\nDiscover detailed information about "
            "each event, including descriptions, schedules, and prices, all in one place.\nUse Eventopia today "
            "and unlock a world of exciting experiences at your fingertips!"
        ), wraplength=400, justify="center")
        description_label.pack(pady=10)

        # Event buttons
        fun_art_button = tk.Button(self.root, text="Fun Art", command=self.show_fun_art_event)
        fun_art_button.pack(pady=5)

        cooking_class_button = tk.Button(self.root, text="Cooking Class", command=self.show_cooking_class_event)
        cooking_class_button.pack(pady=5)

        concert_button = tk.Button(self.root, text="Konser", command=self.show_concert_event)
        concert_button.pack(pady=5)

        exit_button = tk.Button(self.root, text="Keluar", command=self.root.quit)
        exit_button.pack(pady=20)

    def show_fun_art_event(self):
        events = self.load_events(r'C:\Users\ASUS\Documents\TUBES PRAKPROKOM\Eventopia\Fun_Art.csv')
        self.show_events(events, "Fun Art")

    def show_cooking_class_event(self):
        events = self.load_events(r'C:\Users\ASUS\Documents\TUBES PRAKPROKOM\Eventopia\Cooking_Class.csv')
        self.show_events(events, "Cooking Class")

    def show_concert_event(self):
        events = self.load_events(r'C:\Users\ASUS\Documents\TUBES PRAKPROKOM\Eventopia\Suara_Sejuta_Rasa.csv')
        self.show_events(events, "Konser")

    def load_events(self, filename):
        events = []
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                header = next(reader) 
                for row in reader:
                    if len(row) >= 4 and all(row):  
                        events.append(row)
        except FileNotFoundError:
            messagebox.showerror("Error", f"File {filename} tidak ditemukan.")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat membaca file: {e}")
        return events

    def show_events(self, events, event_type):
        if not events:
            messagebox.showinfo("Info", f"Tidak ada event {event_type} yang tersedia.")
            return
        top = tk.Toplevel(self.root)
        top.title(f"Daftar {event_type} yang Tersedia")

        count = 1
        for event in events:
            event_label = tk.Label(top, text=(
                f"Nomor Event: {count}\n"
                f"Nama Kegiatan: {event[0]}\n"
                f"Tempat: {event[1]}\n"
                f"Tanggal: {event[2]}\n"
                f"Harga Tiket: {event[3]}\n"
                "========================================="
            ), justify="left")
            event_label.pack(pady=5)
            count += 1

        choose_label = tk.Label(top, text="Masukkan nomor event yang Anda pilih:")
        choose_label.pack(pady=5)
        entry = tk.Entry(top)
        entry.pack(pady=5)
        choose_button = tk.Button(top, text="Pilih", command=lambda: self.choose_event(events, entry.get(), top))
        choose_button.pack(pady=5)

    def choose_event(self, events, choice, top):
        try:
            choice = int(choice)
            if 1 <= choice <= len(events):
                chosen_event = events[choice - 1]
                self.buy_ticket(chosen_event)
                top.destroy()
            else:
                messagebox.showerror("Error", "Nomor event yang Anda pilih tidak valid.")
        except ValueError:
            messagebox.showerror("Error", "Input yang Anda masukkan bukan nomor event yang valid.")

    def buy_ticket(self, event):
        top = tk.Toplevel(self.root)
        top.title(f"Beli Tiket untuk {event[0]}")

        labels = ["Nama", "No. Handphone", "Email", "Jumlah Tiket", "No. Rekening"]
        entries = []
        for label in labels:
            lbl = tk.Label(top, text=f"Masukkan {label}:")
            lbl.pack(pady=5)
            entry = tk.Entry(top)
            entry.pack(pady=5)
            entries.append(entry)

        buy_button = tk.Button(top, text="Beli", command=lambda: self.confirm_purchase(event, entries, top))
        buy_button.pack(pady=20)

    def confirm_purchase(self, event, entries, top):
        details = [entry.get() for entry in entries]
        total_harga = float(event[3].replace("Rp", "").replace(".", "").replace(",", ".")) * int(details[3])
        messagebox.showinfo("Konfirmasi Pembelian", f"Total Pembayaran: Rp {total_harga}\n"
                                                     f"Harap segera lakukan pembayaran! {event[0]}")
        top.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EventopiaApp(root)
    root.mainloop()

