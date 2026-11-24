---
internal_title: SUREWAVE integrated modelling toolchain — one-page infographic
documentclass: extarticle
fontsize: 10pt
mainfont: TeX Gyre Heros
geometry: "a4paper,top=11mm,bottom=10mm,left=14mm,right=14mm"
colorlinks: true
---

```{=latex}
\begin{minipage}[c]{0.21\linewidth}
\includegraphics[width=\linewidth]{../images/surewave_logo.png}
\end{minipage}\hfill
\begin{minipage}[c]{0.76\linewidth}\raggedleft
{\fontsize{17}{20}\selectfont\bfseries\color{swdark} SUREWAVE integrated modelling toolchain}\\[0.3em]
{\fontsize{10.5}{13}\selectfont\color{swteal} From site wind and waves to the condition of a concrete breakwater\\that protects offshore floating PV}
\end{minipage}

\vspace{0.3em}\swrule\vspace{0.2em}
```

Floating PV at exposed offshore sites needs shelter from waves. In SUREWAVE a floating concrete breakwater provides it, and the breakwater itself has to last for decades at sea. The project partners built a chain of linked models that carries a site's wind and wave conditions through to loads, stresses, fatigue cracking and corrosion in the breakwater, as a basis for designing it, predicting its remaining life and planning inspections.

```{=latex}
\begin{center}
\input{2026-11-22_surewave_modelling_toolchain_figure.tikz.tex}

\vspace{0.15em}
{\small\color{swgrey}\itshape Schematic of the workflow: boxes are the project's tools, arrows show data flow, partners are named under each box.}
\end{center}
\vspace{0.1em}
```

# The tools and where they are reported

```{=latex}
\raggedright
```

- \textcolor{swdark}{Site conditions and load cases:} three sea sites, 25 years of ERA5 hindcast. SINTEF\ (D2.1), Sunlit\ Sea\ (D2.3).
- \textcolor{swdark}{Coupled aero-hydrodynamics:} diffraction and time-domain models of floats, breakwater and moorings; CFD for damping and wind loads. MARIN,\ SINTEF\ (D5.1).
- \textcolor{swdark}{Mooring optimisation:} up to 56\ % lower mooring mass in selected cases, without exceeding proof loads. MARIN\ (D5.1).
- \textcolor{swdark}{Structural finite-element assessment:} global model and submodels locate the most loaded parts. Ceit\ (D5.3).
- \textcolor{swdark}{Fatigue crack propagation:} new stress-intensity-factor solutions for cracks in rebar. Ceit\ (D5.5).
- \textcolor{swdark}{Concrete property prediction:} machine learning to screen circular concrete mixes. SINTEF\ (D5.2).
- \textcolor{swdark}{Corrosion monitoring:} eddy-current sensor for embedded rebar, tested in the lab and on the prototype at sea. Ceit\ (D5.4).
- \textcolor{swdark}{Structural Health Management System:} condition, remaining life and inspection intervals. Ceit\ (D5.6).
- \textcolor{swdark}{Validation:} against ABS and DNV guidance, concrete tests, published fracture-mechanics results, towing-tank and wave-basin tests. Ceit\ (D5.7), MARIN\ (D5.1,\ D6.2).

# Read more

Project website: [surewave.eu](https://surewave.eu) · Public deliverables and publications: [zenodo.org/communities/surewave](https://zenodo.org/communities/surewave)

Partners: SINTEF (coordinator), MARIN, Ceit, ACCIONA, Clement Germany, IFEU and Sunlit Sea.

```{=latex}
\vfill
{\color{swlight}\rule{\linewidth}{0.6pt}}\\[0.3em]
\begin{minipage}[c]{0.34\linewidth}
\includegraphics[width=\linewidth]{../images/eu_funded_by_lockup.jpg}
\end{minipage}\hfill
\begin{minipage}[c]{0.62\linewidth}\raggedright
{\footnotesize\color{swgrey} SUREWAVE has received funding from the European Union's Horizon Europe programme under grant agreement No 101083342. Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Climate, Infrastructure and Environment Executive Agency (CINEA). Neither the European Union nor the granting authority can be held responsible for them.}
\end{minipage}
```
