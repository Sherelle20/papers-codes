# Phase 1 — Fondations (Mois 1–3)

**Objectif** : maîtriser le signal audio, les architectures clés, et les paradigmes end-to-end.

## Contenu

```
01-audio-signal-processing/   STFT, mel spectrogramme, MFCC — implémentés à la main
02-transformer-conformer/     Architecture Transformer + bloc Conformer
03-e2e-paradigms/             CTC, RNN-Transducer, AED
04-paper-reproductions/       Whisper, wav2vec 2.0, HuBERT
05-deliverable-asr-pipeline/  Pipeline complet audio → features → Conformer → WER
```

## Ressources

- [HuggingFace Audio Course](https://huggingface.co/learn/audio-course)
- [Papier Whisper (Radford 2022)](https://arxiv.org/abs/2212.04356)
- [torchaudio docs](https://pytorch.org/audio/stable/index.html)
- [SpeechBrain](https://speechbrain.github.io)

## Livrable

Pipeline ASR complet en Python publié sur GitHub :
`chargement audio → features → Conformer fine-tuné → décodage → WER sur LibriSpeech`

---

# Phase 1 — Foundations (Months 1–3) *(English)*

**Goal**: master audio signal processing, key architectures, and end-to-end paradigms.

## Contents

```
01-audio-signal-processing/   STFT, mel spectrogram, MFCC — implemented from scratch
02-transformer-conformer/     Transformer architecture + Conformer block
03-e2e-paradigms/             CTC, RNN-Transducer, AED
04-paper-reproductions/       Whisper, wav2vec 2.0, HuBERT
05-deliverable-asr-pipeline/  Full pipeline: audio → features → Conformer → WER
```

## Resources

- [HuggingFace Audio Course](https://huggingface.co/learn/audio-course)
- [Whisper Paper (Radford 2022)](https://arxiv.org/abs/2212.04356)
- [torchaudio docs](https://pytorch.org/audio/stable/index.html)
- [SpeechBrain](https://speechbrain.github.io)

## Deliverable

Complete Python ASR pipeline published on GitHub:
`audio loading → features → fine-tuned Conformer → decoding → WER on LibriSpeech`
