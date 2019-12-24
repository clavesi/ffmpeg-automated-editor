# Éditeur Automatisé
Une application qui permet d'automatiser des vidéos ensemble de manière simple. L'idée est basée sur la [tentative de Devon Crawford](https://github.com/DevonCrawford/Video-Editing-Automation) dans laquelle il utilise [ffmpeg](https://ffmpeg.org/).

*Lire ceci en: [English](README.md)*

## Comment Ça Marche
Ce projet utilise [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) pour le traitement de la vidéo et [PIL](http://www.pythonware.com/products/pil/) pour le traitement d'image. Pour l'exécuter, vous devez d'abord [installer ffmpeg](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg) et ffmpeg-python.

## Guide de Répertoire
- **src/** (code source)
- **frames/** (où les vues de couleur et de gris sont stockés pour l'édition. **Peut prendre beaucoup de stockage pendant l'exécution du programme, s'efface automatiquement une fois terminé**)
- **imports/** (répertoire pour toutes les vidéos que vous voulez éditer)
- **exports/** (c'est là que la vidéo finale est placée)

### **Ne Pas Faire**
1. **Ne pas faire** placer des vidéos avec des fréquences d'images très différentes et utiliser une fréquence d'images de base encore plus différente - le programme la coupera par accident.
2. **Ne pas faire** mettre un dossier dans le dossier imports/ car il lira cela mais ne pourra pas accéder à ces fichiers
3. **Ne pas faire** ouvrir les dossiers créés dans frames/ jusqu'à ce que le programme se termine car l'invite de commande refusera l'accès à ce dossier et cassera

### Mode d'emploi
1. Placez les vidéos dans **imports/**, en vous assurant que les noms de fichiers n'ont **pas d'espaces**.
2. Exécutez **editor.py** et sélectionnez les variables souhaitées
3. Attendre que la vidéo éditée soit créée
4. Profitez de votre nouvelle vidéo

### Paramètres
| Arg      | Desc          |
| -------- |:-------------:|
| -fps     | fréquence d'images de la vidéo [int] <br> par default=30|
| -cs      | taille pour chaque morceau d'image, xth sur chaque y pixels, plus petit prendra plus de temps [x:y]<br> par default=5:9|
| -cl      | la durée de chaque vidéo coupée [x:y]  <br> par default=5:7 |
| -r       | la résolution de la vidéo finale [w:h]  <br> par default=1920:1080 |