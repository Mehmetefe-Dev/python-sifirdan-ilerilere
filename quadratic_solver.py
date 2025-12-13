# ----- Tanıtım Kısmı -----

print("--- Diskriminant Hesaplama Makinemize Hoş geldiniz ---")

#----- Kullanıcıdan Veri Alma -----

print("kökleri hesaplamamız için bize öncelikle denklemimizin\nkatsayıları gerekiyor (ax**2 + bx+ c ) formatında")
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
delta=(b**2 - 4*a*c)

#----- Delta Ve Kök Hesaplama -----

if delta>0:
    print("Delta sıfırdan büyük, İki farklı kök var.")
    print("x1= ", (-b + delta**0.5)/(2*a))
    print("x2= ", (-b - delta**0.5)/(2*a))
elif delta==0:
    print("Delta sıfır, kökler birbirine eşit.")
    print("x1=x2=",(-b/(2*a)))
else:
    print("⛔ Reel kök yok.")
