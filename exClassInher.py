class Hayvan():
    def __init__(self, data):
        self.tur = data.get("tur")
        self.yas = data.get("yas")


class Kus(Hayvan):
    def __init__(self, data, kusTuru):
        super().__init__(data)
        self.kus = kusTuru


hayvan = Hayvan({"tur": "Kedi", "yas": 7})

kus = Kus({"tur": "Kuş", "yas": 2}, "Saksağan")

print(hayvan)

print(kus)

print(kus.kus)
print(hayvan.tur)
