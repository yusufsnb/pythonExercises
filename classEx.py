class Student():
    def __init__(self, data):
        self.no = data.get("no")
        self.ad = data.get("ad")
        self.soyad = data.get("soyad")


s1 = Student({"no": 100, "ad": "Yusuf Sina", "soyad": "Bakan"})
s2 = Student({"no": 101, "ad": "Zeynep Nisa", "soyad": "Bakan"})

print(s1.no)
print(s2.no)
