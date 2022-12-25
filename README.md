# list-files-in-excel
 
# List Files

Ce script Python liste tous les fichiers dans un dossier et ses sous-dossiers et écrit les noms des fichiers dans un fichier CSV.
Le fichier CSV contiendra des colonnes faisant référence au nom du client, à la semaine de livraison, au numéro de livraison et au chemin relatif vers le fichier.


## Exigences

- Python 3.8.2
- Module CSV (pour créer un fichier Excel) ou csv (pour créer un fichier CSV)

## Installation

1. Clonez ou téléchargez le projet sur GitHub.
2. Installez Python 3.x depuis python.org.
3. Installez les modules requis en exécutant pip install -r requirements.txt.

## Usage

1. Spécifiez le chemin du dossier d'entrée dans le fichier "input_folder.txt", en enlevant tout slash de fin ou le programme ne fonctionnera pas.
2. Spécifiez le chemin du dossier de sortie où vous voulez que votre fichier CSV apparaisse.
3. Exécutez le script en utilisant Python : python main.py

## Executable

Pour créer un fichier exécutable autonome (.exe), vous pouvez utiliser un outil appelé PyInstaller.
Des modifications du script doivent être apportées pour que l'installation autonome fonctionne.

1. Installez PyInstaller en exécutant pip install pyinstaller.
2. Exécutez pyinstaller main.py pour créer un fichier exécutable dans le dossier dist.

## License

Ce projet est sous licence MIT.