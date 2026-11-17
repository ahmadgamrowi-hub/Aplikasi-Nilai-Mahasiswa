# ====================================
# PROJECT APLIKASI NILAI MAHASISWA
# MENGGUNAKAN KONSEP OOP PYTHON
# ====================================

# CLASS INDUK
class Mahasiswa:
    def __init__(self, nama, nim, tugas, uts, uas):
        self.__nama = nama
        self.__nim = nim
        self.nilai_tugas = tugas
        self.nilai_uts = uts
        self.nilai_uas = uas

    # ENCAPSULATION DAN PROPERTY
    @property
    def nama(self):
        return self.__nama

    @property
    def nim(self):
        return self.__nim

    @property
    def nilai_tugas(self):
        return self.__nilai_tugas

    @nilai_tugas.setter
    def nilai_tugas(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai_tugas = nilai
        else:
            raise ValueError("Nilai harus 0-100")

    @property
    def nilai_uts(self):
        return self.__nilai_uts

    @nilai_uts.setter
    def nilai_uts(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai_uts = nilai
        else:
            raise ValueError("Nilai harus 0-100")

    @property
    def nilai_uas(self):
        return self.__nilai_uas

    @nilai_uas.setter
    def nilai_uas(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai_uas = nilai
        else:
            raise ValueError("Nilai harus 0-100")

    # MENGHITUNG NILAI AKHIR
    @property
    def nilai_akhir(self):
        return (
            self.nilai_tugas * 0.30
            + self.nilai_uts * 0.30
            + self.nilai_uas * 0.40
        )

    # MENENTUKAN GRADE
    @property
    def grade(self):
        nilai = self.nilai_akhir

        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"

    @property
    def status(self):
        return "LULUS" if self.nilai_akhir >= 60 else "TIDAK LULUS"

    # METHOD UNTUK POLYMORPHISM
    def keterangan(self):
        return "Mahasiswa Umum"

    def tampilkan_info(self):
        print("\n----------------------------")
        print("NAMA         :", self.nama)
        print("NIM          :", self.nim)
        print("JENIS        :", self.keterangan())
        print("NILAI TUGAS  :", self.nilai_tugas)
        print("NILAI UTS    :", self.nilai_uts)
        print("NILAI UAS    :", self.nilai_uas)
        print("NILAI AKHIR :", round(self.nilai_akhir, 2))
        print("GRADE        :", self.grade)
        print("STATUS       :", self.status)
        print("----------------------------")


# CLASS TURUNAN / INHERITANCE
class MahasiswaReguler(Mahasiswa):
    def keterangan(self):
        return "Mahasiswa Reguler"


class MahasiswaBeasiswa(Mahasiswa):
    def keterangan(self):
        return "Mahasiswa Beasiswa"


# CLASS PENGELOLA DATA
class Akademik:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self):
        print("\n=== TAMBAH MAHASISWA ===")

        nama = input("Nama mahasiswa: ")
        nim = input("NIM: ")

        if self.cari(nim, tampil=False):
            print("NIM sudah terdaftar!")
            return

        jenis = input("Jenis (1.Reguler / 2.Beasiswa): ")

        if jenis not in ["1", "2"]:
            print("Jenis tidak valid!")
            return

        try:
            tugas = float(input("Nilai tugas: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))

            if jenis == "1":
                mahasiswa = MahasiswaReguler(
                    nama, nim, tugas, uts, uas
                )
            else:
                mahasiswa = MahasiswaBeasiswa(
                    nama, nim, tugas, uts, uas
                )

            self.data_mahasiswa.append(mahasiswa)
            print("Data berhasil ditambahkan!")

        except ValueError as e:
            print("Input tidak valid:", e)

    def tampilkan(self):
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
            return

        for mahasiswa in self.data_mahasiswa:
            mahasiswa.tampilkan_info()

    def cari(self, nim, tampil=True):
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa.nim == nim:
                if tampil:
                    mahasiswa.tampilkan_info()
                return mahasiswa

        if tampil:
            print("Mahasiswa tidak ditemukan.")

        return None

    def ubah(self):
        nim = input("Masukkan NIM yang ingin diubah: ")
        mahasiswa = self.cari(nim, tampil=False)

        if mahasiswa is None:
            print("Data tidak ditemukan.")
            return

        try:
            mahasiswa.nilai_tugas = float(input("Nilai tugas baru: "))
            mahasiswa.nilai_uts = float(input("Nilai UTS baru: "))
            mahasiswa.nilai_uas = float(input("Nilai UAS baru: "))

            print("Data berhasil diperbarui!")

        except ValueError as e:
            print("Input tidak valid:", e)

    def hapus(self):
        nim = input("Masukkan NIM yang ingin dihapus: ")
        mahasiswa = self.cari(nim, tampil=False)

        if mahasiswa:
            self.data_mahasiswa.remove(mahasiswa)
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan.")


# PROGRAM UTAMA
def main():
    aplikasi = Akademik()

    while True:
        print("\n================================")
        print("   APLIKASI NILAI MAHASISWA")
        print("================================")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Ubah Nilai Mahasiswa")
        print("5. Hapus Mahasiswa")
        print("6. Keluar")
        print("================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            aplikasi.tambah()

        elif pilihan == "2":
            aplikasi.tampilkan()

        elif pilihan == "3":
            nim = input("Masukkan NIM: ")
            aplikasi.cari(nim)

        elif pilihan == "4":
            aplikasi.ubah()

        elif pilihan == "5":
            aplikasi.hapus()

        elif pilihan == "6":
            print("Terima kasih telah menggunakan aplikasi!")
            break

        else:
            print("Pilihan tidak tersedia!")


if __name__ == "__main__":
    main()