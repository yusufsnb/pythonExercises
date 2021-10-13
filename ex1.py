# P1: Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

print("Toplam: {}".format((a*b*c)))
"""
# P2: Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
"""
kilo = int(input("Kilonuz:"))
boy = int(input("Boyunuz:"))

boy /= 100

print("Kitle Endexiniz: {}".format((kilo/(boy**2))))
"""
# P3: Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre
# yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
kmFiyat = float(input("Kilometre başına yakılan benzin fiyatı: "))
km = float(input("Kilometre: "))

print("Toplam Ücret: {}".format((kmFiyat*km)))
"""
# P4: Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""
ad = input("ad:")
soyad = input("soyad:")
nu = input("numara:")

print("Adınız {}\nSoyadınız {}\nNumarınız {}".format(ad, soyad, nu))
"""
# P5: Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""
a = int(input("Lütfen 1. sayıyı giriniz: "))
b = int(input("Lütfen 2. sayıyı giriniz: "))

print("Sayılar değiştiriliyor...")

c = b
b = a
a = c
print("Sayılar değiştirildi... a: {}, b: {}".format(a, b))
"""
# P6: Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
"""
a = int(input("1. kenarı giriniz: "))
b = int(input("2. kenarı giriniz: "))

print("Hipotenüs : {}".format((a**2 + b**2)**0.5))
"""
