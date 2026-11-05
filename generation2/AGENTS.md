# Maintenance du générateur

- **SUPER IMPORTANT : passer par le générateur standard de `NodeImplementation`, avec les descriptions d'implémentation ordinaires.** Ne pas créer de générateur dédié par famille de nœuds. Si un hack semble nécessaire, en parler à l'utilisateur avant de l'implémenter.

- Avant de modifier les règles d'introspection ou de génération, lire [GENERATION_RULES.md](GENERATION_RULES.md).
- Mettre ce document à jour lorsque le comportement change. Distinguer les règles appliquées des traitements restant à implémenter.
- Conserver les exceptions de nœuds dans les dictionnaires de `config.py`.
- Modifier le générateur ou les classes manuscrites, puis régénérer les fichiers produits ; ne pas corriger les fichiers générés à la main.
