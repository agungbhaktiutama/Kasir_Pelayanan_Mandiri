#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd  # Mengimpor modul pandas untuk pengolahan data tabel


# In[ ]:


class Transaction:
    def __init__(self):
        self.data_order = dict()  # Membuat kamus (dictionary) untuk menyimpan pesanan
    
    # Fungsi untuk menambahkan item ke dalam pesanan
    def add_item(self, nama_item, jumlah_item, harga_item):
        self.data_order.update({nama_item: [jumlah_item, harga_item, (jumlah_item * harga_item)]})
    
    # Fungsi untuk mengubah nama item dalam pesanan
    def update_item_name(self, nama_item, nama_baru):
        
        temp = self.data_order[nama_item]
        self.data_order.pop(nama_item)
        self.data_order.update({nama_baru: temp})
        
    # Fungsi untuk mengubah jumlah item dalam pesanan
    def update_item_qty(self, nama_item, jumlah_baru):
        
        self.data_order[nama_item][0] = jumlah_baru
        self.data_order[nama_item][2] = jumlah_baru * self.data_order[nama_item][1]
    
    # Fungsi untuk mengubah harga item dalam pesanan
    def update_item_price(self, nama_item, harga_baru):
        
        self.data_order[nama_item][1] = harga_baru
        self.data_order[nama_item][2] = harga_baru * self.data_order[nama_item][0]
    
    # Fungsi untuk menghapus item dari pesanan
    def delete_item(self, nama_item):

        self.data_order.pop(nama_item)
    
    # Fungsi untuk mereset transaksi (menghapus semua item dari pesanan)
    def reset_transaction(self):
    
        self.data_order.clear()
        print("Semua Item Berhasil Dihapus!")
        
    # Fungsi untuk memeriksa pesanan dan menampilkan informasi pesanan dalam bentuk tabel
    def check_order(self):
        if len(self.data_order) == 0:
            print("Anda Belum Memesan Apapun")
        else:
            data_transac = pd.DataFrame(self.data_order).T
            data_transac.index.name = "Nama Item"
            data_transac.columns = ["Jumlah Item", "Harga", "Total Harga"]
            
            # Memeriksa apakah ada kesalahan input data (nama item kosong)
            if any(item == "" for item in data_transac.index):
                print("Terdapat Kesalahan Input Data")
                print("")
                print(data_transac.to_markdown())
            else:
                print("Pemesanan Sudah Benar")
                print("")
                print(data_transac.to_markdown())
    
    # Fungsi untuk menghitung total harga pesanan dan memberikan diskon berdasarkan total harga
    def total_price(self):
        self.check_order()
        print("")
        total_harga = 0
        for item in self.data_order:
            total_harga += self.data_order[item][2]
        
        if total_harga > 500_000:
            total = total_harga * 0.9
            print(f"Selamat! Anda Mendapatkan Diskon 10%\nTotal Belanja Anda Setelah Diskon Sebesar Rp. {total}")
        elif total_harga > 300_000:
            total = total_harga * 0.92
            print(f"Selamat! Anda Mendapatkan Diskon 8%\nTotal Belanja Anda Setelah Diskon Sebesar Rp. {total}")
        elif total_harga > 200_000:
            total = total_harga * 0.95
            print(f"Selamat! Anda Mendapatkan Diskon 5%\nTotal Belanja Anda Setelah Diskon Sebesar Rp. {total}")
        else:
            print(f"Total Belanja Anda Sebesar Rp. {total_harga}")

