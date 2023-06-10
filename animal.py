def animal():
    def czy_slowo(imie, typ, rasa):
        if imie.isalpha() and typ.isalpha() and rasa.isalpha():
            return True
        else:
            return False
        
    imie = input("Podaj imię zwierzaka: ")
    typ = input("Co to za zwierzak: ")
    rasa = input("Podaj rasę zwierzaka: ")

    while not czy_slowo(imie, typ, rasa):
        print("Wprowadzone dane są niepoprawne. Spróbój ponownie!")
        imie = input("Podaj imię zwierzaka: ")
        typ = input("Co to za zwierzak: ")
        rasa = input("Podaj rasę zwierzaka: ")


        
    wiek = input("Podaj wiek zwierzaka: ")
    while not wiek.isdigit():
        print("Wprowadzony wiek nie jest liczbą.")
        wiek = input("Podaj wiek ponownie: ")
        
    print("Zwierzak nazywa się "+ imie.capitalize())
    print("Zwierzakiem jest: "+ typ.capitalize())
    print("Rasa zwierzaka to: " + rasa.capitalize())
    print("Zwierzak ma "+ wiek + " lat")
    