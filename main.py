print ("Exercitiul 1")
casa = "2"
string_in_string = "In padurea cu alune aveau casa {} pitici.".format(casa)
print (string_in_string)

print ("Extercitiul 2")
a = 10
a += len(str(a))
a = str(a)
print (a)

print ("Extercitiul 3")
a = 10
a += 1
print (a)

print ("Extercitiul 4")
a = input("Value=")
a = int(a)
a += int(1)
print (a)

print ("Extercitiul 5")
print ("nu am idee cum sa il fac")

print ("Extercitiul 6")
a=['a','b','c','d']
print(a[int(int('3' * 2)) // 11] )
a.insert(0, 'j')
print (a)
del a[:2]
print (a)
a.sort(reverse=True)
print (a)
b = a.copy()
print (a)
print (b)

print("Exercitiul 7")
a = { 'scaune': 30, 'plapume' : 15, 'pere' : 15}
values = a.values()
total = sum(values)
print(total)