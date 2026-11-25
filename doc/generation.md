# Générer une API par version de Blender

Chaque version majeure/mineure possède son dossier : `core_5_3` pour Blender
5.3.x, `core_5_4` pour Blender 5.4.x, etc. L'import public calcule le nom depuis
`bpy.app.version`. Si le dossier manque ou si sa configuration active concerne
une autre version mineure, l'import échoue explicitement.

Le générateur est commun dans `generation`. Il utilise le même nom de dossier
pour sa destination : Blender 5.3 ne peut pas écrire dans `core_5_2`. Il n'existe
plus de bascule `core` / `core_new`, ni d'options `new` ou `use_core_new`.
Les classes manuscrites, le kernel et les fichiers générés restent propres à chaque version.
Les descriptions et les dimensions se trouvent dans `generation/api_<majeur>_<mineur>`.

## Étape 0 — Préparer une nouvelle version

Copier une API existante vers le dossier de la nouvelle version, par exemple
`core_5_3` vers `core_5_4`. Copier aussi `generation/api_5_3` vers
`generation/api_5_4` : ce dossier contient `config.py` et `node_dims.py`.
Le kernel est inclus dans la copie du core. Mettre à jour `__version__` dans le nouvel
`__init__.py`. Garder la configuration précédente pour la comparaison jusqu'à
la génération. Ne pas toucher au dossier de la version publiée.

Un dossier copié n'est pas une garantie de compatibilité : adapter les classes
manuscrites et les descriptions du générateur, puis valider dans Blender cible.
En particulier, une API 5.2 doit encore être générée et testée séparément.

## Étape 1 — Identifier les nouvelles sockets

Dans `generation/gen API.blend`, utiliser le texte **Step 1 - New Sockets**.
Examiner Geometry Nodes et Shader Nodes. Compléter les types dans
`core_<majeur>_<mineur>/kernel/constants.py`, les classes racines, spécialisations et registres du
nouveau dossier de version. Les tables de sockets sont générées automatiquement.

## Étape 2 — Mesurer les nœuds

Afficher `NODE DIMS` dans un éditeur Geometry Nodes et le matériau
`MAT NODE DIMS` dans un éditeur Shader. Lancer **Step 2 - Node Dims** dans Blender
avec interface : ce texte reconstruit les nœuds, rafraîchit les éditeurs et écrit
`generation/api_<majeur>_<mineur>/node_dims.py`. Il ne nécessite pas d'importer l'API.

## Étape 3 — Create API

Lancer **Step 3 - Create API** dans le `.blend`, ou exécuter
`generation/create_api.py` depuis l'éditeur de texte Blender.
Le script fonctionne sans charger le package public, génère les deux
environnements dans le dossier de la version courante, écrit la configuration
et le rapport `comparison_<version>.md`. La référence est conservée avant son
écrasement éventuel, pour ne pas comparer un fichier à lui-même.

Examiner le rapport et les méthodes produites. Si nécessaire, ajuster les
**descriptions ordinaires** de `generation/api_<majeur>_<mineur>/config.py`, puis relancer. Ne pas
modifier manuellement les fichiers générés ni ajouter un générateur spécifique
à un nœud quand `NodeImplementation` suffit.

Activer ensuite le nouveau `config_<version>.py` dans le `constants.py` du dossier
cible. Redémarrer Blender et tester les groupes, modifiers, tools, matériaux et
Package. Aucune promotion par renommage n'est nécessaire : les dossiers de
versions restent en place.

## Régénérer une version existante

Démarrer la version de Blender concernée et lancer **REGENERATE** ou
`generation/regenerate_core.py`. Cela remplace les fichiers générés et écrit la
configuration uniquement dans `core_<majeur>_<mineur>` correspondant.

Dans une session où cette API est déjà importable, les appels sont simplement :

```python
from geonodes.generation import generate, gen_config

generate.generate()
gen_config.write_file()
```

Les autres dossiers de versions sont inchangés. Pour une régénération dans
Blender 5.2, préparer `core_5_2` puis résoudre les incompatibilités de nœuds et
valider son API ; l'existence de `core_5_3` n'implique pas ce support.

## Comparer deux versions explicitement

```bash
python3 generation/compare_versions.py \
  core_5_3/config_5_3_0.py \
  core_5_4/config_5_4_0.py \
  -o comparaison.md
```

Cette comparaison fonctionne sans Blender et ignore les dimensions par défaut.
Les nœuds sont identifiés par leur identifiant Blender. Les règles détaillées
sont dans [GENERATION_RULES.md](../generation/GENERATION_RULES.md).

## Structure

```text
geonodes/
├── core_5_3/
│   ├── kernel/
│   ├── root/
│   ├── common/
│   ├── geonodes/
│   └── shadernodes/
└── generation/
    ├── context.py
    ├── generate.py
    └── api_5_3/
        ├── config.py
        └── node_dims.py
```

Le moteur charge le kernel et les descriptions de la version ciblée sans
initialiser l'API publique de ce core. Les deux dossiers doivent donc exister
avant de démarrer le parcours des nœuds. Le kernel n'est plus partagé entre les
versions. Le moteur reste commun et doit être validé dans chaque Blender pris
en charge.

### Headers des nœuds ajoutés

Le rapport lit les `cross_reference.py` générés dans le core de destination,
sans importer ses modules. Pour chaque nœud ajouté, il affiche les signatures
des implémentations hors `nd`, ou `Static only` si seul `nd` est enregistré.
Ces références couvrent aussi les implémentations supplémentaires : elles ne
portent pas encore de provenance distinguant défaut et ajouts. Des références
absentes sont signalées comme non renseignées, jamais comme `Static only`.

Pour les nœuds modifiés, le rapport contient une sous-section `Old version`
et une sous-section `New version` avec les signatures de chaque core, puis
`Changes` avec les différences de configuration. `create_api.py` conserve
également les références croisées avant régénération pour préserver ces anciennes
signatures. Le rapport explicite 5.2 vers 5.3 est `generation/comparison_52_53.md`.

La section `Argument changes` rapproche les signatures par classe (ou `nd`),
nom et nature de méthode. Les nouveaux arguments sont marqués `arguments
appended` s'ils suivent tous les arguments existants, ou `CAUTION: arguments
inserted` s'ils sont insérés avant un argument existant. Les noms et leur ordre
sont analysés par AST, sans évaluer annotations ou valeurs par défaut.
Suppressions, réordonnancements et modifications des défauts ne sont pas
présentés à tort comme des ajouts ; les signatures complètes restent affichées.
