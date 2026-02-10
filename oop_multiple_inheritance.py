class Calisan:
    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas
        pass
    def bilgileri_goster(self):
        print(f"İsim: {self.isim} | Maaş: {self.maas}")
        pass
    

class Yazilimci:
    def kod_yaz(self):
        print("Python kodu yazılıyor...")

class Yonetici:
    def toplantı_yap(self):
        print("Toplantı Yönetiliyor")

class YazilimciYonetici(Calisan,Yazilimci,Yonetici):
    def __init__(self, isim, maas):
        super().__init__(isim, maas)

YazılımcıYonetici = YazilimciYonetici("Mustafa","2000")
YazılımcıYonetici.bilgileri_goster()
YazılımcıYonetici.kod_yaz()       
YazılımcıYonetici.toplantı_yap() 
print(YazilimciYonetici.__mro__)