# Principes de maintenance

- **SUPER IMPORTANT : utiliser le générateur standard de `NodeImplementation`.** Les implémentations se décrivent avec les informations ordinaires (classe cible, nom, méthode de classe, etc.) ; ne pas ajouter de générateur dédié ou de traitement spécial pour un nœud ou une famille quand le mécanisme standard suffit.
- Réduire les hacks au minimum. Si une exception ou un traitement particulier semble nécessaire, l'expliquer à l'utilisateur avant de l'implémenter.
- Pour `generation2`, lire aussi ses consignes et son document `GENERATION_RULES.md`.
