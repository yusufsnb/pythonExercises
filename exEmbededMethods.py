# P1
"""
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.
[(3, 4), (10, 3), (5, 6), (1, 9)]
Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin 
her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.
[12, 30, 30, 9]
"""
"""
liste = [(3, 4), (10, 3), (5, 6), (1, 9)]


def recArea(a):
    return a[0]*a[1]


areaList = list(map(recArea, liste))
print(areaList)
"""
# P2
"""
Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]
"""
"""
liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]
def isTriangle(edges):
    x, y, z = edges
    if((abs(y-z) < x and x < y+z) and
       (abs(x-z) < y and y < x+z) and
       (abs(x-y) < z and z < x+y)):
        return True
    return False


newList = list(filter(isTriangle, liste))
print(newList)
"""

# P3
"""
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.
"""
"""
from functools import reduce
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenList = list(filter(lambda x: x % 2 == 0, liste))
print(evenList)
sumOfEvens = reduce(lambda x, y: x+y, evenList)
print(sumOfEvens)
"""
# P4
"""
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.
"""
"""
names = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
lastNames = ["Yılmaz", "Öztürk", "Dağdeviren",
             "Atatürk", "Dikmen", "Kaya", "Polat"]

zipList = list(zip(names, lastNames))
print(zipList)
for i, j in zipList:
    print(i, j)
"""
