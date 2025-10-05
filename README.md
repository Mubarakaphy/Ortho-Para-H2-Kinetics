# Ortho–Para H₂ Kinetics

A minimal, reproducible **Python package** for modeling the equilibrium and relaxation dynamics of ortho–para hydrogen.

> **Why it matters:** The ortho/para spin isomer composition crucially affects low-temperature **hydrogen storage**, **cooling efficiency**, and **materials testing**.

<p align="center">
  <img src="figs/equilibrium.png" width="500" alt="Equilibrium fraction vs. temperature">
</p>

<p align="center">
  <img src="figs/relaxation_T20K.png" width="500" alt="Relaxation at 20 K">
</p>

---

## Model Overview

Compute:
- **Equilibrium ortho fraction** $f_\mathrm{ortho}^{eq}(T) $
- **First-order relaxation dynamics** $\dot f = -k (f - f_{eq}(T)) $

---

## Quick Start

### Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e . pytest
```

### Run scripts
```bash
python scripts/plot_equilibrium.py
python scripts/plot_relaxation.py
pytest -q
```

---

## Features
- Analytical equilibrium expression and relaxation ODE  
- Lightweight (no external data dependencies)  
- Reproducible plots and tests included  

---

📘 **License:** MIT  
🧠 **Author:** Mubarak A. S. Mohammed (GitHub: @Mubarakaphy)
