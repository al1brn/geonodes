# Environnements de nœuds

Règles de traitement des nœuds : [GENERATION_RULES.md](../generation2/GENERATION_RULES.md).

```text
core_new/
    common/                 utilitaires et mécanismes partagés
    root/                   classes racines manuscrites
    geonodes/
        geonodes.py         GeoNodes
        sockets/            classes manuscrites de cet environnement
        domains/            domaines et attributs de géométrie
        generated/          classes concrètes et fonctions générées
    shadernodes/
        shadernodes.py      ShaderNodes
        sockets/            classes manuscrites de cet environnement
        generated/          classes concrètes et fonctions générées
    environment.py          sélection du contexte et registres
    __init__.py             exports publics
```

`common` contient notamment `scripterror`, `sockettype`, `utils`, les couleurs,
les interfaces et l'arrangement des arbres. `root` contient les racines des
sockets, nœuds et arbres. Les domaines existent uniquement dans `geonodes`.
Les dossiers `sockets` et leurs exports ne contiennent que les classes prises
en charge dans leur environnement. Le générateur utilise ces classes manuscrites
comme cibles : une classe retirée n’est pas recréée automatiquement. Les racines
partagées restent disponibles dans `root`, et les registres actifs suivent les
exports de chaque environnement.

## Héritage

```text
root.Float
    geonodes.sockets.Float
        geonodes.generated.Float
    shadernodes.sockets.Float
        shadernodes.generated.Float
```

Chaque socket partagé dispose d'une classe manuscrite dans chacun des deux
environnements, même lorsqu'elle est vide. Elle peut définir un `__init__`
spécifique et appeler `super().__init__()`. Ces fichiers ne sont pas régénérés.
Les extensions Vector propres aux shaders (Tangent, UVMap, NormalMap, bump,
displacement, vector_displacement et displacement_out) sont dans
`shadernodes/sockets/vector.py`. FromRotation, mapping, normal et transform
sont fournis par la génération dans les environnements qui les acceptent.
Les géométries Mesh, Curve, etc. possèdent leurs extensions manuscrites dans
`geonodes/sockets/geometries.py`. Les classes générées correspondantes héritent
aussi de la classe Geometry générée pour conserver ses méthodes.

Les noms publics `Float`, `Vector`, etc. restent des classes racines : leur
métaclasse délègue la construction et les méthodes de classe à l'environnement
courant. `isinstance` reste utilisable avec ces racines. Les sorties des nœuds
sont construites par le registre du même environnement. Hors contexte, la
sélection par défaut est la géométrie.

`with` et les décorateurs utilisent la pile d'arbres existante : le contexte
précédent est retrouvé après une imbrication, y compris en cas d'exception.
`environment.ENVIRONMENTS` associe les types d'arbres aux packages ; un futur
moteur de composition pourra fournir son package et y être enregistré.

Les anciens modules de compatibilité à la racine ont été supprimés. Les imports
internes utilisent directement `common`, `root` ou l'environnement concerné.
Les anciens dossiers `gen_geonodes` et `gen_shadernodes` ont été remplacés par
les dossiers `generated` de chaque environnement.

## Génération directe

`generation2.node_implementation.NodeImplementation` produit directement les
modules dans les deux environnements, sans dossier de transition :

```python
NodeImplementation.generate()  # Les deux environnements
NodeImplementation.generate(tree_type='GeometryNodeTree')
NodeImplementation.generate(tree_type='ShaderNodeTree')
```

`write=False` collecte les sources sans écrire. `files` et `cross_refs` sont
indexés par type d'arbre. Les doublons sont vérifiés dans chaque environnement.
Les modules de toutes les cibles sélectionnées sont validés avant l'écriture.
Les fichiers manuscrits de `root`, `sockets` et `domains` restent préservés.

`gen_nodes()` utilise la description de `get_node_implementation()`. Avec
`domain_loop`, il génère dans la classe indiquée avec domaine libre, puis dans
chaque classe de domaine avec sa valeur fixée. Avec `data_type_loop`, il génère
dans chaque classe correspondant aux valeurs du paramètre de type. Les anciens
générateurs par défaut et par domaine ont été supprimés.

Pour les nœuds sans domaine dont le type modifie entrées et sorties, une
première entrée géométrique produit une méthode d’instance avec type déduit
du champ fourni. Si la première entrée et la première sortie sont pilotées par
ce type, une boucle produit des méthodes d’instance typées. Les autres cas
produisent des méthodes de classe par type. La classe correspond à la sortie typée concernée,
pas nécessairement à la première sortie. Les exceptions sont déclarées dans
`generation2/config.py`, dans `DATA_TYPE_IMPLEMENTATIONS`. `Switch` reste exclu
de cette règle. Les accès `nd` conservent leurs paramètres explicites.

Les comparaisons shader utilisent Math ; les comparaisons géométriques utilisent
Compare. Chaque environnement reçoit ses classes intermédiaires, ses imports,
son `__init__.py`, ses références croisées et son accès statique `nd`.
Le `nd` public sélectionne le catalogue de l’arbre actif ; `snd` est supprimé.

`core_new/generated` et le script `build_environments.py` ne sont plus requis
par ce générateur. Les anciens outils `gen_auto` ne sont pas son point d'entrée.

## Vérification Blender

```sh
blender --background --python core_new/tests/test_environments.py
```

Les tests couvrent constructions, résultats, opérations mixtes Float/Vector,
comparaisons, méthodes de classe, géométries, décorateurs, contextes imbriqués,
initialisation spécifique dans la classe intermédiaire et registre shader.
