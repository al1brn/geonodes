# geonodes — contexte pour Claude Code

## Architecture

```
geonodes/
  __init__.py              exports publics
  core/
    nodeclass.py           Node, Group, G, Layout, Panel, ZoneNode, MenuNode
    socket_class.py        Socket + toutes les classes typées
    treeclass.py           Tree, GeoNodes, ShaderNodes
    nodezone.py            repeat(), simulation(), ZoneIterator
    treearrange.py         auto-layout des nœuds
    scripterror.py         NodeError avec traceback Blender
    sockettype.py          correspondance types Blender ↔ Python
    geometries.py          méthodes sur Mesh, Curve, Cloud, Instances, …
    shadernodes.py         classe ShaderNodes
    generated/             wrappers auto-générés — NE PAS MODIFIER
  generation/
    gen_auto.py            générateur de code (à lancer dans Blender)
    node_explore.py        NodeInfo — introspection du catalogue Blender
    gen_config.py          config manuelle du générateur
  demos/                   exemples fonctionnels (source de vérité pour l'API)
  tests/
    unit/                  tests sans Blender
    integration/           tests avec Blender headless
```

## Règles fondamentales

- Le module tourne **dans Blender** — `bpy` est toujours disponible à l'exécution
- Les fichiers dans `core/generated/` et `generation/gen_auto_dicts.py` sont **auto-générés** : ne pas modifier à la main
- Les tests sans Blender → `tests/unit/`, avec Blender → `tests/integration/`
- Convention de nommage : snake_case pour les méthodes, CamelCase pour les classes, préfixe `nd.` pour les nœuds statiques GeoNodes, `snd.` pour les shaders

## Lancer les tests

```bash
/Applications/Blender.app/Contents/MacOS/Blender --background \
  --python run_blender_tests.py -- tests/integration/test_XXX.py -v
```

## Syntaxe des zones — IMPORTANT

Les zones (Repeat, Simulation, For Each Element) utilisent le **protocole itérateur** — syntaxe `for`.

```python
# Repeat
for rep in repeat(count, mesh=mesh, value=0.):
    rep.mesh = rep.mesh + delta
result = rep.mesh

# Simulation
for sim in simulation(cloud=cloud, speed=initial_speed):
    sim.cloud.position += sim.speed * sim.delta_time
    sim.speed += (0, 0, -9.81) * sim.delta_time
    sim.cloud = sim.cloud
result = sim.cloud

# For Each Element
for feel in mesh.faces.for_each(color=nd.position):
    feel.generated.geometry = Mesh(feel.element)
result = feel.generated.geometry
```

## Pièges connus (bugs corrigés ou patterns à respecter)

| Faux | Correct | Raison |
|---|---|---|
| `snd.attribute("X").fac` | `.factor` | Socket renommé Blender 5.x |
| `shader.mix(s, fac=f)` | `factor=f` | Idem |
| `Repeat(n, x=v)` | `repeat(n, x=v)` | Capital = ancienne syntaxe supprimée |
| `Simulation(x=v)` | `simulation(x=v)` | Idem |
| `node.set_input_sockets(…)` | `node.set_input_socket(name, val)` | Méthode au singulier uniquement |
| `Integer.MenuSwitch({…}, menu='Z')` | `menu=2` | `menu` est un index entier |
| `geo.point_cloud.points` | `Cloud(geo.point_cloud).points` | `point_cloud` retourne `Geometry` |
| `isinstance(x, object)` | `x is object` | `isinstance(x, object)` est toujours `True` |
| `Group.Prefix(p, n, d, **kw)` | passer `named_sockets=d` explicitement | Sinon le dict est ignoré |

## Démos actives (sans fichiers OLD)

Les fichiers préfixés `OLD` dans `demos/` sont obsolètes et ne doivent pas être importés.
Démos valides : `arrows`, `cam_culling`, `counters`, `curly`, `examples`, `explosion`,
`forest`, `fractal`, `furniture`, `gizmo`, `gravity`, `observer`, `rain`, `random`,
`shaders`, `simulation`, `topology`, `fourd`.

Les démos `formula`, `formula_tree`, `formula_latex` ont des bugs API en cours de correction.

## Référence API complète

Voir `llms.txt` à la racine pour la référence API complète avec exemples.
