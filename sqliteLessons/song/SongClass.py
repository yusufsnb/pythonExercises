import sqlite3


class Song():
    def __init__(self, music, artist, album, productor, time):
        self.music = music
        self.artist = artist
        self.album = album
        self.productor = productor
        self.time = time

    def __str__(self):
        return "Müzik : {} , Sanatçı : {} , Albüm : {} , Yapımcı : {} , Süre : {}".format(self.music, self.artist,
                                                                                          self.album, self.productor, self.time)


class SongLibrary():
    def __init__(self):
        self.connection = sqlite3.connect("song.db")
        self.cursor = self.connection.cursor()
        self.createTable()

    def createTable(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS songs(music text, artist text, album text,productor text, time INT)")
        self.connection.commit()

    # GET DATA FROM TABLE
    def showTable(self):
        print("Şarkılar getiriliyor...")
        self.cursor.execute("SELECT * FROM songs")
        songs = self.cursor.fetchall()
        if(len(songs) == 0):
            print("Kütüphanende şarkı bulunmuyor...")
        else:
            for i in songs:
                song = Song(i[0], i[1], i[2], i[3], i[4])
                print(song)

    # INSERT INTO TABLE
    def addNewSong(self, songData):
        self.cursor.execute(
            "INSERT INTO songs VALUES(?,?,?,?,?)", (songData.music, songData.artist, songData.album,
                                                    songData.productor, songData.time))
        self.connection.commit()
        print("Yeni şarkı eklendi...")

    def deleteSong(self, music):
        self.cursor.execute(
            "SELECT * FROM songs WHERE music=?", (music, ))
        song = self.cursor.fetchall()
        if(len(song) == 0):
            print("Böyle bir şarkı listenizde bulunmuyor...")
        else:
            self.cursor.execute(
                "DELETE FROM songs WHERE music=?", (music, ))
            self.connection.commit()
            print("Şarkı Silindi")

    def sumOfTimes(self):
        self.cursor.execute("SELECT time FROM songs")
        times = self.cursor.fetchall()
        times = [i[0] for i in times]
        print("Toplam Süre : {} ".format(sum(times)))
