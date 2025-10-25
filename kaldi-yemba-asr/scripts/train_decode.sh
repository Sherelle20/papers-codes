#!/bin/bash

# ================================
# Script pour l'entraînement et le décodage de modèles ASR
# ================================

# Définir le nombre de jobs parallèles et la commande de traitement
nj=20
cmd="run.pl"

# Fonction pour afficher un message
print_msg() {
    echo "================================="
    echo "$1"
    echo "================================="
}

# Vérification des erreurs après chaque commande
check_error() {
    if [ $? -ne 0 ]; then
        echo "Erreur détectée : $1"
        exit 1
    fi
}

# Étape 1 : Entraînement du modèle monophone
print_msg "Entraînement du modèle monophone"
steps/train_mono.sh --boost-silence 1.25 --nj $nj --cmd "$cmd" data/train data/lang exp/mono
check_error "Échec de l'entraînement du modèle monophone"

# Étape 2 : Alignement monophone
print_msg "Alignement du modèle monophone"
steps/align_si.sh --boost-silence 1.25 --nj $nj --cmd "$cmd" data/train data/lang exp/mono exp/mono_ali
check_error "Échec de l'alignement monophone"



# Étape 11 : Création des graphes de décodage et décodage tri_delta tri_delta_delta tri_lda_mllt tri_sat
for model in mono ; do 
    print_msg "Création du graphe et décodage pour le modèle $model"
    utils/mkgraph.sh data/lang_test exp/$model exp/$model/graph
    check_error "Échec de la création du graphe pour $model"
    
    steps/decode.sh --nj 5 --cmd "$cmd" exp/$model/graph data/test exp/$model/decode_test
    check_error "Échec du décodage pour $model"
done

# Étape 12 : Évaluation des résultats (WER)
print_msg "Évaluation des résultats"
for x in exp/*/decode*; do
    if [ -d $x ]; then
        grep WER $x/wer_* | utils/best_wer.sh
        check_error "Échec de l'évaluation pour $x"
    fi
done

print_msg "Processus terminé avec succès !"
