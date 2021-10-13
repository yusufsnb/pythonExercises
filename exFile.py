# Dosya Oluşturma
# w = Create file
# a = If file exists create else append
# r = read file
# file.read() function read one time and cursor goes to end and wait
# file.readLine() function reads only one row at a time Tip: Use with loop
# file.readLines() function get the rows and shows to user as a type of list
# OPEN,WRITE
"""
file = open("deneme.txt", "a", encoding="utf-8")
file.write("Yusuf Sina Bakan\n")

file.close()
"""
# READ ROW
"""
try:
    file = open("deneme.txt", "r", encoding="utf-8")
    for i in file:
        print(i, end="")
except FileNotFoundError:
    print("Dosya bulunamadı")
finally:
    file.close()
"""
# READ
"""
try:
    file = open("deneme.txt", "r", encoding="utf-8")
    contents = file.read()
    print(contents)
except FileNotFoundError:
    print("Dosya bulunamadı")
finally:
    file.close()
"""

# Auto Closing
"""
with open("deneme.txt", "r", encoding="utf-8") as file:
    for i in file:
        print(i)
"""

# seek function moves to cursor to anywhere
# tell function shows in which byte the cursor now
"""
with open("deneme.txt", "r", encoding="utf-8") as file:
    print("Current byte", file.tell())
    file.seek(22)
    for i in file:
        print(i)
"""

# r+ = Overwrite
"""
with open("deneme.txt", "r+", encoding="utf-8") as file:
    file.seek(10)
    file.write("Denemelerim")

with open("deneme.txt", "r", encoding="utf-8") as file:
    for i in file:
        print(i)
"""
