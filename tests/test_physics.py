import numpy as np
from ortho_para.physics import f_ortho_eq
from ortho_para.infer import fit_k

def test_high_T_limit():
    # High-T limit approaches 3/4
    assert np.isclose(f_ortho_eq(1e9), 0.75, rtol=1e-3, atol=1e-3)

def test_low_T_limit():
    # Low-T limit near 0 (para dominates)
    assert f_ortho_eq(2.0) < 0.05

def test_fit_k_recovery():
    T = 20.0
    k_true = 1e-3
    f0 = 0.75
    t = np.linspace(0.0, 3600.0, 60)
    feq = f_ortho_eq(T)
    f = feq + (f0 - feq) * np.exp(-k_true * t)
    k_hat, k_std = fit_k(t, f, T, f0, k0=1e-4)
    assert abs(k_hat - k_true) / k_true < 0.05
