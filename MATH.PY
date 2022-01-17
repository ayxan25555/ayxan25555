print("""********************************
PROSESLƏR
1. Toplama Prosesi
2. Çıxma Prosesi
3. Vurma Prosesi
4. Bölmə Prosesi
****************************************
""")
while True:
    PROSES = input("4 prosesdən birini seçin (Çıxış üçün 'q' ya bas): ")
    if PROSES == 'q':
        print("proses bitdi...")
        quit()
    elif PROSES == "1":
        print("------Toplama Prosesi------")
        sayi1 = int(input("1.ƏDƏD DAXİL EDİN: "))
        sayi2 = int(input("2.ƏDƏD DAXİL EDİN: "))
        print("{}  +   {}    =  {}".format(sayi1, sayi2, sayi1+sayi2))
    elif PROSES == "2":
        print("------Çıxma Prosesi------")
        sayi1 = float(input("1.ƏDƏD DAXİL EDİN: "))
        sayi2 = float(input("2.ƏDƏD DAXİL EDİN: "))
        print("{}  -   {}    =  {}".format(sayi1, sayi2, sayi1-sayi2))
    elif PROSES == "3":
        print("------Vurma Prosesi------")
        sayi1 = float(input("1.ƏDƏD DAXİL EDİN: "))
        sayi2 = float(input("2.ƏDƏD DAXİL EDİN: "))
        print("{}  x   {}    =  {}".format(sayi1, sayi2, sayi1*sayi2))
    elif PROSES == "4":
        print("------Bölmə Prosesi------")
        try:
            sayi1 = int(input("1.ƏDƏD DAXİL EDİN: "))
            sayi2 = int(input("2.ƏDƏD DAXİL EDİN: "))
            print("{}  /   {}    =  {:.2f}".format(sayi1, sayi2, sayi1/sayi2))
        except ZeroDivisionError:
            print("Bir ədədi 0'a bölə bilməzsiniz!")
        except ValueError:
            print("zəhmət olmasa sadəcə ədəd daxil edin!")
    else:
        print("Geçersiz Seçenek...")
