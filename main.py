#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  # Mengimpor modul pandas untuk pengolahan data tabel


# In[ ]:


from transaction import Transaction  # Mengimpor kelas Transaction dari modul transaction


# In[ ]:


def menu(opt): # Fungsi menu yang mengatur tampilan menu dan mengelola transaksi
    print("")
    print("Selamat Datang")
    print("")
    print("Menu: ")
    print("1. Menambahkan Item")
    print("2. Mengubah Nama Item")
    print("3. Mengubah Jumlah Item")
    print("4. Mengubah Harga Item")
    print("5. Menghapus Item")
    print("6. Reset Pesanan")
    print("7. Memeriksa Pesanan")
    print("8. Total Harga")
    print("9. Keluar")
    print("")
    
    option = int(input("Masukkan Pilihan Anda: "))  # Meminta pengguna untuk memasukkan pilihan menu (Pengguna diminta untuk mendefinisikan nilai option)
    
    if option == 1: # Pilihan untuk memasukkan item
        nama_item = input("Masukkan Nama Item yang Ingin Dipesan: ")  # Meminta nama item yang ingin ditambahkan
        
        while True:
            try:
                jumlah_item = int(input("Masukkan Jumlah Item yang Ingin Dipesan: "))  # Meminta jumlah item yang ingin ditambahkan
            except ValueError:
                print("Harus Berupa Angka!")  # Menampilkan pesan kesalahan jika input bukan angka
            else:
                break  # Keluar dari loop jika input valid
                
        while True:
            try:
                harga_item = int(input("Masukkan Harga Item yang Ingin Dipesan: "))  # Meminta harga item yang ingin ditambahkan
            except ValueError:
                print("Harus Berupa Angka!")  # Menampilkan pesan kesalahan jika input bukan angka
            else:
                break  # Keluar dari loop jika input valid
                
        opt.add_item(nama_item, jumlah_item, harga_item)  # Memanggil metode add_item dari objek Transaction
        menu(opt)  # Kembali ke menu utama
            
    # Blok kode serupa berlaku untuk pilihan menu lainnya seperti mengubah nama item, mengubah jumlah item, mengubah harga item, menghapus item, reset pesanan, memeriksa pesanan, dan menghitung total harga.
   
    elif option == 2: # Pilihan untuk mengubah nama Item
        nama_item = input("Masukkan Nama Item yang Ingin Diubah: ")
        nama_baru = input("Masukkan Nama Baru: ")
        opt.update_item_name(nama_item, nama_baru)
        menu(opt) 
            
    elif option == 3: # Pilihan untuk mengubah jumlah item
        nama_item = input("Masukkan Nama Item: ")
        
        while(True):
            try:
                jumlah_baru = int(input("Masukkan Jumlah Baru: "))
            except ValueError:
                    print("Harus Berupa Angka!")
            else:
                break
        
        opt.update_item_qty(nama_item, jumlah_baru)
        menu(opt)
            
    elif option == 4: # Pilihan untuk mengubah harga item
        nama_item = input("Masukkan Nama Item: ")
        
        while(True):
            try:
                harga_baru = int(input("Masukkan Harga Baru: "))
            except ValueError:
                print("Harus Berupa Angka!")
            else:
                break
                
        opt.update_item_price(nama_item, harga_baru)
        menu(opt)
            
    elif option == 5: # Pilihan untuk menghapus item
        nama_item = input("Masukkan Nama Item yang Ingin Dihapus: ")
        opt.delete_item(nama_item)
        menu(opt)
            
    elif option == 6: # Pilihan untuk mereset transaksi
        opt.reset_transaction()
        menu(opt)
            
    elif option == 7: # Pilihan unutk mengecek transaksi
        opt.check_order()
        menu(opt)
            
    elif option == 8: #Plihan untuk mengecek total harga
        opt.total_price()
        menu(opt)
        
    elif option == 9: # Pilihan untuk keluar dari program
        print("")
        print("Terima Kasih")
        print("")
        pass  # Keluar dari program jika pengguna memilih keluar
        
    else:
        print("Inputan Anda Salah!")  # Menampilkan pesan jika input tidak valid
        menu(opt)  # Kembali ke menu utama


# In[ ]:


trans = Transaction()  # Membuat objek Transaction dengan nama 'trans'


# In[ ]:


menu(trans)  # Memulai program dengan memanggil fungsi menu dan meneruskan objek 'trans' sebagai argumen

