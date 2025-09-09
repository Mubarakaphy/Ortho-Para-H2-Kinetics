import numpy as np
from ortho_para.physics import f_ortho_eq

def test_high_T_limit():
    # High-T limit approaches 3/4
    assert np.isclose(f_ortho_eq(1e9), 0.75, rtol=1e-3, atol=1e-3)

def test_low_T_limit():
    # Low-T limit near 0 (para dominates)
    assert f_ortho_eq(2.0) < 0.05
