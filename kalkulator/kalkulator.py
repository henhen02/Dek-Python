class Kalkulator:
    
    def __init__(self):
        # Calling method
        self.menuKalkulator()

    # Method tambah
    def tambah(self, x, y):
        print("Hasil: ", x + y)
    
    # Method kurang
    def kurang(self, x, y):
        print("Hasil: ", x - y)

    # Method kali
    def kali(self, x, y):
        print("Hasil: ", x * y)

    # Method bagi
    def bagi(self, x, y):
        print("Hasil: ", x / y)

    # Method menjalankan kalkulator
    def menuKalkulator(self):
        pilihan = ['Tambah', 'Kurang', 'Kali', 'Bagi']
            
            
        x = int(input("Masukkan bilangan pertama: "))

        for i in range(len(pilihan)):
            print(i+1, pilihan[i])

        pilih = int(input("Pilih operator [1/2/3/4]: "))
            
        if pilih == 1:
            y = int(input("Masukkan penjumlah: "))
            self.tambah(x, y)
        elif pilih == 2:
            y = int(input("Masukkan pengurang: "))
            self.kurang(x, y)
        elif pilih == 3:
            y = int(input("Masukkan pengali: "))
            self.kali(x, y)
        elif pilih == 4:
            y = int(input("Masukkan pembagi: "))
            if y == 0:
                # Menhindari zero division error
                print("Tidak bisa dibagi dengan nol!")
            else :
                self.bagi(x, y)
        else :
            print("Operator tidak tersedia, program berhenti!")