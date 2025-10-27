# --- Import de la bibliothèque ---
# customtkinter est une version moderne et stylisée de tkinter (pour faire des interfaces graphiques)
import customtkinter as ctk

# --- Configuration générale de l'apparence de l'application ---
# On définit le thème de l'application (ici "dark" pour un mode sombre)
ctk.set_appearance_mode("dark")
# On définit la couleur principale du thème (ici "blue")
ctk.set_default_color_theme("blue")

# --- Création de la fenêtre principale ---
# On initialise l'application principale
app = ctk.CTk()
# On définit le titre de la fenêtre
app.title("Test Python")
# On définit la taille de la fenêtre (largeur x hauteur)
app.geometry("400x300")

# --- Fonction exécutée quand on clique sur le bouton "Enregistrer" ---
def enregistrer():
    # On récupère le texte tapé dans les champs "Nom" et "Âge"
    nom = entry_nom.get()
    age = entry_age.get()

    # Vérifie que les deux champs ne sont pas vides
    if not nom or not age:
        label_resultat.configure(text="Champs manquants !")
        return

    # Vérifie que l’âge est bien un nombre
    try:
        age_int = int(age)
    except ValueError:
        label_resultat.configure(text="L'âge doit être un nombre !")
        return

# --- Interface utilisateur ---
# Label = texte affiché à l’écran
ctk.CTkLabel(app, text="Nom :").pack(pady=5)  # Texte "Nom :"
# Champ de saisie pour le nom
entry_nom = ctk.CTkEntry(app, width=200)
entry_nom.pack(pady=5)

# Même chose pour l’âge
ctk.CTkLabel(app, text="Âge :").pack(pady=5)
entry_age = ctk.CTkEntry(app, width=200)
entry_age.pack(pady=5)

# Bouton "Enregistrer" → quand on clique, il appelle la fonction enregistrer()
ctk.CTkButton(app, text="Enregistrer", command=enregistrer).pack(pady=10)

# Label pour afficher les messages (succès, erreur, etc.)
label_resultat = ctk.CTkLabel(app, text="")
label_resultat.pack(pady=10)

# --- Lancement de la boucle principale de l'application ---
# Cette commande garde la fenêtre ouverte et active l’interface
app.mainloop()
