# Project: Simple Login System
# Author: Mehmet Efe Özdemir

import time
import random
import sys

print("*" * 30)
print("----- Sistemimize Hoş Geldiniz -----")
print("*" * 30)

#------ Kayıt Aşaması ------
kayıtlı_kullanıcı = input("Kullanıcı Adı Belirleyiniz: ")
kayıtlı_şifre = input("Şifrenizi belirleniyiz: ")
isim = input("Adınız: ")
telefon = input("Telefon Numaranız: ")

print("\nKaydınız oluşturuluyor...")
time.sleep(1.5)
print("Kayıt Başarılı! Giriş Ekranına Yönlendiriliyorsunuz...\n")
time.sleep(1.5)

#------ Giriş Aşaması ------

while True:
    print("---- GİRİŞ EKRANI ----")
    girilen_kullanıcı = input("Kullanıcı adı: ")
    girilen_şifre = input("Şifre: ")

    #------ Kontrol Mekanizması ------

    if (girilen_kullanıcı == kayıtlı_kullanıcı) and (girilen_şifre == kayıtlı_şifre):
        print("Giriş bilgileri doğru. Telefonunuza doğrulama kodu gönderiliyor...")
        time.sleep(1)
        kod_hakki = 2
        
        while kod_hakki > 0:
            dogrulama_kodu = random.randint(1000, 9999)
            print(f"Telefonunuza Gelen Kod: {dogrulama_kodu}")
            
            try:
                girilen_kod = int(input("Lütfen Kodu Giriniz: "))
            except ValueError:
                print("Lütfen Sadece Rakam Giriniz!")
                girilen_kod = -1 # Hatalı giriş sayalım

            if girilen_kod == dogrulama_kodu:
                print(f"\nHoş Geldiniz Sayın {isim}!")
                break
            
            else:
                kod_hakki -= 1
                
                if kod_hakki == 0:
                    print("Hatalı Kod!! Sistem Güvenliği İçin Kapatılıyor...")
                    sys.exit()
                else:
                    print("Hatalı Kod! Yeni bir kod gönderiliyor...")
                    time.sleep(1.5)
        if kod_hakki > 0:
            break 
            
    # Durum_1.0 -----> Kullanıcı Adı yanlış <-----
    elif (girilen_kullanıcı != kayıtlı_kullanıcı) and (girilen_şifre == kayıtlı_şifre):
        print("Kullanıcı Adınız Yanlış!!")
    
    # Durum_2.0 -----> Şifre Yanlış <-----
    elif (girilen_kullanıcı == kayıtlı_kullanıcı) and (girilen_şifre != kayıtlı_şifre):
        print("Şifreniz Yanlış!!")
        cevap = input("Şifrenizi Değiştirmek İster Misiniz?(E/H)")
        
        if cevap.upper() == "E":
            yeni_parola = input("Yeni Parola Giriniz: ")
            print("Lütfen Bekleyiniz\nŞifreniz Güncelleniyor...")
            time.sleep(1.0)
            kayıtlı_şifre = yeni_parola
            print("Şifreniz Değişti! Lütfen YENİ Şifrenizle Giriş Yapın.\n")
    else:
        print("Kullanıcı Adı Veya Şifre Hatalı. Tekrar Deneyiniz\n")