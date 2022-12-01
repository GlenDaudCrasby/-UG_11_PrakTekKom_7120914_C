print ("memeriksa kelipatan")

angka = int(input("masukkan kelipatan 9 yang ingin di periksa: "))
def kelipatan_sembilan():
    kelipatan = angka % 9
    return kelipatan

if kelipatan_sembilan() == 0:
    print ("benar")

else:
    print("salah")
