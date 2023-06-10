def human():    
    def czy_slowo(imie, nazwisko, zawod):
        if imie.isalpha() and nazwisko.isalpha() and zawod.isalpha():
            return True
        else:
            return False
        
    imie = input("Podaj imie czlowieka: ")
    nazwisko = input("Podaj nazwisko czlowieka: ")
    zawod = input("Podaj zawod czlowieka: ")

    while not czy_slowo(imie, nazwisko, zawod):
        print("Wprowadzone dane są niepoprawne. Spróbój ponownie!")
        imie = input("Podaj imie czlowieka: ")
        nazwisko = input("Podaj nazwisko czlowieka: ")
        zawod = input("Podaj zawod czlowieka: ")


    wiek = input("Podaj wiek czlowieka: ")
    while not wiek.isdigit():
        print("Wprowadzony wiek nie jest liczbą.")
        wiek = input("Podaj wiek ponownie: ")
        
    print("Czlowiek nazywa się "+ imie.capitalize() + " " +nazwisko.capitalize())
    print("Zawod czlowieka: " + zawod.capitalize())
    print("Wiek człowieka to: "+ wiek)
