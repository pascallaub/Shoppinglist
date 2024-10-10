import sqlite3
import tkinter as tk

con = sqlite3.connect('shoppinglist.db')
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS groceries (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(32) NOT NULL,
               amount INTEGER NOT NULL,
               price INTEGER,
               category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
                )
            ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(32) NOT NULL)
               ''')

cursor.execute("PRAGMA foreign_keys = ON;")

def switch_frame(frame):
    frame.tkraise()

def add_item():
    name = entry1.get()
    amount = entry2.get()
    price = entry3.get()
    cursor.execute('''INSERT INTO groceries (name, amount, price) VALUES (?, ?, ?)''', (name, amount, price))
    label2.config(text=f"{name} erfolgreich hinzugefügt!")
    con.commit()
    
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)


def show_shoppinglist():
            cursor.execute("SELECT * FROM groceries")
            list = cursor.fetchall()
            result_text = ""
            for row in list:
                result_text += f"Name: {row[1]}, Menge: {row[2]}, Preis: {row[3]}\n"
            label4.config(text=result_text)
        
def show_search_id():
        srch_id = entry6.get()
        cursor.execute("SELECT * FROM groceries WHERE id = ?", (srch_id,))
        item = cursor.fetchone()
        label5.config(text=f"{item}")

def show_search_name():
        name = entry7.get()
        cursor.execute("SELECT * FROM groceries WHERE name = ?", (name,))
        name_item = cursor.fetchone()
        label6.config(text=f"{name_item}")

def show_search_cat():
        category = entry8.get()
        cursor.execute('''SELECT groceries.* FROM groceries
                        JOIN categories ON groceries.category_id = categories.id
                        WHERE categories.name = ?
                        ''', (category,))
        output = cursor.fetchall()
        for row in output:
              label7.config(text=f"Name: {row[1]}, Menge: {row[2]}, Preis: {row[3]}\n")


def update_list():
    id = entry9.get()
    name = entry10.get()
    amount = entry11.get()
    price = entry12.get()
    cursor.execute('''UPDATE groceries SET name = ?, amount = ?, price = ? WHERE id = ?''', (name, amount, price, id))
    con.commit()
    label8.config(text=f"{name} erfolgreich geändert!")

def delete_item():
    id = entry13.get()
    cursor.execute("DELETE FROM groceries WHERE id = ?", (id,))
    label9.config(text="Erfolgreich gelöscht!")

def categories():
    id = entry4.get()
    category_name = entry5.get()
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))
    category_id = cursor.lastrowid
    cursor.execute("UPDATE groceries SET category_id = ? WHERE id = ?", (category_id, id))
    con.commit()
    label3.config(text="Erolfgreich!")
    switch_frame(frame_menu)

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Einkaufsliste")
root.geometry("400x400")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Hauptmenü Frame
frame_menu = tk.Frame(root)
frame_menu.grid(row=0, column=0, sticky='nsew')

# Artikel hinzufügen Frame
frame_add_item = tk.Frame(root)
frame_add_item.grid(row=0, column=0, sticky='nsew')

# Kategorien Frame
frame_categories = tk.Frame(root)
frame_categories.grid(row=0, column=0, sticky='nsew')

# Artikel anzeigen Menü Frame
frame_show = tk.Frame(root)
frame_show.grid(row=0, column=0, sticky='nsew')

# Artikel suche Frame
frame_show_search = tk.Frame(root)
frame_show_search.grid(row=0, column=0, sticky='nsew')

# Artikel updaten Frame
frame_update = tk.Frame(root)
frame_update.grid(row=0, column=0, sticky='nsew')

# Artikel löschen Frame
frame_delete = tk.Frame(root)
frame_delete.grid(row=0, column=0, sticky='nsew')

# Hauptmenü (Frame1)
label1 = tk.Label(frame_menu, text="Willkommen im Einkaufslisten-Manager!", font=('Arial', 14))
label1.pack(pady=20)

btn_add = tk.Button(frame_menu, text="1. Hinzufügen", command=lambda: switch_frame(frame_add_item), width=20)
btn_add.pack(pady=5)

btn_add = tk.Button(frame_menu, text="2. Anzeigen", command=lambda: switch_frame(frame_show), width=20)
btn_add.pack(pady=5)

btn_add = tk.Button(frame_menu, text="3. Aktualisieren", command=lambda: switch_frame(frame_update), width=20)
btn_add.pack(pady=5)

btn_add = tk.Button(frame_menu, text="4. Löschen", command=lambda: switch_frame(frame_delete), width=20)
btn_add.pack(pady=5)

btn_add = tk.Button(frame_menu, text="5. Kategorien", command=lambda: switch_frame(frame_categories), width=20)
btn_add.pack(pady=5)

btn_add = tk.Button(frame_menu, text="6. Beenden", command=root.quit, width=20)
btn_add.pack(pady=5)

# Artikel hinzufügen Widgets (Frame2)
label_add = tk.Label(frame_add_item, text='Artikel hinzufügen', font=('Arial', 14))
label_add.pack(pady=20)

entry1 = tk.Entry(frame_add_item, width=30)
entry1.pack(pady=10)
entry1.insert(0, 'Artikelname')

entry2 = tk.Entry(frame_add_item, width=30)
entry2.pack(pady=10)
entry2.insert(0, "Menge")

entry3 = tk.Entry(frame_add_item, width=30)
entry3.pack(pady=10)
entry3.insert(0, 'Preis')

label2 = tk.Label(frame_add_item, text="")
label2.pack(pady=10)

btn_save = tk.Button(frame_add_item, text="Artikel speichern", command=add_item, width=20)
btn_save.pack(pady=5)

btn_back = tk.Button(frame_add_item, text="Zurück zum Menü", command=lambda: switch_frame(frame_menu), width=20)
btn_back.pack(pady=5)

# Kategorien (Frame3)
cat_add = tk.Label(frame_categories, text='Kategorien hinzufügen', font=('Arial', 14))
cat_add.pack(pady=20)

entry4 = tk.Entry(frame_categories, width=30)
entry4.pack(pady=10)
entry4.insert(0, "ID")

entry5 = tk.Entry(frame_categories, width=30)
entry5.pack(pady=10)
entry5.insert(0, "Kategorie")

label3 = tk.Label(frame_categories, text="")
label3.pack(pady=10)

btn_save1 = tk.Button(frame_categories, text="Kategorie speichern", command=categories, width=20)
btn_save1.pack(pady=5)

btn_back1 = tk.Button(frame_categories, text="Zurück zum Menü", command=lambda: switch_frame(frame_menu))
btn_back1.pack(pady=5)

# Artikel anzeigen
art_show = tk.Label(frame_show, text="Artikel anzeigen", font=('Arial', 14))
art_show.pack(pady=20)
btn_show = tk.Button(frame_show, text="Alles anzeigen", command=show_shoppinglist, width=20)
btn_show.pack(pady=5)

btn_show1 = tk.Button(frame_show, text="ID/Name/Kategorie suchen", command=lambda: switch_frame(frame_show_search), width=20)
btn_show1.pack(pady=5)

btn_back2 = tk.Button(frame_show, text="Zurück zum Menü", command=lambda: switch_frame(frame_menu), width=20)
btn_back2.pack(pady=5)

label4 = tk.Label(frame_show, text="")
label4.pack(pady=10)

# Suche nach ID/Name Frame
srch_show = tk.Label(frame_show_search, text="Nach ID, Kategorie oder Name suchen", font=('Arial', 14))
srch_show.pack(pady=20)

entry6 = tk.Entry(frame_show_search, width=30)
entry6.pack(pady=10)
entry6.insert(0, "ID")

btn_id = tk.Button(frame_show_search, text="Nach ID suchen", command=show_search_id, width=20)
btn_id.pack(pady=5)

label5 = tk.Label(frame_show_search, text="")
label5.pack(pady=10)

entry7 = tk.Entry(frame_show_search, width=30)
entry7.pack(pady=10)
entry7.insert(0, "Name")

btn_name = tk.Button(frame_show_search, text="Nach Name suchen", command=show_search_name, width=20)
btn_name.pack(pady=5)

label6 = tk.Label(frame_show_search, text="")
label6.pack(pady=5)

entry8 = tk.Entry(frame_show_search, width=30)
entry8.pack(pady=5)
entry8.insert(0, "Kategorie")

btn_cat = tk.Button(frame_show_search, text="Kategorie", command=show_search_cat, width=20)
btn_cat.pack(pady=5)

label7 = tk.Label(frame_show_search, text="")
label7.pack(pady=5)

btn_back3 = tk.Button(frame_show_search, text="Zurück zum Menü", command=lambda: switch_frame(frame_menu), width=20)
btn_back3.pack(pady=5)

# Artikel updaten Frame
update_show = tk.Label(frame_update, text="Artikeldaten aktualisieren", font=('Arial', 14))
update_show.pack(pady=20)

entry9 = tk.Entry(frame_update, width=30)
entry9.pack(pady=10)
entry9.insert(0, "ID")

entry10 = tk.Entry(frame_update, width=30)
entry10.pack(pady=10)
entry10.insert(0, "Neuer Name")

entry11 = tk.Entry(frame_update, width=30)
entry11.pack(pady=10)
entry11.insert(0, "Neue Menge")

entry12 = tk.Entry(frame_update, width=30)
entry12.pack(pady=10)
entry12.insert(0, "Neuer Preis")

btn_update = tk.Button(frame_update, text="Aktualisieren", command=update_list, width=20)
btn_update.pack(pady=10)

label8 = tk.Label(frame_update, text="")
label8.pack(pady=5)

btn_back4 = tk.Button(frame_update, text="Zurück zum Menü", command=lambda: switch_frame(frame_menu), width=20)
btn_back4.pack(pady=5)

# Artikel löschen Frame
delete_show = tk.Label(frame_delete, text="Artikel löschen", font=('Arial', 14))
delete_show.pack(pady=20)

entry13 = tk.Entry(frame_delete, width=30)
entry13.pack(pady=10)
entry13.insert(0, "ID")

btn_delete = tk.Button(frame_delete, text="Löschen", command=delete_item, width=20)
btn_delete.pack(pady=5)

label9 = tk.Label(frame_delete, text="")
label9.pack(pady=5)

btn_back5 = tk.Button(frame_delete, text="Zurück zum Menü", command=lambda: switch_frame(frame_menu), width=20)
btn_back5.pack(pady=5)


switch_frame(frame_menu)



if __name__ == '__main__':
    root.mainloop()