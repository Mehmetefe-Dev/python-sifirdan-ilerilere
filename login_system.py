# Project: Simple Login System
# Author: Mehmet Efe
# Description: A logic-based login system that detects specific user errors.

print("----Sitemize hoş geldiniz----")

# ------ Kayıt Aşaması (Registration) ---------
kayitli_kullanici = input("Kullanıcı adı oluşturunuz: ")
kayitli_sifre = input("Şifre belirleyiniz: ")

print("\n✅ Sisteme başarılı şekilde kayıt oldunuz.\n")

# ---- GİRİŞ AŞAMASI (Login) ----
girilen_kullanici = input("Kullanıcı Adı: ")
girilen_sifre = input("Şifre: ")

# --- KONTROL MEKANİZMASI (Logic Gates) ---

# 1. Senaryo: Her şey doğru (Success)
if (kayitli_kullanici == girilen_kullanici) and (kayitli_sifre == girilen_sifre): 
    print("✅ Giriş başarılı. Hoş Geldiniz!")

# 2. Senaryo: Kullanıcı adı ve şifre yer değiştirmiş (Swapped)
elif (kayitli_kullanici == girilen_sifre) and (kayitli_sifre == girilen_kullanici):
    print("😵 Hocam senin akli melekelerin kötü olmuş, yerleri karıştırdın!")

# 3. Senaryo: Kullanıcı Adı Yanlış, Şifre Doğru (Wrong Username)
elif (kayitli_kullanici != girilen_kullanici) and (kayitli_sifre == girilen_sifre):
    print("❌ Kullanıcı adınızı yanlış girdiniz.")

# 4. Senaryo: Kullanıcı Adı Doğru, Şifre Yanlış (Wrong Password)
elif (kayitli_kullanici == girilen_kullanici) and (kayitli_sifre != girilen_sifre):
     print("❌ Şifrenizi yanlış girdiniz.")

# 5. Senaryo: İkisi de Yanlış (Both Wrong)
else:
    print("⛔ Ooo hocam kafa başka sayfa o galiba... İkisi de yanlış!")