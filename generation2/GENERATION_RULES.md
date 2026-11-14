# Règles de traitement des nœuds

Référence de maintenance : décrire ici les règles effectivement appliquées ; signaler séparément les règles restant à implémenter.

- **Configuration manuelle centralisée**
  - `config.py` définit `TREE_TYPES`, la correspondance `TREE_MODULES` vers les dossiers produits, les listes de classes (`GEOMETRY_CLASSES`, `DOMAIN_CLASSES`, `ATTRIBUTE_CLASSES`, `POINT_DOMAIN_CLASSES`) et les descriptions manuelles de types/sockets (`PYTHON_TYPES`, `TRANSCO`, `SOCKET_BLID_TO_TYPE`, `DATA_TYPE_HOMONYMS`, `INPUT_SOCKETS_PROPS`).
  - `output`, `generate`, `TreeClass` et `gen_config` consultent ces définitions ; `ENVIRONMENTS`, `GEOMETRIES`, `POINT_DOMAINS` et la seconde déclaration de `TREE_TYPES` sont supprimés du générateur.
  - `gen_config.INPUT_SOCKETS_PROPS` est une copie de travail enrichie par Blender, reconstruite depuis `config` à chaque `build`. Les tables manuelles ne sont pas modifiées par l'introspection. Les tables automatiques restent construites et exportées par `gen_config`.

- **Arguments contextuels du générateur**
  - Les rôles `NAMED_ITEMS` et `ANONYMOUS_ITEMS` ont `source=None`. Le premier expose `items={}` et `**named_items`, puis fournit les expansions de sockets et de paramètres dans `NodeCallArguments.named_socket_expansions` / `parameter_expansions` ; le second expose et transmet `*dyn_sockets`. Ces listes contiennent des expressions sans préfixe `**`. La fusion des items nommés est une contribution à l’appel, pas un calcul dans `get_code`. `get_node_arguments` ajoute un wrapper selon `has_items` / `items_with_name` et réserve ses noms avant les autres arguments. L’assembleur doit placer les variadiques positionnels avant les arguments ordinaires et les variadiques nommés en dernier.
  - `node_argument.py` encapsule un `NodeSocket` ou `NodeParam` (nom actuel de NodeParameter), sans les modifier. Le nom Python final, les alias ordonnés et le rôle `ARGUMENT`, `SELF`, `FIXED` ou `COMPUTED` appartiennent au wrapper.
  - `get_typing`, `get_header`, `get_arg_doc`, `get_fixed_doc`, `get_computed_doc`, `get_code` et `get_node_call` reprennent les règles de rendu de `gen_node_call`. Les appels sont décrits par `NodeCallArguments` : expressions positionnelles, sockets nommées et paramètres séparés.
  - Les valeurs fixées sont des valeurs Python, y compris `None` ; les valeurs calculées sont des expressions de source. Les enums peuvent utiliser le registre `TypeAliases` fourni par l'appelant. La résolution des alias s'exécute après initialisation du dictionnaire de sockets et avant l'appel du nœud.
  - `NodeInfo.get_node_arguments` prépare les wrappers à partir de `self_socket`, `fixed_sockets`, `last_sockets`, `use_geo_selection`, `auto_data_type` et des paramètres fixés. Tous les paramètres introspectés sont inclus, pas seulement les enums ; une clé présente avec `None` est fixée, contrairement à une clé absente. L'exploration restaure l'état initial du nœud, y compris après erreur. Les noms Python sont dédoublonnés et les aliases sont ordonnés de manière déterministe. Les sockets de `last_sockets` sont déplacées comme des wrappers entiers ; la sélection utilise l'ordre physique avant ce déplacement et exige le premier récepteur géométrique suivi de la Boolean Selection. Les valeurs fixées restent prioritaires. `gen_node_call` utilise cette liste : il assemble le header, les sections documentaires (arguments, valeurs fixées, valeurs calculées), le code préparatoire et les contributions structurées à l'appel. Ses anciens dictionnaires d'arguments ont été supprimés.

**Principe prioritaire : utiliser le générateur standard de `NodeImplementation` à partir des descriptions d'implémentation. Ne pas ajouter de générateur dédié par famille. Signaler tout besoin de hack à l'utilisateur avant de le mettre en œuvre.**

- **Répartition des responsabilités**
  - Point d'entrée : `from geonodes.generation2.generate import generate`. `generate(tree_type=None, use_core_new=True, write=True)` reconstruit les tables via `gen_config.build()`, puis crée une instance indépendante de `TreeClass` par environnement. Il retourne un dictionnaire `tree_type -> TreeClass`, même avec `write=False`.
  - `gen_config` ne lance plus d'introspection à l'import. `build` vérifie d'abord les sockets non enregistrées, puis les classes manuscrites manquantes, et publie les tables automatiques seulement lorsqu'elles sont complètes. Une erreur arrête la génération avant collecte des sources et avant écriture. `write_file` construit les tables si nécessaire pour ses anciens appelants.
  - `TreeClass` porte les anciennes méthodes de classe de `NodeImplementation` sous forme de méthodes d'instance : collecte, enregistrement, références et étapes `gen_*`. Sources, références et registre `TypeAliases` appartiennent à chaque instance. `TreeClass.generate` collecte un environnement ; `render_modules` le valide.
  - `NodeImplementation` ne conserve que les méthodes d'instance. Son registre d'alias est transmis explicitement au constructeur, puis partagé par ses copies. Aucun état global de génération ne reste dans cette classe.
  - `generate.write_files` valide tous les environnements sélectionnés avant la première écriture dans `core_new`. Les anciens appels `NodeImplementation.generate()` doivent devenir `generate()` depuis le nouveau module.

- **Pipeline actif simplifié**
  - Nettoyage de `NodeInfo` : suppression de `snapshot_config`, `snapshot` et de la classe séparée `DEPRECATED`, sans modification des autres helpers d’introspection.
  - `generate` appelle `gen_static_code`, `gen_math`, `gen_compare`, `gen_mix`, `gen_nodes`, `gen_properties`, `gen_typed_constructors`, puis `gen_additional` pour chaque environnement.
  - Nettoyage : les anciens générateurs mathématiques (`gen_*_functions` et variantes `_DEPR`), leur helper `_check_operations`, `gen_source_code` et `loop_on_parameter` ont été supprimés. `gen_properties_DEPR`, `gen_source`, `_fixed_parameters`, `gen_docstring`, `_gen_source` et `fixed_enums` ont aussi été supprimés ; `gen_handwritten_references` reste disponible, sans appel depuis `generate`.
  - Alias de types : `TreeClass.generate` crée un registre `TypeAliases` neuf pour son environnement, partagé par les implémentations, leurs copies et leurs `SourceWriter`. Les paramètres enum libres de `gen_node_call` fournissent leurs valeurs au registre ; les annotations simples restent des noms de types Python. Le source du registre est conservé dans `files` sous `type_aliases.py`, même avec `write=False`. Le rendu crée ce module, importe ses alias dans les modules générés et le valide avec les autres fichiers avant écriture. Le registre ne connaît pas `tree_type`.
  - `gen_nodes` demande une seule fois `get_node_implementation()` par nœud. Cette méthode contient directement les règles issues de `new_implementation` ; il n'y a plus de couche `_describe_node_implementation` ou d'application des anciens dictionnaires.
  - `domain_loop` : générer dans `class_name` si elle est précisée, avec `domain` libre, puis générer une variante par domaine dans sa classe de domaine, avec le domaine fixé.
  - `data_type_loop` : générer une variante pour chaque valeur possible du paramètre de type, dans la classe correspondant à cette valeur, avec ce paramètre fixé.
  - Sinon, générer dans la classe indiquée. Les noms, méthodes de classe, récepteurs, jumps et retours viennent de la description ; `gen_nodes` ne les redéduit pas.
  - Chaque variante utilise le générateur standard `gen_node_call` et `register_source`. La description n'est pas recalculée et l'état Blender du nœud n'est pas modifié par les boucles.
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

- **Exploration centrale des sockets**
  - `get_possible_sockets(inout='INPUT', group=True, **parameters)` explore les configurations compatibles avec les paramètres fixés. `inout='OUTPUT'` utilise exactement le même parcours pour les sorties.
  - Collecter les sockets actives dans chaque variante, y compris celles absentes de la configuration initiale, puis fusionner les noms/types par identifiant physique. Trier les résultats par indice physique.
  - `group=False` conserve les identifiants physiques ; `inputs` et `outputs` utilisent ce mode et mémorisent le résultat. Le mode par défaut conserve le regroupement des homonymes de types distincts pour les signatures.
  - Les sockets Grid sont reconnues avec `display_shape == 'VOLUME_GRID'`.
  - `is_class_property` consulte les sorties du parcours central, sans table de dépendances.
  - `get_param_dependencies`, `param_dependencies`, `enum_parameters`, `driving_parameters`, `configurations`, `param_filter`, `_reduce_socket_configurations`, `build_max_sockets`, `max_inputs` / `max_outputs`, `data_type_socket_changes`, `has_driving_parameters` et le champ `NodeSocket.dependencies` sont supprimés.
  - La détection des sockets pilotées par le type compare leurs types et leur présence selon les valeurs de l'enum. Elle réutilise le parcours central pour collecter les identifiants actifs. Les variantes de méthodes typées nécessitent une socket réceptrice pour chaque type ; les récepteurs explicitement décrits restent prioritaires.

- **Ordre des paramètres enum**
  - `analyze_config` conserve le calcul existant de `config_order` et des valeurs par défaut des paramètres `ENUM`.
  - `loop_on_configurations` relit les choix après affectation des paramètres précédents et restaure les valeurs par défaut dans un `finally`, y compris si l'exploration échoue.
  - L'ancien parcours `enum_params_order`, sa table locale et les caches de configurations ne sont plus utilisés. Ce parcours n'explore pas les booléens et `ENUM_FLAG`.

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
  - `NodeImplementation.gen_node_call` : la préparation est déléguée à `NodeInfo.get_node_arguments`. Dans `self.parameters`, `None` reste le marqueur libre historique ; les clés explicites de `NodeCall.parameters` prennent priorité, y compris celles fixées à `None`. La docstring est émise après le header : sockets et paramètres libres, valeurs fixées, paramètres calculés, socket réceptrice, jump et retour. Elle est émise directement par `gen_node_call`.
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
  - `gen_static_code` utilise `gen_node_call` : `CLASS_METHOD` ou `CLASS_PROPERTY` retournant `OUT`. Les entrées dynamiques et items anonymes passent par ce même générateur standard.
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
  - Math, Integer Math, Boolean Math, Vector Math et Bit Math utilisent `gen_node_call` avec `FUNCTION` pour `gnmath`, `METHOD` pour les classes et `return_kind='OUT'`. L'opération est fixée ; le récepteur est la première entrée active de cette variante. Les opérateurs délèguent aux méthodes ordinaires.
  - Color Mix et les comparaisons utilisent également `gen_node_call`.
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

- **Générateur standard `gen_node_call`**
  - Prépare une liste `inputs` commune aux arguments et à l'appel, avec une source `ARGUMENT`, `FIXED` ou `COMPUTED`.
  - Produit directement la signature et l'appel ; utilise uniquement l'écriture indentée de `SourceWriter`.
  - Premiers cas vérifiés sans Blender : récepteur explicite ou implicite, paramètres libres ou fixés, sockets fixées, sélection avec désactivation possible, alias et récepteur multi-input.
  - Remplace les anciens générateurs ; les tests historiques propres aux chemins supprimés ont été retirés. Les tests d’alias utilisent désormais `gen_node_call`.
  - `gen_node_call` calcule aussi `data_type` / `input_type` avec `SocketType.get_data_type_for_node`, sans restriction sur le type de fonction. La source est `self` ou le nom final dédoublonné de l'argument ; le paramètre calculé est retiré de la signature. Un type fixé reste prioritaire ; une socket source inconnue ou un paramètre de type absent provoque une erreur explicite.

- **Découpage de `SourceWriter`**
  - Les marqueurs `R0`, `R1`, `R2` valent `§^`, `§%`, `§&`, sans retour à la ligne. Ils sont remplacés par des espaces ou des coupures selon la longueur rendue, indentation comprise. Les retours à la ligne ordinaires utilisent simplement `split("\n")`.
  - Les appels à `write` avec plusieurs lignes n'ajoutent pas de ligne vide supplémentaire. La démonstration du module ne s'exécute plus à l'import.

- **Typing des paramètres enum flags**
  - `NodeParam.__init__` reçoit `enums=None` et construit directement `set[Literal['A', 'B']]` après découverte des choix, sans enregistrement dans `TypeAliases`. Sans choix, utilise `set[str]`.
  - Les enums simples conservent une liste de valeurs pour la capture par `TypeAliases`. Les choix sont découverts avant construction ; `get_enum_list` conserve son interface via un helper statique partagé.

- **Typing des paramètres de `gen_node_call`**
  - Reconstruit les `NodeParam` depuis les snapshots par défaut, sans nouvelle introspection, et utilise leur `typing`.
  - Les listes de choix des enums simples sont enregistrées dans `TypeAliases` au rendu de la signature ; sans registre, un `Literal[...]` direct est émis. Les enum flags gardent leur chaîne `set[Literal[...]]`, sans capture. Un typing absent ne produit pas d'annotation.
  - Les paramètres calculés ou fixés ne sont pas enregistrés dans les alias. Le typing des sockets reste inchangé.

- **Typing des sockets de `gen_node_call`**
  - Utilise `class_name` et, si cette valeur est `None` ou vide, `Socket`, pour les arguments ordinaires comme multi-input.

- **Documentation des arguments sockets de `gen_node_call`**
  - Utilise les noms finaux après dédoublonnage, le type, le nom de socket et son identifiant en cas d'alias. Les arguments ordinaires indiquent le défaut `None` ; les multi-inputs indiquent plusieurs valeurs.

- **Documentation du retour de `gen_node_call`**
  - Suit la priorité du code émis : sortie explicite, `OUT` (jump : deuxième sortie ou `self`, après mise à jour depuis la première), enveloppe `cls`, nœud, puis enveloppe de classe explicite. Pas de section Returns pour les setters.

- `gen_node_call` utilise `sock.group_name` comme clé des sockets arguments regroupées lorsqu’il est renseigné, y compris pour le récepteur ; sinon conserve la clé habituelle.

- `gen_node_call` transmet les sockets issues des arguments avec la clé `ID_identifier` par défaut. `group_name` reste prioritaire ; les alias restent résolus par identifiant physique. Les sockets fixées et la sélection calculée conservent leurs clés nommées.

- `NodeParam` teste les valeurs booléennes avant les entiers : annotation `bool` pour `True` / `False`, `int` pour les entiers.

- La doc des paramètres libres de `gen_node_call` indique le nom d'argument, le type, le défaut et tous les choix enum disponibles, indépendamment de l'alias utilisé dans la signature. Les flags affichent `set[{...}]`.

- `NodeInfo.data_type_input` retourne le nom de la première entrée pilotée par le paramètre de type, depuis les snapshots `data_type_driven_sockets`, ou `None` si aucune entrée n'est concernée. `get_node_implementation` l'utilise pour le récepteur de la boucle typée et la source de déduction du type.

- Les descriptions Grid converties en `NodeCall` utilisent la première entrée comme récepteur pour les méthodes d'instance ; elles conservent la boucle typée et le jump existants, sans déduction automatique du type.

- **Migration des descriptions vers `NodeCall`**
  - `get_node_implementation` retourne désormais des `NodeCall`, ou un tuple pour plusieurs implémentations. Les méthodes d'instance renseignent leur récepteur ; les remplacements partiels `SPECIAL_NODES` sont appliqués avec `replace` sur les branches ordinaires.
  - Les conversions de classe à classe produisent deux descriptions distinctes, méthode d'instance et méthode de classe. Les cas sans implémentation utilisent `implement=False`.
  - Les clés de `SPECIAL_NODES` suivent les attributs d'`NodeCall`, notamment `is_jump` et `method_type`.
  - Le raccordement de `gen_nodes`, qui attend encore des dictionnaires, reste à migrer avant de pouvoir lancer le pipeline avec ces descriptions.

- **Interface de `gen_node_call`**
  - Reçoit une `NodeCall` résolue au lieu d'arguments nommés séparés ; utilise sa propriété `decorator`. Les descriptions intermédiaires des sockets/paramètres restent des dictionnaires internes distincts.
  - Fusionne les paramètres de l'implémentation avec `spec.parameters` (ces derniers prioritaires), sans mutation ; les valeurs fixées filtrent les configurations et sont transmises au nœud.
  - L'expansion des boucles et l'adaptation de `gen_nodes` restent hors de cette migration d'interface.

- **Types de fonction dans `NodeCall`**
  - Centralise les décorateurs et le premier argument ; `first_arg` est une propriété calculée et `has_self` est une propriété indiquant une instance.
  - Valide le type de fonction, le récepteur obligatoire pour les instances et l'absence de récepteur/jump hors instance. Les descriptions `implement=False` sont dispensées des contrôles de récepteur/jump.
  - `replace` valide l'ensemble des changements avant de modifier l'objet. `gen_node_call` conserve uniquement les contrôles dépendant du nœud réel, notamment l'existence des sockets.

- **Migration de `gen_static_code`**
  - Les accès `nd` utilisent `NodeCall.class_property` ou `NodeCall.class_method`, puis `gen_node_call` ; plus d'appel à `_gen_source` dans cette étape.
  - Le retour effectif reste `OUT`. L'enregistrement des références utilise désormais la même valeur, corrigeant l'ancienne métadonnée `NODE` des méthodes de classe qui contredisait leur source.
  - Vérification sans Blender des deux décorateurs et du retour/enregistrement ; les autres étapes de génération restent à migrer.

- **Docstrings NumPy de `gen_node_call`**
  - Résumé en texte standard, sans marqueur de lien personnalisé. Les entrées fixées utilisent un titre Markdown et une liste, pas une section NumPy non standard.
  - La section Returns sépare le type (`Socket`, `Node`, `Self` ou classe explicite) de la description indentée. Les arguments dynamiques indiquent un type et une description distincts ; un paramètre de type inconnu est documenté comme `object`.
  - Vérification du texte produit et de sa syntaxe Python sans Blender ; le rendu complet mkdocstrings reste à vérifier avec ses dépendances installées.

- **Préservation de la mise en forme au rendu**
  - `specialize_source` utilise l'AST pour repérer les branches de contexte, puis remplace uniquement les plages de texte concernées. N'utilise plus `ast.unparse` sur le module complet.
  - Sans branche à spécialiser, le texte est retourné à l'identique. Les branches conservées sont désindentées en préservant les valeurs des chaînes multilignes ; une branche supprimée sans alternative laisse `pass` pour préserver les suites Python valides.
  - Les coupures émises par `SourceWriter` et les commentaires hors branches supprimées sont conservés jusqu'aux fichiers produits. La validation finale par compilation reste active.

- **Migration de `gen_math`**
  - Les fonctions `gnmath` et les méthodes typées utilisent `NodeCall.function` / `NodeCall.method` et `gen_node_call`, avec l'opération fixée dans `parameters` et le récepteur choisi parmi les entrées actives de cette opération.
  - Les opérations communes et propres au contexte sont concaténées par famille au lieu de remplacer la famille Math commune par les seules comparaisons. Les familles absentes du catalogue du contexte sont ignorées.
  - Les déclarations trunc/floor/ceil séparent correctement noms de fonction et d'opérateur. Les opérateurs à code explicite utilisent leur nom complet sans reprendre un préfixe de boucle précédent.
  - Validation Blender 5.3 des deux environnements (104 fonctions Geometry, 98 Shader), des appels fonctions/méthodes, des opérateurs et de la compilation du rendu final. Test dédié : `tests/test_gen_math.py`.

- **Résolution des clés de socket `ID_`**
  - `ItemPath.get_full_name(name, panel)` laisse `None` et les clés `ID_...` intacts, et compose les autres noms avec leur panneau. Les recherches de `Node.set_input_socket` et `Socket.Out` utilisent cette méthode.
  - `Node.socket_by_name` évite aussi la normalisation par `ItemPath` pour les clés `ID_...`, afin de préserver notamment les suffixes `_001` des identifiants Blender.
  - Vérification Blender des 202 fonctions `gnmath` et tests dédiés des identifiants exacts dans les deux environnements (`core_new/tests/test_socket_identifiers.py`).

- **Séparation `NodeCall` / `NodeCalls`**
  - `NodeCall` décrit une fonction unique : nom de méthode scalaire et destination `class_name` scalaire ou `None`. La destination est transmise à l’orchestrateur ; `gen_node_call` ne l’utilise pas. Les constructeurs des accès `nd` et des maths ne transmettent plus de destination à `NodeCall`.
  - `NodeCalls.overrides(base, [{...}, ...])` accepte des dictionnaires de remplacement hétérogènes ; `NodeCalls.attributes(base, champ=[...], autre=...)` construit la même liste depuis des colonnes alignées, avec répétition des scalaires ou listes d'un élément.
  - Une base peut être une `NodeCall` ou une `NodeCalls`. `loop()` (également accessible par itération) produit directement des `NodeCall` portant leur destination ; l'imbrication forme un produit cartésien et les remplacements extérieurs ont priorité. `class_name` est remplacé comme les autres attributs par `NodeCall.replace`.
  - Le constructeur `NodeCalls(base)` transmet les descriptions à l’identique, sans copie ; une liste explicite vide en produit zéro. Les listes de longueurs incompatibles et les clés inconnues sont rejetées.
  - `NodeCalls.replace(**variations)` ajoute une couche extérieure. Les descriptions de `get_node_implementation` utilisent désormais des boucles pour porter leurs destinations, avec des listes de destinations dans `SPECIAL_NODES`. Le raccordement de `gen_nodes` à ces objets reste à migrer.

- Les deux modes de construction de `NodeCalls` sont explicites : `overrides` pour les dictionnaires et `attributes` pour les listes par attribut. Le constructeur ordinaire accepte uniquement la base. Les appels des descriptions ont été adaptés ; le déroulement imbriqué conserve les mêmes règles de priorité.

- **Enregistrement depuis `NodeCall`**
  - `gen_additional` construit les `NodeCall` depuis les champs ordinaires de `ADDITIONAL_IMPLEMENTATIONS` (`method_type`, `return_kind`, etc.), puis utilise `gen_node_call` et `register_source`. `gen_from_spec` est supprimé. Les destinations `LOOP paramètre` sont développées avec `NodeCalls.overrides`, sans mutation des paramètres configurés ; le récepteur explicite est conservé, sinon la socket pilotée par le type est choisie pour chaque variante.
  - Arguments des constructeurs typés : après `value` et `name`, placer les propriétés disponibles dans l'ordre `min`, `max`, `tip`, puis toujours `panel`, avant les autres propriétés. Sans `tip`, `panel` suit donc directement les bornes disponibles.
  - `gen_typed_constructors` travaille uniquement sur `cls.tree_type`. Il enregistre ses méthodes de classe avec `NodeCall.class_method(in_line=source)` et un environnement explicite. Le constructeur de base transmet l'identifiant de socket propre au contexte, le nom, le panneau et la valeur convertie ; les raccourcis fixent leur sous-type. Les sockets sans sous-type conservent leur constructeur de base.
  - Sans nœud, l'appelant fournit explicitement `tree_type`, notamment pour les getters des propriétés en écriture seule. Un environnement absent est rejeté avant tout enregistrement.
  - `register_source(node, node_call, source)` déduit la destination depuis `class_name`, le fichier (`static_nd.py`, `gnmath.py`, module de classe ou `dom_...`), le retour et les règles. Une destination absente est une erreur explicite.
  - Les accès `nd`, maths, opérateurs associés, comparaisons, Mix et les appels d'enregistrement de `gen_nodes` utilisent cette interface.
  - `register_source` centralise aussi les contrôles de collision et la lecture de la signature réelle du source ; `_register_source` est supprimé. Les références manuscrites construisent une `NodeCall` avec leur source `in_line`, puis utilisent `write_source=False`.
  - Les setters sont documentés sans retour ; un `return_socket` explicite est prioritaire sur `return_kind` dans les références.

- **Construction des appels par domaine**
  - `NodeImplementation.get_domain_loop_calls(node_call)` retourne un `NodeCalls` : variante générale si `class_name` est renseigné, puis une variante par valeur de l'enum `domain` du nœud.
  - Chaque variante de domaine conserve les attributs de l'appel et ses paramètres fixés, puis remplace `domain` et la classe de destination. `domain_loop` est désactivé dans les résultats ; l'appel de départ reste inchangé.
  - Méthode ajoutée indépendamment de son futur raccordement dans `get_node_implementation` et `gen_nodes`. Vérifiée sur Store Named Attribute dans Blender.

- `data_type_drives_outputs` consulte les identifiants de sortie. `data_type_input` parcourt les entrées Blender dans leur ordre physique et teste leur identifiant, sans indexation par nom. Les critères restrictifs de détection des types et de présence restent inchangés.

- **Snapshots des sockets pilotées par le type**
  - `NodeInfo.data_type_driven_sockets` remplace `data_type_driven_ids`. Pour chaque valeur du paramètre de type, les listes `inputs` / `outputs` contiennent des snapshots `NodeSocket` ordonnés, avec identifiant, nom et type de cette variante.
  - Les critères de détection et le filtre par type restent inchangés. `data_type_input` et `data_type_drives_first_input` lisent ces objets et acceptent une liste d'entrées vide pour le type courant.
  - Les snapshots restent inchangés après la réinitialisation du nœud Blender. Le choix du récepteur par variante dans le générateur n'est pas modifié à cette étape.

- **Validation des descriptions résolues**
  - `NodeCall` n'appelle plus `_check` à la construction. Les copies et les résultats intermédiaires de `NodeCalls` peuvent être incomplets.
  - `gen_node_call` appelle `_check` avant toute analyse du nœud : la description finale est validée après application de toutes les boucles et de tous les remplacements.
