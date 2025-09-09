#!/usr/bin/env python
import os
from ortho_para.plots import plot_equilibrium_curve
os.makedirs("figs", exist_ok=True)
plot_equilibrium_curve(show=True, save="figs/equilibrium.png")
print("Saved figs/equilibrium.png")
