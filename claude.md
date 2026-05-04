# geonodes — contexte pour Claude Code

## Architecture
- `core/` : classes Socket, Node, Tree, Domain
- `generation/` : auto-génération depuis l'API Blender
- `shadernodes/` : même structure pour les shaders
- Le module tourne **dans Blender** (bpy disponible) — pas de test sans mock bpy

## Conventions
- Les méthodes suivent les règles de nommage snake_case/CamelCase documentées dans README

## Ce qu'il ne faut pas toucher
- Les fichiers générés dans `generation/` sont produits automatiquement