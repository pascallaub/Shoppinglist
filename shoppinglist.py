list = []

def add_item():
    item = input("Bitte gib den Artikel ein, der zu Einkaufsliste hinzugefügt werden soll: ")
    list.append(item)
    print(f"{item} erfolgreich hinzugefügt!")

add_item()