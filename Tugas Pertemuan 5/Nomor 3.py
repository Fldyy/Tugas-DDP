Pertanyaan = int(input("""Silahkan Pilih Soal Berikut:
================================================================
1.Menghitung Luas Persegi
2.Menghitung Luas Lingkaran
3.Menghitung Luas Segitiga
=================================================================
pilihanmu?"""))

match Pertanyaan:
    case 1:
        print("Kamu memilih menghitung Persegi")
        sisi = int(input("sisi="))
        luas = sisi*sisi
        print("untuk luas persegi dengan sisi", sisi, "adalah", luas)
    case 2:
        print("Kamu memilih menghitung Lingkaran dengan jari-jari = 28")
        r = int(input("jari-jari="))
        luaslingkaran = 3.14*r*r
        print("untuk luas lingkaran", r, "adalah", luaslingkaran)
    case 3:
        print("Kamu memilih menghitung Segitiga dengan alas = 12, Tinggi = 20")
        alas = int(input("alas="))
        tinggi = int(input("tinggi="))
        luas = 0.5*alas*tinggi
        print("untuk luas segitga","dengan alas", alas, "dengan tinggi", tinggi, "adalah")
    case _:
        print("Pilihanmu salah! silahkan coba lagi")
