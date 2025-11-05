# 🛰️ Sentinel-AI: Covert Micro-Signature Anti-Drone System (C-MSADS)

A **Proof of Concept (PoC)** built to demonstrate how AI and sensor fusion can help detect drones safely and ethically.  
Developed as a **school research project** by *Eeshaan*.

---

## 🧠 Overview
**Sentinel-AI** combines inputs from multiple sensors — camera, RF receiver, and simulated radar — and uses a small AI model to decide whether a drone might be nearby.

This repository contains the PoC code, documentation, and dataset examples for educational replication.

---

## ⚙️ Features
- ✅ Sensor fusion (optical + RF + simulated radar)
- 🤖 AI classification with Random Forest
- 💡 Python-based simulation
- 🧾 Logging and testing modules
- 📡 MQTT / console alert output

---

## 🧰 Quick Start

```bash
git clone https://github.com/<your-username>/Sentinel-AI-CMSADS.git
cd Sentinel-AI-CMSADS
pip install -r requirements.txt
python sentinel_poc_node.py
 **<2 seconds**
- Deliver alerts through console and MQTT topic
- Log “neutralization” as a **software-only simulation**

---

##  Components & Requirements
**Hardware (optional):**
- Raspberry Pi 4/5 or Jetson Nano  
- mmWave radar module / HB100  
- RTL-SDR (receive-only)  
- Pi Camera / LDR  
- PIR / MLX90640 (thermal)

**Software:**
- Python 3.9+
- `numpy`, `scikit-learn`, `joblib`, `paho-mqtt`, `flask` (optional)

Install dependencies:
```bash
pip install -r requirements.txt
