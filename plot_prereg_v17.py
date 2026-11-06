"""v1.7 preregistration figures. NO simulation or fit: analytic formulas and truth-level quantities of the published
v1.5 samples only (run from a directory containing the v1.5 code: run_v13.py, bkg.py, mag.py)."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import chi2

# ---------------- Figure P1: first- vs second-order visibility and reference distributions (analytic)
fig, ax = plt.subplots(1, 2, figsize=(11, 4.0))
PT, B, s = 10.0, 3.8, 80.0                       # GeV per leg, T, mm of lever arm after the vertex
dw = 2 * 0.3 * B / 1000 / PT
ang = np.logspace(-1, np.log10(20), 200) * 1e-3
ax[0].plot(ang * 1e3, ang**2 / (2 * dw) * 1e3, 'C3-', label=r'transverse: $\Delta\phi^2/(2\Delta\omega)$ (absorbed at 1st order)')
ax[0].plot(ang * 1e3, ang * s * 1e3, 'C0-', label=r'r–z: $\Delta\theta\cdot s$, $s$ = 80 mm (not absorbable)')
ax[0].axhline(15, c='gray', ls=':', lw=1); ax[0].text(3, 9, '15 µm (r-φ) pixel', color='gray', fontsize=7)
ax[0].axhline(25, c='gray', ls='--', lw=1); ax[0].text(3, 30, '25 µm (z) pixel', color='gray', fontsize=7)
ax[0].set_xscale('log'); ax[0].set_yscale('log'); ax[0].set_ylim(0.02, 3e4)
ax[0].set_xlabel('opening angle [mrad]'); ax[0].set_ylabel('hit displacement left for the fit [µm]')
ax[0].legend(fontsize=7, loc='upper left'); ax[0].set_title('(a) why the r–z opening is visible (3.8 T, 10 GeV)', fontsize=10)
k = np.logspace(-3, 1.4, 300)
ax[1].plot(k, chi2.sf(k, 1), 'C0-', label=r'$\chi^2_1$: $\Delta\chi^2_L$ (regular)')
ax[1].plot(k, 0.5 * chi2.sf(k, 1), 'C3--', label=r'$\frac{1}{2}\chi^2_0+\frac{1}{2}\chi^2_1$: $\Delta\chi^2_T$ (boundary, v1.5)')
ax[1].plot(k, 0.5 * chi2.sf(k, 1) + 0.5 * chi2.sf(k, 2), 'k:', lw=2, label=r'$\frac{1}{2}\chi^2_1+\frac{1}{2}\chi^2_2$: $\Delta\chi^2_{3D}$')
ax[1].set_xscale('log'); ax[1].set_yscale('log'); ax[1].set_ylim(1e-3, 1.2)
ax[1].set_xlabel('threshold k'); ax[1].set_ylabel(r'P($\Delta\chi^2$ > k) under the null')
ax[1].legend(fontsize=7, loc='lower left'); ax[1].set_title('(b) preregistered reference distributions', fontsize=10)
fig.suptitle('Fig. P1 (analytic, no simulation)', fontsize=9.5)
plt.tight_layout(); plt.savefig('figP1_rz_visibility_and_references.png', dpi=160)

# ---------------- Figure P2: truth-level planning numbers from the published v1.5 samples
from run_v13 import conversions_truth, signal_truth
fig, ax = plt.subplots(1, 2, figsize=(11, 4.0))
bins = np.logspace(-2, 1.5, 60)
for m, c in zip((0.017, 0.05, 0.1, 0.2), ('C0', 'C1', 'C2', 'C3')):
    S = signal_truth(m, 1.0); b = S['base']; e1, e2 = S['e1'][b], S['e2'][b]
    th1 = np.arctan2(np.hypot(e1[:, 0], e1[:, 1]), e1[:, 2]); th2 = np.arctan2(np.hypot(e2[:, 0], e2[:, 1]), e2[:, 2])
    d = np.abs(th1 - th2) * 1e3
    ds = np.sort(d); ax[0].plot(ds, np.arange(1, len(ds) + 1) / len(ds), c=c,
               label=f'{m*1000:.0f} MeV (median {np.median(d):.2f} mrad)')
    r = np.sort(S['r'][b]); ax[1].plot(r, np.arange(1, len(r) + 1) / len(r), c=c, label=f'ALP {m*1000:.0f} MeV')
C = conversions_truth(); r = np.sort(C['r'][C['base']])
ax[1].plot(r, np.arange(1, len(r) + 1) / len(r), 'k-', lw=2, label='conversions')
ax[0].set_xscale('log'); ax[0].set_xlim(1e-2, 30); ax[0].set_xlabel(r'true polar opening $|\Delta\theta|$ [mrad]'); ax[0].set_ylabel('cumulative fraction (base selection)')
ax[0].legend(fontsize=7); ax[0].set_title('(a) polar opening of ALP pairs (truth)', fontsize=10)
for x in (29, 68, 109, 160):
    ax[1].axvline(x, c='gray', lw=0.6, alpha=0.6)
ax[1].axvspan(0, 110, color='C0', alpha=0.08); ax[1].text(15, 0.9, 'r–z information\n(≥ 2 pixel z hits)', fontsize=7)
ax[1].set_xscale('log'); ax[1].set_xlim(3, 900); ax[1].set_xlabel('true vertex radius [mm]')
ax[1].set_ylabel('cumulative fraction (base selection)'); ax[1].legend(fontsize=7, loc='lower right')
ax[1].set_title('(b) where the pairs decay (truth)', fontsize=10)
fig.suptitle('Fig. P2 (truth-level numbers of the published v1.5 samples; no v1.7 simulation or fit)', fontsize=9.5)
plt.tight_layout(); plt.savefig('figP2_truth_planning.png', dpi=160)
print('ok')
