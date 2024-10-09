import tkinter as tk
from tkinter import ttk
from service import add_user, get_all_users

# Fungsi untuk memperbarui data yang telah diinputkan
def show_users(tree):
    records = get_all_users()  # Mengambil data pengguna dari database
    # Menghapus data lama dari Treeview sebelum menampilkan data baru
    for row in tree.get_children():
        tree.delete(row)

    # Menambahkan data pengguna ke Treeview
    for record in records:
        tree.insert("", tk.END, values=record)

# Fungsi untuk menangani jika ada inputan
def handle_add_user(nim_entry, nama_entry, nilai_kuis_entry, tree):
    nim = nim_entry.get()  # Mendapatkan input NIM dari Entry
    nama = nama_entry.get()  # Mendapatkan input Nama dari Entry
    nilai_kuis = nilai_kuis_entry.get()  # Mendapatkan input Nilai Kuis dari Entry

    # Menambahkan pengguna dan membersihkan input jika berhasil
    if add_user(nim, nama, nilai_kuis):
        nim_entry.delete(0, tk.END)
        nama_entry.delete(0, tk.END)
        nilai_kuis_entry.delete(0, tk.END)
        show_users(tree)  # Memperbarui Treeview dengan data terbaru

# Fungsi untuk membuat tampilan GUI
def create_gui():
    root = tk.Tk()
    root.title("Tambah Data ke Tabel kuis_alpro")

    # NIM Entry
    nim_label = tk.Label(root, text="NIM:")
    nim_label.pack()
    nim_entry = tk.Entry(root)
    nim_entry.pack()

    # Nama Entry
    nama_label = tk.Label(root, text="Nama:")
    nama_label.pack()
    nama_entry = tk.Entry(root)
    nama_entry.pack()

    # Nilai Kuis Entry
    nilai_kuis_label = tk.Label(root, text="Nilai Kuis:")
    nilai_kuis_label.pack()
    nilai_kuis_entry = tk.Entry(root)
    nilai_kuis_entry.pack()

    # Add Button
    add_button = tk.Button(root, text="Tambah Data", 
                           command=lambda: handle_add_user(nim_entry, nama_entry, nilai_kuis_entry, tree))
    add_button.pack()

    # Treeview for displaying data
    tree = ttk.Treeview(root, columns=("NIM", "Nama", "Nilai Kuis"), show='headings')
    tree.heading("NIM", text="NIM")
    tree.heading("Nama", text="Nama")
    tree.heading("Nilai Kuis", text="Nilai Kuis")
    tree.pack()

    # Show users on startup
    show_users(tree)

    root.mainloop()  # Menjalankan loop utama untuk GUI
