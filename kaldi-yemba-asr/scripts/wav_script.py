"""
Wav script file
"""
import os

def remove_suffix(filename):
    parts = filename.split('_')  # Divise le nom de fichier en parties séparées par '_'
    base_name = '_'.join(parts[:-1])  # Rejoint toutes les parties sauf la dernière avec '_'
    return base_name
    
def generate_wav_scp(directory, output_scp_file):
    entries = []
    # Parcourt tous les fichiers et sous-répertoires dans le répertoire donné
    for root, _, files in os.walk(directory):
        for file in files:
            # Vérifie si le fichier a l'extension .wav
            if file.endswith('.wav'):
                # Chemin complet vers le fichier actuel
                file_path = os.path.join(root, file)
                # Nom du fichier sans l'extension
                file_name = os.path.splitext(file)[0]
                res = remove_suffix(file_name)
                # Ajoute l'entrée à la liste
                entries.append(f"{file_name} {file_path}")
                print(f"Added to wav.scp: {file_name} {file_path}")
    
    # Trie les entrées
    entries.sort()
    
    # Écrit les entrées triées dans le fichier .scp
    with open(output_scp_file, 'w') as scp_file:
        for entry in entries:
            scp_file.write(entry + '\n')

main_data= '/home/sherelle/Documents/yemba_dataset_1'
projet_dir = '/home/sherelle/Documents/Stage5GI/implementation/Kaldi/kaldi-master/kaldi-master/egs/YembaEgraASR/'

#train_data=main_data+'/yemba_all'


# Exemple d'utilisation
directory = main_data # Remplacez par le chemin vers votre dossier contenant les fichiers .wav
output_scp_file = projet_dir+'data/wav.scp'  # Le fichier .scp à générer

generate_wav_scp(directory, output_scp_file)

