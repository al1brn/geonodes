# Comparaison des signatures : core → core_new

Comparaison effectuée le 2 novembre 2026 sur les fichiers présents après la génération utilisateur, avec Blender 5.3.0 Beta.

Suivi : le traitement multi-input (`join`, `to_instance` et variantes de Mesh Boolean) a depuis été corrigé et les fichiers régénérés. Les tableaux et fichiers de différences ci-dessous conservent l'état de l'audit avant cette correction.

## Conclusion

La couverture des nœuds est large, mais la nouvelle API n'est pas compatible à l'identique avec l'ancienne. Certaines différences sont structurelles et attendues ; d'autres cassent des appels auparavant valides.

Aucune correction du générateur ou des classes n'a été effectuée pendant cet audit.

## Périmètre et méthode

- Ancienne référence : `core` (version déclarée 5.2.0 ; en-tête des fichiers générés consultés : 21 septembre 2026).
- Nouvelle référence : `core_new`, variantes concrètes `geonodes.generated` et `shadernodes.generated`.
- Chargement des deux versions sous des noms de packages distincts dans Blender ; inspection des signatures et des descripteurs, sans exécuter les getters pendant l'inventaire.
- Comparaison des méthodes publiques, propriétés et opérateurs spéciaux, en respectant l'héritage effectif et les surcharges manuscrites.
- Comparaison de `nd` et `gnmath` ; ancien `snd` comparé au nouveau `shadernodes.nd`.
- Les classes qui n'existent plus dans un environnement, telles que Collection dans les shaders, ne sont pas considérées comme des classes manquantes.
- Le catalogue historique des classes de sockets et de `gnmath` est commun aux deux environnements : les absences dans un environnement ne sont donc pas toutes des régressions.
- Les membres hérités sont comptés dans chaque classe qui les expose. Les nombres ci-dessous ne comptent pas des régressions distinctes.
- Une même signature ne garantit ni le même retour, ni un fonctionnement équivalent. Cet audit n'est pas un test exhaustif des graphes produits.

## Bilan brut

| Environnement | Identiques hors annotations | Annotations seules | Paramètres différents | Nature différente | Noms anciens absents | Noms nouveaux |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| geonodes | 2127 | 72 | 344 | 30 | 838 | 505 |
| shadernodes | 803 | 7 | 139 | 6 | 380 | 90 |

« Nature différente » comprend méthode → propriété, méthode → méthode de classe, et ajout/retrait de setter. « Noms anciens absents » ne signifie pas nœuds indisponibles.

## Écarts prioritaires

| API | Avant | Maintenant | Conséquence |
| --- | --- | --- | --- |
| `Geometry.join` | `join(self, *geometry)` | `join(self)` | Impossible de passer les géométries à joindre. Même perte pour `Bundle.join` et `Geometry.to_instance`. |
| `Vector.x/y/z/xyz` | Propriétés disponibles | Non déclarées | La lecture de `Vector((1,2,3)).x` lève effectivement `AttributeError`. `separate_xyz()` existe, mais ne préserve pas cette API. |
| `Face.set` | `Domain.set(self, name, value)` | Méthode de classe `set(cls)` utilisant Face Set | Le générateur masque une méthode manuscrite héritée de Domain. La version manuscrite existe toujours dans les sources. |
| `Float.IndexSwitch` | `IndexSwitch(cls, *values, index=None, default_index=0)` | `IndexSwitch(cls, named_sockets=None, index=None, _0=None, _1=None, **sockets)` | Le constructeur généré masque le constructeur manuscrit hérité de Socket ; anciens appels positionnels et `default_index` incompatibles. `MenuSwitch` présente le même mécanisme de masquage. |
| `Float.add` et opérations voisines | Argument `value` | Argument `value_1` | Les appels par mot-clé `value=...` cassent. Sur Vector : `vector` devient `vector_1`. Les appels positionnels correspondants restent valides. |
| `Float.list_length` et famille des listes | Méthodes typées disponibles sur plusieurs classes | `data_type` réexposé sur Float ; plusieurs variantes absentes sur Vector et autres classes | Complément typé incomplet ; correspond au traitement restant à faire lorsque seul le premier input dépend du type. |

Les quatre contrôles d'appels `join(other)`, `add(value=1)`, `Face.set(name, value)` et `IndexSwitch(1,2,index=0)` ont été vérifiés avec `inspect.signature(...).bind(...)` : ils échouent sur les signatures nouvelles. Le contrôle de `Vector.x` a réellement exécuté l'accès dans un arbre Geometry Nodes. Les détails figurent dans [signature_probes.json](signature_probes.json).

## Changements attendus ou choix d'API à conserver en connaissance de cause

| Ancien accès | Nouveau accès / traitement |
| --- | --- |
| `Mesh.UVSphere(...)` | `Mesh.UvSphere(...)` : capitalisation. |
| `Float.blur(...)` | `Float.blur_attribute(...)` : renommage. |
| `Geometry.merge(...)` | `Geometry.merge_by_distance(...)` : renommage. |
| `Mesh.extrude_faces(...)` | `mesh.extrude(..., mode='FACES')` : variante générique ; le raccourci sur Face n’est pas déclaré dans cette génération. |
| `Face.evaluate_at_index(...)` | `Face.EvaluateAtIndex(...)` : méthode de classe sur le domaine. |
| `Face.scale(...)` | `Face.scale_elements(...)` : renommage. |
| Variantes `map_range_linear`, `trim_factor`, `CircleRadius`, etc. | Méthode générique avec paramètres de mode/interpolation exposés. |
| `curve.length()` | `curve.length` : propriété selon la règle « aucun argument libre ». |
| `rotation.invert()` | `rotation.invert` : même règle ; changement de syntaxe à prendre en compte. |
| `Float.grid_to_points(...)` | `Float.GridToPoints(...)` : méthode de classe selon les règles typées. |
| Ancien `snd` | `nd` dans le contexte shader. |

Les signatures génériques rassemblent désormais les entrées de plusieurs configurations. Cela augmente la couverture, mais peut déplacer les arguments positionnels : `Mesh.Line` introduit notamment `resolution` avant `start_location`, `Curve.Circle` introduit les points avant `radius`. Les anciens appels par position nécessitent une vérification ; les mots-clés sont plus explicites.

Les anciens constructeurs de sous-types tels que `Float.Angle`, `Float.Factor`, `Vector.Direction`, `Vector.Velocity` ne sont pas déclarés dans la nouvelle API. Les constructeurs génériques restent présents ; la reprise des raccourcis et des sous-types mérite un traitement séparé.

## Catalogue statique

- Geometry Nodes : tous les noms de l'ancien `nd` sont présents ; 356 anciens membres comparés, 377 nouveaux.
- Shaders : 116 anciens membres de `snd`, 144 nouveaux ; seul `line_style_output` est absent, conformément à l'exclusion temporaire de ShaderNodeOutputLineStyle.
- Cela établit la présence des points d'accès statiques, pas l'équivalence de leurs signatures ou du comportement.

## Détail par classe

| Environnement | Classe | Anciens | Nouveaux | Identiques | Paramètres modifiés | Nature modifiée | Anciens noms absents | Ajouts |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| geonodes | Boolean | 89 | 93 | 61 | 13 | 0 | 14 | 18 |
| geonodes | Bundle | 60 | 55 | 46 | 6 | 0 | 7 | 2 |
| geonodes | Closure | 51 | 48 | 45 | 2 | 0 | 4 | 1 |
| geonodes | Cloud | 118 | 116 | 72 | 11 | 1 | 33 | 31 |
| geonodes | CloudPoint | 48 | 38 | 19 | 6 | 0 | 22 | 12 |
| geonodes | Collection | 50 | 50 | 43 | 2 | 0 | 5 | 5 |
| geonodes | Color | 126 | 93 | 80 | 6 | 0 | 40 | 7 |
| geonodes | Corner | 40 | 30 | 19 | 2 | 0 | 18 | 8 |
| geonodes | Curve | 192 | 149 | 88 | 30 | 4 | 68 | 25 |
| geonodes | Edge | 65 | 51 | 30 | 5 | 0 | 29 | 15 |
| geonodes | Face | 61 | 51 | 22 | 7 | 2 | 29 | 19 |
| geonodes | Float | 210 | 172 | 123 | 24 | 2 | 54 | 16 |
| geonodes | Font | 48 | 49 | 42 | 2 | 0 | 4 | 5 |
| geonodes | Geometry | 108 | 100 | 68 | 9 | 1 | 29 | 21 |
| geonodes | GreasePencil | 123 | 110 | 70 | 17 | 1 | 34 | 21 |
| geonodes | Image | 55 | 51 | 43 | 2 | 0 | 10 | 6 |
| geonodes | Instance | 41 | 35 | 20 | 1 | 1 | 18 | 12 |
| geonodes | Instances | 119 | 109 | 72 | 10 | 2 | 34 | 24 |
| geonodes | Integer | 148 | 144 | 114 | 18 | 0 | 15 | 11 |
| geonodes | Layer | 39 | 29 | 18 | 1 | 0 | 19 | 9 |
| geonodes | Material | 48 | 50 | 42 | 2 | 0 | 4 | 6 |
| geonodes | Matrix | 94 | 63 | 56 | 4 | 2 | 32 | 1 |
| geonodes | Menu | 48 | 45 | 41 | 3 | 0 | 4 | 1 |
| geonodes | Mesh | 191 | 137 | 91 | 16 | 3 | 80 | 26 |
| geonodes | Object | 53 | 52 | 45 | 2 | 0 | 6 | 5 |
| geonodes | Point | 47 | 37 | 19 | 5 | 0 | 22 | 12 |
| geonodes | Rotation | 84 | 62 | 56 | 4 | 1 | 23 | 1 |
| geonodes | Sound | 48 | 50 | 42 | 2 | 0 | 4 | 6 |
| geonodes | Spline | 55 | 44 | 20 | 8 | 1 | 25 | 14 |
| geonodes | SplinePoint | 56 | 38 | 19 | 6 | 0 | 30 | 12 |
| geonodes | String | 84 | 69 | 58 | 4 | 2 | 19 | 4 |
| geonodes | Vector | 180 | 168 | 116 | 19 | 2 | 42 | 30 |
| geonodes | Vertex | 58 | 42 | 21 | 5 | 1 | 30 | 14 |
| geonodes | Volume | 114 | 109 | 70 | 9 | 1 | 31 | 26 |
| geonodes | nd | 356 | 377 | 232 | 81 | 3 | 0 | 21 |
| geonodes | gnmath | 104 | 162 | 104 | 0 | 0 | 0 | 58 |
| shadernodes | Boolean | 89 | 46 | 40 | 5 | 0 | 44 | 1 |
| shadernodes | Bundle | 60 | 49 | 45 | 4 | 0 | 11 | 0 |
| shadernodes | Closure | 51 | 47 | 45 | 2 | 0 | 4 | 0 |
| shadernodes | Color | 126 | 94 | 79 | 5 | 1 | 41 | 9 |
| shadernodes | Float | 210 | 139 | 115 | 18 | 1 | 74 | 3 |
| shadernodes | Integer | 148 | 74 | 63 | 5 | 0 | 76 | 2 |
| shadernodes | Menu | 48 | 44 | 41 | 3 | 0 | 4 | 0 |
| shadernodes | Shader | 69 | 69 | 58 | 8 | 0 | 3 | 3 |
| shadernodes | String | 84 | 61 | 52 | 4 | 2 | 25 | 2 |
| shadernodes | Vector | 180 | 133 | 99 | 21 | 0 | 60 | 13 |
| shadernodes | VolumeShader | 50 | 46 | 46 | 0 | 0 | 4 | 0 |
| shadernodes | nd | 116 | 144 | 49 | 64 | 2 | 1 | 29 |
| shadernodes | gnmath | 104 | 99 | 71 | 0 | 0 | 33 | 28 |

## Fichiers de détail

- [signature_differences.csv](signature_differences.csv) : toutes les différences, anciennes et nouvelles signatures, nature des membres et nœuds identifiés dans le corps des fonctions.
- [signature_comparison.json.gz](signature_comparison.json.gz) : inventaire complet compressé, y compris membres inchangés, annotations, setters et classe propriétaire effective.
- [signature_probes.json](signature_probes.json) : contrôles ciblés de compatibilité.

Les correspondances de noms et de nœuds proposées ci-dessus sont des conclusions de l'inspection, pas des alias déjà ajoutés au code.
