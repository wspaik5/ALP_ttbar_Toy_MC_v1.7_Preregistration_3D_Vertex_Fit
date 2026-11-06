# ALP-ttbar Toy MC v1.7 — Preregistration: Three-Dimensional Two-Hypothesis Vertex Fit (Adding the r–z Opening Angle) for Displaced Light ALP → e⁺e⁻

**Author:** Won Shik Paik (Independent Researcher, Auckland, New Zealand)
**Date frozen:** 2026-11-06 (this file is committed to GitHub before any v1.7 simulation or fit is run)
**Builds on:** v1.6, https://doi.org/10.5281/zenodo.23952888 (preregistration https://doi.org/10.5281/zenodo.23942338); v1.5, https://doi.org/10.5281/zenodo.23924862; toy study motivated by arXiv:2610.38932
**Zenodo (this preregistration, PDF):** https://doi.org/10.5281/zenodo.23995668
**GitHub:** https://github.com/wspaik5/ALP_ttbar_Toy_MC_v1.7_Preregistration_3D_Vertex_Fit
**Status:** plan only. No v1.7 outcome exists at the time of this commit.
**Amendment (2026-11-06, before any v1.7 simulation or fit):** variant V-allpixel (Sec. 3.2) and prediction P7 added;
the first commit of this repository contained the same text without them.
**PDF version:** same text plus two figures drawn only from analytic formulas and truth-level numbers of the
published v1.5 samples (no new simulation or fit).

---

## 0. Why v1.7

v1.5 and v1.6 used only the transverse (bending-plane) view. There, a free vertex absorbs a small ALP opening angle
Δφ by moving along the track, leaving a mismatch Δφ²/(2Δω) that is below the hit resolution at 17–50 MeV; and
bremsstrahlung, which changes the curvature, makes about 10% of conversions look opening-angle-like. Both v1.5 and v1.6
listed the r–z view as the main untested ingredient (first item of the v1.6 future directions).

In the r–z view the situation is different:

- **The field does not bend the tracks** in r–z: z = z_v + cotθ · s, a straight line in the transverse path length s.
- **A vertex shift cannot absorb a polar opening.** Two lines with different slopes cotθ₁ ≠ cotθ₂ leave from one point;
  a fit that forces them to be parallel cannot reproduce them by moving the vertex. The opening Δcotθ therefore enters
  the hits at first order, unlike Δφ in the transverse view.
- **Bremsstrahlung barely changes the polar angle**: the radiated photon removes energy, not direction.
- **Photon conversions have Δcotθ ≈ 0** (opening ≈ m_e/E), apart from multiple scattering.

Truth-level facts used for planning (published v1.5 samples, base selection, no fit): the median polar opening |Δθ| of
ALP pairs is 0.42 / 1.14 / 2.06 / 3.68 mrad at 17 / 50 / 100 / 200 MeV, and the fraction of pairs decaying at
r < 110 mm (at least two pixel layers with z measurement after the vertex) is 15.5% / 19.4% / 25.0% / 34.5%; for
conversions it is 14.8%. In the default geometry only pixel layers measure z, so most of the r–z information is
available only for vertices inside the pixel volume.

## 0a. Related work (prior art)

- **Using the r–z opening against conversions is standard.** Conversion reconstruction pairs tracks with a cut on
  Δcotθ, the opening in the r–z plane (e.g. the CMS conversion producer [B1]); low-mass dielectron analyses use the
  orientation of the opening relative to the field, φ_V [B2]. Three-dimensional vertex fitting is standard [B3].
- **Electron vs. muon displaced vertices** have been compared with a real detector (CMS, 8 TeV [B4]).
- **All-pixel trackers** are pursued by next-generation concepts such as ALICE 3 [B5] and the FCC-ee detectors [B6];
  V-allpixel only mimics the z coverage of such trackers in this toy and makes no statement about their performance.

What v1.7 adds is limited to this series: it quantifies, in the preregistered toy of v1.0–v1.6, how much the r–z
opening recovers the conversion-induced loss in reach for top-associated displaced ALP → e⁺e⁻. No claim of novelty for
the method is made.

## 1. Questions

- **Q1 (primary).** With the two-hypothesis selection extended to 3D, how large is the limit degradation from
  conversions at 17, 50, 100 and 200 MeV (cτ = 1 mm), compared with the transverse-only result on the same subsample
  (v1.6 config R: 127×, 68×, 28×, 8.2×)?
- **Q2.** How are Δχ²_L (r–z) and Δχ²_3D distributed for conversions and ALP pairs, and does bremsstrahlung leave the
  r–z test unaffected as expected?

## 2. Unchanged from v1.5/v1.6 (frozen)

- Transverse simulation and fits exactly as in v1.5/v1.6 config R (3.8 T, nominal material): the same samples, seeds,
  hits, H_conv (v1.4 fit (b)), H_ALP and Δχ²_T. The transverse part must reproduce v1.6 config R (Sec. 5).
- Statistics as in v1.6: first 100,000 base conversion pairs and first 60,000 base signal pairs per mass (whole chunks).
- Selection framework `scan_v15` (threshold k, veto width nσ, mass window), counting rule and metrics.

## 3. What is new (frozen)

**3.1 Longitudinal simulation.** Each track also gets z hits. The polar direction is propagated as a straight line in
s; at every material surface after the vertex the polar angle receives an independent Highland scattering kick with the
same θ₀ as the transverse kick; bremsstrahlung changes only the momentum (and thereby the transverse path, which is
taken from the transverse simulation). The longitudinal random numbers come from a **separate generator** (seeds
1031 for conversions, 1041 for signal), so the transverse hits are bit-for-bit those of v1.5/v1.6.

**3.2 z measurement.**
- Default: the four pixel layers (r = 29, 68, 109, 160 mm) measure z with σ_z = 25 µm; strip layers do not measure z.
- Variant **V-stereo** (secondary): in addition, stereo strip layers TIB 1–2 (255, 339 mm) measure z with 0.25 mm and
  TOB 1–2 (608, 692 mm) with 0.5 mm.
- Variant **V-allpixel** (secondary): all 14 layers measure z with σ_z = 25 µm (and r–φ as in the default). The
  material, the field and the transverse simulation are unchanged. This is a toy stand-in for an all-pixel tracker
  of the kind pursued by next-generation concepts [B5, B6]; it changes only where z is measured, not the material
  budget of such trackers, which v1.6 showed to matter separately.

**3.3 Longitudinal fit.** For each hypothesis, after its transverse fit, the transverse path lengths s from the
fitted vertex to each layer are computed along each fitted track. The r–z fit is then linear least squares:
- H_conv,L: z_v and one common slope c (tracks parallel in 3D);
- H_ALP,L: z_v, c₁, c₂.
The covariance includes the z resolution and the scattering of the polar angle (lever arms along s, true momentum, as
for the transverse term). Δχ²_L = χ²_conv,L − χ²_ALP,L is defined when each track has at least two z hits; otherwise
Δχ²_L = 0 (no r–z information).

**3.4 Test statistic.** Δχ²_3D = Δχ²_T + Δχ²_L.

**3.5 Regularity check and reference distributions (v1.6 future direction (vi)).**
- Δχ²_L: Δcotθ enters linearly, the null value 0 is inside the parameter space, the fit is linear → regular; reference
  **χ²₁** (Wilks).
- Δχ²_T: as diagnosed in v1.5, boundary case → reference **½χ²₀ + ½χ²₁**.
- Δχ²_3D: sum of the two independent parts → reference **½χ²₁ + ½χ²₂** (a Self–Liang-type mixture). Median 0.867,
  P(>3.84) = 9.8%, P(>9) = 0.69%.
These references are used only for validation; the selection threshold k is scanned as before.

## 4. Selection (frozen)

`scan_v17` = `scan_v15` with Δχ²_3D in place of Δχ² (k ∈ {none, 1, 2, 4, 9, 16, 25, 49}). k = none reproduces the
v1.6 config R degradation exactly. Reported side by side: Δχ²_T only (= v1.6 R), Δχ²_L only, Δχ²_3D; each with and
without mass window (V-nomass); and the V-stereo and V-allpixel variants for Δχ²_3D.

## 5. Sanity gate (frozen)

Before any degradation is computed, for every sample:
1. **Identity.** Transverse vertex radius and Δχ²_T equal v1.6 config R within 10⁻⁶ for ≥ 99.9% of pairs.
2. **Fit success** ≥ 95% (transverse and longitudinal).
3. **Linear fit.** Fraction with Δχ²_L < −10⁻⁶ ≤ 0.1% (nested linear least squares cannot be negative).

If the gate fails, the code is fixed, the failure and the fix are reported, and the gate is re-run.

## 6. Validation (independent samples only; criteria frozen)

- **Z1 (null, no brems).** The v1.3 V4 collinear sample (seed 404) with z hits (longitudinal seed 1404), zero opening in
  3D. Δχ²_L restricted to pairs with r–z information: median 0.30–0.65 and 3–8% above 3.84 (χ²₁). Δχ²_3D on the same
  pairs: median 0.60–1.15 and 6–14% above 3.84 (½χ²₁ + ½χ²₂).
- **Z2 (response, no brems).** Two 10 GeV tracks from a common vertex at r uniform in 30–100 mm, |η| < 1.0, Δφ = 0 and
  polar opening Δθ ∈ {0, 0.5, 1, 2} mrad (seed 808). The median Δχ²_L must increase monotonically with Δθ.
- **Z3 (propagation).** Without scattering, z hits agree with z_v + cotθ · s to better than 0.1 µm.

If a criterion fails, the code is fixed and the fix is reported.

## 7. Predictions (written before running)

Values are degradations with the Δχ²_3D selection, default z geometry, cτ = 1 mm, compared with v1.6 config R on the
same subsample (127×, 68×, 28×, 8.2×).

- **P1 (17 MeV, primary).** Between **100× and 127×**: a gain of at most about 20%, because the median polar opening
  (0.42 mrad) is comparable to the r–z resolution and only about 15% of pairs decay inside the pixel volume.
- **P2 (200 MeV, primary).** Between **3× and 7×**.
- **P3 (100 MeV).** Between **12× and 25×**.
- **P4 (bremsstrahlung, mechanism).** For conversions (r < 800 mm) with r–z information, the fraction with Δχ²_L > 9 is
  **≤ 1%**, i.e. bremsstrahlung does not fake an r–z opening (v1.5 transverse: 9.6% with Δχ²_T > 9).
- **P5 (ALP, mechanism).** Among ALP pairs with r–z information, the fraction with Δχ²_L > 9 is **5–25%** at 17 MeV and
  **≥ 60%** at 200 MeV.
- **P6 (V-stereo, secondary).** Adding stereo z improves the 200 MeV degradation by **at least 10%** relative to the
  default geometry.
- **P7 (V-allpixel, secondary).** With z measured at every layer, at least 95% of pairs have r–z information, and the
  17 MeV degradation is **at least 25% lower** than with the default geometry, but **still above 20×**: the r–z
  opening becomes available for vertices outside the pixel volume, while multiple scattering (about 0.1–0.3 mrad per
  layer at 10 GeV, comparable to the 0.42 mrad median opening) and the conversion yield remain.

Each prediction is reported as confirmed or refuted against these statements. Refuted predictions are not re-framed.

## 8. Reporting

v1.7 note with a Figure 11: (a) Δχ²_L distributions for conversions and ALP pairs with the χ²₁ reference; (b)
degradation versus mass for Δχ²_T only, Δχ²_L only, Δχ²_3D, V-stereo and V-allpixel, with the no-brems bound; (c) the fraction of
pairs with r–z information and with Δχ²_L > 9 versus vertex radius. The note contains the Z1–Z3 validation, the
prediction table, "Deviations from preregistration", "Limitations" and "Future directions" (Gaussian-sum filter on top
of the 3D fit; dimuon control study; and, depending on the V-allpixel result, geometry studies such as a first layer
closer to the beam and an all-pixel tracker with reduced material, combining the v1.6 material result with full z
coverage).

## 9. Limitations known in advance

- All v1.0–v1.6 limitations apply (barrel only, idealised layers, no pattern recognition, toy material map, crude
  counting rule, selection optimised on the same samples, truth used for the material list and the scattering momentum,
  single-Gaussian bremsstrahlung model).
- The 3D fit is sequential (transverse first, then r–z with the transverse path lengths), not a joint 3D fit.
- The z resolution is a single number per layer type; cluster shapes, Lorentz drift and pixel-size effects are ignored.
- The pair mass is still generated independently of the hits (see V-nomass).
- Subsampled statistics; only trends and ratios are meaningful. No statement about real detectors is made.

[B1] CMS Collaboration, conversion producer (CMSSW `RecoEgamma/EgammaPhotonProducers`, parameter `DeltaCotTheta`); see
also CMS Collaboration, Performance of photon reconstruction and identification with the CMS detector at √s = 8 TeV,
JINST 10 (2015) P08010, arXiv:1502.02702.
[B2] ALICE Collaboration, Dielectron production in proton-proton collisions at √s = 7 TeV, arXiv:1805.04391.
[B3] R. Frühwirth, Application of Kalman filtering to track and vertex fitting, Nucl. Instrum. Meth. A 262 (1987) 444.
[B4] CMS Collaboration, Search for long-lived particles that decay into final states containing two electrons or two
muons in proton-proton collisions at √s = 8 TeV, Phys. Rev. D 91 (2015) 052012, arXiv:1411.6977.
[B5] ALICE Collaboration, Letter of intent for ALICE 3, arXiv:2211.02491.
[B6] N. Bacchetta et al., CLD – A Detector Concept for the FCC-ee, arXiv:1911.12230; The IDEA detector concept for
FCC-ee, arXiv:2502.21223.
