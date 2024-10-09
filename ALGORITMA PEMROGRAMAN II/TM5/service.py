from database import insert_user, fetch_all_users # memanggil file database.py
from tkinter import messagebox

# Fungsi untuk menambahkan inputan dengan Validasi
def add_user(nim, nama, nilai_kuis):
    # Validasi input: memastikan bahwa NIM dan Nama terisi, dan Nilai Kuis adalah angka
    if nim and nama and nilai_kuis.isdigit():
        insert_user(nim, nama, nilai_kuis)  # Memasukkan data ke database menggunakan fungsi dari database
        return True  # Mengembalikan True jika data berhasil ditambahkan
    else:
        # Menampilkan pesan peringatan jika input tidak valid
        messagebox.showwarning("Input Error", "Harap masukkan NIM, Nama, dan Nilai Kuis yang valid.")
        return False  # Mengembalikan False jika input tidak valid

# Fungsi untuk menampilkan semua inputan
def get_all_users():
    return fetch_all_users()  # Mengambil semua data pengguna dari database
