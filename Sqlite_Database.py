import sqlite3

con = sqlite3.connect("ogrenciler.db")
cursor = con.cursor()


def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT,soyad TEXT,numara INT,ogrenci_notu INT)")


def degerekle():
    cursor.execute("INSERT INTO ogrenciler VALUES('Gulay Busenur','Elmas','2014010213007','78')")
    con.commit()
    con.close()

tabloolustur()
degerekle()
