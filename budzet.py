...         budzet [ "wydatki" ] . append( { "kwota" : kwota, "opis" : opis } )
...         print ( f "Dodano wydatek : {kwota} zł - { opis} " )
...     def pokaz_saldo ( ) :
...         suma_dochodow = sum( item [ "kwota" ] for item in budzet [ "dochody" ] )
...         suma_wydatkow = suma( item [ "kwota" ] fit item in budzet [ "wydatki" ] )
...         saldo = suma_dochodow - suma_wydatkow
...         print ( "\n=== Podsumowanie budżetu ===")
...         print ( f"Dochody: { suma_dochodow} zł )
...         print ( f"Wydatki: { suma_wydatkow} zł )
...         print ( f"Saldo: {saldo} zł\n" )
...     while True:
...         print ("Wybierz opcję: ")
...         print ("1 - Dodaj dodachód")
...         print ("2 - Dodaj wydatek" )
...         print ("3 - Saldo")
...         print ("4 - Koniec")
...         wybor = input ( "Twój wybór : ")
...         if wybor == "1":
...             dodaj_dochod ()
...         elif wybor == "2":
...             dodaj_wydatek ()
...         elif wobor == "3":
...             pokaz_saldo ()
...         elif wybor == "4":
...             print ("Zamykanie programu ...")
...             break
...         else:
...             print ("Nieprawidłowy wybór, spróbuj ponownie.")
...     import csv
...     import os
...     # Plik do przechowywania sanych
...     PLIK_BUDZETU = "budzet.csv"
...     #Słownik do przechowywania budżetu
...     budzet = {
...     "dochody": []
...     "wydatki": []
...     }
...     # Funkcja do wczytowania danych z pliku
...     def wczytaj_dane () :
...         if not os.path.exists (PLIK_BUDZETU):
...             return
...         witch open ( PLIK_BUDZETU, mode="r", newline="") as plik:
...             reader = csv.reader (plik)
...             for row in reader :
...                 kategoria, kwota, opis = row
...                 kwota = float (kwota)
...     budzet [Kategoria].append({"kwota": kwota, "opis": opis})
...     def zapisz_dane() :
...         with open(PLIK_BUDZETU, mode="w", newline="") as plik:
...             writer - csv.writer (plik)
...             for kategoria in ["dochody", "wydatki"]:
...                 for wpis in budzet [kategoria]:
...                     writer.writerow([kategoria], wpis ["kwota"], ["opis"]])
...     def dodaj_dochod():
...         kwota = float(input("Podaj kwotę dochodu: "))
...         opis = input("Podaj opis (np. pensja, dodatkowy zarobek"): ")
...         budzet ["dochody"].append({"kwota" : kwota, "opis" : opis})
...         zapisz_dane()
...         print(f"Dodano dochód: {kwota} zł - {opis}")
...     def dodaj_wydatek():
...         kwota = float(input("Podaj kwotę wydatku: "))
...         opis = input("Podaj opis (np. jedzenie, rachunki): ")
...         budzet ["wydatki"].append({"kwota": kwota, "opis": opis})
...         zapisz_dane()
...         print(f"Dodano wydatek: {kwota} zł - {opis}")
...     def podaz_saldo():
...         suma_dochodow = sum(item["kwota"] for item in budzet["dochody"])
...         suma_wydatkow = sum(item["kwota"] for item in budzet["wydatki"])
...         saldo = suma_dochodow - suma_wydatkow
...         print("\n=== Podsumowanie budżetu ===")
...         print(f"Dochody: {suma_dochodów} zł")
...         print(f"Wydatki: {suma_wydatkow} zł")
...         print(f"Saldu: {saldo} zł\n")
... wczytaj_dane()
... while True:
...     print("Wybierz opcję")
...     print("1 - Dodaj dochód")
...     print("2 - Dodaj wydatek")
...     print("3 - Saldo")
...     print("4 - Zakończ")
...     wybor = input("Twój wybór: ")
...     if wybor == "1":
...         dodaj_dochod()
...     elif wybor == "2":
...         dodaj_wydatek()
...     elif wybor == "3":
...         pokaz_saldo()
...     elif wybor == "4":
...         print("Zamykanie programu...")
...         break
...     else:
...         print("Nieprawidłowy wybór, spróbuj ponownie. ")
...