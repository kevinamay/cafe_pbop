import mysql.connector
from datetime import datetime
from prettytable import PrettyTable
from mysql.connector import Error

class cafe:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cafe_management"  # nama database
        )
        self.cursor = self.db.cursor()

    def main_menu(self):
        while True:
            print("=== SISTEM PENGELOLAAN CAFE ===")
            print("1. Pembeli")
            print("2. Pegawai")
            print("0. Keluar")
            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == '1':
                self.pembeli()
            elif pilihan == '2':
                self.pegawai()
            elif pilihan == '0':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def pembeli(self):
        while True:
            print("\n=== Pembeli ===")
            print("1. Tampilkan Menu ")
            print("0. Kembali ke Menu Utama")

            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == '1':
                self.tampilkan_menu()
            elif pilihan == '0':
                print("Kembali ke Menu Utama")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi!")

    def pegawai(self):
        while True:
            print("\n=== Pegawai ===")
            print("1. Tambahkan Menu")
            print("2. Tampilkan Menu")
            print("3. Ubah Menu")
            print("4. Hapus Menu")
            print("5. Tambahkan Pesanan")
            print("6. Tampilkan Pesanan")
            print("7. Ubah Pesanan")
            print("8. Hapus Pesanan")
            print("9. Cetak Struk Pesanan")
            print("0. Kembali ke Menu Utama")

            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == '1':
                self.tambahkan_menu()
            elif pilihan == '2':
                self.tampilkan_menu()
            elif pilihan == '3':
                self.mengubah_menu()
            elif pilihan == '4':
                self.menghapus_menu()
            elif pilihan == '5':
                self.tambahkan_pesanan()
            elif pilihan == '6':
                self.tampilkan_pesanan()
            elif pilihan == '7':
                self.mengubah_pesanan()
            elif pilihan == '8':
                self.menghapus_pesanan()
            elif pilihan == '9':
                self.mencetak_struk_pesanan()
            elif pilihan == '0':
                print("Kembali ke Menu Utama")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tambahkan_menu(self):
        try:
            jenis = str(input("Masukkan Jenis Menu: "))
            nama = str(input("Masukkan Nama Menu :"))
            harga = int(input("Masukkan Harga Menu :"))

            query = "INSERT INTO menu (jenis, nama, harga) VALUES (%s, %s, %s)"
            values = (jenis, nama, harga)
            self.cursor.execute(query, values)
            self.db.commit()
            print(f"{jenis, nama, harga} telah ditambahkan ke database.")

        except ValueError:
            print("Harga harus berupa angka. Silakan coba lagi.")
        except Error as e:
            print(f"Error: {e}")
            self.db.rollback()

    def tampilkan_menu(self):
        query = "SELECT * FROM menu"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["ID Menu", "Jenis", "Nama", "Harga"]
        
        for row in result:
            table.add_row(row)
        print(table)

    def mengubah_menu(self):
        try:
            id_menu = int(input("Masukkan ID Menu yang Diubah :"))
            field_to_ubah = input("Masukkan Field yang ingin Diubah(Jenis/Nama/Harga) :")
            new_value = input (f"Masukkan Nilai Baru untuk {field_to_ubah} :")
            query = f"UPDATE menu SET {field_to_ubah} = %s WHERE id_menu = %s"

            values = (new_value, id_menu)
            self.cursor.execute(query, values)
            self.db.commit()
            print("Data Menu Berhasil Diubah")

        except ValueError:
            print("ID Menu harus berupa angka. Silakan coba lagi.")
        except Error as e:
            print(f"Error: {e}")
            self.db.rollback()

    def menghapus_menu(self):
        try:
            id_menu = int(input("Masukkan ID Menu dihapus :"))
            query = "DELETE FROM menu WHERE id_menu = %s"
            values = (id_menu,)

            self.cursor.execute(query, values)
            self.db.commit()
            print("Menu tersebut berhasil dihapus.")

        except ValueError:
            print("ID Menu salah. Silakan coba lagi.")
        except Error as e:
            print(f"Error: {e}")
            self.db.rollback()


    def tambahkan_pesanan(self):
        try:
            id_menu = input("Masukkan ID Menu :")
            tgl_pesanan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            jumlah = int(input("Masukkan jumlah pesanan: "))
            harga = int(input("Masukkan Harga Menu :"))
            total_harga =  harga * jumlah 
            tunai = int(input("Masukkan Jumlah Tunai :"))
            kembali = tunai - total_harga

            query = "INSERT INTO pesanan (id_menu, tgl_pesanan, jumlah, harga, total_harga, tunai, kembali) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (id_menu , tgl_pesanan, jumlah, harga, total_harga, tunai, kembali)
            self.cursor.execute(query, values)
            self.db.commit()
            print(f"{id_menu, tgl_pesanan, jumlah, harga, total_harga, tunai, kembali} telah ditambahkan ke database.")
        except ValueError:
            print("ID Menu, Jumlah, Harga, Total Harga, Tunai, Kembali harus berupa angka. Silakan coba lagi.")
        except Error as e:
            print(f"Error: {e}")
            self.db.rollback()

    def tampilkan_pesanan(self):
        query = "SELECT * FROM pesanan"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["ID Pesanan", "ID Menu", "Tanggal Pesanan", "Jumlah ","Harga", "Total Harga", "Tunai", "Kembali"]
        
        for row in result:
            table.add_row(row)
        print(table)

    def mengubah_pesanan(self):
        try:
            id_pesanan = int(input("Masukkan ID Pesanan : "))
            field_to_ubah = input("Masukkan Field yang ingin Diubah(harga/jumlah): ")
            new_value = input(f"Masukkan pesanan baru {field_to_ubah}: ")

            query = f"UPDATE pesanan SET {field_to_ubah} = %s WHERE id_pesanan = %s"
            values = (new_value, id_pesanan)

            self.cursor.execute(query, values)
            self.db.commit()
            print("Pesanan berhasil diedit.")

        except ValueError:
            print("ID pesanan harus berupa angka. Silakan coba lagi.")
        except Error as e:
            print(f"Error: {e}")
            self.db.rollback()

    def menghapus_pesanan(self):
        try:
            id_pesanan = int(input("Masukkan ID Pesanan yang ingin Dihapus :"))
            query = "DELETE FROM pesanan WHERE id_pesanan = %s"
            values = (id_pesanan,)

            self.cursor.execute(query, values)
            self.db.commit()
            print("Pesanan tersebut berhasil dihapus.")

        except ValueError:
            print("ID Pesanan salah. Silakan coba lagi.")
        except Error as e:
            print(f"Error: {e}")
            self.db.rollback()

    def mencetak_struk_pesanan(self):
        try:
            id_pesanan = int(input("Masukkan ID Pesanan yang ingin di cetak : "))
            query = "SELECT * FROM pesanan WHERE id_pesanan = %s"
            values = (id_pesanan,)

            self.cursor.execute(query, values)
            result = self.cursor.fetchone()

            if result:
                id_pesanan, id_menu, tgl_pesanan, jumlah, harga, total_harga, tunai, kembali = result

                print("=" * 40)
                print("        STRUK PEMBAYARAN        ")
                print("=" * 40)
                print(f"ID Pesanan       : {id_pesanan}")
                print(f"ID Menu          : {id_menu}")
                print(f"Tanggal Pesanan  : {tgl_pesanan}")
                print(f"Jumlah Pesanan   : {jumlah}")
                print(f"Harga            : {harga}")
                print(f"Total Harga      : {total_harga}")
                print(f"Tunai            : {tunai}")
                print(f"Kembali          : {kembali}")
                print("=" * 40)
                print("        TERIMA KASIH          ")
                print("=" * 40)
            else:
                print(f"Tidak ada pesanan dengan ID {id_pesanan}")

        except ValueError:
            print("ID Pesanan harus berupa angka. Silakan coba lagi.")
        except Error as e:
            print(f"Error: {e}")
            self.db.rollback()



if __name__ == "__main__":
    cafe_obj = cafe()
    cafe_obj.main_menu()
