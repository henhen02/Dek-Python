class Angkot:

    def __init__(self, merek, model, warna, kecepatan, jumlahPenumpang):
        # Adding attribute
        self.merek = merek
        self.model = model
        self.warna = warna
        self.kecepatan = kecepatan
        self.jumlahPenumpang = jumlahPenumpang
        self.kecepatanSekarang = 0
        self.penumpangSekarang = 0
        self.mesin = False

        # Calling method
        self.narik()

    # Method start
    def start(self):
        if self.mesin == False:
            print("Mesin menyala.")
            self.mesin = True
        else :
            print("Mesin sudah menyala!")
    
    # Method stop
    def stop(self):
        if self.mesin == True:
            if (self.kecepatanSekarang > 0):
                print("Mesin tidak boleh dimatikan saat mobil masih melaju!")
            else :        
                print("Mesin dimatikan.")
                self.mesin = False
        else :
            print("Mesin sudah mati!")
        
    # Method menambah kecepatan mobil
    def accelerate(self, speed):
        if self.mesin == True:
            if self.kecepatanSekarang < self.kecepatan:
                self.kecepatanSekarang += speed
                if self.kecepatanSekarang > self.kecepatan:
                    self.kecepatanSekarang = self.kecepatan
                    print("Tidak bisa menambah kecepatan diatas batas maksimal, kecepatan disesuaikan kedalam kecepatan maksimal (", self.kecepatanSekarang,"km/h)")
                    
                else :
                    print("Kecepatan berhasil ditambah menjadi", self.kecepatanSekarang,"km/h")
            else :
                print("Tidak bisa menambah kecepatan lagi!")
        else :
            print("Mesin belum dinyalakan, silahkan nyalakan mesin terlebih dahulu!")

    # Method mengurangi kecepatan mobil
    def brake(self):
        if self.mesin == True:
            if self.kecepatanSekarang > 0:
                self.kecepatanSekarang -= 10
                if self.kecepatanSekarang <= 0:
                    self.kecepatanSekarang = 0
                    print("Mobil berhenti!")
                else :
                    print("Berhasil mengurangi kecepatan menjadi", self.kecepatanSekarang, "km/h")
            else :
                print("Tidak bisa mengurangi kecepatan lagi karena mobil sudah berhenti!")
        else :
            print("Mesin belum dinyalakan, nyalakan mesin terlebih dahulu!")    

    # Method menambah jumlah penumpang
    def addPassenger(self):
        if self.penumpangSekarang < self.jumlahPenumpang:
            self.penumpangSekarang += 1
            print("Jumlah penumpan: ", self.penumpangSekarang)
        else :
            print("Mobil sudah penuh.")

    # Method mengurangi jumlah penumpang
    def removePassenger(self):
        if self.penumpangSekarang > 0:
            self.penumpangSekarang -= 1
            print("Jumlah penumpang: ", self.penumpangSekarang)
        else :
            print("Penumpang sudah kosong.")
    
    # Method menampilkan tipe mobil
    def mobil(self):
        print("Merek mobil:", self.merek)
        print("Model mobil:", self.model)
        print("Warna mobil:", self.warna)
        print("Kecepatan maksimal:", self.kecepatan, "km/h")
        print("Jumlah penumpang maksimal:", self.jumlahPenumpang)
    
    # Method memanggil semua method
    def narik(self):

        # Define
        menu = ['Cek mobil', 'Nyalakan mesin', 'Matikan mesin', 'Tambah kecepatan', 'Rem', 'Tambah penumpang', 'Kurangi penumpang', 'Turun dari mobil']
        cek = True
        # Mengulang program dengan kondisi True
        while (cek):
            for i in range(len(menu)):
                print(i+1, menu[i])
            print()
            
            pilih = int(input("Pilih menu: "))

            if pilih == 1:
                self.mobil()
                print()
            elif pilih == 2:
                self.start()
                print()
            elif pilih == 3:
                self.stop()
                print()
            elif pilih == 4:
                # Meminta input untuk parameter method
                speed = int(input("Masukkan jumlah kecepatan: "))
                self.accelerate(speed)
                print()
            elif pilih == 5:
                self.brake()
                print()
            elif pilih == 6:
                self.addPassenger()
                print()
            elif pilih == 7:
                self.removePassenger()
                print()
            elif pilih == 8:
                if self.kecepatanSekarang > 0:
                    print("Supir tidak boleh turun saat mobil masih melaju!")
                else :
                    # Program berhenti
                    cek = False
                    print("Supir turun dari mobil")
                print()
            else :
                print("Pilihan tidak tersedia.")
                print()