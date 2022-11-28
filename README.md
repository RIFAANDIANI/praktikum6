# latihan
- buatlah dictonary daftar kontak (nama sebagai key,dan nomer sebagai value)
- tampilkan kontak nya daud
- tambahkan kontak baru dengan nama bagas 085920785679
- ubah kontak sipa dengan nomer baru 085939776788
- tampilkan semua nama 
- tampilkan semua nomer
- tampilkan daftar nama dan nomer 
- hapus kontak daud
# rumus nya
print("Nama : rifa andiani")
print("NIM  : 312210377")

daftarkontak = {"Nama": "Nomer Telepon"}
kontak = {'daud': '085888339177', 'sipa': '087688992682'}

# print
print("============================")
print("|   # Nama   |Nomor Telepon|")
print("============================")
print("|   # daud    |  ", kontak['daud'], '|')
print("|   # sipa   |  ", kontak['sipa'], '|')
print("============================")
print()

# Tampilkan kontaknya daud
print("# Tampilkan kontaknya daud")
print("===========================")
print("|    daud     | ", kontak['daud'], '|')
print("===========================")
print()

# Tambah kontak baru dengan nama bagas, nomor 085920785679
print("# Tambah kontak baru dengan nama bagas, nomor 085920785679")
kontak['bagas'] = '085920785679'
print("===========================")
print("|    bagas    | ", kontak['bagas'], '|')
print("===========================")
print()

# Ubah kontak sipa dengan nomor baru 085939776788
print("# Ubah kontak sipa dengan nomor baru 085939776788")
kontak['sipa'] = '085939776788'
print("===========================")
print("|    sipa    | ", kontak['sipa'], '|')
print("===========================")
print()

# Tampilkan semua Nama
print("# Tampilkan semua Nama")
print("==================================")
print(kontak.keys())
print("==================================")
print()

# Tampilkan semua Nomor
print("# Tampilkan semua Nomor")
print("====================================================")
print(kontak.values())
print("====================================================")
print()

# Tampilkan daftar Nama dan nomornya
print("# Tampilkan daftar Nama dan nomornya")
print("====================================================")
print(kontak.items())
print("====================================================")
print()

# Menghapus kontak daud
print("# Hapus kontak daud")
print("====================================================")
kontak.pop('daud')
print(kontak.items())
print("====================================================")
# program nya
![img](gambar/pemograman%201.png)
![img](gambar/pemograman%202.png)
# hasil dari pemograman (run)
![img](gambar/hasil%20dari%20pemograman.png)
![img](gambar/hasil%20dari%20pemograman%202.png)
# rumus praktikum6
### python x = {}

### while True: c = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")
if c.lower() == 't':
    print("Tambah Data")
    nama = input("Nama           : ")
    nim = int(input("NIM            : "))
    uts = int(input("Nilai UTS      : "))
    uas = int(input("Nilai UAS      : "))
    tugas = int(input("Nilai Tugas    : "))
    akhir = tugas*30/100 + uts*35/100 + uas*35/100
    x[nama] = nim, uts, uas, tugas, akhir

elif c.lower() == 'u':
    print("Ubah Data")
    nama = input("Masukkan Nama  : ")
    if nama in x.keys():
        nim = int(input("NIM            : "))
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        tugas = int(input("Nilai Tugas    : "))
        akhir = tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100
        x[nama] = nim, uts, uas, tugas, akhir
    else:
        print("Nama {0} tidak ditemukan".format(nama))

elif c.lower() == 'h':
    print("Hapus Data")
    nama = input("Masukkan Nama  : ")
    if nama in x.keys():
        del x[nama]
    else:
        print("Nama {0} Tidak Ditemukan".format(nama))

elif c.lower() == 'c':
    print("Cari Data")
    nama = input("Masukkan Nama : ")
    if nama in x.keys():
        print("="*73)
        print("|                             Daftar Mahasiswa                          |")
        print("="*73)
        print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("="*73)
        print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
              .format(nama, nim, uts, uas, tugas, akhir))
        print("="*73)
    else:
        print("Nama {0} Tidak Ditemukan".format(nama))

elif c.lower() == 'l':
    if x.items():
        print("="*78)
        print("|                               Daftar Mahasiswa                             |")
        print("="*78)
        print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("="*78)
        i = 0
        for z in x.items():
            i += 1
            print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                  .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
        print("=" * 78)
    else:
        print("="*78)
        print("|                               Daftar Mahasiswa                             |")
        print("="*78)
        print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("="*78)
        print("|                                TIDAK ADA DATA                              |")
        print("="*78)

elif c. lower() == 'k':
    break

else:
    print("Pilih menu yang tersedia")

### Penjelasan :
1.) Pertama kita membuat sebuah dictionary kosong yang nantinya akan diinputkan data ketika program dijalankan. python

2.) Lalu kita membuat kondisi perulangan dan sebuah keterangan untuk pilihan menu yang akan menjalankan program. python Gambar 2

3.) Membuat syntax untuk menambahkan data. python
Disini apabila kita menginputkan 't' maka kita akan diminta untuk menginputkan beberapa data. Data yang kita inputkan akan masuk ke dictionary 'x' yang telah dibuat tadi dengan data 'nama' sebagai keys dan sisanya sebagai valuesnya.

4.) Membuat syntax untuk mengubah data. python 
Apabila kita menginput 'u' maka akan ada keterangan untuk mengubah data dan kita akan diminta untuk menginputkan nama yang mau diubah datanya, apabila nama tidak ada maka outputnya "Nama {} tidak ditemukan". Dimana {} adalah nama/data yang mau kita ubah.

5.) Membuat syntax untuk menghapus data. python
Apabila kita menginput 'h' maka kita akan diminta menginput nama yang akan dihapus. Jika nama ada di dalam dictionary, maka system akan menghapus keys/nama tersebut beserta valuesnya pada statement del x[nama].

6.) Membuat syntax untuk mencari data. python
Apabila kita menginputkan 'c' maka kita akan diminta untuk memasukkan nama yang akan dicari. Apabila nama yang dicari ada di dalam dictionary maka outputnya akan menampilkan data dari nama tersebut.

7.) Membuat syntax untuk melihat atau menampilkan data. python
Apabila kita menginput 'l' maka sistem akan menampilkan data - data yang sudah kita masukkan. Jika kita belum memasukkan data maka outputnya menjadi "TIDAK ADA DATA".

8.) Membuat syntax untuk menghentikan perulangan. python
Apabila kita menginput 'k' maka program akan langsung berhenti.

9.) Membuat syntax untuk apabila memilih pilihan yang tidak ada di menu. python
kita menginputkan selain yang ada pada menu (t, u, h, c, l, k) maka kita akan diminta untuk memilih menu yang tersedia.

### Tampilan Program Saat Dijalankan
# Tambah Data + Lihat Data
# contoh codingan dictionary
![img](gambar/gambar%202.png)
![img](gambar/gambar%203.png)
![img](gambar/gambar%204.png)
# hasil dari codingan dictionary
![img](gambar/ubah%20data.png)
![img](gambar/cari%20dan%20hapus%20data.png)