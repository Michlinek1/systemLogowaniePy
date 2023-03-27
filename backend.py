"""Laczenie z baza danych i dodanie ich"""
"""Laczenie z baza danych i dodanie ich"""
import mysql.connector
from main import App
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="systemLogowania"
)

mycursor = mydb.cursor()
def add(imie:str,nazwisko:str,wiek:int,miesiac:str,pesel = None):
    sql = "INSERT INTO uzytownik (`imie`, `nazwisko`, `imie`, `nazwisko`, `wiek`, `miesiac`, `pesel` ) VALUES (%s, %s)"
    val = (imie,nazwisko,wiek,miesiac,pesel if pesel is not None else "NULL")
    mycursor.execute(sql, val)

mycursor.execute("SELECT * FROM uzytkownik")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
