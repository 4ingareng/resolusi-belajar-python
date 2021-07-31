print(r"=== Selamat Datang Di Toko Penjualan Komponen Robot ===")
Komponen = [
    "Arduino Uno R3 + Cable",
    "Adaptor 12V",
    "LED Biru",
    "Mini Saklar On/Off",
    "Black Housing 3P",
    "Buzzer",
    "Jumper Male/Male",
    "Pin Header Male",
    "Sensor Infrared",
    "Timah Solder",
    "GearBox",
    "Relay 4 Channel 12VDC"]
harga = [85000, 60000, ]
keranjang = []
mulai = True

print(r"Berikut Item-item yang tersedia : ",)
for Urutan, barang in enumerate(Komponen):
    print(Urutan, ":", barang)

while mulai:
    pesan = str(input("Masukan Pesanan Anda :"))
    if pesan in Komponen:
        print("Item", pesan, "Masuk dalam Keranjang")
        Komponen.remove(pesan)
        keranjang.append(pesan)
        ulang = True
        while ulang:
            pertanyaan = str(input("ingin Memesan lagi ?! "))
            if pertanyaan == "iya":
                ulang = False
                mulai = True
            elif pertanyaan == "tidak":
                ulang = False
                mulai = False
            else:
                print("Kami tidak Mengerti")
                ulang = True
    else:
        print("Item", pesan, "Tidak Tersdia")
else:
    print("Item yang  Anda Beli :", keranjang)
print("Item Komponen Yang Tersisa : ", Komponen)
