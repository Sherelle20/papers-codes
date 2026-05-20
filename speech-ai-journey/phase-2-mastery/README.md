# Phase 2 — Maîtrise technique (Mois 4–6)

**Objectif** : Speech-LLM, ASR streaming, diarisation, ASR multilingue.

## Contenu

```
01-speech-llm/              Intégration encodeur audio + LLM (projection layer, Q-Former)
02-streaming-asr/           Chunk-wise inference, lookahead context, latence/accuracy
03-diarization/             Speaker embeddings, clustering, joint ASR+diarization
04-multilingual/            Datasets multilingues, low-resource, transfer cross-lingual
05-deliverable-meeting-demo/ Démo web : upload réunion → diarisation + transcription → JSON
```

## Ressources

- [Whisper code](https://github.com/openai/whisper)
- [Common Voice 17](https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0)
- [pyannote-audio](https://github.com/pyannote/pyannote-audio)
- [JEDIS-LLM paper](https://arxiv.org/abs/2511.16046)

## Livrable

Démo web : `upload audio de réunion → diarisation + transcription en temps réel → export JSON structuré`

---

# Phase 2 — Technical Mastery (Months 4–6) *(English)*

**Goal**: Speech-LLM integration, streaming ASR, diarization, multilingual ASR.

## Contents

```
01-speech-llm/              Audio encoder + LLM integration (projection layer, Q-Former)
02-streaming-asr/           Chunk-wise inference, lookahead context, latency/accuracy trade-offs
03-diarization/             Speaker embeddings, clustering, joint ASR+diarization
04-multilingual/            Multilingual datasets, low-resource, cross-lingual transfer
05-deliverable-meeting-demo/ Web demo: upload meeting → diarization + transcription → JSON
```

## Resources

- [Whisper code](https://github.com/openai/whisper)
- [Common Voice 17](https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0)
- [pyannote-audio](https://github.com/pyannote/pyannote-audio)
- [JEDIS-LLM paper](https://arxiv.org/abs/2511.16046)

## Deliverable

Web demo: `upload meeting audio → real-time diarization + transcription → structured JSON export`
