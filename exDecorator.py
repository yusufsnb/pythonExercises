# P1 : 1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın.
# Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den
# 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.

def extra(func):
    def wrapper(sayilar):
        sonuc = func(sayilar)
        perfectNums = list()
        for i in sayilar:
            tamBolenler = []
            for j in range(1, i):
                if(i % j == 0):
                    tamBolenler.append(j)
            if(i == sum(tamBolenler)):
                perfectNums.append(i)
        print("Mükemmel Sayılar :", perfectNums)
        return sonuc
    return wrapper


@extra
def primeNum(sayilar):
    def isPrime(x):
        if(x == 1):
            return False
        elif(x == 2):
            return True
        else:
            i = 2
            while i < x:
                if(x % i == 0):
                    return False
                i += 1
        return True
    print("Asal Sayılar : ", list(filter(isPrime, sayilar)), "\n")


primeNum(range(1, 1001))
