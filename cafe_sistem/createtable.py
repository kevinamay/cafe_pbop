import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'cafe_management'

def connect_db():
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor, table_name, columns):
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    cursor.execute(query)

def main():
    conn, cursor = connect_db()

    print("=" * 40)
    create_table(cursor, "menu", """
        id_menu INT AUTO_INCREMENT PRIMARY KEY,
        jenis VARCHAR(255) NOT NULL,
        nama VARCHAR(255) NOT NULL,
        harga DECIMAL(10, 2) NOT NULL
    """)
    print("Tabel Makanan_minuman Berhasil Dibuat")

    print("=" * 40)

    create_table(cursor, "pesanan", """
        id_pesanan INT AUTO_INCREMENT PRIMARY KEY,
        id_menu INT,
        tgl_pesanan DATETIME,
        jumlah INTEGER NOT NULL,
        harga DECIMAL(10, 2) NOT NULL,
        total_harga DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (id_menu) REFERENCES menu(id_menu),
        tunai DECIMAL(10, 2) NOT NULL,
        kembali DECIMAL(10, 2) NOT NULL
    """)
    print("Tabel Pesanan Berhasil Dibuat")
    print("=" * 40)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
