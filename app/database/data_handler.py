import json

class data_handler:
    def __init__(self):
        self.data_siswa = {}
        try:
            with open("app/database/Data_Siswa.json", "r") as file:
                self.data_siswa = json.load(file)
        except FileNotFoundError:
            print("error loading")

    def simpan_data(self):
        try:
            with open("app/database/Data_Siswa.json", "w") as file:
                json.dump(self.data_siswa, file, indent=2)
            return True
        except Exception as e:
            return f"Error: {e}"

    def tambah_data(self, nisn, nama, jenis_kelamin, kelas, jurusan):
        if nisn not in self.data_siswa:
            if len(nama) >= 5 and all(word.isalpha() for word in nama.split()):
                self.data_siswa[nisn] = {
                    "Nama": nama.title(),
                    "Jenis Kelamin": jenis_kelamin.title(),
                    "Kelas": kelas,
                    "Jurusan": jurusan.upper(),
                }
                self.simpan_data()
                return True
            else:
                return False
        else:
            return False

    def ubah_data(self, nisn, nama,jenis_kelamin, kelas,  jurusan):
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
        if nisn in self.data_siswa:
            del self.data_siswa[nisn]
            self.simpan_data()
            return f"Data siswa dengan NISN {nisn} telah dihapus."
        else:
            return "Error: Data siswa tidak ditemukan."
        
    def seacrh_data(self,nisn):
        for key,index in self.data_siswa.items():
            if key == nisn:
                return index