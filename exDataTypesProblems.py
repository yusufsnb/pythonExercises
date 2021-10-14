# P1: Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
"""
text = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
text = text.lower().strip()

harfler = set(text)
harf_sayi = dict()

for i in harfler:
    harf_sayi[i] = text.count(i)

print(harf_sayi)
"""
# P2: Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek
# bir string oluşturun ve bu string'i ekrana yazdırın.
"""
text = ""
with open("siir.txt", "r", encoding="utf-8") as file:
    for i in file:
        text += i[0]
print(text)
"""
# P3: Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun.
# Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.
"""
mailList = []


def isVariable(x):
    if(x.endswith(".com") and x.find("@") != -1):
        return True
    return False


with open("mailler.txt") as file:
    listOfRows = []
    for i in file:
        i = i[:-1]
        listOfRows.append(i)
    print(list(filter(isVariable, listOfRows)))
"""
# P4
"""
Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri isimlere göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
"""
names = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
lastNames = ["Yılmaz", "Öztürk", "Dağdeviren",
             "Atatürk", "Dikmen", "Kaya", "Polat"]

users = []
for i, j in list(zip(names, lastNames)):
    users.append(i + " " + j)

users.sort()
print(users)
