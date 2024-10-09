import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Function to establish the database connection
def establish_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",    # Alamat server database (gunakan 'localhost' jika ada di komputer lokal)
            user="root",         # Username MySQL
            password="",         # Password MySQL (kosongkan jika tidak ada password)
            database="alproii"   # Nama database yang ingin digunakan
        )
        return conn  # Mengembalikan objek koneksi jika berhasil
    except mysql.connector.Error as err:
        # Menampilkan pesan kesalahan jika koneksi gagal
        messagebox.showerror("Database Error", f"Error: {err}")
        return None  # Mengembalikan None jika koneksi gagal

# Function untuk menambahkan data ke tabel kuis_alpro
def add_user():
    nim = nim_entry.get()         # Mendapatkan input NIM dari entry field
    nama = nama_entry.get()       # Mendapatkan input Nama dari entry field
    nilai_kuis = nilai_kuis_entry.get()  # Mendapatkan input Nilai Kuis dari entry field

    # Validasi input: memastikan NIM, Nama terisi dan Nilai Kuis adalah angka
    if nim and nama and nilai_kuis.isdigit():
        conn = establish_db_connection()  # Membuka koneksi ke database
        if conn:
            cursor = conn.cursor()  # Membuat cursor untuk menjalankan query SQL
            # Menjalankan query INSERT untuk menambahkan data ke tabel 'kuis_alpro'
            cursor.execute("INSERT INTO kuis_alpro (Nim, Nama, `Nilai Kuis`) VALUES (%s, %s, %s)",
                           (nim, nama, int(nilai_kuis)))
            conn.commit()  # Menyimpan perubahan ke database
            cursor.close()  # Menutup cursor
            conn.close()    # Menutup koneksi

            # Menghapus input field setelah data berhasil ditambahkan
            nim_entry.delete(0, tk.END)
            nama_entry.delete(0, tk.END)
            nilai_kuis_entry.delete(0, tk.END)
            
            # Memperbarui tampilan pengguna
            show_users()  
    else:
        # Menampilkan pesan peringatan jika input tidak valid
        messagebox.showwarning("Input Error", "Harap masukkan NIM, Nama, dan Nilai Kuis yang valid.")

# Function untuk menampilkan data dari tabel kuis_alpro ke Treeview
def show_users():
    conn = establish_db_connection()  # Membuka koneksi ke database
    if conn:
        cursor = conn.cursor()  # Membuat cursor untuk menjalankan query SQL
        cursor.execute("SELECT * FROM kuis_alpro")  # Mengambil semua data dari tabel 'kuis_alpro'
        records = cursor.fetchall()  # Menyimpan hasil query ke dalam variabel 'records'
        
        # Membersihkan Treeview sebelum menampilkan data baru
        for row in tree.get_children():
            tree.delete(row)

        # Menambahkan data ke dalam Treeview
        for record in records:
            tree.insert("", tk.END, values=record)

        cursor.close()  # Menutup cursor
        conn.close()    # Menutup koneksi setelah selesai

# Membuat window utama
root = tk.Tk()
root.title("Tambah Data ke Tabel kuis_alpro")

# Label dan Entry untuk NIM
nim_label = tk.Label(root, text="NIM:")
nim_label.pack()

nim_entry = tk.Entry(root)
nim_entry.pack()

# Label dan Entry untuk Nama
nama_label = tk.Label(root, text="Nama:")
nama_label.pack()

nama_entry = tk.Entry(root)
nama_entry.pack()

# Label dan Entry untuk Nilai Kuis
nilai_kuis_label = tk.Label(root, text="Nilai Kuis:")
nilai_kuis_label.pack()

nilai_kuis_entry = tk.Entry(root)
nilai_kuis_entry.pack()

# Tombol untuk menambah data ke tabel kuis_alpro
add_button = tk.Button(root, text="Tambah Data", command=add_user)
add_button.pack()

# Treeview untuk menampilkan data dari tabel kuis_alpro
tree = ttk.Treeview(root, columns=("NIM", "Nama", "Nilai Kuis"), show='headings')
tree.heading("NIM", text="NIM")
tree.heading("Nama", text="Nama")
tree.heading("Nilai Kuis", text="Nilai Kuis")
tree.pack()

# Memanggil fungsi untuk menampilkan data ketika aplikasi dimulai
show_users()

# Menjalankan loop utama untuk GUI
root.mainloop()
