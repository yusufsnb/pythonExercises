# P1:Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.
"""
import math
print("Hesap Makinesi")
print(\"""
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
5.Üs
9.Çıkış
\""")

while True:
    sayi = int(input("1.sayıyı giriniz"))
    sayi2 = int(input("2.sayıyı giriniz"))
    islem = int(input("İşlemi seçiminiz"))
    if(islem == 1):
        print("{} + {} = {}".format(sayi, sayi2, sum(sayi + sayi2)))
    elif(islem == 2):
        print("{} - {} = {}".format(sayi, sayi2, sayi - sayi2))
    elif(islem == 3):
        print("{} * {} = {} ".format(sayi, sayi2, sayi * sayi2))
    elif(islem == 4):
        print("{} / {} = {}".format(sayi, sayi2, sayi / sayi2))
    elif(islem == 5):
        print("{} ^ {} = {}".format(sayi, sayi2, sayi ** sayi2))
    elif(islem == 9):
        break
"""
