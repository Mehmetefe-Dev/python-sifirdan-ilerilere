import random

print("*"* 40 + "\n1 ile 100 arasında bir sayı tuttum.\nBakalım bulabilecek misin?\n"+"*"*40)

# Sayı bir kez tutulur (Döngünün dışında)
gizli_sayi = random.randint(1, 100)

while True:
    try:
        tahmin = int(input("Tahminin nedir?: "))
        
        if tahmin < gizli_sayi:
            print("Daha büyük bir sayı dene.")
        elif tahmin > gizli_sayi:
            print("Daha küçük bir sayı dene.")     
        else:
            print(f"Tebrikler! gizli sayı {gizli_sayi} idi, doğru bildin 🎯👏")
            break
            
    except ValueError:
        print("Lütfen sadece sayı giriniz.")