# Furniture

![Exemple de meuble construit avec la démo Furniture](images/demo_furniture.png)

Cette démo construit un meuble en agençant des **blocs**, puis en plaçant des
planches sur ces blocs. Un bloc décrit un volume de référence : sa position,
ses dimensions et les limites utiles à la construction. Les ressources, les
paramètres nommés et les propriétés des blocs sont conservés dans le Bundle de
la géométrie, tout au long de la pile de modifiers.

Pour créer les groupes et modifiers :

```python
from geonodes.demos import furniture

furniture.demo()
```

Après une mise à jour de la démo, utiliser `furniture.demo(rebuild=True)` pour
reconstruire les groupes existants.

## Conventions

Les coordonnées sont exprimées dans le repère local du meuble :

| Axe | Dimension |
| --- | --- |
| X | Profondeur |
| Y | Largeur |
| Z | Hauteur |

L'origine `(0, 0, 0)` est le coin inférieur gauche du meuble, côté arrière.
La façade se trouve du côté des X croissants, la droite du côté des Y croissants
et le haut du côté des Z croissants.

## Ressources et paramètres globaux

Les premiers modifiers définissent les ressources et les noms utilisés ensuite
pour construire le meuble.

**Define Resource** définit un matériau de construction : nom, dimensions,
épaisseur, matériau Blender et couleur. Les modifiers de construction choisissent
leurs planches à partir de ces ressources. **Define Plinth** précise la ressource,
la hauteur et les retraits de la plinthe.

**Capture Resources** récupère les ressources d'un autre objet. On peut ainsi
centraliser leur définition dans un objet de référence et l'utiliser pour
plusieurs meubles. Pour créer une variante de matériau ou d'épaisseur, il suffit
de changer les ressources de référence, sans refaire l'agencement des blocs.

**Define Named Dimensions** définit des valeurs nommées servant de paramètres
globaux : largeur d'un module, hauteur du meuble, jeu, etc. Les modifiers suivants
peuvent utiliser ces noms au lieu de répéter des valeurs numériques.

## Agencer les blocs

**Define Block** crée un bloc vide. Il n'ajoute aucune planche ; `Show Frame`
permet de visualiser son volume de référence.

Pour définir les positions et les dimensions, les champs proposent plusieurs
sources :

- **Value** : une valeur saisie directement dans `Offset`.
- **Name** : un paramètre global nommé, auquel on peut ajouter un décalage.
- **Block** : une propriété d'un bloc déjà défini, avec un décalage éventuel.

Une référence à un bloc peut utiliser sa largeur, son sommet, son bord droit,
son centre, etc. Le choix des limites du bloc permet de travailler avec ses
dimensions de référence, intérieures ou extérieures. Les dimensions proposent
aussi les modes `Dimension` et `Target` : donner une taille ou la coordonnée
à atteindre.

Par exemple, pour placer un module à droite d'un autre, référencer le bord
`Right` de ce dernier pour la position Y. Pour aligner leurs sommets, utiliser
sa propriété `Top` comme cible en Z. Le bloc référencé doit apparaître plus tôt
dans la pile de modifiers.

## Placer les planches

Une fois le bloc défini, les modifiers suivants le désignent par son nom :

| Modifier | Éléments construits |
| --- | --- |
| **Add Box** | Côtés gauche et droit, dessus, dessous et plinthe selon les options |
| **Add Face** | Portes ou façades de tiroirs, selon le choix `Type` |
| **Add Shelves** | Étagères horizontales |
| **Add Separators** | Séparateurs verticaux |

**Add Block** regroupe ces étapes : il crée le bloc et permet de construire
directement son caisson, ses étagères, ses séparateurs et sa façade. On peut donc
choisir entre un bloc vide à compléter et un bloc déjà équipé de planches.

L'orientation du fil agit sur les UV et sur l'ordre largeur/longueur dans le
débit. Elle ne change pas la géométrie de la planche : `Normal` conserve le sens
initial et `Rotate` tourne le fil de 90°. Le matériau doit utiliser `UV Map` pour
visualiser ce choix.

## Diviser et dupliquer

**Divide Block** crée des sous-blocs suivant une division verticale ou horizontale.
`Count` donne le nombre de parties. Avec `Even`, leurs dimensions intérieures
sont égales, en tenant compte des planches de séparation ; sinon, les champs
`Size` définissent les dimensions successives. Le champ `Plank` choisit la
ressource des séparations ; un nom vide permet de ne pas les construire.

**Duplicate Block** crée une copie d'un bloc. L'option `Planks` permet de copier
également ses planches. La copie peut être placée :

- par translation, avec `Offset Y` et `Offset Z` ;
- par symétrie suivant Y ou Z, autour du centre choisi ;
- en série, avec `Count`, lorsque `Symmetry` vaut `No`.

Dans une série, chaque copie repart du bloc source. Le décalage vaut une fois
l'offset pour la première copie, deux fois pour la deuxième, etc. Le bloc source
reste présent. En mode symétrie, une seule copie est créée.

### Noms des blocs

**Chaque bloc doit avoir un nom unique**, y compris les blocs produits par une
division ou une duplication.

- Une division compose le nom avec le nom du bloc parent, `Name Suffix` et un
  index commençant à zéro : par exemple `Module Part 0`, `Module Part 1`.
- Une duplication utilise `New Name`.
- Une duplication en série ajoute un index en suffixe : avec `New Name = Module`,
  les copies s'appellent `Module 0`, `Module 1`, etc.

Le modifier **Cut Sheet** affiche les noms de blocs dans une colonne à droite
de la liste des ressources. Cette liste permet de retrouver les noms à utiliser
dans les modifiers suivants.

## Animation des portes et tiroirs

**Open Door** simule l'ouverture d'une porte avec un angle, un axe et un côté
de pivot. **Open Drawer** déplace une façade de tiroir et ajoute une boîte de
tiroir simplifiée pour visualiser son ouverture.

La sélection se fait par bloc, rôle et index. Ces modifiers peuvent servir à
préparer une vue fixe ou à animer les paramètres d'ouverture dans Blender.
La boîte de tiroir est une représentation visuelle simplifiée ; ses panneaux
ne sont pas ajoutés au débit.

## Cotations et vues dérivées

**Add Cotes** affiche les dimensions et, au choix, les positions d'un bloc sur
les axes X, Y et Z. Ses options permettent de régler la taille des textes,
la section des lignes et le placement des cotations.

**Delete Plank** enlève des planches de la géométrie affichée pour rendre les
cotations plus lisibles : on peut par exemple enlever les portes pour montrer
l'intérieur du meuble. Les métadonnées de construction et le débit sont conservés.

**Capture Furniture** permet de préparer ces vues sur un objet distinct du meuble
de référence. Le choix `Source` récupère soit un objet avec `Object`, soit une
géométrie connectée avec `Geometry`. La géométrie et son Bundle sont transmis aux
modifiers suivants.

Une pile de présentation peut par exemple être :

```text
Capture Furniture
→ Delete Plank
→ Add Cotes
```

Une autre vue peut utiliser `Capture Furniture`, puis `Open Door` ou `Open Drawer`.
Ces objets suivent le meuble de référence tout en ayant leurs propres réglages
de présentation.

## Produire le débit avec Cut Sheet

1. Construire le meuble et définir les ressources de ses planches.
2. Créer un autre objet destiné au débit et lui ajouter le modifier **Cut Sheet**.
3. Dans le champ `Furniture`, sélectionner l'objet du meuble de référence.
4. La géométrie produite affiche les identifiants et noms des ressources, ainsi
   que les noms des blocs à droite. Elle contient aussi les données de débit
   sous forme d'un nuage de points.
5. Dans la console Python de Blender, appeler `get_cut_sheet` avec le nom de
   **l'objet portant le modifier Cut Sheet** :

```python
from geonodes.demos import furniture

print(furniture.get_cut_sheet("Furniture Cuts"))
```

Remplacer `Furniture Cuts` par le nom de cet objet. Le résultat regroupe les
pièces de même ressource, dimensions et orientation, et additionne leurs quantités.
Les dimensions sont exprimées en millimètres. Le texte affiche chaque identifiant
de ressource, puis les lignes `longueur x largeur (orientation) : quantité`.

Pour récupérer les données en JSON :

```python
cuts_json = furniture.get_cut_sheet("Furniture Cuts", json=True)
print(cuts_json)
```

Chaque entrée contient `res_id`, `count`, `size` et `orient`. Le champ `size`
contient la largeur, la longueur et l'épaisseur en millimètres ; `orient` vaut
`0` pour `Normal` et `1` pour `Rotate`. La largeur et la longueur du débit sont
déjà permutées lorsque le fil est tourné.
