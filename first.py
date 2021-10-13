import math
##FAKTORİYEL
zakkum=5
factorial=1

yumak="YUMAK"
for i in range(1,zakkum+1):
    factorial *= i
i=1
print(yumak, factorial)

##DEĞİŞKENLER
#NUMBER, STRING, LIST, TUPPEL, DICTIONARY

##LİSTELER
user = {
    "username": "zeyneps",
    "name": "zeynep nisa",
    "lastname": "bakan",
    "password": "123456s",
    "age": 18
}

print(user.get("age"))

newFacto = math.factorial(5)
print(newFacto)