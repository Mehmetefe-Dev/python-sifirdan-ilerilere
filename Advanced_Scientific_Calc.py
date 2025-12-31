import math
import time

def hesap_makinesi():
    

    print("---- Hesap Makinesi ----")

    print("1- Toplama        2- Çıkarma     3- Çarpma     4-Bölme\n5- Kök alma       6- Üs alma     7-faktoriyel  8- Logaritma\n9- Mutlak değer   10- Mod alma   11-Trigonometrik işlemler\n12- Doğal logaritma")

    while True:
        try:
            secim=input("Yapmak istediğiniz işlemi seçiniz (Çıkış için 0): ")
            
            if secim == "0" :
                print("Program kapatılıyor...")
                time.sleep(1.2)
                break
            elif secim in ["1","2","3","4","6","8","10"]:
                s1 =float(input("1. Sayıyı giriniz: "))
                s2 =float(input("2. Sayıyı giriniz: "))

                if secim =="1":
                    sonuc=s1+s2
                    print(f"Sonuç: {sonuc}")
                elif secim=="2":
                    sonuc=s1-s2
                    print(f"Sonuç: {sonuc}")
                elif secim=="3":
                    sonuc=s1*s2
                    print(f"Sonuç: {sonuc}")
                elif secim=="4":
                    try:
                        sonuc=s1/s2
                        print(f"Sonuç: {sonuc}")
                    except ZeroDivisionError:
                        print("bir sayıyı sıfıra bölmek hoş olmaz!")
                elif secim=="6":
                    while True:
                        print(f"Girdiğiniz sayılar: {s1} ve {s2}")
                        sec=input(f"Taban {s1} olsun istiyorsanız 1, {s2} olsun istiyorsanız 2 ye basınız")
                        if sec=="1":
                            taban=s1
                            us=s2
                            break
                        elif sec=="2":
                            taban=s2
                            us=s1
                            break
                        else:
                            print("lütfen 1 veya 2 giriniz.")
                    try:
                        sonuc=math.pow(taban, us) 
                        print(f"Sonuç: {sonuc}")
                    except Exception as e:
                        print(f"Hesaplama hatası :{e}")
                elif secim=="8":
                    print(f"Girdiğiniz sayılar: {s1} ve {s2}")
                    while True:
                        sec=input(f"Taban {s1} olsun istiyorsanız 1, {s2} olsun istiyorsanız 2 ye basınız")
                        
                        if sec=="1":
                            taban=s1
                            us=s2
                        elif sec=="2":
                            taban=s2
                            us=s1
                        else:
                            print("Lütfen sadece 1 veya 2 giriniz")
                            continue
                        try:
                            sonuc=math.log(us, taban)
                            print(f"Sonuç: {sonuc}")
                            break
                        except (ValueError,ZeroDivisionError):
                            print("Hata: Logaritma kurallarına aykırı giriş! (Taban 1,0 veya negatif olamaz)")
                            break
                elif secim=="10":
                    try:
                        sonuc=s1%s2
                        print(f"Sonuç: {sonuc}")
                    except ZeroDivisionError:
                        print("Hata: Mod alma işleminde bölen sayı sıfır olamaz!")

            elif secim in ["5","7","9","12"]:

                if secim =="5":
                    sayi=float(input("kökü alınacak sayıyı giriniz: "))
                    if sayi<0:
                        print("Hata: Negatif sayıların karekökü alınamaz!")
                    else:
                        sonuc= math.sqrt(sayi)
                        if sonuc==0:
                            sonuc=0.0
                        print(f"sonuç: {sonuc:.3f}") 
                elif secim=="7":
                    while True:
                        sayi=float(input("Faktöriyel için sayı giriniz: "))

                        if not sayi.is_integer():
                            print("Hata: Faktöriyel sadece tam sayılar için tanımlıdır.")
                            continue
                                
                        if sayi<0:
                            print("Hata: Negatif sayıların faktöriyeli alınmaz.")
                            continue
                        print(f"Sonuç: {math.factorial(int(sayi))}")
                        break
                elif secim=="9":
                    sayi=float(input("Bir sayı giriniz: "))
                    sonuc=math.fabs(sayi)
                    print(f"Sonuç: {sonuc}")
                elif secim=="12":
                    while True:
                        print("\n1- Normal Sayı Girmek\n2- Euler Üssü (e^x) Girmek\n0 Ana Menü")
                        alt_sec=input("Seçiminiz: ")

                        if alt_sec=="0":
                            break
                        elif alt_sec=="1":
                            sayi=float(input("Sayıyı giriniz: "))
                        elif alt_sec=="2":
                            us=float(input("e'nin üssü kaç olsun (örn: 10): "))
                            sayi =math.exp(us)
                        else: 
                            print("Lütfen sadece 1, 2 veya 0 giriniz!")
                            continue
                        try:
                            if sayi<=0:
                                print("Logaritmanın içi 0 veya negatif olamaz")
                            else:
                                sonuc=math.log(sayi)
                                print(f"Sonuç: {sonuc}")
                            break
                        except Exception as e:
                            print(f"Matematiksel bir hata oluştu: {e}")
                            
            elif secim=="11":
                time.sleep(0.3)
                print("---- Trigonometri Menüsü -----")
                print("1- Sin   2- Cos\n3- Tan   4- Cot\n5- Sec   6- Cosec\n0- Çıkmak için")
                while True:
                    tri_sec=input("İşleminizi Seçiniz: ")
                    if tri_sec=="0":
                        print("Ana Menüye Dönülüyor")
                        time.sleep(0.6)
                        break
                    if tri_sec in ["0","1","2","3","4","5","6"]:
                        try:
                            derece=float(input("Derece cinsinden açıyı giriniz(Örn: 120):"))
                            radyan=math.radians(derece)
                            if tri_sec=="1":
                                print(f"Sin{derece} = {round(math.sin(radyan), 4)}")
                            elif tri_sec=="2":
                                print(f"Cos{derece} = {round(math.cos(radyan), 4)}")
                            elif tri_sec=="3":
                                if (derece) % 180 == 90:
                                    print(f"Hata: Tan({derece}) tanımsızdır!")
                                else:
                                    print(f"tan{derece} = {round(math.tan(radyan), 4)}")
                            elif tri_sec=="4":
                                if (derece) % 180 == 0:
                                    print(f"Hata: Cot{derece} tanımsızdır!")
                                else:
                                    print(f"Cot{derece} = {round(1/(math.tan(radyan)), 4)}")
                            elif tri_sec=="5":
                                if derece % 180 ==90:
                                    print(f"Hata: Sec{derece} tanımsızdır!")
                                else:
                                    payda =math.cos(radyan)
                                    if abs(payda)<1e-15:
                                        print(f"Sec{derece} tanımsızdır!")
                                    else:
                                        print(f"Sec({derece}) = {round(1/payda, 4)}")
                            elif tri_sec=="6":
                                if derece % 180 ==0:
                                    print(f"Hata: Cosec{derece} tanımsızdır!")
                                else:
                                    payda=math.sin(radyan)
                                    if abs(payda)<1e-15:
                                        print(f"Cosec{derece} tanımsızdır!")
                                    else:
                                        print(f"Cosec({derece}) = {round(1/payda, 4)}")
                                              
                        except ValueError:
                            print("Hata: Derece için geçerli bir sayı giriniz!")            
                    else:
                        print("Hata: Trigonometri menüsünde sadece 1 ile 6 arasında bir seçim yapabilirsiniz!")
            else:
                print(f"Hata: '{secim}' geçerli bir işlem numarası değildir.\nLütfen 0-12 arasında bir seçim yapın.")
        except ValueError:
            print("Kritik hata: Lütfen sadece sayısal değerler giriniz!")
        except Exception as e:
            print(f"Beklenmedik bir hata oluştu: {e}")

if __name__=="__main__":
    hesap_makinesi()
