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