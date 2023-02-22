from buku import Buku

class Anggota(Buku):
    def __init__(self, id, judul, penulis, jumlah):
        super().__init__(id, judul, penulis, jumlah)
    
    def pinjam(self, peminjam, idPeminjam, idBuku):
        return super().pinjam(peminjam, idPeminjam, idBuku)

    def kembalikan(self):
        return super().kembalikan()
    