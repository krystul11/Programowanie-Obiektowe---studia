import importlib

while True:
    wybor = input("Jak chcesz stworzyć człowieka wpisz 'czlowiek', a jak zwierzaka to wpisz 'zwierzak'\n")

    if wybor == "zwierzak":
        try:
            module = importlib.import_module('animal')
            module.animal()
        except ModuleNotFoundError:
            print("Nie można zaimportować modułu 'b'.")
    elif wybor == "czlowiek":
        try:
            module = importlib.import_module('human')
            module.human()
        except ModuleNotFoundError:
            print("Nie można zaimportować modułu 'b'.")
        
    wybor = input("Czy chcesz zrobić coś nowego? (t/n): ")
    if wybor.lower() != "t":
        break
    