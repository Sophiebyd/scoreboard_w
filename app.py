import os
from dotenv import load_dotenv
from pymongo import MongoClient
import customtkinter as ctk

# Charger le .env
load_dotenv()
mongo_url = os.getenv("MONGO_URL")  # récupère l'URL de connexion

# Connexion à MongoDB Atlas
client = MongoClient(mongo_url)

# Sélection de la DB et de la collection
db = client["Waterpolo"]  # le nom de ta base
collection = db["Score"]  # le nom de ta collection

# --- Configuration interface ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Application Python + MongoDB Atlas")
app.geometry("400x300")

# --- Fonctions ---
def enregistrer():
    nom = entry_nom.get()
    age = entry_age.get()

    if not nom or not age:
        label_resultat.configure(text="Champs manquants !")
        return

    try:
        age_int = int(age)
    except ValueError:
        label_resultat.configure(text="L'âge doit être un nombre !")
        return

    collection.insert_one({"nom": nom, "age": age_int})
    label_resultat.configure(text=f"{nom} enregistré !")

    entry_nom.delete(0, "end")
    entry_age.delete(0, "end")

# --- Interface utilisateur ---
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
