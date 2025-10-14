# bilangan = float(input("Masukan bilangan:"))
# if bilangan == 0:
#     print("Termasuk bilangan nol")
# elif bilangan % 1 == 0:
#     print("Termasuk bilangan bulat")
# else:
#     print("Termasuk bilangan pecahan")


bilangan = input("Masukkan bilangan: ")
if bilangan:
    bilangan = float(bilangan)
    if bilangan == 0:
        print("Ini adalah bilangan nol.")
    elif bilangan % 1 == 0:
        print("Ini adalah bilangan bulat.")
    else:
        print("Ini adalah bilangan pecahan.")
else:
    print("Bilangan yang anda masukan tidak valid.")