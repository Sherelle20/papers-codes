# 01 — Traitement du signal audio

## Objectifs

- Comprendre et implémenter STFT, mel spectrogramme, MFCC en Python
- Visualiser les représentations sur de vrais fichiers audio
- Comparer librosa vs torchaudio

## Contenu

- `notebooks/` — exploration interactive (Jupyter)
- `scripts/` — versions Python pures, réutilisables

## Concepts clés

| Concept | Description |
|---------|-------------|
| STFT | Short-Time Fourier Transform — transforme le signal temporel en fréquences |
| Mel spectrogramme | STFT sur échelle mel (perceptive) — entrée standard des modèles ASR |
| MFCC | Mel-Frequency Cepstral Coefficients — représentation compacte du spectre |
| SpecAugment | Augmentation : masquage fréquences/temps |

---

# 01 — Audio Signal Processing *(English)*

## Goals

- Understand and implement STFT, mel spectrogram, MFCC in Python
- Visualize representations on real audio files
- Compare librosa vs torchaudio

## Contents

- `notebooks/` — interactive exploration (Jupyter)
- `scripts/` — reusable pure Python implementations

## Key Concepts

| Concept | Description |
|---------|-------------|
| STFT | Short-Time Fourier Transform — converts time-domain signal to frequency domain |
| Mel spectrogram | STFT on mel scale (perceptual) — standard input for ASR models |
| MFCC | Mel-Frequency Cepstral Coefficients — compact spectral representation |
| SpecAugment | Data augmentation: frequency and time masking |
