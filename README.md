📚 Automatització del Registre d'Estudiants
Benvingut/da a aquest projecte! L'objectiu principal és llegir les dades d'un fitxer CSV, generar automàticament un correu electrònic i una contrasenya segura per a cada estudiant i, finalment, emmagatzemar aquesta informació actualitzada en un nou fitxer CSV.

🚀 Què fa el codi?
Lectura de Dades

Es carrega el fitxer estudiants_nous.csv i s’extreuen els noms, cognoms i el curs de cada estudiant.
Generació del Correu

A partir del nom i dels cognoms, es crea un correu institucional (per exemple: joan.perez@institutgm.cat).
Generació de Contrasenya

S’utilitzen funcions de Python (random, secrets, etc.) per a generar una contrasenya aleatòria i segura per a cada estudiant.
Funció per Escriure el Nou CSV (pendent)

Cal completar la part del codi que crea el fitxer alta_alumnes.csv afegint el correu i la contrasenya als registres dels estudiants.

💻 Ús
git clone https://github.com/blaster-coder/gabriela-csv
cd gabriela-csv

RECORDA QUE HAS DE CONTRUBIR EN AQUESTA APP, DESENVOLUPA LA FUNCIÓ escriure_csv 
