from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from vosk import Model, KaldiRecognizer
import soundfile as sf
import json
import numpy as np
import io

app = FastAPI(title="Kaldi HMM ASR API", version="1.0")  

# Charger le modèle Vosk (basé sur ton modèle HMM)
MODEL_PATH = "./model"
print(f"📦 Chargement du modèle depuis : le dossier ./model")
model = Model(MODEL_PATH)

@app.get("/")
def home():
    return {"message": "✅ Kaldi HMM ASR API en ligne avec Vosk !"}

@app.post("/asr")
async def asr(file: UploadFile = File(...)):
    """
    Endpoint principal : upload un fichier audio (.wav)
    et retourne la transcription texte.
    """
    try:
        # Lire le fichier audio
        data, samplerate = sf.read(io.BytesIO(await file.read()))
        if data.ndim > 1:
            data = np.mean(data, axis=1)  # Convertir stéréo → mono
        
        # Créer le reconnaisseur Kaldi/Vosk
        rec = KaldiRecognizer(model, samplerate)
        
        # Passer les données audio en float32 → bytes
        rec.AcceptWaveform(data.astype(np.float32).tobytes())
        
        result = json.loads(rec.FinalResult())
        return {"text": result.get("text", "")}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

