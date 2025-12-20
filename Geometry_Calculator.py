import math
import time

def geometri(sekil):
    #--- Güvenlik ---
    for kenar in sekil:
        if kenar <=0 :
            print("Hata Kenar uzunluğu 0 veya negatif olamaz!!")
            return
    # ---- Çevre Hesabı ( Tüm Şekilleri Kapsıyor ) ----
    cevre=sum(sekil)
    #---- Üçgenler ----     
    if len(sekil) == 3:
        a,b,c=sekil

        if (a+b) > c and (a+c) > b and (b+c) > a:
            u = (a+b+c)/2
            alan = math.sqrt(u*(u-a)*(u-b)*(u-c))
            if (a==b) and (a==c):
                tip = "Eşkenar Üçgen"   
            elif (a==b) or (b==c) or (a==c):
                tip = "Şeklimiz İkiz Kenar Üçgen"
            else:
                tip = "Şeklimiz Çeşitkenar Üçgen"

            print(f"Şeklimiz: {tip}\nÇevre: {cevre}\nAlan: {alan:.2f}")    
        
        else:
            print("Üçgen Belirtmiyor!!")
    #---- Dikdörtgenler ----
    elif len(sekil)==4:
        a,b,c,d=sekil
        if (a==b) and (a==c) and (a==d):
            while True:
                aci=input("Şeklimizin en az 2 köşesi 90 derecemi ? (E/H): ")
                if aci.upper()=="E":
                    alan=a**2
                    print(f"Şeklimiz Kare\nÇevre: {cevre}\nAlan: {alan:.2f}")
                    break
                elif aci.upper()=="H":
                    while True:
                        try:
                            derece=float(input("Kenarlar arasındaki açıyı giriniz (Örn: 30,60): "))
                            if 0<derece<180:
                                radyan = math.radians(derece)
                                alan=(a * b) * math.sin(radyan)
                                print(f"Şeklimiz Eşkenar Dörtgen\nÇevre: {cevre}\nAlan: {alan:.2f}")
                                break
                            else:  
                                print("Hata: Açı 0 ile 180 arasında olmalıdır!")       
                        except ValueError:
                            print("Lütfen geçerli bir sayısal açı giriniz!")    
                    break
                else:       
                    print("Sadece E veya H harflerini giriniz!!") 
        elif ((a==c) and (b==d)) or ((a==b) and (c==d)) or((a==d) and (b==c)):
            while True:
                aci=input("Şeklimizin en az 2 köşesi 90 derecemi ? (E/H): ")
                if aci.upper()=="E":
                    kenarlar= sorted(list(sekil))
                    alan= kenarlar[0]*kenarlar[2]
                    print(f"Şeklimiz Dikdörtgen\nÇevre: {cevre}\nAlan:{alan:.2f}")
                    break
                elif aci.upper()=="H":
                    while True:
                        try:
                            derece=float(input("Kenarlar arasındaki açıyı giriniz(Örn: 30,60): "))
                            if 0<derece<180:
                                radyan=math.radians(derece)
                                kenarlar= sorted(list(sekil))
                                alan=(kenarlar[0] * kenarlar[2])* math.sin(radyan)
                                print(f"Şeklimiz Paralelkenar\nÇevre: {cevre}\nAlan: {alan:.2f}")
                                break
                            else:
                                print("Açı mantıksız")
                        except ValueError:
                            print("Geçersiz giriş!")        
                    break

                else:
                    print("Sadece 'E' veya 'H' harflerini giriniz.")
        #---- Sıradan dörtgen ----
        else:
            print(f"Şeklimiz Sıradan bir Dörtgen\nÇevre: {cevre}\nAlan hesaplamak için ek bilgi (açı/köşegen) gereklidir")            

while True:
    print("\n--- Geometrik Şekil Ve Alan Bulucu ---")
    try:
        eleman_sayisi=int(input("Kenar sayısını giriniz (çıkış için 0): "))
        if eleman_sayisi==0:
            print("Programdan çıkılıyor...")
            time.sleep(1.2)
            break
        if eleman_sayisi==3:
            kenarlar=[float(input(f"{k}. Kenar: ")) for k in ["a", "b", "c"]]
            geometri(kenarlar)

        elif eleman_sayisi==4:
            kenarlar=[float(input(f"{k}. Kenar: ")) for k in ["a", "b", "c", "d"]]
            geometri(kenarlar)
        else:
            print("Sadece 3 ve 4 kenarlı şekilleri destekliyoruz.")
    except ValueError:
        print("Lütfen sadece sayı giriniz!")
