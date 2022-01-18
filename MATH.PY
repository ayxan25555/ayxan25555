print("""********************************
PROSESLƏR
1. Toplama Prosesi
2. Çıxma Prosesi
3. Vurma Prosesi
4. Bölmə Prosesi
5. Mod alma Prosesi
6. Tam hissə alma Prosesi
7. Üst alma Prosesi
****************************************
""")
while True:
    PROSES = input("7 prosesdən birini seçin (Çıxış üçün 'q' ya bas): ")
    if PROSES == 'q':
        print("proses bitdi...")
        quit()
    elif PROSES == "1":
        print("------Toplama Prosesi------")
        sayi1 = float(input("1.ƏDƏD DAXİL EDİN: "))
        sayi2 = float(input("2.ƏDƏD DAXİL EDİN: "))
        print("{}  +   {}    =  {}".format(sayi1, sayi2, sayi1+sayi2))
    elif PROSES == "2":
        print("------Çıxma Prosesi------")
        sayi1 = float(input("1.ƏDƏD DAXİL EDİN: "))
        sayi2 = float(input("2.ƏDƏD DAXİL EDİN: "))
        print("{}  -   {}    =  {}".format(sayi1, sayi2, round(sayi1-sayi2, 5)))
    elif PROSES == "3":
        print("------Vurma Prosesi------")
        sayi1 = float(input("1.ƏDƏD DAXİL EDİN: "))
        sayi2 = float(input("2.ƏDƏD DAXİL EDİN: "))
        print("{}  x   {}    =  {}".format(sayi1, sayi2, sayi1*sayi2))
    elif PROSES == "4":
        print("------Bölmə Prosesi------")
        try:
            sayi1 = float(input("1.ƏDƏD DAXİL EDİN: "))
            sayi2 = float(input("2.ƏDƏD DAXİL EDİN: "))
            print("{}  /   {}    =  {:.2f}".format(sayi1, sayi2, sayi1/sayi2))
        except ZeroDivisionError:
            print("Bir ədədi 0'a bölə bilməzsiniz!")
        except ValueError:
            print("zəhmət olmasa sadəcə ədəd daxil edin!")
    elif PROSES == "5":
        print("------Mod alma Prosesi------")
        sayi1 = float(input("1.ƏDƏD DAXİL EDİN: "))
        sayi2 = float(input("2.ƏDƏD DAXİL EDİN: "))
        print("{}  %   {}    =  {}".format(sayi1, sayi2, sayi1 % sayi2))
    elif PROSES == "6":
        print("------Tam hissə alma Prosesi------")
        sayi1 = float(input("1.ƏDƏD DAXİL EDİN: "))
        sayi2 = float(input("2.ƏDƏD DAXİL EDİN: "))
        print("{}  //  {}    =  {}".format(sayi1, sayi2, sayi1 // sayi2))
    elif PROSES == "7":
        print("------Üst alma Prosesi------")
        sayi1 = float(input("1.ƏDƏD DAXİL EDİN: "))
        sayi2 = float(input("2.ƏDƏD DAXİL EDİN: "))
        print("{}  **  {}    =  {}".format(sayi1, sayi2, round(sayi1 ** sayi2, 6)))
    else:
        print("Geçersiz Seçenek...")
