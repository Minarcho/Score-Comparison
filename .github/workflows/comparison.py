def comparison():
    homeside = None
    awayside = None

    while not homeside:
        try:
            homeside = int(input("Ev sahibi takımın attığı gol sayısını giriniz:"))
        except ValueError:
            print("Lütfen bir rakam giriniz!")


    while not awayside:
        try:
            awayside = int(input("Deplasman takımının attığı gol sayısını giriniz:"))
        except ValueError:
            print("Lütfen bir rakam giriniz!")


    if homeside > awayside:
        print("Ev sahibi takım 3 puan kazandı.")

    elif homeside < awayside:
        print("Deplasman takımı 3 puan kazandı.")
    else:
        print("İki takım da sahadan birer puan ile ayrıldı")


comparison()
