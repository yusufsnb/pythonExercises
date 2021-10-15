from SongClass import *

print("""
Şarkı Programı

1. Şarkıları Göster
2. Yeni Şarkı Ekle
3. Şarkı Sil
4. Kütüphane Toplam Şarkı Süresi

Çıkmak için q'ya basınız.
""")

songs = SongLibrary()

while True:
    islem = input("İşlem seçiniz : ")
    if(islem == 'q'):
        print("Program sona erdi")
        break
    elif(islem == "1"):
        songs.showTable()
    elif(islem == "2"):
        music = input("Şarkı : ")
        artist = input("Sanatçı : ")
        album = input("Albüm : ")
        productor = input("Yapımcı : ")
        time = int(input("Süre : "))
        new_song = Song(music, artist, album, productor, time)
        songs.addNewSong(new_song)
    elif(islem == "3"):
        music = input("Silmek istediğiniz şarkının ismini giriniz : ")
        songs.deleteSong(music)
    elif(islem == "4"):
        songs.sumOfTimes()
