import json
import pwinput
from prettytable import PrettyTable
import os
os.system("cls")

#dictionary
akun_admin = {"Username" : ["adminpa3"],
                "Password" : ["123"]}

uang_cust = {"Cash": 0, "e-Money": 0, "hasil_topup": 0}

#prettytable
tabel_produk = PrettyTable()
tabel_produk.field_names = ["No","Nama Produk","Harga Produk", "Stok Produk"]


                                        #DATABASE
#json login
jsonlogin = "regis.json"
with open(jsonlogin, "r") as lihat_admin:
    admin = json.load(lihat_admin)

def tambah_admin(data_admin):
    with open(jsonlogin, "w") as add_admin:
        json.dump(data_admin, add_admin, indent=4)

name = admin.get("Nama")
pasw = admin.get("Password")

#json produk
jsonproduk = open("produk.json")
data = json.loads(jsonproduk.read())

def dinamis():
    with open("produk.json", "w") as sn:
        json.dump(data, sn)

                                        #LOGIN
#login untuk admin
def login_admin():
    print("=============== LOGIN ADMIN =================\n")
    while True :
        try : 
            Username1 = input("~ Username : ")
            Password1 = pwinput.pwinput("~ Password : ")

            cari_admin = akun_admin.get("Username").index(Username1)
            cari_pasw = akun_admin.get("Password").index(Password1)

            if Username1 == akun_admin.get("Username")[cari_admin] and Password1 == akun_admin.get("Password")[cari_pasw]:
                print("")
                print("            ---LOGIN BERHASIL---\n")
                print("")
                print("Selamat datang,", akun_admin.get("Username")[cari_admin])
                break
      
        except ValueError :
            print("\n[] USERNAME ATAU PASSWORD SALAH")
            print("[] SILAHKAN LOGIN LAGI\n")

#login customer
def registrasi_akun():
    print("=============== REGISTRASI AKUN BARU ================\n")
    while True:
        try:
            nama = input("~ Masukan Username yang anda inginkan : ")
            if nama == "":
                print("[] INPUT TIDAK BOLEH KOSONG")
                print("[] SILAHKAN COBA LAGI\n")
            elif all(x.isalpha() for x in nama):
                if nama in admin["Nama"]:
                    print("[] USERNAME TELAH TERDAFTAR\n")
                    while True :
                        print("1. Login")
                        print("2. Registrasi Akun Baru")
                        p = input("Masukan pilihan anda : ")
                        if p == "1":
                                login_cust()
                                break
                        elif p == "2":
                                print("[] SILAHKAN MASUKAN USERNAME BARU\n")
                                break
                        else :
                                print("[] PILIHAN TIDAK TERSEDIA\n")
                else:
                    password = pwinput.pwinput("~ Masukan Password yang anda inginkan : ")
                    if password == "":
                        print("[] INPUT TIDAK BOLEH KOSONG")
                        print("[] SILAHKAN COBA LAGI\n")
                    elif all(x.isnumeric() for x in password):
                        name.append(nama)
                        pasw.append(password)
                        tambah_admin(admin)

                        print("\n          ---REGISTRASI AKUN BERHASIL---\n")
                        login_cust()
                        break
                    else :
                        print("[] PASSWORD HARUS ANGKA")
            else :
                print("[] USERNAME HANYA BOLEH ALPHABET")
        except :
            print("INVALID INPUT\n")

def login_cust():
    print("======================= LOGIN CUSTOMER =======================\n")
    try:
        while True :
            nama = input("~ Username : ")
            password = pwinput.pwinput("~ Password : ")
            cari = name.index(nama)
            if nama == name[cari] and password == pasw[cari]:
                print("                      ---LOGIN BERHASIL---\n")
                print("\nSelamat Datang", name[cari])
                menucustomer()
                break
            elif nama == name[cari] and password != pasw[cari]:
                print("[] PASSWORD SALAH")
                print("[] SILAHKAN COBA LAGI\n")

    except ValueError:
        print("\n[] USERNAME BELUM TERDAFTAR")
        print("[] SILAHKAN COBA LAGI\n")
        login_cust()

                                            #MENU-MENU

def menu_awal():
    print(
        """
                --------- MASUK SEBAGAI ---------
                |1.|          ADMIN             |
                |2.|         CUSTOMER           |
                |3.|        EXIT (END)          |
                ---------------------------------
        """
    )

def menu_homeadmin():
    print(
        """
                ------------- MENU HOME ADMIN -------------
                |1.| TAMBAH PRODUK                        |   
                |2.| TAMPILKAN PRODUK                     |
                |3.| UBAH PRODUK                          |
                |4.| HAPUS PRODUK                         |   
                |5.| EXIT                                 |
                -------------------------------------------
        """
    )

def customer_option():
    print(
        """
                ------------- PILIH LOGIN -------------
                |1.| Login                            |
                |2.| Registrasi                       |
                |3.| Exit                             |
                ---------------------------------------
        """
    )

def menu_homecust():
    print(
        """
                ----------------------------------------
                |          MENU HOME CUSTOMER          |
                ----------------------------------------
                |1.| Beli Produk                       |
                |2.| Top Up E-Money                    |
                |3.| Lihat Saldo E-Money               |
                |4.| Exit                              |
                ----------------------------------------
        """
    )

def top_up():
    print(
        """
                --------- TOP UP E-MONEY ---------
                ----------------------------------
                |1.|  Rp 500.000                 |
                |2.|  Rp 1.000.000               |
                |3.|  Rp 3.000.000               |
                |4.|  Rp 5.000.000               |
                |5.|  Rp 8.000.000               |
                ----------------------------------
        """
    )

def metode_buy():
    print(
        """
                ---------------------------------
                |       METODE PEMBAYARAN       |
                ---------------------------------
                |1.| Cash                       |
                |2.| E-Money                    |
                ---------------------------------
            """
    )

# CRUD admin
def create():
    read()
    print("\n============ MENAMBAHKAN PRODUK BARU ============")
    while True:
        try :
            tambah = str(input("~ Nama Produk : "))
            if tambah in data["Nama Produk"]:
                cari_produk = data.get("Nama Produk").index(tambah)
                data["Stok Produk"][cari_produk] = data.get("Stok Produk")[cari_produk] +1
                read()
                while True :
                    balik = input("Apakah anda ingin ke menu home? (y/t) : ")
                    if balik == "y":
                        menuadmin()
                        break
                    elif balik == "t":
                        create()
                    else :
                        print("[] PILIHAN TIDAK TERSEDIA")
            elif all(x.isspace () for x in tambah):
                print("[] INPUT TIDAK BOLEH KOSONG")
            elif all(x.isalpha() for x in tambah) and len(tambah) <= 20:
                break
            elif len(tambah) > 20:
                print("[] Nama Produk tidak boleh lebih dari 20 huruf\n")
            elif all(x.isnumeric() for x in tambah):
                print("[] INPUT TIDAK BOLEH ANGKA\n")
            else:
                print("[] INPUT YANG DIMASUKAN TIDAK SESUAI")
                print("[] SILAHKAN COBA LAGI\n")
            dinamis()
        except :
            print("[] PERHATIKAN INPUT")

    while True:
        try:
            harga = int(input("~ Harga Produk : Rp "))

            if harga < 0:
                print("HARGA TIDAK BOLEH KURANG DARI 0")
            elif harga == 0:
                print("HARGA HARUS LEBIH DARI 0")
            elif harga < 100000000 :
                break
            elif harga > 100000000 :
                print("[] Harga Produk tidak boleh lebih dari 100000000\n")
            else:
                print("[] TOLONG MASUKAN INPUT YANG BENAR")
                print("[] SILAHKAN COBA LAGI\n")
        except ValueError:
            print("[] MASUKAN ANGKA")

    while True:
        try:
            stok = int(input("~ Stok Produk : "))
            if stok < 0:
                print("STOK TIDAK BOLEH KURANG DARI 0")
            elif stok > 0 and stok <= 1000 :
                break
            elif stok > 1000 :
                print("[] Stok Produk tidak boleh lebih dari 1000\n")
            else :
                print("[] TOLONG PERHATIKAN INPUT")
        except ValueError:
            print("[] MASUKAN ANGKA")

    data["Nama Produk"].append(tambah)
    data["Harga Produk"].append(harga)
    data["Stok Produk"].append(stok)
    dinamis()
    print("--- PRODUK BERHASIL DITAMBAHKAN ---\n")

def read():
    no = 1

    tabel_produk.clear_rows()
    for i in range(len(data["Nama Produk"])):
        tabel_produk.add_row(
            [
                no,
                data["Nama Produk"][i],
                "Rp." + str(data["Harga Produk"][i]),
                data["Stok Produk"][i],
            ]
        )
        no += 1
        dinamis()

    print(tabel_produk)


def update():
    read()
    print("\n================ MENGUBAH PRODUK ================")
    while True:
        try :
            nama_p = input("~ Masukkan nama produk yang ingin diubah : ")
            cari_n = data.get("Nama Produk").index(nama_p)
            break
        except :
            print("\n[] NAMA PRODUK TIDAK DITEMUKAN")
            print("[] SILAHKAN COBA LAGI")
           
    while True :
        nm = input("\n>> Apakah anda ingin mengubah nama produk? (y/t) : ")
        if nm == "y":
            nub = input("~ Masukan nama produk baru : ")
            if nub in data["Nama Produk"] :
                print("[] NAMA PRODUK SUDAH ADA")
                print("[] SILAHKAN MASUKAN NAMA PRODUK YANG BERBEDA\n")
            elif all(x.isalpha() for x in nub) and len(nub) <= 20:
                data.get("Nama Produk")[cari_n] = nub
                print("--- Nama Produk berhasil diubah ---\n")
                break
            else :
                print("[] NAMA PRODUK HANYA BOLEH ALPHABET")
                print("[] NAMA TIDAK BOLEH LEBIH DARI 20 HURUF")

        elif nm == "t":
            break
        else :
            print("[] PILIHAN TIDAK TERSEDIA")

    while True:
        hm = input("\n>> Apakah anda ingin mengubah harga produk? (y/t) : ")
        if hm == "y":
            while True :
                try :
                    hp_b = int(input("~ Masukkan harga produk baru : Rp. "))
                    if hp_b < 0:
                        print("HARGA TIDAK BOLEH KURANG DARI 0")
                    elif hp_b == 0:
                        print("HARGA HARUS LEBIH DARI 0")
                    elif hp_b > 0 and hp_b < 100000000:
                        data.get("Harga Produk")[cari_n] = hp_b
                        print("--- Harga Produk berhasil diubah ---\n")
                        break
                    else :
                        print("[] HARGA PRODUK TIDAK BISA LEBIH DARI 100000000")
                except :
                    print("[] PERHATIKAN INPUTAN")
            break
        elif hm == "t":
            break
        else :
            print("[] PILIHAN TIDAK TERSEDIA")
        

    while True:
        sm = input("\n>> Apakah anda ingin mengubah stok produk? (y/t) : ")
        if sm == "y":
            while True :
                try:
                    sp_b = int(input("~ Masukkan stok produk baru : "))
                    if sp_b < 0 :
                        print("STOK TIDAK BOLEH KURANG DARI 0")
                    elif sp_b <= 1000:
                        data.get("Stok Produk")[cari_n] = sp_b
                        print("--- Stok Produk berhasil diubah ---\n")
                        break
                    else:
                        print("[] STOK TIDAK BOLEH LEBIH DARI 1000")
            
                except ValueError :
                    print("\n[] TOLONG MASUKAN ANGKA")
                    print("[] SILAHKAN COBA LAGI")
            break
        elif sm == "t":
            break
        else :
            print("[] PILIHAN TIDAK TERSEDIA")

    dinamis()
    read()


def delete():
    read()
    print("\n=============== MENGHAPUS PRODUK ================")
    while True:
        try:
            hapus_n = input("~ Masukan nama barang yang akan dihapus : ")
            if hapus_n == "" :
                print("input tidak boleh kosong")
            elif hapus_n in data["Nama Produk"]:
                cari_n = data.get("Nama Produk").index(hapus_n)
                data.get("Nama Produk").pop(cari_n)
                data.get("Harga Produk").pop(cari_n)
                data.get("Stok Produk").pop(cari_n)
            elif hapus_n not in data["Nama Produk"]:
                print("----- PRODUK TIDAK DITEMUKAN -----")
            elif all(x.isspace for x in hapus_n):
                print("Input tidak boleh kosong")
                
            dinamis()
            read()
            break
        except:
            print("\n[] PRODUK TIDAK DITEMUKAN")
            print("[] SILAHKAN COBA LAGI")


def menuadmin():
    while True:
        try :
            menu_homeadmin()
            Menu = int(input("~ Masukan Menu yang dipilih : "))
            if Menu == 1:
                os.system("cls")
                while True :
                    create()
                    while True:
                        Lanjut = input(">> Apakah anda ingin menambahkan data lagi? (y/t) : ")
                        if Lanjut == "y":
                            create()
                        elif Lanjut == "t":
                            os.system('cls')
                            menuadmin()
                        else :
                            print("[] TOLONG PERHATIKAN INPUT")
                    
            elif Menu == 2:
                os.system("cls")
                while True :
                    read()
                    while True :
                        Lanjut = input(">> Apakah anda ingin kembali ke Menu Home? (y/t) : ")
                        if Lanjut == "y":
                            menuadmin()
                        elif Lanjut == "t":
                            break
                        else :
                            print("[] TOLONG PERHATIKAN INPUT")

            elif Menu == 3:
                os.system("cls")
                while True:
                    update()
                    while True:
                        Lanjut = input(">> Apakah anda ingin mengubah data lagi? (y/t) : ")
                        if Lanjut == "y":
                            update()
                        elif Lanjut == "t":
                            os.system('cls')
                            menuadmin()
                        else :
                            print("[] TOLONG PERHATIKAN INPUT")

            elif Menu == 4:
                os.system("cls")
                while True :
                    delete()
                    while True:
                        Lanjut = input(">> Apakah anda ingin menghapus data lagi? (y/t) : ")
                        if Lanjut == "y":
                            delete()
                        elif Lanjut == "t":
                            os.system('cls')
                            menuadmin()
                        else :
                            print("[] TOLONG PERHATIKAN INPUT")

            elif Menu == 5:
                os.system('cls')
                raise SystemExit

            else:
                print("[] PILIHAN TIDAK TERSEDIA")
                print("[] SILAHKAN COBA LAGI")
                menuadmin()

        except ValueError:
            print("[] TOLONG MASUKAN INPUT DENGAN BENAR")
            print("[] SILAHKAN COBA LAGI\n")
          

#menu customer       
def menu_logincust():
    while True:
        print("                           SELAMAT DATANG DI")
        print("                       TOKO ALAT OLAHRAGA ASTERIX \n")
        customer_option()
        try:
            pil = int(input("~ Masukan Pilihan Anda : "))
            if pil == 1:
                os.system("cls")
                login_cust()
                break
            elif pil == 2:
                os.system("cls")
                registrasi_akun()
                break
            elif pil == 3:
                os.system("cls")
                print("---------- PROGRAM TELAH SELESAI ----------")
                print("--------------- TERIMA KASIH --------------")
                exit()
            
            else:
                print("[] PILIHAN TIDAK TERSEDIA")
                print("[] SILAHKAN COBA LAGI\n")
                menu_logincust()
                break
        except ValueError:
            print("[] TOLONG MASUKAN ANGKA\n")
            
def emoney():
    while True:
        try :
            top_up()
            topup = int(input("Pilih Top Up : "))
            if topup == 1:
                uang_cust["hasil_topup"] = uang_cust["e-Money"] + 500000
                uang_cust["e-Money"] = uang_cust["hasil_topup"]

                with open("emoney.txt", "a") as c:
                    print(
                        "===========================================================",
                        file=c,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 500000, file=c)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["hasil_topup"],
                        end="\n",
                        file=c,
                    )
                    print(
                        "===========================================================",
                        file=c,
                    )

                print("\n--- Pengisian saldo e-Money Berhasil ---")
                print("Saldo e-Money : Rp", uang_cust["hasil_topup"])
                break
            elif topup == 2:
                uang_cust["hasil_topup"] = uang_cust["e-Money"] + 1000000
                uang_cust["e-Money"] = uang_cust["hasil_topup"]

                with open("emoney.txt", "a") as c:
                    print(
                        "===========================================================",
                        file=c,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 1000000, file=c)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["hasil_topup"],
                        end="\n",
                        file=c,
                    )
                    print(
                        "===========================================================",
                        file=c,
                    )

                print("\n--- Pengisian saldo e-Money Berhasil ---")
                print("Saldo e-Money : Rp", uang_cust["hasil_topup"])
                break
            elif topup == 3:
                uang_cust["hasil_topup"] = uang_cust["e-Money"] + 3000000
                uang_cust["e-Money"] = uang_cust["hasil_topup"]

                with open("emoney.txt", "a") as c:
                    print(
                        "===========================================================",
                        file=c,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 3000000, file=c)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["hasil_topup"],
                        end="\n",
                        file=c,
                    )
                    print(
                        "===========================================================",
                        file=c,
                    )

                print("\n--- Pengisian saldo e-Money Berhasil---")
                print("Saldo e-Money : Rp", uang_cust["hasil_topup"])
                break
            elif topup == 4:
                uang_cust["hasil_topup"] = uang_cust["e-Money"] + 5000000
                uang_cust["e-Money"] = uang_cust["hasil_topup"]
                with open("emoney.txt", "a") as c:
                    print(
                        "===========================================================",
                        file=c,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 5000000, file=c)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["hasil_topup"],
                        end="\n",
                        file=c,
                    )
                    print(
                        "===========================================================",
                        file=c,
                    )

                print("\n--- Pengisian saldo e-Money Berhasil ---")
                print("Saldo e-Money : Rp", uang_cust["hasil_topup"])
                break
            elif topup == 5:
                uang_cust["hasil_topup"] = uang_cust["e-Money"] + 8000000
                uang_cust["e-Money"] = uang_cust["hasil_topup"]

                with open("emoney.txt", "a") as c:
                    print(
                        "===========================================================",
                        file=c,
                    )
                    print("Saldo e-Money berhasil ditambah Rp", 8000000, file=c)
                    print(
                        "Saldo e-Money anda sekarang Rp",
                        uang_cust["hasil_topup"],
                        end="\n",
                        file=c,
                    )
                    print(
                        "===========================================================",
                        file=c,
                    )

                print("\n--- Pengisian saldo e-Money Berhasil ---")
                print("Saldo e-Money : Rp", uang_cust["hasil_topup"])
                break
            else :
                print("[] PILIHAN TIDAK TERSEDIA")
                print("[] SILAHKAN COBA LAGI\n")
        except :
            print("[] MOHON PERHATIKAN INPUTAN")
            break

def buy():
    while True:
        read()
        dinamis()
        belanja = input("~ Masukan nama produk yang ingin anda beli : ")
        if belanja in data["Nama Produk"]:
            cari_produk = data.get("Nama Produk").index(belanja)

            if data["Stok Produk"][cari_produk] >= 0:
                jml = int(input("~ Jumlah Produk : "))
                if jml > 0:
                    if jml < data["Stok Produk"][cari_produk] or jml == data["Stok Produk"][cari_produk]:
                    
                            cari_harga = data.get("Nama Produk").index(belanja)
                            harga_total = data.get("Harga Produk")[cari_harga]
                            total_a = jml * harga_total
                            
                            metode_pembayaran(belanja, jml, total_a, cari_produk)
                            
                    else :
                        print ("[] STOK PRODUK TIDAK CUKUP")
                        print("[] SILAHKAN COBA LAGI\n")
                else :
                    print("[] JUMLAH TIDAK BOLEH KURANG DARI 0")   
            else : 
                print("--- STOK PRODUK TELAH HABIS ---")
                break
        else:
            print("[] PRODUK TIDAK DITEMUKAN")
                    
        while True:
            try:
                Lanjut = input(">> Apakah anda ingin belanja lagi? (y/t) : ")
                if Lanjut == "y":
                    pass
                    buy()
                elif Lanjut == "t":
                    os.system('cls')
                    menucustomer()
                    break
                else:
                    print("[] INPUT SALAH\n")
            except:
                print("[] MOHON PERHATIKAN INPUTAN\n")
            


def metode_pembayaran(belanja, jml, total_a, cari_produk):
    
    with open("pembelianproduk.txt", "a") as n:
        print()
        print("\n============ PEMBELIAN PRODUK ============", file=n) 
        print("- Barang :", belanja, file=n)
        print("- Jumlah :", jml, file=n)
        print("")
        print("Total: Rp", total_a, file=n)
        print("==========================================", file=n)
    print("    ```Silahkan lakukan pembayaran```\n")

    pajak = total_a * 0.1
    total_bayar = total_a + pajak
    print("-Total: Rp", total_bayar)                
    metode_buy()
    while True:
        pilbayar = int(input("Pilih metode pembayaran : "))
        if pilbayar == 1:
            uang = int(input("Masukkan nominal uang anda : "))
            harga = total_a
            pajak = harga * 0.1
            total_bayar = harga + pajak
            if uang > total_bayar:
                
                kembalian = uang - total_bayar
                with open("transaksi.txt", "a") as s:
                    print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                    print("\n============= STRUK PEMBELIAN =============", file=s)
                    print(" Uang      : Rp", uang, file=s)
                    print(" PPN 10%    : Rp", pajak, file=s)
                    print(" Total     : Rp", total_bayar, file=s)
                    print(" Kembalian : Rp", kembalian, file=s)
                    print("===========================================", file=s)
                data["Stok Produk"][cari_produk] = data.get("Stok Produk")[cari_produk] - jml

            elif uang < total_bayar:
                total_kurang = total_bayar - uang
                print("\n----------TRANSAKSI ANDA GAGAL-----------")
                print("- Uang anda kurang sebesar Rp.", total_kurang)
                
            
            elif uang == total_bayar:
                print("")
               
                kembalian = uang - total_bayar
                with open("transaksi.txt", "a") as s:
                    print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                    print("\n============ STRUK PEMBELIAN ===========", file=s)
                    print(" Uang      : Rp", uang, file=s)
                    print(" PPN 10%    : Rp", pajak, file=s)
                    print(" Total     : Rp", total_bayar, file=s)
                    print(" Kembalian : Rp", kembalian, file=s)
                    print("===========================================", file=s)
                data["Stok Produk"][cari_produk] = data.get("Stok Produk")[cari_produk] - jml
    

        elif pilbayar == 2:
            saldo = uang_cust["e-Money"]
            harga = total_a
            pajak = harga * 0.1
            total_bayar = harga + pajak
            
            if saldo > total_bayar:
                
                uang_cust["e-Money"] = saldo - total_bayar
                with open("transaksi.txt", "a") as s:
                    print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                    print("\n============= STRUK PEMBELIAN =============", file=s)
                    print(" e-Money    : Rp", saldo, file=s)
                    print(" PPN 10%    : Rp", pajak, file=s)
                    print(" Total      : Rp", total_bayar, file=s)
                    print(" Sisa Saldo : Rp", uang_cust["e-Money"], file=s)
                    print("===========================================", file=s)
                data["Stok Produk"][cari_produk] = data.get("Stok Produk")[cari_produk] - jml
            
            elif saldo < total_bayar:
                print("Saldo e-Money anda kurang")
                while True :
                    tny = input("Apakah anda ingin top up saldo e-Money? (y/t) : ")
                    if tny == "y":
                        emoney()
                        saldo_b = uang_cust["hasil_topup"]
                    
                        if saldo_b > total_bayar :
                            uang_cust["e-Money"] = saldo_b - total_bayar
                            with open("transaksi.txt", "a") as s:
                                print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                                print("\n============= STRUK PEMBELIAN =============", file=s)
                                print(" e-Money    : Rp", saldo_b, file=s)
                                print(" PPN 10%    : Rp", pajak, file=s)
                                print(" Total      : Rp", total_bayar, file=s)
                                print(" Sisa Saldo : Rp", uang_cust["e-Money"], file=s)
                                print("===========================================", file=s)
                            data["Stok Produk"][cari_produk] = data.get("Stok Produk")[cari_produk] - jml
                            break
                        else :
                            kurang = total_bayar - uang_cust["e-Money"]
                            print("\n----------TRANSAKSI ANDA GAGAL-----------")
                            print("- Saldo e-Money anda kurang sebesar Rp. ", kurang)
                            break
                    

                    elif tny == "t":
                        print("\n---------- SALDO ANDA TIDAK CUKUP ----------")
                        print("------------- TRANSAKSI GAGAL --------------")
                        break
                    else :
                        print("\n[] INPUT TIDAK SESUAI")

            elif saldo == total_bayar:
                
                uang_cust["e-Money"] = saldo - total_bayar
                with open("transaksi.txt", "a") as s:
                    print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                    print("\n============= STRUK PEMBELIAN =============",file=s)
                    print(" e-Money    : Rp", saldo, file=s)
                    print(" PPN 10%    : Rp", pajak, file=s)
                    print(" Total      : Rp", total_bayar, file=s)
                    print(" Sisa Saldo : Rp", uang_cust["e-Money"], file=s)
                    print("===========================================", file=s)
                data["Stok Produk"][cari_produk] = data.get("Stok Produk")[cari_produk] - jml
        else :
            print("[] PILIHAN TIDAK TERSEDIA")
            print("[] SILAHKAN COBA LAGI\n")

        while True : 
            lagi = input(">> Apakah anda ingin kembali ke menu home (y/t) : ")
            if lagi == "y" :
                os.system("cls")
                menucustomer()
            elif lagi == "t":
                buy()
            else :
                print("[] TOLONG PERHATIKAN INPUT")

def menucustomer():
    while True:
        try :
            menu_homecust()
            pilih = int(input("~ Masukan Menu yang dipilih : "))
            if pilih == 1:
                os.system('cls')
                buy()
                while True :
                    kembali = input(">> Apakah anda ingin kembali ke menu sebelumnya? (y/t) : ")
                    if kembali == "t":
                        buy()
                    elif kembali == "y":
                        os.system('cls')
                        break
                    else :
                        print("[] PILIHAN TIDAK TERSEDIA")

            elif pilih == 2:
                os.system('cls')
                emoney()
                while True :
                    kembali = input(">> Apakah anda ingin kembali ke menu sebelumnya? (y/t) : ")
                    if kembali == "t":
                        emoney()
                    elif kembali == "y":
                        os.system('cls')
                        break
                    else :
                        print("[] PILIHAN TIDAK TERSEDIA")

            elif pilih == 3:
                os.system('cls')
                while True :
                    print("\n------------------------- E-Money -------------------------\n")
                    print(f' Saldo e-Money anda adalah Rp. {uang_cust["e-Money"]}')
                    print("\n-----------------------------------------------------------\n")
                    kembali = input(">> Apakah anda ingin kembali ke menu sebelumnya? (y/t) : ")
                    if kembali == "t":
                        pass
                    elif kembali == "y":
                        os.system('cls')
                        break
                    else :
                        print("[] PILIHAN TIDAK TERSEDIA")
                        
            elif pilih == 4:
                os.system('cls')
                print("---------- PROGRAM TELAH SELESAI ----------")
                print("--------------- TERIMA KASIH --------------")
                exit()
            else :
                print("[] PILIHAN TIDAK TERSEDIA")
                print("[] SILAHKAN COBA LAGI\n")
        except ValueError :
            print("[] MOHON MASUKAN INPUT DENGAN BENAR")
        
#jalankan program
def main_program():
    print("                        SELAMAT DATANG DI")
    print("                   TOKO ALAT OLAHRAGA ASTERIX \n")
    while True :
        try :
            menu_awal()
            Menu = int(input("~ Masukan Menu yang dipilih : "))
            os.system("cls")
            if Menu == 1:
                login_admin()
                menuadmin()
                break
            elif Menu == 2:
                menu_logincust()
                menucustomer()
                break
            elif Menu == 3:
                print("---------- PROGRAM TELAH SELESAI ----------")
                print("--------------- TERIMA KASIH --------------")
                raise SystemExit
            else:
                print("[] PILIHAN TIDAK TERSEDIA")
                print("[] SILAHKAN COBA LAGI")
        except ValueError:
            print("[] MOHON PERHATIKAN INPUT")
            print("[] INPUT HARUS ANGKA\n")


main_program()