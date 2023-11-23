import json

class data_handler:
    def __init__(self):
        self.data_siswa = {}
        try:
            with open("app/database/Data_Siswa.json", "r") as file:
                self.data_siswa = json.load(file)
        except FileNotFoundError:
            print("error loading")


    def tambah_data(self, nisn, nama, jenis_kelamin, kelas, jurusan):
        # validasi data
        if nisn not in self.data_siswa:
                if len(nama) >=5 :
                    kata = nama.split()
                    for i in kata:
                        if i.isalpha():
                            self.data_siswa[nisn] = {
                            "Nama": nama.title(),
                            "Jenis Kelamin":jenis_kelamin.title(),
                            "Kelas": str(kelas),
                            "Jurusan": jurusan.upper(),
                            }
                            print(f"Data siswa dengan NISN {nisn} telah ditambahkan.")
                            self.simpan_data()
                        else:
                            print("nama Tidak huruf")
                else:
                    print("nama kurang dari ")
        else:
            print("Data siswa sudah ditambahkan")


    def simpan_data(self):
        try:
            with open("app/database/Data_Siswa.json", "w") as file:
                json.dump(self.data_siswa, file, indent=2)
        except FileNotFoundError:
            print("error save")

    def ubah_data(self, nisn, nama, jurusan, kelas, jenis_kelamin):
        if nisn in self.data_siswa:
            if nisn.isdigit() and len(nisn) == 10 and jurusan.isalpha() and kelas.isdigit():
                if len(nama) >=5 :
                    kata = nama.split()
                    for i in kata:
                        if i.isalpha():
                            self.data_siswa[nisn] = {
                            "Nama": nama.title(),
                            "Jenis Kelamin":jenis_kelamin.title(),
                            "Kelas": str(kelas),
                            "Jurusan": jurusan.upper(),
                            }
                            print(f"Data siswa dengan NISN {nisn} telah ditambahkan.")
                            self.simpan_data()
                        else:
                            print("nama Tidak huruf")
                else:
                    print("nama kurang dari ")
            else:
                print("Data salah")
        else:
            print("Data siswa sudah ditambahkan")

    def hapus_data(self, nisn):
        print(nisn)
        if nisn in self.data_siswa:
            del self.data_siswa[nisn]
            print(f"Data siswa dengan NISN {nisn} telah dihapus.")
        self.simpan_data()
        

    def tampilkan_data(self):
        print("Data Siswa:")
        print("")
        for nisn, data in self.data_siswa.items():
            print(f"NISN: {nisn}")
            print(f"Nama: {data['Nama']}")
            print(f"Jenis Kelamin: {data['Jenis Kelamin']}")
            print(f"Kelas: {data['Kelas']}")
            print(f"Jurusan: {data['Jurusan']}")
            print("")

# manajemen = data_handler()

# while True:
#     print("\nPilih operasi yang ingin Anda lakukan:")
#     print("1. Tambah data siswa")
#     print("2. Ubah data siswa")
#     print("3. Hapus data siswa")
#     print("4. Tampilkan data siswa")
#     print("5. Simpan data")
#     print("6. Keluar")

#     pilihan = input("Masukkan nomor pilihan (1/2/3/4/5/6): ")

#     if pilihan == '1':
#         nisn = input("Masukkan NISN siswa: ")
#         nama = input("Masukkan nama siswa: ")
#         jenis_kelamin = input("Masukkan Jenis Kelamin siswa: ")
#         kelas = input("Masukkan Kelas siswa: ")
#         jurusan = input("Masukkan jurusan siswa: ")
#         manajemen.tambah_data(nisn, nama, jenis_kelamin, kelas, jurusan)
#     elif pilihan == '2':
#         nisn = input("Masukkan NISN siswa yang akan di ubah: ")
#         nama = input("Masukkan nama: ")
#         jenis_kelamin = input("Masukkan Jenis Kelamin: ")
#         kelas = input("Masukkan Kelas: ")
#         jurusan = input("Masukkan jurusan: ")
#         manajemen.ubah_data(nisn, nama, jenis_kelamin, kelas, jurusan)
#     elif pilihan == '3':
#         nisn = input("Masukkan NISN siswa yang akan dihapus: ")
#         manajemen.hapus_data(nisn)
#     elif pilihan == '4':
#         manajemen.tampilkan_data()
#     elif pilihan == '5':
#         manajemen.simpan_data()
#     elif pilihan == '6':
#         print("Selesai.")
#         break
#     else:
#         print("Pilihan tidak valid. Silakan pilih angka 1-6.")