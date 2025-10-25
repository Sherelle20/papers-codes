"""
create text
"""
import sys

def read_text_segments(text_file, segments_file, output_file):
    # Lecture du fichier text
    with open(text_file, 'r', encoding='utf-8') as text_f:
        lines_text = text_f.readlines()

    # Lecture du fichier segments
    with open(segments_file, 'r', encoding='utf-8') as segments_f:
        lines_segments = segments_f.readlines()

    # Dictionnaire pour mapper les identifiants de word vers les mots correspondants
    word_mapping = {}
    for line in lines_text:
        parts = line.strip().split(' ', 1)
        if len(parts) == 2:
            word_mapping[parts[0]] = parts[1]
        #print(word_mapping)

    # Ouverture du fichier de sortie
    with open(output_file, 'w', encoding='utf-8') as output_f:
        for segment_line in lines_segments:
            parts = segment_line.strip().split(' ')
            if len(parts) >= 1:
                segment_id = parts[0]
                word_id = int(segment_id.split('_')[1])  # Extrait l'identifiant de word
                word_id=str(word_id)
                print(word_id)

                if word_id in word_mapping:
                    output_line = f"{segment_id} {word_mapping[word_id]}\n"
                    output_f.write(output_line)
                    print(f"Added to {output_file}: {output_line.strip()}")
                else:
                    print(f"Word ID {word_id} not found in text mapping")

# Exemple d'utilisation
#text_file = '/home/sherelle/Documents/Stage5GI/implementation/Kaldi/kaldi-master/kaldi-master/egs/teste1/help_scripts/text'  # Remplace avec ton chemin vers le fichier text
segments_file ='/home/sherelle/Documents/Stage5GI/implementation/Kaldi/kaldi-master/kaldi-master/egs/YembaEgraASR/data/segments'  # Remplace avec ton chemin vers le fichier segments
output_file = '/home/sherelle/Documents/Stage5GI/implementation/Kaldi/kaldi-master/kaldi-master/egs/YembaEgraASR/data/text'  # Remplace avec le chemin où tu veux créer le fichier text

text_file = '/home/sherelle/Documents/Stage5GI/implementation/Kaldi/kaldi-master/kaldi-master/egs/teste1/help_scripts/text'  # Remplace avec ton chemin vers le fichier text
read_text_segments(segments_file=segments_file, output_file=output_file, text_file=text_file)
"""
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <main_data> <projet_dir> <segments_file> <output_file>")
        sys.exit(1)

    segments_file = sys.argv[1]
    output_file = sys.argv[2]
    read_text_segments(text_file, segments_file, output_file)
"""