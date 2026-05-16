import os
import re

# Expression régulière pour extraire les parties de la nomenclature
pattern = re.compile(r'spkr_(\d+)_word_(\d+)_st_(\d+)\.wav')

def rename_files(directory):
    print('u')
    for filename in os.listdir(directory):
        print(filename)
        match = pattern.match(filename)
        if match:
            spkr_id, word_id, stmt_id = match.groups()
            
            # Formater les identifiants avec des zéros en tête
            spkr_id = spkr_id.zfill(4)
            word_id = word_id.zfill(4)
            stmt_id = stmt_id.zfill(4)
            
            # Nouveau nom de fichier
            new_filename = f"{spkr_id}_{word_id}_{stmt_id}.wav"
            
            # Chemin complet des fichiers
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            
            # Renommer le fichier
            os.rename(old_file, new_file)
            print(f"Renommé : {filename} -> {new_filename}")

# Répertoire contenant les fichiers à renommer
directory = 'yemba_dataset_1'

rename_files(directory)
