import mysql.connector
from tkinter import messagebox

# Fungsi untuk mengoneksikan ke database
def establish_db_connection():
    try:
        # Membuat koneksi ke database MySQL dengan parameter host, user, password, dan database
        conn = mysql.connector.connect(
            host="localhost",  # Alamat server database (localhost jika berada di komputer lokal)
            user="root",       # Username MySQL
            password="",       # Password MySQL (dikosongkan jika tidak ada password)
            database="alproii" # Nama database yang ingin diakses
        )
        return conn  # Mengembalikan objek koneksi
    except mysql.connector.Error as err:
        # Menampilkan pesan kesalahan jika terjadi error saat koneksi
        messagebox.showerror("Database Error", f"Error: {err}")
        return None  # Mengembalikan None jika koneksi gagal

# Fungsi untuk menginput data ke database
def insert_user(nim, nama, nilai_kuis):
    conn = establish_db_connection()  # Membuka koneksi ke database
    if conn:
        cursor = conn.cursor()  # Membuat cursor untuk menjalankan query SQL
        # Menjalankan query INSERT untuk memasukkan data ke dalam tabel 'kuis_alpro'
        cursor.execute("INSERT INTO kuis_alpro (Nim, Nama, `Nilai Kuis`) VALUES (%s, %s, %s)",
                       (nim, nama, int(nilai_kuis)))
        conn.commit()  # Menyimpan perubahan di database
        cursor.close()  # Menutup cursor
        conn.close()    # Menutup koneksi

# Fungsi untuk menampilkan inputan data dari database
def fetch_all_users():
    conn = establish_db_connection()  # Membuka koneksi ke database
    if conn:
        cursor = conn.cursor()  # Membuat cursor untuk menjalankan query SQL
        cursor.execute("SELECT * FROM kuis_alpro")  # Mengambil semua data dari tabel 'kuis_alpro'
        records = cursor.fetchall()  # Menyimpan hasil query ke dalam variabel 'records'
        cursor.close()  # Menutup cursor
        conn.close()    # Menutup koneksi
        return records  # Mengembalikan hasil query sebagai list
    return []  # Mengembalikan list kosong jika koneksi gagal
