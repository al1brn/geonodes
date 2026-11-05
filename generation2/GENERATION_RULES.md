# Règles de traitement des nœuds

Référence de maintenance : décrire ici les règles effectivement appliquées ; signaler séparément les règles restant à implémenter.

**Principe prioritaire : utiliser le générateur standard de `NodeImplementation` à partir des descriptions d'implémentation. Ne pas ajouter de générateur dédié par famille. Signaler tout besoin de hack à l'utilisateur avant de le mettre en œuvre.**

- **Pipeline actif simplifié**
  - `generate` appelle `gen_static_code`, `gen_gnmath`, puis `gen_nodes` pour chaque environnement.
  - `gen_nodes` demande une seule fois `get_node_implementation()` par nœud. Cette méthode contient directement les règles issues de `new_implementation` ; il n'y a plus de couche `_describe_node_implementation` ou d'application des anciens dictionnaires.
  - `domain_loop` : générer dans `class_name` si elle est précisée, avec `domain` libre, puis générer une variante par domaine dans sa classe de domaine, avec le domaine fixé.
  - `data_type_loop` : générer une variante pour chaque valeur possible du paramètre de type, dans la classe correspondant à cette valeur, avec ce paramètre fixé.
  - Sinon, générer dans la classe indiquée. Les noms, méthodes de classe, récepteurs, jumps et retours viennent de la description ; `gen_nodes` ne les redéduit pas.
  - Chaque variante utilise une copie de `NodeImplementation`, `_gen_source` et `register_source`. La description n'est pas recalculée et l'état Blender du nœud n'est pas modifié par les boucles.
  - Les anciens générateurs d'implémentations par défaut et par domaine, ainsi que leur helper commun, ont été supprimés.
  - Les traitements historiques des propriétés, accès par indice, ajouts de code et références manuscrites ne sont plus appelés depuis `gen_nodes`. Les anciennes règles ci-dessous documentent encore ces chemins historiques, distincts du pipeline actif.
  - Une description incohérente ou une collision reste une erreur explicite, sans recours automatique à l'ancien générateur.

- **Exceptions et exclusions — prioritaires**
  - `DEPRECATED_NODES` : nœuds exclus de l'introspection `NodeInfo`.
  - `NO_DEFAULT_IMPLEMENTATION` : pas d'implémentation par défaut ; accès `nd` conservé.
  - `REPLACE_DEFAULT_IMPLEMENTATIONS` : remplace les champs inférés de la proposition par défaut.
  - `ADDITIONAL_IMPLEMENTATIONS` : ajoute des propositions explicites.
  - `DATA_TYPE_IMPLEMENTATIONS` : exceptions à la règle des types d'entrée/sortie.
  - `INPUT_IMPLEMENTATIONS` : exceptions au traitement dédié des nœuds `INPUT`.
  - Index Switch : générer automatiquement les constructeurs typés et `nd.index_switch` avec `*values` ; conserver le raccourci manuscrit `Socket.index_switch(...)`.
  - Menu Switch : exclure le constructeur par défaut ; conserver `Socket.MenuSwitch(...)`, `Socket.menu_switch(...)` et l'accès généré `nd.menu_switch`.
  - `HANDWRITTEN_IMPLEMENTATIONS` : enregistrer les signatures réelles des méthodes manuscrites dans les références croisées, sans recopier leur code dans les modules générés.
  - Exclusion temporaire d'introspection : `ShaderNodeOutputLineStyle`, dont l'exploration d'enum produit des avertissements RNA.

- **Ordre et nature des sockets**
  - Reconnaître les sockets Grid avec `display_shape == 'VOLUME_GRID'`, dans l'introspection comme dans `Socket.is_grid` ; une entrée non connectée peut avoir `inferred_structure_type == 'SINGLE'`.
  - Conserver l'ordre physique dans chaque configuration explorée.
  - Les sockets physiques (`NodeInfo.inputs` / `outputs`, indexées par identifiant) conservent `names`, la liste ordonnée de tous leurs noms possibles.
  - `max_inputs` / `max_outputs` contiennent une entrée par nom possible, avec un champ `name` constant et les configurations d'activation propres à ce nom. Les variantes de types physiques peuvent partager cette entrée si elles ne sont jamais actives ensemble ; les sockets physiques de même type restent distinctes.
  - Le header de `_gen_source` utilise ces entrées filtrées par les paramètres fixés. Si des variantes restent possibles, l'appel au nœud sélectionne leurs noms et valeurs selon les paramètres à l'exécution.
  - Ne pas déduire l'ordre d'une variante de l'ordre de la liste fusionnée `max_inputs`.
  - Pour choisir le récepteur d'une méthode : placer `Factor` / `Fac` après les valeurs.
  - Sockets virtuels `CUSTOM` : arguments dynamiques, pas des récepteurs.
  - Détecter les changements dus au paramètre de type en maintenant les autres paramètres pilotes constants.

- **Ordre des paramètres enum**
  - `NodeInfo.enum_params_order` compare uniquement les paramètres `ENUM`, à l'exclusion des `ENUM_FLAG` et booléens.
  - Sans ordre déclaré, une dépendance détectée provoque une erreur demandant de déclarer l'ordre dans `ENUM_PARAMS_ORDERS`, avec le nom du nœud comme clé.
  - Sans dépendance, conserver l'ordre des paramètres `ENUM` ; un ordre déclaré est retourné directement.
  - Explorer les combinaisons dans cet ordre, en relisant les choix après affectation des paramètres précédents ; conserver aussi les axes `ENUM_FLAG` et booléens pour les états des sockets.
  - Un enum sans choix conserve sa valeur courante pendant l'exploration, sans tentative d'affectation.
  - Ne plus inférer de graphe de dépendances entre paramètres pendant l'exploration. `param_dependencies` expose seulement les contraintes de précédence déclarées (chaque paramètre suit tous ses prédécesseurs dans la table).
  - Générer les arguments de paramètres dans cet ordre, puis les autres arguments dans leur ordre existant.
  - Conserver tous les états des sockets par configuration (présence, activation, nom, type, indice), puis réduire uniquement les axes sans effet sur ces états.

- **Aucune input socket exploitable**
  - Sortie géométrique : constructeur sur la classe de sortie.
  - Une seule sortie, aucun argument ou paramètre libre : propriété de classe.
  - Entrées virtuelles : conserver les arguments dynamiques ; ne pas assimiler le nœud à un nœud entièrement sans entrée.
  - Sinon : pas d'implémentation ordinaire par défaut.
  - Nœud `INPUT` : appliquer le traitement dédié ci-dessous.

- **Input sockets présentes**
  - **Une seule**
    - Elle devient normalement `self`.
    - Sa classe détermine la classe porteuse.
  - **Plusieurs**
    - Placer `Factor` / `Fac` après les valeurs.
    - La première entrée restante devient normalement `self`.
    - Les autres entrées deviennent des arguments.
  - **Cas donnant priorité à un constructeur**
    - Sortie géométrique sans entrée géométrique.
    - Nœud `Combine`.
    - Import de géométrie.
    - BSDF dans les shaders.
    - Conversion reconnue entre deux classes.
    - Une règle ou exception explicite imposant `METHOD` prend la priorité sur ces heuristiques.
  - **Sinon**
    - Aucun argument libre et une seule sortie : propriété d'instance.
    - Sinon : méthode d'instance.

- **Paramètre `domain`, sans `data_type` / `input_type`**
  - Implémentation par défaut : garder `domain` libre.
  - Génération complémentaire, uniquement en Geometry Nodes :
    - Boucler sur les valeurs autorisées de `domain`.
    - Fixer `domain` et le retirer des arguments.
    - Classe porteuse : classe du domaine.
    - Entrée géométrique servant de récepteur : méthode d'instance.
    - Pas d'entrée géométrique servant de récepteur : méthode de classe.
    - Réutiliser le code par défaut complet, sans délégation à une méthode de géométrie.
  - Correspondances :
    - `POINT` → `Point`, hérité par `Vertex`, `SplinePoint` et `CloudPoint`.
    - `EDGE` → `Edge`.
    - `FACE` → `Face`.
    - `CORNER` → `Corner`.
    - `CURVE` / `SPLINE` → `Spline`.
    - `INSTANCE` → `Instance`.
    - `LAYER` → `Layer`.
  - Zones et Viewer : exclus de cette génération complémentaire.
  - Active Element : méthode de classe ; utilisable en contexte Tool.

- **Paramètre `data_type` / `input_type`, sans `domain`**
  - **Modifie seulement les sorties**
    - Aucun traitement complémentaire ; conserver le défaut.
  - **Modifie seulement les entrées**
    - Socket concerné en première position :
      - Traitement par défaut actuel.
      - **À compléter : boucle par classe avec type fixé.**
    - Socket concerné après la première :
      - Pour une méthode d'instance : calculer le type depuis cet argument.
      - Retirer le paramètre de type de la signature.
      - Documenter le paramètre comme calculé.
  - **Modifie les entrées et les sorties**
    - Première entrée géométrique :
      - Méthode d'instance sur la géométrie.
      - Type calculé depuis l'argument typé concerné.
    - Sinon, première entrée **et** première sortie pilotées par le type :
      - Boucler sur les types autorisés.
      - Méthode d'instance sur chaque classe.
      - La première entrée de la variante devient `self`.
      - Type fixé et retiré des arguments.
      - Implicit Conversion relève de cette règle, **sans exception**.
    - Sinon :
      - Boucler sur les types autorisés.
      - Méthode de classe pour chaque type.
      - Classe choisie depuis la sortie typée concernée, pas forcément la première sortie.
      - Type fixé et retiré des arguments.
  - **Exceptions actuelles**
    - Random Value : constructeur `Random`, classe choisie depuis la sortie typée.
    - Enable Output : méthode typée ; `Value` devient `self`, `enable` reste argument.
    - Switch : règle historique, indépendante du pipeline simplifié.
    - Combine List : constructeur `CombineList` explicitement conservé dans les remplacements.
  - **Portée de la déduction automatique**
    - Seulement les méthodes d'instance.
    - Ne pas activer cette déduction pour les constructeurs, méthodes statiques ou accès `nd`.
    - Un paramètre de type explicitement fixé reste fixé.

- **Paramètres `domain` et de type présents ensemble**
  - Conserver l'implémentation par défaut, avec `domain` et le paramètre de type exposés.
  - Générer aussi une variante par valeur autorisée de `domain`, sur la classe du domaine.
  - Fixer `domain` et le retirer des arguments ; réutiliser le même code, documentation et références croisées.
  - Entrée géométrique servant de récepteur : méthode d'instance ; appliquer la même déduction du type depuis l'argument typé que pour les méthodes de géométrie sans domaine.
  - Pas de récepteur géométrique : méthode de classe sur le domaine ; conserver le paramètre de type explicite, comme pour les autres méthodes de classe.
  - Ne pas appliquer la déduction aux accès `nd`, ni modifier les implémentations par défaut.

- **Nœuds `INPUT`**
  - Traités par `gen_nodes` à partir de `get_node_implementation()`, comme les autres nœuds.
  - L'ancien générateur dédié et son helper ont été supprimés.

- **Accès par indice déclarés (`ITEM_IMPLEMENTATIONS`)**
  - Dictionnaire : classe cible → `getitem` / `setitem` → description du nœud.
  - Description : `node`, `self_socket`, `key_socket`, `output`, et `value_socket` pour l'affectation.
  - `parameters` et `sockets` fixent les autres valeurs ; les paramètres non indiqués gardent leur valeur par défaut.
  - `key_type_parameter` : lecture avec clé `(chemin, type)` ; convertir le type pour le paramètre du nœud.
  - `value_type_parameter` : déduire ce paramètre depuis la valeur affectée.
  - Getter : retourner la sortie configurée sans modifier `self`.
  - Setter : mettre à jour `self` avec la sortie configurée, sans valeur de retour.
  - Bundle : `bundle["nom", Float]` via Get Bundle Item (`Remove=False`) ; `bundle["nom"] = valeur` via Store Bundle Item.
  - Générer uniquement dans les environnements où le nœud est disponible.
  - Classes non déclarées : conserver le comportement existant, notamment la sélection des géométries et domaines.
  - Réutiliser la génération de documentation et l'enregistrement des références croisées ; conserver les erreurs de collision.

- **Arguments**
  - Prototype `NodeImplementation._gen_source` : la préparation sépare les paramètres fixés et libres selon `self.parameters` (`None` signifie libre), sans inférer de configuration. La docstring est émise après le header : sockets et paramètres libres, valeurs fixées, paramètres calculés, socket réceptrice, jump et retour. Elle utilise le rendu commun `gen_docstring`.
  - Le header du prototype reprend l'annotation et la valeur par défaut des paramètres libres préparés dans `param_args` ; les valeurs simples utilisent leur type Python, les enums leur annotation `Literal`. Les défauts sont sérialisés avec `repr`. Les sockets restent à `None` ; leur annotation est leur classe précise si elle reste constante dans les configurations compatibles avec les paramètres fixés, sinon `Socket`. Cette règle vaut aussi pour les arguments multi-input.
  - Dans ce prototype, `auto_data_type` désigne explicitement le nom de la socket utilisée pour calculer `data_type` / `input_type` avec `SocketType.get_data_type_for_node`. L'expression utilisée est `self` si cette socket est le récepteur, sinon le nom final de son argument après dédoublonnage. Uniquement pour `METHOD` ; un type fixé reste fixé. Le paramètre calculé est retiré de la signature et documenté comme calculé.
  - Le prototype émet `selection = self.get_selection()` lorsqu'une socket a été marquée `is_selection` par le traitement explicite de `use_geo_selection`.
  - `arguments` décrit la signature ; `node_sockets` décrit séparément les sockets à initialiser, avec leur `socket_name` et l'expression `arg_value` (argument, `self`, sélection calculée ou valeurs multi-input).
  - Le prototype émet l'appel `node = Node(...)` depuis `node_sockets` : multi-input en arguments positionnels dépliés, autres sockets dans `named_sockets`, puis paramètres fixés, libres ou calculés dans l'ordre déclaré.
  - Le bloc sockets du prototype sélectionne uniquement les descriptions de sockets présentes et actives dans au moins une configuration compatible avec les paramètres fixés. La transformation en arguments reste à implémenter.
  - Récepteur : remplacer le socket par `self`.
  - Le nom de la première socket réceptrice reste réservé lors du dédoublonnage des arguments (`value_1`, `vector_1`, etc.) ; ses autres alias ne réservent pas de noms supplémentaires.
  - `Selection` suivant une géométrie : utiliser `self.get_selection()` dans une méthode d'instance.
  - Paramètre fixé ou calculé : le retirer de la signature.
  - Multi-input : conserver les valeurs supplémentaires.
  - Exposer une socket multi-input en `*argument`, y compris lorsqu'elle sert de récepteur : transmettre `[self, *argument]`.
  - Les variantes de nom d'une même socket multi-input partagent le même argument variadique ; sélectionner le nom actif pour la configuration.
  - Si le récepteur séparé disparaît dans une variante, l'inclure dans la socket multi-input active (Mesh Boolean en Union / Intersect).
  - Transmettre les multi-inputs directement à `Node(..., *argument)` ; pour un récepteur multi-input, appeler `Node(..., self, *argument)`. Mesh Boolean utilise la même règle dans `static_nd`, sans exception de nommage.
  - À l'exécution, résoudre la socket courante pour relier une liste ; ne pas dépendre d'un nom multi-input mis en cache avant le réglage des paramètres.
  - Items anonymes : reconnaître l'absence de paramètre `name` dans la signature RNA de `items.new`. Exposer `*values`, sans sockets numérotées artificielles ni `**sockets` pour les items.
  - Index Switch : `default_index` règle le défaut du sélecteur et celui de l'entrée de groupe directement liée, pour l'interface du modificateur.
  - Plusieurs sockets multi-input physiques distinctes : utiliser des listes, Python n'autorisant qu'un seul argument variadique. Un setter de propriété reçoit également une liste plutôt que `*args`.
  - Entrées dynamiques : conserver `named_sockets` et `**sockets`.
  - Employer les noms uniques de sockets pour les appels à `Node`, pas les identifiants physiques Blender.
  - Signature : `Node(node_name, *args, named_sockets=None, **parameters)` ; le dictionnaire de sockets est explicitement nommé.
  - Après réglage des paramètres : si `args` est non vide, brancher directement les valeurs dans l'unique socket multi-input active ; sinon, si la collection d'items n'accepte pas de nom (signature RNA de `new`), créer directement les items et alimenter leurs sockets ; sinon lever une erreur.
  - Utiliser `set_input_socket_value` pour les sockets déjà identifiées ; ne pas reconvertir les valeurs positionnelles en noms ou en dictionnaire.
  - Traiter ensuite les entrées nommées : le sélecteur Index arrive après les items positionnels, sans branche spéciale Index Switch dans le constructeur.
  - Sans cible unique, lever une erreur explicite. Ne pas interpréter implicitement un dictionnaire positionnel comme `named_sockets`.
  - Ne pas contrôler les doublons entre arguments positionnels et entrées nommées ; une entrée multi-input nommée ajoute ses valeurs aux valeurs positionnelles.

- **Propriétés déclarées (`PROPERTIES`) — Geometry Nodes uniquement**
  - Dictionnaire : classe cible → nom de propriété → descriptions `getter` et `setter`.
  - Chaque description indique `node`, les `parameters` fixés et les `sockets` fixés.
  - Getter : sortie principale par défaut, ou sortie `output` explicitement choisie.
  - Setter : une seule valeur, liée à `socket` ou à `parameter` ; conserver la sélection de `self` et mettre à jour sa géométrie avec `_jump`.
  - Autres paramètres : valeurs par défaut du nœud, sauf configuration explicite.
  - Autres sockets : conserver les valeurs par défaut du nœud, sauf configuration explicite.
  - Getter absent : propriété en écriture seule ; la lecture lève `NodeError`.
  - Un getter ou accès de classe automatique de même nom, même classe et même nœud getter déclaré est remplacé par la propriété explicite.
  - Les autres conflits de nom restent des erreurs ; un getter et son setter peuvent partager le nom.
  - Enregistrer séparément les références croisées du getter et du setter (`is_get` / `is_set`).
  - `Geometry.bundle` : lire la sortie `Bundle` de Get Geometry Bundle avec `Remove=False` ; affecter via Set Geometry Bundle.

- **Retour**
  - Première sortie par défaut.
  - Nœud `Separate` ou sortie virtuelle : retourner le `Node`.
  - Entrée et sortie géométriques de même classe : jump.
  - Dans le prototype, après le jump : retourner `node._second_out(self)`, soit la deuxième sortie disponible ou `self` en son absence.
  - Jump sur un domaine : mettre à jour sa géométrie et retourner cette géométrie.

- **Noms et conversions**
  - Constructeur : CamelCase.
  - Méthode ou propriété : snake_case.
  - Retirer les mots redondants avec la classe porteuse.
  - Conversion reconnue : constructeur `From…` sur la destination.
  - Si la source est une classe connue : proposer également `to_…` sur la source.
  - Les méthodes de classe typées ne sont pas automatiquement traitées comme des conversions vers leur classe porteuse.

- **Environnements et accès `nd`**
  - Générer séparément Geometry Nodes et shaders.
  - Cibles : `core_new/geonodes/generated` et `core_new/shadernodes/generated`.
  - Le `nd` public sélectionne le catalogue de l'arbre actif.
  - Une entrée `nd` par nœud disponible, sous réserve des exclusions d'introspection.
  - `gen_static_code` utilise `_gen_source` : `CLASS_METHOD` retournant `NODE`, ou `CLASS_PROPERTY` retournant `OUT` pour les propriétés de classe. Les entrées dynamiques et items anonymes passent par ce même générateur standard.
  - Paramètres de type explicites ; aucune déduction automatique.
  - Classes de sockets limitées à celles de l'environnement.
  - `Texture` est une cible ordinaire du rendu dans les deux environnements, dans `generated/texture.py`. C'est un catalogue, sans héritage de `Socket`. La classe est vide tant qu'aucune implémentation standard ne la cible ; aucun constructeur dédié n'est ajouté.
  - `NodeImplementation.get_node_implementation()` décrit `self.node` ; ses tables sont dans `config.py`. Cette description est utilisée par la boucle générale ; `NodeInfo.default_implementation` reste disponible pour les traitements historiques.
  - Dans le prototype `NodeImplementation.get_node_implementation`, `color_tag='TEXTURE'` propose une méthode de classe sur `Texture`. Le nom du constructeur retire le mot `Texture` et joint les mots restants (`White Noise Texture` → `WhiteNoise`). La sortie reste celle choisie par défaut (`_out`), sans traitement particulier.

- **Code manuscrit, documentation et conflits**
  - Méthode déjà définie dans un parent manuscrit : omettre la version générée et hériter de la méthode manuscrite.
  - Deux propositions générées de même nom sur la même classe et dans le même environnement : erreur détaillant les deux nœuds.
  - Résoudre les conflits dans la configuration ; ne pas écraser silencieusement une proposition.
  - Variantes : même génération de code, documentation et références croisées que le défaut.
  - `copy_code` reste disponible pour copier du code spécifique.
  - Valider tous les modules des environnements sélectionnés avant l'écriture.

- **Catalogues mathématiques**
  - `gnmath` : opérations Math, Integer Math, Boolean Math, Vector Math, Bit Math, Color Mix et comparaisons.
  - Math, Integer Math, Boolean Math, Vector Math et Bit Math utilisent `_gen_source` avec `FUNCTION` pour `gnmath`, `METHOD` pour les classes et `return_kind='OUT'`. L'opération est fixée ; le récepteur est la première entrée active de cette variante. Les opérateurs délèguent aux méthodes ordinaires.
  - Color Mix et les comparaisons restent à migrer vers `_gen_source`.
  - Opérations disponibles : vérifier qu'elles sont toutes couvertes par les tableaux explicites.
  - Geometry Nodes : comparaisons typées via le nœud Compare, résultat `Boolean`.
  - Shaders : comparaisons scalaires Float/Integer via Math, résultat `Float`.
  - Les opérations Math `LESS_THAN`, `GREATER_THAN`, `COMPARE` sont générées sans exclusion sur `Float` et dans `gnmath` : `less_than`, `greater_than`, `compare` en Shader ; `mless_than`, `mgreater_than`, `mcompare` en Geometry Nodes. Aucun `Float.compare` manuscrit. Les fonctions composées utilisent les noms du contexte.
  - `<`, `<=`, `>`, `>=`, `==`, `!=` : déléguer aux méthodes nommées correspondantes.
  - FunctionNodeCompare : exclure sa proposition générique, puisque les comparaisons sont déjà générées explicitement.

## Points d'entrée du code

- [config.py](config.py) : exclusions, remplacements, ajouts et exceptions.
- [node_info.py](node_info.py) : introspection, classification et propositions.
- [node_socket.py](node_socket.py) : snapshots des sockets et ordre physique.
- [node_implementation.py](node_implementation.py) : orchestration, génération du code et écriture.
- [output.py](output.py) : héritage, filtre des méthodes manuscrites, rendu et validation des modules.
- [tests/test_contexts.py](tests/test_contexts.py) : tests des règles de génération.
- [../core_new/tests/test_environments.py](../core_new/tests/test_environments.py) : tests du comportement produit dans Blender.
