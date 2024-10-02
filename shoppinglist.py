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

add_item()
show_shoppinglist()