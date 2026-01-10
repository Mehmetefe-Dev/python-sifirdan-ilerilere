import sqlite3

con = sqlite3.connect("Ogrenci_Notlari.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT,soyad TEXT,numara INT,notu INT)")

def ogrenci_ekle(ad, soyad, numara, notu):
    cursor.execute("INSERT INTO ogrenciler VALUES(?,?,?,?)", (ad, soyad, numara, notu ))
    con.commit()
    print(f"{ad} {soyad} başarıyla kaydedildi!")

tablo_olustur()

print("--- Öğrenci Kayıt Sistemine Hoş Geldiniz ---")
while True:
    secim=input("Öğrenci Eklemek için 'e', çıkmak için'q' basın: ").lower()

    if secim =='q':
        break
    elif secim == 'e':
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        no= int(input("Numara: "))
        not_bilgisi= int(input("Notu: "))
        ogrenci_ekle(ad, soyad, no, not_bilgisi)
    else:
        print("Geçersiz Komut!")

print("Sistemden Çıkıldı. Veriler 'Ogrenci_Notlari.db' dosyasına kaydedildi.")
con.close()
