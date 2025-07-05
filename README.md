# Production nucléaire annuelle en France

Ce script Python télécharge et analyse les données de production et de consommation d'électricité en France, fournies par RTE . Il calcule et affiche la **production nucléaire** et la **consommation totale d'électricité en France**, pour chaque mois et pour l'année en cours.

### 📥 Prérequis

- Python 3.7+
- Bibliothèques requises :
  ```bash
  pip install pandas requests 
  ```
ou bien 
  ```bash
  pip install -r requirements.txt
  ```


### 🚀 Utilisation

```bash
python total_nuc.py
```

Le fichier `.xls` sera extrait dans le dossier courant.

### 📄 Exemple de sortie

```
-----------------------------

samedi 05 juillet 2025 à 22:15

-----------------------------

        Mois Nucléaire (TWh) Consommation (TWh)
Janvier 2025           38,59              48,68
Février 2025           31,88              41,40
   Mars 2025           32,18              39,93
  Avril 2025           26,96              32,16
    Mai 2025           25,40              30,01
   Juin 2025           26,10              31,00
Juillet 2025            4,46               5,64

-----------------------------

🔋 Production nucléaire totale en 2025: 185,57 TWh
⚡ Consommation totale en 2025: 228,82 TWh
```

### 📁 Source des données

[eco2mix – RTE France](https://www.rte-france.com/eco2mix)

---

# Annual Nuclear Production in France

This Python script downloads and analyzes electricity production and consumption data in France, provided by RTE. It focuses on **nuclear power production** and **total electricity consumption**, calculating the monthly totals for the current year.

### 📥 Requirements

- Python 3.7+
- Required libraries:
  ```bash
  pip install pandas requests

### 🚀 How to Run

  ```bash
  pip install pandas requests 
  ```
or 
  ```bash
  pip install -r requirements.txt
  ```


### 📄 Sample Output

```
-----------------------------

samedi 05 juillet 2025 à 22:15

-----------------------------

        Mois Nucléaire (TWh) Consommation (TWh)
Janvier 2025           38,59              48,68
Février 2025           31,88              41,40
   Mars 2025           32,18              39,93
  Avril 2025           26,96              32,16
    Mai 2025           25,40              30,01
   Juin 2025           26,10              31,00
Juillet 2025            4,46               5,64

-----------------------------

🔋 Production nucléaire totale en 2025: 185,57 TWh
⚡ Consommation totale en 2025: 228,82 TWh
```

### 📁 Data Source

Data provided by [RTE France – eco2mix](https://www.rte-france.com/eco2mix)

---

The output is in French. Deal with it 😊. 
>>>>>>> a273b76 (Initial commit ⚛️)
