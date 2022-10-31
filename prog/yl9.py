print("Sisesta kolmnurga külgede pikkused")

x = int(input("Sisesta külg x: "))
y = int(input("Sisesta külg y: "))
z = int(input("Sisesta külg z: "))

if x == y == z :
    print("Kolmnurk on Võrdkülgne")
elif (x + y < z) or (x + z < y) or (z + y < x):
    print("Ei ole võimalik")
elif x==y or y==z or z==x :
    print("kolmnurk on võrdhaarne")
else :
    print("kolmnurk on erikülgne")    