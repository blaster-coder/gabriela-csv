import csv
import random 
import string

def llegir_dades_csv(nom_arxiu):
    estudiants = []
    with open(nom_arxiu, mode='r', encoding='utf-8') as fitxer:
        lector = csv.DictReader(fitxer)
        for fila in lector:
            estudiants.append(fila)
    return estudiants
    
def generar_mail(nom, cognoms):
    email = f"{nom}.{cognoms}@insgabrielamistral.cat".lower().replace(" ","")
    print(email)
    
def generar_contrasenya():
    caracters = string.ascii_letters + string.digits + string.punctuation
    contrasenya = "".join(random.choice(caracters) for _ in range(1,11))  
    
    print(contrasenya)
    
    
# Funció per fer de deures
def escriure_csv(estudiants, nom_arxiu):
    print("Escriure csv")
    
    
# EXEMPLE D'US DEL PROGRAMA 
nom_arxiu_entrada = "estudiants_nous.csv"
estudiants = llegir_dades_csv(nom_arxiu_entrada)
for estudiant in estudiants:
    estudiant["email"] = generar_mail(estudiant["nom"], estudiant["cognoms"])
    estudiant["contrasenya"] = generar_contrasenya()
    
print(estudiants)