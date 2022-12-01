print("==================")
print ("operasi matematika")
print ("1. jumlah  [+]")
print ("2. kurang [-]")
print ("3. kali [*]")
print ("4. bagi [/]")
print("==================")
pilihan = input ("pilih operasi (1/2/3/4):")
print("==================")
satu = eval(input("masukkan bilangan pertama : "))
dua = eval(input("masukkan bilangan kedua : "))

def penjumlahan(satu,dua):
    jumlah = satu + dua
    return jumlah
def pengurangan(satu,dua):
    kurang= satu - dua
    return kurang
def perkalian(satu,dua):
    kali = satu * dua
    return kali
def pembagian(satu,dua):
    bagi = satu / dua
    return bagi

if pilihan == "1":
    print (f"hasil operasi dari",satu,"+",dua,"=",penjumlahan(satu,dua))

elif pilihan == "2":
    print (f"hasil operasi dari",satu,"-",dua,"=",pengurangan(satu,dua))

elif pilihan == "3":
    print (f"hasil operasi dari",satu,"*",dua,"=",perkalian(satu,dua))

elif pilihan == "4":
    print (f"hasil operasi dari",satu,"/",dua,"=",pembagian(satu,dua))
