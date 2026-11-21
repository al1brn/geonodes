# Générer l’API pour une nouvelle version de Blender

Le générateur courant est `geonodes.generation2`. Il produit les API Geometry Nodes et Shader Nodes dans `core_new`. Effectuer la procédure dans la version de Blender à prendre en charge.

## Avant la génération

### Préparer core_new

Copier le contenu du `core` courant dans `core_new` avant de commencer les adaptations. Conserver le fichier `config_<ancienne_version>.py` comme référence de comparaison. Ne pas refaire cette copie entre deux essais : elle écraserait les adaptations déjà faites dans `core_new`.

### Identifier les nouvelles sockets

Dans le fichier Blender de génération de l’API (`gen_api.blend`, lancer le texte **`Step 1 - New Sockets`**.

Il inventorie les classes `NodeSocket` et les sockets des nœuds du groupe de test. Adapter le nom de ce groupe : le script actuel utilise `Test 53`. Examiner les deux environnements Geometry et Shader et comparer les types trouvés aux déclarations existantes.

Si de nouveaux types sont présents :

1. Les déclarer dans `kernel/constants.py` : correspondance type → classe dans `CLASS_NAMES`, alias dans `DATA_TYPE_HOMONYMS`, types Python dans `PYTHON_TYPES` et listes de classes concernées selon le besoin.
2. Créer une classe manuscrite par nouveau type dans `core_new/root`, avec son `SOCKET_TYPE`, puis les spécialisations nécessaires dans `core_new/geonodes/sockets` et `core_new/shadernodes/sockets`. Suivre une classe comparable existante.
3. Ajouter les imports et inscriptions dans les registres de `core_new/__init__.py`, notamment `SOCKET_CLASSES`, et `GEOMETRY_CLASSES` pour une nouvelle géométrie.
4. Vérifier les sous-types et propriétés d’interface à exposer. Les tables automatiques `SOCKETS`, `SOCKET_IDS` et `SOCKET_SUBTYPES` seront reconstruites par `gen_config` ; ne pas les modifier dans les fichiers produits.

### Calculer les dimensions des nœuds

Dans le même fichier Blender, lancer le texte **`Step 2 - Node Dims`**. Ouvrir au préalable les deux groupes dans des éditeurs visibles :

- `NODE DIMS` dans un éditeur Geometry Nodes ;
- `SHADER NODE DIMS` dans un éditeur Shader Nodes.

Le script recrée les nœuds, rafraîchit l’interface et mesure leurs dimensions réelles. Il doit être exécuté dans Blender avec interface, pas en arrière-plan.

Copier le dictionnaire `NODE_DIMS` imprimé dans la console dans `generation2/node_dims.py`, en remplaçant le précédent. Il contient les dimensions des deux environnements. Recharger les modules ou redémarrer Blender avant de générer pour prendre en compte ce dictionnaire.

## Génération

### Lancer la génération automatique

Dans un texte Python du fichier Blender de travail :

```python
from geonodes.generation2.generate import generate
from geonodes.generation2 import gen_config

trees = generate()
gen_config.write_file(new=True)
```

`generate()` reconstruit les tables, collecte les implémentations des deux environnements et compile tous les modules rendus avant de commencer à les écrire dans `core_new`. Une erreur de collecte ou de validation arrête la génération. `gen_config.write_file(new=True)` enregistre ensuite la configuration `core_new/config_<version_Blender>.py` pour la comparaison.

Pour un seul environnement, utiliser `generate(tree_type='GeometryNodeTree')` ou `generate(tree_type='ShaderNodeTree')`. Pour collecter les sources sans écrire les modules : `generate(write=False)`.

### Produire la synthèse des différences

Après une génération réussie et l’écriture de la configuration, comparer les deux versions. Depuis la racine du dépôt, par exemple :

```bash
python3 generation2/compare_versions.py \
  core/config_5_2_0_LTS.py \
  core_new/config_5_3_0_Beta.py \
  -o comparaison.md
```

Adapter les noms aux versions concernées. Le rapport liste, par environnement, les nœuds supprimés, ajoutés et modifiés, avec le détail des changements. Les nœuds sont identifiés par leur identifiant Blender : un renommage est une modification.

Cette comparaison fonctionne sans Blender. Les dimensions sont ignorées par défaut ; utiliser `--include-dimensions` pour les inclure. Les différences de structure entre configurations sont également signalées : les examiner avant de conclure à un changement de Blender. La synthèse est une étape explicite ; `generate()` ne la lance pas automatiquement.

### Ajuster les implémentations

Si le résultat par défaut ne convient pas, utiliser les dictionnaires et listes de `generation2/config.py`, puis régénérer :

- `DEFAULT_IMPLEMENTATION` : remplacer les attributs de la description par défaut (nom, destination, retour, jump, etc.) ;
- `ADDITIONAL_IMPLEMENTATIONS` : ajouter des implémentations ;
- `PROPERTIES` : décrire les getters et setters ;
- `STATIC_IMPLEMENTATION_ONLY` : conserver uniquement l’accès par le catalogue `nd` ;
- `NO_STATIC_CODE` et `DEPRECATED_NODES` : exclure les nœuds au niveau requis ;
- les tables de types, d’entrées et d’items : compléter les descriptions utilisées par les chemins correspondants du générateur.

Passer par les descriptions ordinaires de `NodeCall` et le générateur standard de `NodeImplementation`. Ne pas corriger les fichiers générés à la main ni créer de générateur dédié à un nœud ou à une famille lorsque le mécanisme standard suffit.

Après les ajustements, régénérer, examiner les différences et tester les appels concernés dans Blender. La compilation vérifie la syntaxe des modules ; le comportement des nœuds doit aussi être vérifié.

Pour les détails internes, consulter [les règles de génération](../generation2/GENERATION_RULES.md). Documentation de génération documentaire : [gendoc](gendoc.md#gendoc).
