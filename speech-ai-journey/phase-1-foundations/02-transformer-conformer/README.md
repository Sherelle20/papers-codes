# 02 — Transformer & Conformer

## Objectifs

- Implémenter un Transformer minimal en PyTorch (attention multi-têtes, positional encoding, layer norm)
- Comprendre le bloc Conformer : convolution + self-attention
- Comprendre pourquoi le Conformer surpasse le Transformer pur en ASR

## Concepts clés

| Concept | Description |
|---------|-------------|
| Multi-head attention | Parallélisation de l'attention sur plusieurs sous-espaces |
| Positional encoding | Injection de l'information de position dans l'encodeur |
| Conformer block | Feed-forward → Self-attention → Convolution → Feed-forward |
| Layer norm | Normalisation par couche — stabilise l'entraînement |

## Papiers de référence

- [Attention Is All You Need (Vaswani 2017)](https://arxiv.org/abs/1706.03762)
- [Conformer (Gulati 2020)](https://arxiv.org/abs/2005.08100)

---

# 02 — Transformer & Conformer *(English)*

## Goals

- Implement a minimal Transformer in PyTorch (multi-head attention, positional encoding, layer norm)
- Understand the Conformer block: convolution + self-attention
- Understand why the Conformer outperforms a pure Transformer in ASR

## Key Concepts

| Concept | Description |
|---------|-------------|
| Multi-head attention | Parallelizing attention over multiple sub-spaces |
| Positional encoding | Injecting position information into the encoder |
| Conformer block | Feed-forward → Self-attention → Convolution → Feed-forward |
| Layer norm | Layer normalization — stabilizes training |

## Reference Papers

- [Attention Is All You Need (Vaswani 2017)](https://arxiv.org/abs/1706.03762)
- [Conformer (Gulati 2020)](https://arxiv.org/abs/2005.08100)
