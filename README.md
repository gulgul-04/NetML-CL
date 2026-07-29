# NetML-CL: Continual Learning for Cyber Threat Detection

This project implements an **Optimized Latent-Temporal Fusion Architecture** to detect Zero-Day cyber attacks in high-velocity network traffic without catastrophic forgetting. Built on the NetML-2020 dataset, the model dynamically learns new attack patterns while operating in real-time.

---

## 🧠 Project Architecture

The detection engine relies on three distinct AI frameworks working collaboratively to balance inference speed, accuracy, and continuous learning:

1. **Autoencoder (AE) - The Denoising Gate:** Compresses 121 raw flow features into a low-dimensional latent vector, stripping away background network noise and resolving the curse of dimensionality.
2. **1D-TCN + Attention - The Temporal Engine:** Replaces traditional BiLSTMs with a Temporal Convolutional Network. It uses dilated causal convolutions to process sequences of latent vectors in parallel, achieving microsecond-level latency while tracking the behavioral context of network flows.
3. **SF-SOINN - The Zero-Day Hunter:** A Soft-Forgetting Self-Organizing Incremental Neural Network. It uses geometric distance in the latent space to cluster unknown anomalies into distinct new attack families on the fly, without requiring computationally heavy backpropagation.

## 🔄 The Data Workflow

1. **Ingestion:** Statistical flow features (e.g., flow duration, byte counts) are extracted over a set time window.
2. **Compression:** The Autoencoder reduces the flow vector to a dense latent representation.
3. **Tracking:** The 1D-TCN analyzes the temporal sequence of these latent vectors.
4. **Routing:** 
   * If Softmax confidence is **> 50%**, the threat is instantly classified and blocked.
   * If Softmax confidence is **< 50%**, the traffic is flagged as an unknown anomaly and routed to the SF-SOINN.
5. **Evolution:** The SF-SOINN calculates the Euclidean distance of the anomaly. If it exceeds known thresholds, a new node is generated to represent the Zero-Day attack.

---

## 🛠️ Cloning and Setup

This repository is configured to work across Windows, Mac (Intel), and Mac (Apple Silicon).

### 1. Clone the Repository
```bash
git clone https://github.com/gulgul-04/NetML-CL
cd NetML-CL

## 2. Create and Activate the Virtual Environment

### For macOS and Linux

```bash
python3 -m venv netml_env
source netml_env/bin/activate
```

### For Windows (Command Prompt / PowerShell)

```dos
python -m venv netml_env
netml_env\Scripts\activate
```

---

## 3. Install Dependencies

Always upgrade `pip` first to ensure it can read modern package tags.

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ⚡ Hardware Acceleration Check (Crucial)

Because collaborators are using different hardware, the system must correctly route tensor operations to the appropriate backend (**CUDA**, **MPS**, or **CPU**).

Run the device check script:

```bash
python device_check.py
```

**Expected output:**

- **Windows (NVIDIA GPU):** `Using CUDA`
- **macOS (Apple Silicon M-Series):** `Using MPS (Metal Performance Shaders)`
- **macOS (Intel) or Windows (No GPU):** `Using CPU with X threads`

---

## 📁 Data Setup

Due to GitHub's size constraints, the NetML datasets (1.2M+ flows) are **not** hosted in this repository.

1. Download the datasets from the official NetML repository.
2. Place the `.json` or `.csv` files inside the `data/` folder at the root of this project.

> **Note:** The `data/` folder is git-ignored to prevent accidental uploads.