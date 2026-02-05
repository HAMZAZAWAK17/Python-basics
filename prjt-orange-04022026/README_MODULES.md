# 📦 Guide des Modules en Python

Les modules permettent d'utiliser des fonctionnalités prêtes à l'emploi créées par d'autres développeurs ou faisant partie de la bibliothèque standard de Python.

## 1. Comment importer un module ?

Il existe trois façons principales d'importer :

```python
import math               # Importe tout le module
from random import randint # Importe uniquement une fonction spécifique
import datetime as dt      # Importe avec un alias (nom raccourci)
```

## 2. Les Modules Standards Utilisés

### 📐 Module `math`
Utilisé pour les calculs mathématiques avancés.
- `math.sqrt(x)` : Racine carrée.
- `math.pi` : La constante Pi (~3.14).
- `math.ceil(x)` / `math.floor(x)` : Arrondi supérieur/inférieur.

### 🎲 Module `random`
Utilisé pour générer de l'aléatoire.
- `randint(a, b)` : Génère un nombre entier entier entre `a` et `b` (inclus).
- `choice(liste)` : Choisit un élément au hasard dans une liste.

### 📅 Module `datetime`
Utilisé pour manipuler les dates et les heures.
- `datetime.now()` : Récupère l'instant présent (date + heure).
- `.strftime("%d/%m/%Y")` : Formate une date en texte lisible.

## 3. Avantages des Modules
1. **Productivité** : Ne pas réinventer la roue.
2. **Maintenance** : Code plus clair et bien organisé.
3. **Performance** : Les fonctions des modules standards sont optimisées.

---
*Référence : Chapitre 25 - modules.py*
