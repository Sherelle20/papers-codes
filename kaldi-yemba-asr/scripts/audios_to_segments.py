"""
Audios vers le fichier segments
"""

import os
from pydub import AudioSegment

def remove_suffix(filename):
    parts = filename.split('_')  # Divise le nom de fichier en parties séparées par '_'
    base_name = '_'.join(parts[:-1])  # Rejoint toutes les parties sauf la dernière avec '_'
    return base_name
    
def generate_segments(directory, output_segments_file):
    segments = []
   
    # Parcourt tous les fichiers et sous-répertoires dans le répertoire donné
    for root, _, files in os.walk(directory):
        for file in files:
            # Vérifie si le fichier a l'extension .wav
            if file.endswith('.wav'):
                print("yes")
                # Chemin complet vers le fichier actuel
                file_path = os.path.join(root, file)
                # Nom du fichier sans l'extension
                file_name = os.path.splitext(file)[0]
                # Nom sans le numéro du fichier
                base_name = remove_suffix(file_name)
                # Charge le fichier audio pour obtenir sa durée
                audio = AudioSegment.from_wav(file_path)
                duration = len(audio) / 1000.0  # Durée en secondes
                
                # Ajoute l'entrée à la liste des segments avec le format demandé
                #segments.append(f"{file_name} {base_name} 0.0 {duration:.3f}")
                segments.append(f"{file_name} {file_name} 0.0 {duration:.3f}")
                print(f"Added to segments: {file_name} {base_name} 0.0 {duration:.3f}")
                print(f"Added to segments: {file_name} {file_name} 0.0 {duration:.3f}")
        #print(len(segments))
    
    # Trie les segments par identifiant de segment
    segments.sort()
    
    
    # Écrit les segments triés dans le fichier
    with open(output_segments_file, 'w') as segments_file:
        for segment in segments:
            segments_file.write(segment + '\n')

main_data='/home/sherelle/Documents/yemba_dataset_1'

projet_dir = '/home/sherelle/Documents/Stage5GI/implementation/Kaldi/kaldi-master/kaldi-master/egs/YembaEgraASR/'

#folder = main_data

# Exemple d'utilisation
directory = main_data # Remplacez par le chemin vers votre dossier contenant les fichiers .wav
output_segments_file = projet_dir+'data/segments'  # Le fichier segments à générer

generate_segments(directory, output_segments_file)

# Vérifie si le fichier segments a été correctement rempli
with open(output_segments_file, 'r') as f:
    lines = f.readlines()
    if not lines:
        print("Le fichier segments est vide.")
    else:
        print(f"Le fichier segments contient {len(lines)} entrées.")

