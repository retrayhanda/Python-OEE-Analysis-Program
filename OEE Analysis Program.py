import time

print(''' 
    ||=======================================================================================||
    ||                                                                                       ||
    ||                                                                                       ||
    ||                      "Analisis Overall Equipment Efectiveness(OEE)                    || 
    ||                         Dalam Meminimalisi Six Big Losses pada                        ||
    ||                            Mesin Produksi Dual Filter DD07"                           ||
    ||                                                                                       ||
    ||                                     DISUSUN OLEH:                                     ||
    ||                                 Rahmad Haret Rayhanda                                 || 
    ||                                                                                       ||                           
    ||=======================================================================================||
    ''')

print("="*99)
print("{0:^99}".format("Program Analisis OEE pada Mesin DD07"))
print("="*99)

class Login:
    def __init__(self):
        self.username = None
        self.password = None
    
    def registrasi(self):
        print("{0:^99}".format("Silahkan Registrasi Terlebih Dahulu!"))
        print("="*99)
        self.username_registrasi = input("Masukkan Username : ").lower()
        self.password_registrasi = input("Masukkan Password : ").lower()
    
    def login(self):
        print("="*99)
        print("{0:^99}".format(" Berhasil Register, Silahkan Login!"))
        print("="*99)
        kesempatan = 3
        while kesempatan > 0:
            username = input('Masukkan Username : ').lower()
            password = input('Masukkan Password : ').lower()
            if username == self.username_registrasi and password == self.password_registrasi:
                print("="*99)
                print("{0:^99}".format('Selamat Anda Berhasil Login'))
                print("="*99)
                break
            else:
                kesempatan -= 1
                print("="*99)
                print("{0:^99}".format('Username atau Password Anda Salah'))
                print("="*99)
                if kesempatan > 0:
                    print("Harap beri jeda beberapa detik...")
                    time.sleep(4)
                    print("="*99)
                    print("{0:^99}".format('Silahkan Masukkan Password dan Username yang Benar!'))
                    print("="*99)
                else:
                    print("{0:^99}".format('Anda Sudah Mencoba Login Sebanyak 3x, Silahkan Login Beberapa Saat Lagi!'))
                    print("="*99)
                    exit()

masuk = Login()
masuk.registrasi()
masuk.login()

class OEE:
    def __init__(self, months):
        self.months = []
        self.defect_product = {}
        self.availability = {}
        self.performance_rate = {}
        self.quality = {}
        self.oee = {}
    
    def input_month(self):
        print("")
        masukkan_bulan = int(input("Masukkan jumlah bulan yang diinginkan: "))
        print("Contoh bulan : Januari, Februari")
        print("\n")
        for i in range(masukkan_bulan):
            while True:
                month = input(f"Masukkan bulan ke-{i + 1}: ").capitalize()
                if month not in self.months:
                    self.months.append(month)
                    break
                else:
                    print("Bulan sudah dimasukkan, silakan masukkan bulan yang berbeda.")

    def calculate_defect(self):
        print("")
        print("="*99)
        print("{0:^99}".format("Program Menentukan Jumlah Produk Cacat"))
        print("="*99)
        for month in self.months:
            print(f"\nMasukkan data produk cacat (defect) untuk bulan {month}:")
            waste = int(input("  Waste      : "))
            reject = int(input("  Reject     : "))
            jumlah_defect = waste + reject
            self.defect_product[month] = (waste, reject, jumlah_defect)
    
    def display_defect(self):
        print("\nSedang menghitung total product cacat, harap bersabar...")
        time.sleep(4)
        print("\n")
        print("{0:^83}".format("Data Jumlah Produk Cacat (Defect) TSP 100938 Mesin Dual Filters DD07"))
        print("\n" + "=" * 83)
        print("| {0:^20} | {1:^15} | {2:^15} | {3:^20} |".format("Bulan", "Waste", "Reject", "Jumlah Defect"))
        print("=" * 83)
        
        for month, (waste, reject, jumlah_defect) in self.defect_product.items():
            print("| {0:^20} | {1:^15} | {2:^15} | {3:^20} |".format(month, waste, reject, jumlah_defect))
        
        print("=" * 83)

    def calculate_availability(self):
        print("\n")
        print("="*99)
        print("{0:^99}".format("Program Menentukan Availabilty Ratio"))
        print("="*99)
        for month in self.months:
            print(f"\nMasukkan data pada bulan {month}")
            available_time = int(input("    Masukkan available time                                                  : "))
            autonomous_maintenance = int(input("    Masukkan autonomous maintenance (jika tidak ada, masukkan nilai 0)       : "))
            istirahat_makan = int(input("    Masukkan waktu istirahat makan (jika tidak ada, masukkan nilai 0)        : "))
            preventive_maintenance = int(input("    Masukkan waktu preventive maintenance (jika tidak ada, masukkan nilai 0) : "))

            planned_downtime = autonomous_maintenance + istirahat_makan + preventive_maintenance
            loading_time = available_time - planned_downtime

            loading_time = int(input("    Masukkan waktu jeda (loading time)                                       : "))
            unplanned_downtime = int(input("    Masukkan waktu pemberhentian yang tidak direncanakan (unplanned downtime): "))
            
            operating_time = loading_time - unplanned_downtime
            availability = round((operating_time * 100 / loading_time), 3)

            self.availability[month] = (loading_time, unplanned_downtime, operating_time, availability)
    
    def display_availability(self):
        print("\nSedang menghitung availability rate, harap bersabar...")
        time.sleep(4)
        print("\n")
        print("{0:^84}".format("Data Hasil Perhitungan Availability"))
        print("Keterangan :\nLT = Loading Time (Menit) \nUD = Unplanned Downtime (Menit) \nOT = Operating Time (Menit) \nAR = Availability Rate (%)")
        print("\n" + "="*84)
        print("| {0:^20} | {1:^12} | {2:^12} | {3:^12} | {4:^12} |".format("Bulan", "LT", "UD", "OT", "AR"))
        print("="*84)

        total_availability = sum(availability for _, _, _, availability in self.availability.values())
        rata_rata = round((total_availability / len(self.months)), 3)

        for month, (loading_time, unplanned_downtime, operating_time, availabilty) in self.availability.items():
            print("| {0:^20} | {1:^12} | {2:^12} | {3:^12} | {4:^12} |".format(month, loading_time, unplanned_downtime, operating_time, availabilty))

        print("=" * 84)    
        print("| {0:^65} |".format("Rata-rata")
              , "{0:^12} |".format(f"{rata_rata}"))
        print("=" * 84)

    def calculate_performance_rate(self):
        print("\n")
        print("="*99)
        print("{0:^99}".format("Program Menentukan Performance Rate"))
        print("="*99)
        irt = 646
        for month in self.months:
            if month in self.availability:
                print(f"\nMasukkan data performance rate untuk bulan {month}")
                total_produksi = int(input("    Total Produksi  : "))

                _, _, operating_time, _ = self.availability[month]
                acp = round((total_produksi / operating_time), 3)
                performance_rate = round(((acp / irt) * 100), 3)

                self.performance_rate[month] = (total_produksi, acp, irt, performance_rate)
    
    def display_performance_rate(self):
        print("\nSedang menghitung performance rate, harap bersabar...")
        time.sleep(4)
        print("\n")
        print("{0:^84}".format("Data Hasil Perhitungan Performance Rate"))
        print("\nKeterangan :\nTP = Total Produksi (rod) \nACP = Actual Capacity Production (rod/menit) \nIRT = Ideal Run Time (rod/menit) \nPR = Performance Rate (%)")
        print("\n" + "=" * 84) 
        print("| {0:^20} | {1:^12} | {2:^12} | {3:^12} | {4:^12} |".format("Bulan", "TP", "ACP", "IRT", "PR"))
        print("=" * 84) 

        jumlah_performance_rate = sum(performance_rate for _, _, _, performance_rate in self.performance_rate.values())
        rata_rata = round((jumlah_performance_rate / len(self.months)), 3)

        for month, (total_produksi, actual_capacity_production, ideal_run_time, performance_rate) in self.performance_rate.items():
           print("| {0:^20} | {1:^12} | {2:^12} | {3:^12} | {4:^12} |".format(month, total_produksi, actual_capacity_production, ideal_run_time, performance_rate)) 
        
        print("=" * 84)    
        print("| {0:^65} |".format("Rata-rata")
              , "{0:^12} |".format(f"{rata_rata}"))
        print("=" * 84)

    def calculate_quality(self):
        print("\n")
        print("="*99)
        print("{0:^99}".format("Program Menentukan Quality Rate"))
        print("="*99)
        for month in self.months:
            if month in self.defect_product and month in self.performance_rate:
                total_produksi, _, _, _ = self.performance_rate[month]
                _, _, jumlah_defect = self.defect_product[month]
                quality = round((((total_produksi - jumlah_defect) / total_produksi) * 100), 3)
                self.quality[month] = (total_produksi, jumlah_defect, quality)

    def display_quality(self):
        print("\n")
        print("Sedang menghitung quality rate, harap bersabar...")
        time.sleep(5)
        print("\n")
        print("{0:^83}".format("Data Hasil Perhitungan Quality Rate "))
        print("\nKeterangan :\nTP = Total Produksi (rod) \nDA = Defect Amount \nQR = Quality Rate (%)")
        print("\n" + "=" * 83)
        print("| {0:^20} | {1:^15} | {2:^15} | {3:^20} |".format("Bulan", "TP", "DA", "QR"))
        print("=" * 83)
        
        total_quality = sum(quality for _, _, quality in self.quality.values())
        rata_rata = round((total_quality / len(self.months)), 3)

        for month, (total_produksi, jumlah_defect, quality) in self.quality.items():
            print("| {0:^20} | {1:^15} | {2:^15} | {3:^20} |".format(month, total_produksi, jumlah_defect, quality))
        
        print("=" * 83)    
        print("| {0:^56} |".format("Rata-rata")
              , "{0:^20} |".format(f"{rata_rata}"))
        print("=" * 83)
    
    def calculate_oee(self):
        print("\n")
        print("="*99)
        print("{0:^99}".format("Program Menentukan OEE"))
        print("="*99)
        for month in self.months:
            if month in self.availability and month in self.performance_rate and month in self.quality:
                _, _, _, availability = self.availability[month]
                _, _, _, performance_rate = self.performance_rate[month]
                _, _, quality = self.quality[month]

                oee = round((availability * performance_rate * quality / 10000), 3)
                self.oee[month] = (availability, performance_rate, quality,oee)
    
    def display_oee(self):
        print("\n")
        print("Sedang menghitung OEE, harap bersabar...")
        time.sleep(7)
        print("\n")
        print("{0:^84}".format("Data Hasil Perhitungan OEE"))
        print("\nKeterangan :\n Availability (%) \nPR = Performance Rate (%) \nQR = Quality Rate (%) \nOEE = Overall Equipment Effectiveness (%)")
        print("\n" + "=" * 84) 
        print("| {0:^20} | {1:^12} | {2:^12} | {3:^12} | {4:^12} |".format("Bulan", "Availability", "PR", "QR", "OEE"))
        print("\n" + "=" * 84) 
        
        total_oee = sum(oee for _, _, _, oee in self.oee.values())
        rata_rata = round((total_oee / len(self.months)), 3)

        for month, (availability, performance_rate, quality, oee) in self.oee.items():
           print("| {0:^20} | {1:^12} | {2:^12} | {3:^12} | {4:^12} |".format(month, availability, performance_rate, quality, oee))

        print("=" * 84)    
        print("| {0:^65} |".format("Rata-rata")
              , "{0:^12} |".format(f"{rata_rata}"))
        print("=" * 84)
    
    def update_defect_data(self, month):
        if month in self.defect_product:
            print(f"Updating defect data for {month}:")
            waste = int(input("  Waste      : "))
            reject = int(input("  Reject     : "))
            jumlah_defect = waste + reject
            self.defect_product[month] = (waste, reject, jumlah_defect)
        else:
            print(f"Data tidak ditemukan untuk bulan {month}. Harap masukkan bulan yang tepat.")

    def update_availability_data(self, month):
        if month in self.availability:
            print(f"Updating availability data for {month}:")
            available_time = int(input("    Masukkan available time                                                  : "))
            autonomous_maintenance = int(input("    Masukkan autonomous maintenance (jika tidak ada, masukkan nilai 0)       : "))
            istirahat_makan = int(input("    Masukkan waktu istirahat makan (jika tidak ada, masukkan nilai 0)        : "))
            preventive_maintenance = int(input("    Masukkan waktu preventive maintenance (jika tidak ada, masukkan nilai 0) : "))

            planned_downtime = autonomous_maintenance + istirahat_makan + preventive_maintenance
            loading_time = available_time - planned_downtime

            loading_time = int(input("    Masukkan waktu jeda (loading time)                                       : "))
            unplanned_downtime = int(input("    Masukkan waktu pemberhentian yang tidak direncanakan (unplanned downtime): "))

            operating_time = loading_time - unplanned_downtime
            availability = round((operating_time * 100 / loading_time), 3)

            self.availability[month] = (loading_time, unplanned_downtime, operating_time, availability)
        else:
            print(f"Data tidak ditemukan untuk bulan {month}. Harap masukkan bulan yang tepat.")

    def update_performance_rate_data(self, month):
        if month in self.performance_rate:
            print(f"Updating performance rate data for {month}:")
            irt = 646
            total_produksi = int(input("    Total Produksi  : "))

            _, _, operating_time, _ = self.availability[month]
            acp = round((total_produksi / operating_time), 3)
            performance_rate = round(((acp / irt) * 100), 3)

            self.performance_rate[month] = (total_produksi, acp, irt, performance_rate)
        else:
            print(f"Data tidak ditemukan untuk bulan {month}. Harap masukkan bulan yang tepat.")

    def update_quality_data(self, month):
        if month in self.quality:
            print(f"Updating quality data for {month}:")
            total_produksi = int(input("    Total Produksi  : "))
            _, _, jumlah_defect = self.defect_product[month]
            quality = round((((total_produksi - jumlah_defect) / total_produksi) * 100), 3)
            self.quality[month] = (total_produksi, jumlah_defect, quality)
        else:
            print(f"Data tidak ditemukan untuk bulan {month}. Harap masukkan bulan yang tepat.")

months = []

data = OEE(months)
data.input_month()
data.calculate_defect()
data.display_defect()
data.calculate_availability()
data.display_availability()
data.calculate_performance_rate()
data.display_performance_rate()
data.calculate_quality()
data.display_quality()
data.calculate_oee()
data.display_oee()

while True:
    if any(oee < 65 for _, _, _, oee in data.oee.values()):
        print("\n")
        print("=" * 99)
        print("{0:^99}".format('OEE dibawah 65 %, silahkan ubah data yang ada!'))
        print("=" * 99)
        print("\nPilih tindakan yang ingin dilakukan:")
        print("1. Update Defect Data")
        print("2. Update Availability Data")
        print("3. Update Performance Rate Data")
        print("4. Update Quality Data")
        print("5. Tampilkan Semua Data yang Sudah Dirubah")
        print("6. Keluar")
        pilihan = input("\nMasukkan pilihan Anda (1/2/3/4/5/6): ")
        if pilihan == '1':
            print("\n")
            print("=" * 99)
            print("{0:^99}".format("Mengubah Data Defect Product"))
            print("=" * 99)
            print("\n")
            month = input("Masukkan bulan yang ingin diubah datanya: ").capitalize()
            data.update_defect_data(month)
        elif pilihan == '2':
            print("\n")
            print("=" * 99)
            print("{0:^99}".format("Mengubah Data Availabilty"))
            print("=" * 99)
            print("\n")
            month = input("Masukkan bulan yang ingin diubah datanya: ").capitalize()
            data.update_availability_data(month)
        elif pilihan == '3':
            print("\n")
            print("=" * 99)
            print("{0:^99}".format("Mengubah Data Performance Rate"))
            print("=" * 99)
            print("\n")
            month = input("Masukkan bulan yang ingin diubah datanya: ").capitalize()
            data.update_performance_rate_data(month)
        elif pilihan == '4':
            print("\n")
            print("=" * 99)
            print("{0:^99}".format("Mengubah Data Quality Rate"))
            print("=" * 99)
            print("\n")
            month = input("Masukkan bulan yang ingin diubah datanya: ").capitalize()
            data.update_quality_data(month)
        elif pilihan == '5':
            print("\n")
            print("=" * 99)
            print("{0:^99}".format("Berikut Data yang Sudah Dirubah"))
            print("=" * 99)
            data.display_defect()
            data.display_availability()
            data.display_performance_rate()
            data.display_quality()
            data.display_oee()
        elif pilihan == '6':
            print("\n")
            print("=" * 99)
            print("{0:^99}".format("Terimakasih Sudah Menggunakan Program"))
            print("=" * 99)
            print("")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
    else:
        print("Nilai Overall Equipment Efectiveness Sudah Memenuhi Syarat")
        break