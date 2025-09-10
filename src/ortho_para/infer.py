import numpy as np
from scipy.optimize import curve_fit
from .physics import f_ortho_eq

def _relaxation_model(t, k, T, f0):
    """Analytic solution of df/dt = -k (f - f_eq(T))."""
    t = np.asarray(t, dtype=float)
    f_eq = f_ortho_eq(T)
    return f_eq + (f0 - f_eq) * np.exp(-k * t)

def fit_k(t_s, f_obs, T, f0, k0=1e-3):
    """
    Estimate k (s^-1) from time series (t_s, f_obs) at temperature T and initial fraction f0.
    Returns (k_hat, k_std).
    """
    t_s = np.asarray(t_s, dtype=float)
    f_obs = np.asarray(f_obs, dtype=float)

    def _model(tt, kk):
        return relaxation_model(tt, kk, T, f0)

    (k_hat,), pcov = curve_fit(
        _model, t_s, f_obs, p0=[k0], bounds=(0, np.inf), maxfev=20000
    )
    k_std = float(np.sqrt(pcov[0, 0])) if pcov.size else np.nan
    return float(k_hat), k_std
