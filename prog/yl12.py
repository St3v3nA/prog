puuviljad : ["pirn", "Õun", "Mango"]

print(puuviljad)

print("Esimene puuvili:", puuviljad[0])

puuviljad.append("Banaan")
print("Viimane puuvili:", puuviljad[len(puuviljad)-1])

puuviljad[1] = "Viinamarjad"
print(puuviljad)

if "Õun" in puuviljad:
    print("Õun on olemas.")
else:
    print("Õuna ei ole olemas.")

print("Listis on:" len(puuviljad),)

puuviljad.remove("pirn")
print(puuviljad)

puuviljad.reverse()
puuviljad.sort()
print(puuviljad)