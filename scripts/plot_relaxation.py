#!/usr/bin/env python
import os
from ortho_para.plots import plot_relaxation
os.makedirs("figs", exist_ok=True)
plot_relaxation(T=20.0, show=True, save="figs/relaxation_T20K.png")
print("Saved figs/relaxation_T20K.png")
