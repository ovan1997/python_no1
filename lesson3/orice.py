print("exercitiul1")

Celsius = int(input("Introduceti grade Celsius: "))

Fahrenheit = (Celsius * 9/5) - 32

print (Fahrenheit)



Fahrenheit = int(input("Introduceti grade Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5/9

print (Celsius)

print("exercitiul2")

a = input('introdu_cuvin :')

if  a[0] == a[-1] and a[1] == a[-2]:
    print('palindrom')
else:
    print('cuvint_simplu')

 
print("Exercitiul3")

a = int(input('introdu cifra: '))
for i in range(a):
    if i % 2 != 0:
        continue
    a += (i)
    print(i)
print(a)

print("Exercitiul4")

count = 1000
sum = 0
while count < 2300:
    if count % int(5 and 7) == 0:
        sum += count 
    count += 1
print(sum)

print("Exercitiul5")

a = input("introduceti cuvintul: ")
cif = 0
lit = 0
for i in a:
    if (i.isdigit()):
            cif = cif + 1
    if (i.isalpha()):
            lit = lit + 1
print("cifre")
print(cif)
print("litere")
print(lit)    



