# P3:1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
# Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
"""
def perfectNumbers():
    pList = list()
    for i in range(1, 1000):
        listForNumber = []
        for j in range(1, i):
            if(i % j == 0):
                listForNumber.append(j)
        if(sum(listForNumber) == i):
            pList.append(i)
    return pList


print(perfectNumbers())
"""
# P3: Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""
sayi = int(input("1. sayıyı giriniz"))
sayi2 = int(input("2. sayıyı giriniz"))

def EBOB(sayi, sayi2):
    bolenler = list()
    for i in range(2, (min(sayi, sayi2) + 1)):
        if(sayi % i == 0 and sayi2 % i == 0):
            bolenler.append(i)
    if(len(bolenler) == 0):
        return "Ortak bölen yoktur!!!"
    else:
        bolenler.sort(reverse=True)
        return bolenler[0]


print(EBOB(sayi, sayi2))
"""
# P3: Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
"""
sayi = int(input("1. sayıyı giriniz"))
sayi2 = int(input("2. sayıyı giriniz"))

def EKOK(sayi, sayi2):
    kat = max(sayi, sayi2)
    while True:
        if(kat % sayi == 0 and kat % sayi2 == 0):
            print("{} ve {} sayılarının en küçük ortak katı {} sayısıdır.".format(
                sayi, sayi2, kat))
            break
        else:
            kat += 1
            continue

EKOK(sayi, sayi2)
"""
# P4: Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
"""
birler = ["bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["On", "Yirmi", "Otuz", "Kırk", "Elli",
         "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunusu(sayi):
    if(int(sayi[1]) == 0):
        return onlar[int(sayi[0]) - 1]
    else:
        return onlar[int(sayi[0]) - 1] + " " + birler[int(sayi[1]) - 1]


while True:
    sayi = input("2 basamaklı bir sayı giriniz")
    if(sayi == "q"):
        print("Program sonlandırıldı")
        break
    elif(int(sayi) < 10 or int(sayi) >= 100):
        print("Girdiğiniz sayi iki basamaklı değildir!!!")
        continue
    else:
        print(okunusu(sayi))
"""
# P5:1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
"""
def pisagor():
    liste = list()
    for i in range(1, 101):
        for j in range(1, 101):
            c = (i**2 + j**2) ** 0.5
            if(c == int(c)):
                liste.append((i, j, int(c)))
    return liste

print(pisagor())
"""
