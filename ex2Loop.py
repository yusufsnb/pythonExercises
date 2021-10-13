# P1: Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
"""
sayi = None
dizi = []
sayi = int(input("Bir sayı giriniz:"))

for i in range(1, sayi):
    if(sayi % i == 0):
        dizi.append(i)

if(sum(dizi) == sayi):
    print("Mükemmel sayı")
else:
    print("Mükemmel sayı değildir!")
"""
# P2: Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
"""
sayi = None
sayi = int(input("Bir sayı giriniz:"))

lenSayi = len(str(sayi))
toplam = 0
print(str(sayi)[0])
for i in range(0, lenSayi):
    toplam += (int(str(sayi)[i]) ** lenSayi)

if(toplam == sayi):
    print("{} sayısı bir Armstrong sayıdır.".format(sayi))
else:
    print("{} sayısı Armstrong sayı değildir.".format(sayi))
"""
# P3: 1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
"""
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t")
    print("\n")
"""
# P4:Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
# Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
"""
toplam = 0
while True:
    sayi = input("Bir sayı giriniz")
    if(sayi == "q"):
        print("Toplam : {}".format(toplam))
        break
    else:
        try:
            toplam += int(sayi)
        except:
            print("Sayı girmediniz!!!")
            continue
"""
# P5: 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
"""
list = list()
for i in range(1, 101):
    if(i % 3 == 0):
        list.append(i)
print(list)
"""
# P6: 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.
"""
liste = list()
liste = [i for i in range(1, 101) if i % 2 == 0]
print(liste)
"""
