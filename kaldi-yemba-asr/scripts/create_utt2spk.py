"""
utt2spk file
"""
def read_text_segments(segments_file, output_file):
    # Lecture du fichier segments
    with open(segments_file, 'r', encoding='utf-8') as segments_f:
        lines_segments = segments_f.readlines()

    # Liste pour stocker les tuples (segment_id, spkr_id)
    segments_data = []

    for segment_line in lines_segments:
        parts = segment_line.strip().split(' ')
        if len(parts) >= 1:
            segment_id = parts[0]
            spkr_id = segment_id.split('_')[0]  # Extrait l'identifiant de speaker
            segments_data.append((spkr_id, segment_id))

    # Tri des segments par spkr_id
    segments_data.sort(key=lambda x: x[0])

    # Ouverture du fichier de sortie
    with open(output_file, 'w', encoding='utf-8') as output_f:
        for spkr_id, segment_id in segments_data:
            output_line = f"{segment_id} {spkr_id}\n"
            output_f.write(output_line)
            print(f"Added to {output_file}: {output_line.strip()}")

projet_dir = 'kaldi-master/kaldi-master/egs/YembaEgraASR/'


# Exemple d'utilisation
segments_file =projet_dir+'data/segments'  # Remplace avec ton chemin vers le fichier segments
output_file = projet_dir + 'data/utt2spk'  # Remplace avec le chemin où tu veux créer le fichier utt2spk

read_text_segments(segments_file, output_file)
