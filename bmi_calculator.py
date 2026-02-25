print("Vücut Kitle İndeksi Hesaplama Makinesine Hoş Geldiniz Hesap Makinemiz SI Birimlerine Göre Çalışmaktadır.")
kilo=float(input("Kilonuzu giriniz: ")) 
boy=float(input("Boyunuzu giriniz (1.69 M, 1.81 M gibi): "))

# BMI means Body Mass Index
if boy>3:
    print(f"⚠️ Uyarı: Boyunuzu cm olarak({boy})girdiniz, sistem otomatik olarak metreye çevirdi.")
    boy = boy/100
bmi= kilo/(boy**2)

print(f"---------------------------------\nVücut Kitle İndeksiniz: {bmi:.2f}")

if bmi<18.5:
    print("Zayıf. Sağlık Riski Bulunmakta")
elif bmi<25 :
    print("Normal. Kilonuz İdeal")
elif bmi<30 :
    print("Fazla Kilo. Riski Var")
elif bmi<35 :
    print("Obez (Sınıf I). Dikkat!")
else:
    print("Yüksek Obez Seviyesi. Doktora Danışın!")


