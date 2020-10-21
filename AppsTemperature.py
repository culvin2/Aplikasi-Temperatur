print("-----Apps Temperature-----")
print("-----****************-----")
print('''
1. Celcius   --> Reamur
2. Celcius   --> Farenheit
3. Farenheit --> Celcius
4. Faremheit --> Reamur
5. Reamur    --> Farenheit
6. Reamur    --> Celcius''')
a = int(input("Masukkan pilihan program : "))

if a ==1:
    b = int(input("Masukkan ^C : "))
    re = 4/5 * b
    print("^Reamur :",re)
elif a ==2:
    c = int(input("Masukkan ^C : "))
    fa = (9/5 * c)+32
    print("^Farenheit :",fa)
elif a ==3:
    d = int(input("Masukkan ^F : "))
    ce = 5/9 * (d-32)
    print("^Celcius :",ce)
elif a ==4:
    e = int(input("Masukkan ^F : "))
    rea = 4/9 * (e-32)
    print("^Reamur :",rea)
elif a ==5:
    f = int(input("Masukkan ^R : "))
    Fa = (9/4 * f+32)
    print("^Farenheit :",Fa)
elif a ==6:
    g = int(input("Masukkan ^R : "))
    cel = 5/4 * g
    print("^Celcius :",cel)
else:
    print("Syntax Error")
