"""
Split des données en train et tes
"""
import os

def extract_ids_from_line(line):
    # Extraire le premier élément de la ligne
    first_element = line.split()[0]
    print(first_element)
    # Diviser le premier élément en parties
    parts = first_element.split('_')
    if len(parts) == 3:
        spkr_id, word_id, stmt_id = parts
        return int(spkr_id), int(word_id), int(stmt_id)
    else:
        raise ValueError("Le format du premier élément de la ligne ne correspond pas à la nomenclature attendue.")

def split_data(all_dir, train_dir, test_dir, test_size=0.2):
    files = ['wav.scp', 'text', 'utt2spk', 'segments']

    for file in files:
        with open(os.path.join(all_dir, file), 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Trier les lignes par spkr_id, word_id, stmt_id
        lines.sort(key=lambda line: extract_ids_from_line(line))

        # Déterminer l'index de division
        split_index = int(len(lines)* (1 - test_size))
        print("split index",split_index)

        # Diviser les lignes en train et test
        train_lines = lines[:split_index]
        test_lines = lines[split_index:]
        print(len(test_lines))
        print(len(train_lines))
        # Écrire les lignes dans les fichiers de train et test
        with open(os.path.join(train_dir, file), 'w', encoding='utf-8') as f:
            f.writelines(train_lines)

        with open(os.path.join(test_dir, file), 'w', encoding='utf-8') as f:
            f.writelines(test_lines)

projet_dir = 'kaldi-master/kaldi-master/egs/YembaEgraASR/'

# Chemins vers vos répertoires de données
all_dir = projet_dir + 'data'
train_dir = projet_dir + 'data/train'
test_dir = projet_dir + 'data/test'

# Créer les répertoires de train et test s'ils n'existent pas
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Diviser les données avec 20% pour le test
split_data(all_dir, train_dir, test_dir, test_size=0.2)
