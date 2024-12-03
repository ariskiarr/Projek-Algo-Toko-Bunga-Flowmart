import os 
import csv 
import datetime 
import pandas as pd 
from pathlib import Path 

def MenuAwal():
    os.system('cls')
    print("="* 51)
    print(2*' ',"SELAMAT DATANG DI APLIKASI TOKO BUNGA FLOMART ")
    print("="*51)
    print("\n1. LOGIN")
    print("\n2. REGISTER")
    print("\n3. LOGIN ADMIN")

    input_menulogin = input("\nMasukkan Pilihan [1],[2],[3]: ")
    if input_menulogin == "1":
        Login()
    elif input_menulogin == "2" :
        if not(Path('akun.csv').is_file()):
                with open('akun.csv','w', newline='') as filecsv:
                    header = csv.DictWriter(filecsv, fieldnames=['username', 'password'], delimiter = ',')
                    header.writeheader()

                    Register()
                    input("\nEnter untuk melanjutkan")
                    MenuAwal()
        else:
            Register()
            input("\nEnter untuk melanjutkan")
            MenuAwal()

    elif input_menulogin == "3":
        if not(Path('admin.csv').is_file()):
            with open('admin.csv','w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['username', 'password'], delimiter = ',')
                header.writeheader()
                writer = csv.writer(filecsv)
                writer.writerow(['admin','123'])

                filecsv.close()
        LoginAdmin()
    else :
        input("\n=====| Inputan Salah, Enter Untuk Coba Lagi ! |=====")
        MenuAwal()


def Login():
    os.system('cls')
    print(51*"=")
    print(20*" ","LOGIN")
    print(51*"=")
    username = input("\nMasukan Usernamemu : ")
    password = input("Masukan Passwordmu : ")

    Hasil = False
    with open('akun.csv', 'r') as f:
        reader = csv.reader(f, delimiter=",")
        for x in reader:
            if x == [username,password]:
                Hasil = True
                break
            else:
                Hasil = False
        if Hasil == True:
            print('\n==============| Anda Berhasil Masuk |==============')
            input("\nEnter untuk lanjutkan")
            MenuUtama(username)
            
        elif Hasil == False:
            print("\n=======| Maaf anda gagal login, coba lagi ! |=======")
            input("\nEnter untuk lanjutkan")
            MenuAwal()


def Register():
    os.system('cls')
    print(51*"=")
    print(20*" ","REGISTER")
    print(51*"=")

    username = input("\nMasukan username baru : ")
    password = input('Masukan password baru : ')
    password2 = input('konfirmasi password : ')
    Hasil = False
    with open('akun.csv','r') as r:
     reader = csv.reader(r)
     for x in reader:
        if x[0] == username:
          Hasil = False
          break
        else:
            Hasil = True
     if Hasil == True:
        with open('akun.csv', 'a', newline="") as f:
         csvtambah1 = csv.writer(f)
         if password == password2:
            csvtambah1.writerow([username,password])
            print("\n===========| Berhasil Membuat Akun Baru |==========")
         else:
                input('\nPassword Salah, Enter Untuk Coba Lagi')
                Register()
     elif Hasil == False :
        input('\nMaaf Username sudah digunakan, Enter untuk coba lagi !')
        Register()


def LoginAdmin():
    os.system('cls')
    print(51*"=")
    print(18*" ","LOGIN ADMIN")
    print(51*"=")
    username = input("\nMasukan Usernamemu : ")
    password = input("Masukan Passwordmu : ")

    Hasil = False
    with open('admin.csv', 'r') as f:
        reader = csv.reader(f)
        for x in reader:
            if x == [username,password]:
                Hasil = True
                break
            else:
                Hasil = False
        if Hasil == True:
            print('\n==============| Anda Berhasil Masuk |==============')
            input("\nEnter untuk lanjutkan")
            MenuAdmin()
        elif Hasil == False:
            print("\n=======| Maaf anda gagal login, coba lagi ! |=======")
            input("\nEnter untuk lanjutkan")
            MenuAwal()


def MenuUtama(username):
    os.system('cls')
    print(51*"=")
    print(20*" ","MENU UTAMA")
    print(51*"=")
    MenampilkanStok()
    print(51*'=')
    print("\n1. TAMBAH KERANJANG\n2. TAMPILKAN KERANJANG\n3. EDIT KERANJANG\n4. KELUAR")
    input_MenuUtama = input("\nMasukkan Pilihan [1],[2],[3],[4]: ")
    if input_MenuUtama == "1" :
        if not(Path('keranjang.csv').is_file()):
            with open('keranjang.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['Username','Bunga','Jumlah','Harga','Total Harga'],  delimiter=',') 
                header.writeheader()
        TambahKeranjang(username)
    elif input_MenuUtama == "2" :
        MenampilkanKeranjang(username)
    elif input_MenuUtama == "3" :
        EditKeranjang(username)
    elif input_MenuUtama == "4":
        MenuAwal()
    else:
        input("\n=====| Inputan Salah, Enter Untuk Coba Lagi ! |=====")
        MenuUtama(username)


def TambahKeranjang(username):
    os.system('cls')
    print("="* 51)
    print(18*' ',"TAMBAH KERANJANG")
    print("="*51)
    MenampilkanStok()
    print(51*"=")
    df = pd.read_csv('stock.csv')
    Pilihan = int(input("\nPilih Nomor Barang Yang Diinginkan: "))
    panjang_dataStok = len(df)
    if Pilihan <= panjang_dataStok :
        jumlah = int(input('Jumlah Barang: '))
        if jumlah > int(df.iloc[Pilihan-1, 2]):
                input('\n====| Mohon maaf, Jumlah Stok Tidak Mencukupi |====  ')
                TambahKeranjang(username)
        else:
            with open('keranjang.csv','a',newline="") as f:
                bunga = df.iloc[Pilihan-1,0]
                harga = df.iloc[Pilihan-1,1]
                total_harga = harga * jumlah
                writer = csv.writer(f)
                writer.writerow([username,bunga,jumlah,harga,total_harga])
                f.close()
                pf = pd.read_csv('keranjang.csv')
                a = pf[pf['Username'] == username]
                a = a.iloc[:, 1:5]
                os.system('cls')
                print("="* 53)
                print(16*' ',"TAMPILAN KERANJANG")
                print("="*53)
                Keranjang(username)
                total_pembelian = 0
                for x in range(len(a)):
                    total_pembelian += a.iloc[x,3]
                print(53*'=')
                print(f'Total Harga Pembelian : {total_pembelian}')
                print(53*'=')
                print("\n1. PILIH BARANG LAGI\n2. KEMBALI\n3. ENTER UNTUK BAYAR")
                input_jawaban =input("\nMasukkan Pilihan [1],[2],[Enter] : ")
                if input_jawaban == "1":
                    TambahKeranjang(username)
                elif input_jawaban == "2" :
                    MenuUtama(username)
                elif input_jawaban == "" or input_jawaban =='3' :
                    Pembayaran(username)
                else:
                    input('\n Maaf inputan tidak sesuai, Enter untuk kembali !')
                    MenuUtama()
    else: 
        input('\n Maaf inputan tidak sesuai, Enter untuk coba lagi !')
        TambahKeranjang(username)


def MenampilkanKeranjang(username):
    os.system('cls')
    print(51*"=")
    print(15*" ","TAMPILAN KERANJANG")
    print(51*"=")
    Keranjang(username)
    total_pembelian = 0
    pf = pd.read_csv('keranjang.csv')
    a = pf[pf['Username'] == username]
    a = a.iloc[:, 1:5]
    for x in range(len(a)):
       total_pembelian += a.iloc[x,3]
    print(51*'=')
    print(f'Total Harga Pembelian : {total_pembelian}')
    print(51*'=')
    print('\n1. BAYAR\n2. ENTER UNTUK KEMBALI')
    inputan = input('\nMasukkan pilihan [1],[Enter] : ')
    if inputan == '1' :
        Pembayaran(username)
    else : 
        MenuUtama(username)
        

def EditKeranjang(username) :
    os.system('cls')
    print(51*"=")
    print(15*" ","MENU EDIT KERANJANG")
    print(51*"=")
    Keranjang(username)
    print(51*"=")
    print("\n1. TAMBAH JUMLAH BARANG\n2. KURANGI JUMLAH BARANG\n3. MENGHAPUS BARANG\n4. KEMBALI ")
    input_EditKeranjang = input("\nMasukkan pilihan [1],[2],[3],[4]: ")
    if input_EditKeranjang == "1" : 
        TambahJumlahBarang(username)
    elif input_EditKeranjang == "2":
        KurangiJumlahBarang(username)
    elif input_EditKeranjang == "3":
        HapusBarang(username)
    elif input_EditKeranjang == "4":
        MenuUtama(username)
    else:
        input("\n======| Maaf inputan salah, Enter untuk Coba lagi! |======")
        EditKeranjang(username)


def TambahJumlahBarang(username):
    os.system('cls')
    print("="* 51)
    print(15*' ',"TAMBAH JUMLAH BARANG")
    print("="*51)
    Keranjang(username)
    print(51*"=")
    pf = pd.read_csv('keranjang.csv')
    df = pd.read_csv('stock.csv')
    a = pf[pf['Username'] == username]
    a = a.iloc[:, 1:5]    
    pilihan = int(input('\nPilih Nomor Barang Yang Ingin DiTambahkan: '))
    if pilihan <= len(a):
        Tambah = int(input('Jumlah Barang Yang Ingin Ditambahkan: '))
        bunga = a.iloc[pilihan-1,0]
        NoIndex1 = df.loc[df['Bunga'] == bunga].index
        NoIndex1= NoIndex1.values
        NoIndex1 = NoIndex1[0]
        stock = df.iloc[NoIndex1,2]

        if Tambah > stock:
            input('\n====| Mohon maaf, Jumlah Stok Tidak Mencukupi |====  ')
            TambahJumlahBarang(username)
        else: 
            NoIndex = a.index[pilihan-1]
            jumlah = int(a.iloc[pilihan-1,1])
            harga = int(a.iloc[pilihan-1, 2])
            JumlahBaru = jumlah + Tambah
            total_hargabaru = harga * JumlahBaru
            pf.iloc[NoIndex,2] = JumlahBaru
            pf.iloc[NoIndex,4]  = total_hargabaru
            pf.to_csv('keranjang.csv', index=False)
            os.system('cls')
            print("="* 51)
            print(15*' '," TAMBAH JUMLAH BARANG")
            print("="*51)
            Keranjang(username)
            print(51*"=")
            input("\nEnter untuk Selesai!")
            EditKeranjang(username)
    else:
        input('\n====| Mohon maaf, Inputan Tidak Sesuai |====  ')
        TambahJumlahBarang(username)


def KurangiJumlahBarang(username):
    os.system('cls')
    print("="* 51)
    print(15*' ',"MENGURANGI JUMLAH BARANG")
    print("="*51)
    Keranjang(username)
    print(51*"=")
    pf = pd.read_csv('keranjang.csv')

    a = pf[pf['Username'] == username]
    a = a.iloc[:, 1:5]
    pilihan = int(input('\nPilih Nomor Barang Yang Ingin Dikurangi: '))
    if pilihan <= len(a):
        jumlah = int(a.iloc[pilihan-1,1])
        harga = int(a.iloc[pilihan-1, 2])
        Kurang = int(input('Jumlah Barang Yang Ingin Dikurangi: '))
        if Kurang < jumlah:
            NoIndex = a.index[pilihan-1]
            JumlahBaru = jumlah - Kurang
            total_hargabaru = harga * JumlahBaru
            pf.iloc[NoIndex,2] = JumlahBaru
            pf.iloc[NoIndex,4]  = total_hargabaru
            pf.to_csv('keranjang.csv', index=False)
        else:
            input('\n====| Mohon maaf, Inputan Anda Salah, Tolong Cek Kembali |====  ')
            KurangiJumlahBarang(username)

    else:
        input('\n====| Mohon maaf, Inputan Tidak Sesuai |====  ')
        KurangiJumlahBarang(username)

    os.system('cls')
    print("="* 51)
    print(15*' ',"MENGURANGI JUMLAH BARANG")
    print("="*51)
    Keranjang(username)
    print(51*"=")
    input("\nEnter untuk Selesai!")
    EditKeranjang(username)


def HapusBarang(username):
    os.system('cls')
    print("="* 51)
    print(15*' ',"MENGHAPUS BARANG")
    print("="*51)
    Keranjang(username)
    hapus = int(input("\nPilih Nomor Barang Yang Ingin Dihapus : "))
    pf = pd.read_csv('keranjang.csv')
    a = pf[pf['Username'] == username]
    if hapus <= len(a):
        NoIndex = a.index[hapus-1]
        pf = pf.drop(NoIndex)
        pf.to_csv('keranjang.csv', index=False)   
        print("\n==============| Data Berhasil Dihapus |=============\n")
        input("Enter Untuk Melanjutkan")
        os.system('cls')
        print("="* 51)
        print(15*' ',"TAMPILAN KERANJANG")
        print("="*51)
        Keranjang(username)
        print(51 *'=')
        print("\n1. Hapus Lagi\n2. Enter Untuk Selesai ")
        inputan = input("\n Masukkan Pilihan [1],[Enter]: ")
        if inputan == "1" :
            HapusBarang(username)
        elif inputan == "" or inputan == "2":
            MenuUtama(username)
        else: 
            print("=====| Inputan Salah, Mohon coba lagi! |=====")
            HapusBarang(username)
    else:
        input('\n====| Mohon maaf, Inputan Tidak Sesuai |====  ')
        HapusBarang(username)



def Keranjang(username):
    data = pd.read_csv("keranjang.csv")
    a = data[data['Username'] == username]
    a = a.iloc[:, 1:5]
    a.index = range(1, len(a) + 1)
    print(a)


def Pembayaran(username):
    total_pembelian = 0
    data = pd.read_csv("keranjang.csv")
    a = data[data['Username'] == username]
    a = a.iloc[:, 1:5]
    for x in range(len(a)): 
             total_pembelian += a.iloc[x,3] 
    df = pd.read_csv('stock.csv')

    os.system('cls')
    print("="* 51)
    print(16*' ',"MENU PEMBAYARAN")
    print("="*51)
    print(f"Total Pembayaran   : Rp {total_pembelian}")
    bayar_tagihan = int(input('Masukkan Uang Anda : Rp '))
    kembalian = bayar_tagihan - total_pembelian
    bunga = []
    Bunga = ""
    jumlahbunga = []
    if bayar_tagihan < total_pembelian :
        input('\nUang anda tidak cukup! Silahkan masukkan uang kembali !')
        Pembayaran(username)
    else :
        print(f"\nTotal Kembalian    : Rp {kembalian}")
        print(51*'=')
        print(3*' ','Terima Kasih Sudah Berbelanja Di Flowmart !')
        print(51*'=')
        for x in range(len(a)):
            nama_bunga = a.iloc[x,0] 
            Jumlah = a.iloc[x,1] 
            NoIndex = df.loc[df['Bunga'] == nama_bunga].index
            NoIndex= NoIndex.values 
            NoIndex = NoIndex[0] 
            Stokbaru = df.loc[NoIndex,'Stok'] - Jumlah
            df.loc[NoIndex, 'Stok'] = Stokbaru 
            df.to_csv('stock.csv', index = False)
        for x in range(len(a)):
            nama = a.iloc[x,0]
            jumlah = str(a.iloc[x,1])
            bunga.append(nama)
            jumlahbunga.append(jumlah)
    
        for x in range(len(bunga)):
            if x == 0:
                Bunga += f"{bunga[x]}:{jumlahbunga[x]}"
            elif x > 0:
                Bunga += ','+' ' + f'{bunga[x]}:{jumlahbunga[x]}'
        

        TambahRiwayat(username,total_pembelian,Bunga) 

        for x in range(len(a)):
            NoIndex = a.index[x]
            data = data.drop(NoIndex) 
            data.to_csv('keranjang.csv', index=False)
        input("\n Enter untuk Kembali !")     
        MenuUtama(username)


def MenuAdmin():
    os.system('cls')
    print("="* 51)
    print(6*' ',"SELAMAT DATANG ADMIN TOKO BUNGA FLOMART ")
    print("="*51)
    print("\n1. STOK BARANG \n2. RIWAYAT\n3. KEMBALI")

    input_MenuAdmin = input("\nMasukkan Pilihan [1],[2],[3] ")
    if input_MenuAdmin == "1" :
        MenuStokBarang()
    elif input_MenuAdmin == "2" :
        Riwayat()
    elif input_MenuAdmin =="3" :
        MenuAwal()
    else:
        input("\n=====| Inputan Salah, Enter Untuk coba lagi! |=====")
        MenuAdmin()


def MenuStokBarang():
    os.system('cls')
    print("="* 51)
    print(20*' ',"STOK BARANG")
    print("="*51)
    print("\n1. MENAMBAHKAN STOK BARANG\n2. MENGURANGI STOK BARANG\n3. MENAMPILKAN STOK\n4. KEMBALI")
       
    input_MenuStok = input("\nMasukkan pilihan anda [1],[2],[3],[4]: ")
    if input_MenuStok == "1" :
        MenambahStok()
    elif input_MenuStok == "2":
        MengurangiStok()
    elif input_MenuStok == "3":
        os.system('cls')
        print("="* 51)
        print(16*' ',"TAMPILAN STOK BARANG")
        print("="*51)
        MenampilkanStok()
        print(51*'=')
        input("\nEnter Untuk Kembali !")
        MenuStokBarang()
    elif input_MenuStok == "4" :
        MenuAdmin()
    else: 
        input("\n====| Inputan Salah, Enter Untuk Coba lagi ! |=====")
        MenuStokBarang()


def MembuatStok() :
        if not(Path('stock.csv').is_file()): 
            with open('stock.csv','w', newline='') as filecsv: 
                header = csv.DictWriter(filecsv, fieldnames=['Bunga', 'Harga','Stok'], delimiter = ',') 
                header.writeheader() 
                csvwriter = csv.writer(filecsv) 
                csvwriter.writerow(['Mawar',1500,50]) 
                csvwriter.writerow(['Baby Breath',2000,50]) 
                csvwriter.writerow(['Hydrangea',2500,50])
                csvwriter.writerow(['Peony',2500,50])
                csvwriter.writerow(['Garbera',1500,50])
                csvwriter.writerow(['Lily of the Valley',2000,50])
                csvwriter.writerow(['Calla Lily',2000,50])
                csvwriter.writerow(['Gardenia',1500,50])
                csvwriter.writerow(['Tulip',1500,50])
                csvwriter.writerow(['Matahari',2000,50])

def MenampilkanStok():
    MembuatStok()  
    df = pd.read_csv('stock.csv') 
    df.index =  range(1,len(df) + 1,) 
    print(df) 


def MenambahStok():
    os.system('cls')
    print("="* 51)
    print(15*' ',"MENAMBAH STOK BARANG")
    print("="*51)
    MenampilkanStok()  
    print(51*'=') 
    df = pd.read_csv('stock.csv') 
    Pilihan = int(input("\nPilih Nomor Bunga Yang Stoknya Mau Ditambahkan: "))
    Stok = df.iloc[Pilihan-1,2]
    Tambah = int(input('Jumlah Stock Yang Ingin Ditambahkan: '))
    StokBaru = Stok + Tambah 
    df.iloc[Pilihan-1,2] = StokBaru 
    df.to_csv('stock.csv', index=False) 
    os.system('cls')
    print(52*"=")
    print(18*' ',"TAMPILAN STOK BARU")
    print(52*"=")
    MenampilkanStok() 
    print("\n===========| Stok Berhasil Ditambahkan |============")
    print("\n1. Tambah stok\n2. Enter Untuk Kembali")
    inputan = input("Maukkan Pilihan [1] atau [Enter] : ") 
    if inputan == "1": 
        MenambahStok()
    elif inputan == "" or inputan == '2':
        MenuStokBarang()
    else :
        input("\n======| Inputan Salah, Enter Untuk kembali! |=====")
        MenuStokBarang()


def MengurangiStok():
    os.system('cls')
    print("="* 51)
    print(15*' ',"MENGURANGI STOK BARANG")
    print("="*51)
    MenampilkanStok() 
    print(51*'=')
    df = pd.read_csv('stock.csv') 
    Pilihan = int(input("\nPilih Nomot Bunga Yang Stoknya Mau Dikurangi: ")) 
    Stok = df.iloc[Pilihan-1,2]
    Kurang = int(input('Jumlah Stok Yang Ingin Dikurangi: ')) 
    StokBaru = Stok - Kurang  
    df.iloc[Pilihan-1,2] = StokBaru
    df.to_csv('stock.csv', index=False)
    os.system('cls')
    print(52*'=')
    print(18*' ',"TAMPILAN STOK BARU")
    print(52*"=")
    MenampilkanStok()
    print("\n============| Stok Berhasil Dikurangi |=============")
    print("\n1. Kurangi Stok \n2. Enter Untuk Kembali ")
    inputan = input("\nMaukkan Pilihan [1] atau [Enter] : ")
    if inputan == "1":
        MengurangiStok()
    elif inputan == "":
        MenuStokBarang()
    else :
        input("\n=====| Inputan Salah, Enter Untuk kembali ! |=====")
        MenuStokBarang()


def TambahRiwayat(username,total_pembelian,Bunga):
    waktu_sekarang = datetime.datetime.now()
    tanggal_pembelian = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")

    riwayat_path = Path('riwayat.csv')

    if not riwayat_path.is_file() :
        with open(riwayat_path, 'w', newline='') as filecsv:
            header = csv.DictWriter(filecsv, fieldnames=['Username', 'Tanggal/Waktu', "Bunga", 'Total Harga Pembelian'], delimiter=',')
            header.writeheader()

    with open(riwayat_path, 'a', newline='') as filecsv:
        writer = csv.writer(filecsv)
        writer.writerow([username,tanggal_pembelian,Bunga,total_pembelian]) 


def Riwayat():
    os.system('cls')
    print("="* 90)
    print(40*' ',"RIWAYAT")
    print("="*90)
    df = pd.read_csv('riwayat.csv') 
    df.index = range(1,len(df) + 1) 
    print(df)
    jumlah_total_pembelian = 0
    for x in range(len(df)):
        jumlah_total_pembelian += df.iloc[x,3]
    print(90*'=')
    print(f'Jumlah Total Pembelian : Rp {jumlah_total_pembelian}')
    print(90*'=')
    input('\nEnter untuk Kembali')
    MenuAdmin()


MenuAwal()


def obat():
    return
def manu():
    return
def gyu():
    pass