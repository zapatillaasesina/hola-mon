'''Notes'''
print("(Molt Deficient(D), Insuficient(I), Suficient(S), Be(B), Notable(N), excelent(E)")
A = input("Nota Alfabetica:")
if A == 'D' or A == 'd':
    print("La nota es: 1.5")
else:
    if A == 'I' or A == 'i':
        print("La nota es: 4.0")
    else:
        if A == 'S' or A == 's':
            print("La nota es: 5.5")
        else:
            if A == 'B'or A == 'b':
                print("La nota es: 6.5")
            else:
                if A == 'N' or A == 'n':
                    print("La nota es: 8")
                else:
                    if A == 'E' or A == 'e':
                        print("La nota es: 9.5")
                    else:
                        print("Error")
