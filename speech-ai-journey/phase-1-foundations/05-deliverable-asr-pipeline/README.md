# Livrable Phase 1 — Pipeline ASR complet

Pipeline end-to-end : `audio → features → Conformer fine-tuné → décodage → WER`

## Dataset

[LibriSpeech clean-100](https://www.openslr.org/12) — 100h d'anglais lu, qualité studio.

## Architecture

```
Audio (.wav / .flac)
    ↓ torchaudio
Mel spectrogramme (80 bins, 25ms window, 10ms hop)
    ↓
Conformer encoder (N layers)
    ↓
CTC decoder
    ↓
Texte prédit → calcul WER
```

## Utilisation

```bash
# Installation
pip install -r requirements.txt

# Entraînement
python src/train.py --config configs/conformer_ctc.yaml

# Évaluation
python src/eval.py --checkpoint checkpoints/best.pt --split test-clean
```

## Résultats

| Modèle | Dataset | WER |
|--------|---------|-----|
| Baseline Whisper-small | LibriSpeech test-clean | — |
| Conformer-CTC (le mien) | LibriSpeech test-clean | — |

## Structure

```
src/          code source (modèle, dataloader, training loop)
tests/        tests unitaires
data/samples/ quelques fichiers audio d'exemple
configs/      hyperparamètres YAML
checkpoints/  modèles sauvegardés (gitignored)
```

---

# Phase 1 Deliverable — Full ASR Pipeline *(English)*

End-to-end pipeline: `audio → features → fine-tuned Conformer → decoding → WER`

## Dataset

[LibriSpeech clean-100](https://www.openslr.org/12) — 100 hours of read English, studio quality.

## Architecture

```
Audio (.wav / .flac)
    ↓ torchaudio
Mel spectrogram (80 bins, 25ms window, 10ms hop)
    ↓
Conformer encoder (N layers)
    ↓
CTC decoder
    ↓
Predicted text → WER computation
```

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Training
python src/train.py --config configs/conformer_ctc.yaml

# Evaluation
python src/eval.py --checkpoint checkpoints/best.pt --split test-clean
```

## Results

| Model | Dataset | WER |
|-------|---------|-----|
| Baseline Whisper-small | LibriSpeech test-clean | — |
| Conformer-CTC (mine) | LibriSpeech test-clean | — |

## Structure

```
src/          source code (model, dataloader, training loop)
tests/        unit tests
data/samples/ a few sample audio files
configs/      YAML hyperparameters
checkpoints/  saved models (gitignored)
```
