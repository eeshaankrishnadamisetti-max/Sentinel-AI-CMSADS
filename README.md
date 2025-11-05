# 🛰️ Sentinel-AI: Covert Micro-Signature Anti-Drone System (C-MSADS)

A Proof of Concept (PoC) project built to demonstrate **drone detection using sensor fusion** — combining radar micro-signatures, RF cues, optical triggers, and IR/thermal inputs.

This repository contains all files, scripts, and documentation required to **replicate or extend** the Sentinel-AI PoC in a safe, simulation-only environment.

---

## 🎯 Purpose
The goal of C-MSADS is to validate the idea of a **low-cost, edge-based detection node** that can:
- Fuse data from multiple sensors
- Detect small UAVs in near real time
- Log and simulate a neutralization response — **without any actual RF transmission**

This project is built only for **educational and research purposes.**

---

## ⚙️ Objectives
- Achieve reliable sensor fusion on a single node (PoC)
- Detect simulated drones within **<2 seconds**
- Deliver alerts through console and MQTT topic
- Log “neutralization” as a **software-only simulation**

---

## 🧩 Components & Requirements
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
