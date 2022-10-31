import re

letters="a","e","i","o","u","ö","ä","ü","õ"

a=input("Sisesta tekst: ")

b= a.count("a") +a.count("e") + a.count("i") + a.count("o") + a.count ("u") + a.count("ö") + a.count("ä") + a.count("õ") + a.count("ü")

print(b)