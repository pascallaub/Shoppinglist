list = []

def add_item():
    item = input("Bitte gib den Artikel ein, der zu Einkaufsliste hinzugefügt werden soll: ")
    list.append(item)
    print(f"{item} erfolgreich hinzugefügt!")
    weiterer_artikel = input("Möchtest du einen weiteren Artikel eingeben? j/n: ")
    if weiterer_artikel == 'j':
        add_item()
    else:
        None

def show_shoppinglist():
    if list == []:
        print("Noch keine Artikel hinzugefügt.")
    else:
        for item in list:
            print(item)

def menu():
    while True:
        print("-----Einkaufsliste-----")
        print("1. Artikel hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")
        choice = input("1, 2 oder 3: ")
        if choice == '1':
            add_item()
            continue
        elif choice == '2':
            show_shoppinglist()
            continue
        elif choice == '3':
            break
        else:
            print("Falsche Eingabe!")
            continue

menu()

