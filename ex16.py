'''Notes'''
A = float(input("Nota Numerica:"))
if A >= 0 and A < 1.5:
    print("Molt Deficient")
else:
    if A >= 1.5 and A < 4.0:
        print("Insuficient")
    else:
        if A >= 4.0 and A < 5.5:
            print("Suficient")
        else:
            if A >= 5.5 and A < 6.5:
                print("Be")
            else:
                if A >= 6.5 and A < 8.5:
                    print("Notable")
                else:
                    if A >= 8.5 and A < 10:
                        print("excel·lent")
                    else:
                        if A > 10:
                            print("La nota ha de ser sobre 10")
