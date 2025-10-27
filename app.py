import customtkinter as ctk
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Waterpolo"]
collection = db["historique"]

# Configuration de la fenêtre
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Application Python + MongoDB")
app.geometry("400x300")

# Fonctions
def enregistrer():
    nom = entry_nom.get()
    age = entry_age.get()
    if nom and age:
        collection.insert_one({"nom": nom, "age": int(age)})
        label_resultat.configure(text=f"{nom} enregistré !")
        entry_nom.delete(0, "end")
        entry_age.delete(0, "end")
    else:
        label_resultat.configure(text="Champs manquants !")

# Interface
ctk.CTkLabel(app, text="Nom :").pack(pady=5)
entry_nom = ctk.CTkEntry(app, width=200)
entry_nom.pack(pady=5)

ctk.CTkLabel(app, text="Âge :").pack(pady=5)
entry_age = ctk.CTkEntry(app, width=200)
entry_age.pack(pady=5)

ctk.CTkButton(app, text="Enregistrer", command=enregistrer).pack(pady=10)
label_resultat = ctk.CTkLabel(app, text="")
label_resultat.pack(pady=10)

app.mainloop()
