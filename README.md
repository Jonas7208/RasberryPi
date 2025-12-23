# RasberryPi Müll-Erkennungssystem 🗑️📷

Automatisches Müllerkennungssystem mit Raspberry Pi Kamera und TensorFlow Lite CNN. 

**Hybrid-System:** Nutzt Python 3.13 für die Kamera und Python 3.11 für TensorFlow Lite.

## ⚡ Quick Start

```bash
# 1. Repository klonen
git clone https://github.com/Jonas7208/RasberryPi.git
cd RasberryPi

# 2. Setup ausführen
./setup.sh

# 3. System testen
./run.sh
```

## 📋 Funktionen

- Erfasst Bilder mit der Raspberry Pi Kamera (Python 3.13)
- Klassifiziert Müll in 6 Kategorien mit CNN (Python 3.11):
  - Karton (cardboard)
  - Glas (glass)
  - Metall (metal)
  - Papier (paper)
  - Plastik (plastic)
  - Allgemeiner Müll (trash)

## 🤔 Warum Hybrid-System?

**Problem:** TensorFlow Lite Runtime unterstützt Python 3.13 nicht.

**Lösung:** 
- **Python 3.13** (System) → picamera2 für Kamera
- **Python 3.11** (venv) → TensorFlow Lite für CNN

## 🔧 Systemanforderungen

- Raspberry Pi mit Kamera Modul
- Raspberry Pi OS (Bookworm oder neuer)
- Python 3.13 (System)
- Python 3.11 (wird installiert)

## 📦 Manuelle Installation

### 1. Python 3.11 installieren

```bash
sudo apt update
sudo apt install python3.11 python3.11-venv
```

### 2. Kamera-Abhängigkeiten (Python 3.13)

```bash
sudo apt install libcamera-dev python3-libcamera python3-picamera2
```

### 3. Python 3.11 Virtual Environment

```bash
python3.11 -m venv ~/py311env
source ~/py311env/bin/activate
pip install tflite-runtime numpy pillow
deactivate
```

### 4. Test

```bash
# Kamera testen
python3 -c "from picamera2 import Picamera2; print('✓ OK')"

# TensorFlow Lite testen
~/py311env/bin/python -c "import tflite_runtime.interpreter; print('✓ OK')"
```

## 🚀 Verwendung

### Vollständiger Workflow (Bild aufnehmen + klassifizieren)

```bash
./run.sh
```

### Nur Bild aufnehmen

```bash
python3 capture.py
# oder mit eigenem Dateinamen:
python3 capture.py mein_bild.jpg
```

### Nur Bild klassifizieren

```bash
~/py311env/bin/python classify.py still_2025-12-16_15-30-00.jpg
```

## 📂 Projektstruktur

```
RasberryPi/
├── capture.py         # Bildaufnahme (Python 3.13)
├── classify.py        # CNN-Klassifizierung (Python 3.11)
├── run.sh            # Kombiniertes Script
├── setup.sh          # Automatische Installation
├── model.tflite      # Trainiertes CNN-Modell
├── CNN.py            # Legacy: Alte Version
├── Kamera.py         # Legacy: Alte Version
└── README.md         # Diese Datei
```

## 🔍 Technische Details

### Bildaufnahme (`capture.py`)
- **Python:** 3.13 (system)
- **Library:** picamera2
- **Output:** JPEG-Bilder mit Zeitstempel

### Klassifizierung (`classify.py`)
- **Python:** 3.11 (venv: `~/py311env`)
- **Framework:** TensorFlow Lite Runtime
- **Input:** 299x299 RGB Bilder
- **Preprocessing:** Normalisierung [0, 1]
- **Output:** Klasse + Konfidenz

### CNN-Modell
- **Format:** TensorFlow Lite (`.tflite`)
- **Input Shape:** (1, 299, 299, 3)
- **Output:** 6 Klassen
- **Größe:** ~24 MB

## ⚠️ Fehlerbehebung

### Kamera wird nicht erkannt

```bash
# Kamera aktivieren
sudo raspi-config  # Interface Options → Camera

# Testen
libcamera-hello
```

### `ModuleNotFoundError: No module named 'picamera2'`

```bash
# Für System-Python (3.13) installieren
sudo apt install python3-picamera2
```

### `ModuleNotFoundError: No module named 'tflite_runtime'`

```bash
# Im Python 3.11 venv installieren
source ~/py311env/bin/activate
pip install tflite-runtime
deactivate
```

### Python-Version prüfen

```bash
# System Python
python3 --version  # Sollte 3.13.x sein

# venv Python
~/py311env/bin/python --version  # Sollte 3.11.x sein
```

## 🎓 Jugend forscht Projekt

Dieses Projekt wurde für Jugend forscht 2026 entwickelt.

## 📄 Lizenz

Open Source - Jugend forscht Projekt

## 🤝 Beitragen

Pull Requests sind willkommen!

## 📧 Kontakt

GitHub: [@Jonas7208](https://github.com/Jonas7208)
