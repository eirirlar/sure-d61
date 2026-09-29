# Hydrodynamic Simulations of a 2MW Offshore Solar Farm with Floating Breakwater Protection

Tim Bunnik, Naman Baderiya and Joep van der Zanden

Maritime Research Institute Netherlands (MARIN), 6708 PM Wageningen, The Netherlands. Correspondence: j.v.d.zanden@marin.nl

Published in *Energies* 2026, 19, 1609. https://doi.org/10.3390/en19071609. Received 27 February 2026; revised 13 March 2026; accepted 23 March 2026; published 25 March 2026. Academic Editors: Wilfried Van Sark, Santiago Silvestre and Sara Mirbagheri Golroodbari. © 2026 by the authors, licensee MDPI, Basel, Switzerland. Open access under Creative Commons Attribution (CC BY) license.

## Abstract

Following successful applications in inland water bodies, floating photovoltaics (FPV) developers are now targeting offshore sites. This advancement requires numerical tools that can quantify the hydrodynamic performance of large-scale FPV farms. The existing wave-diffraction solver DIFFRAC was extended to simulate the response of a large number of interconnected floating objects on a supercomputer. The applicability is demonstrated by simulating a 2 MWp offshore solar farm, consisting of 3660 FPV modules moored inside a protective ring of 32 interconnected floating breakwaters (FBWs). The FPV motions and loads on FPV connectors in regular and irregular waves are compared to a reference case without FBW protection. Results show an average reduction in axial FPV connector loads in the setup with FBW ring, but local load enhancements occur due to dynamic amplifications of horizontal FPV module motions. Vertical loads and overturning moments onto FPV connectors are globally reduced by up to 50% in steep irregular seas but are locally enhanced due to standing waves that develop inside the ring. The insights of the hydrodynamic behaviour lead to recommendations for improving the farm configuration to further reduce fatigue and survival loads onto FPV modules and connectors.
Keywords: floating PV; solar energy; floating breakwater; hydrodynamic analysis; linear diffraction; high-performance computing; very large floating structure (VLFS); offshore renewable energy.

## 1. Introduction
Floating PhotoVoltaics (FPV) is gaining increasing attention due to the growth in energy demand, the phasing-out of fossil fuels to limit climate change and the need for a diverse energy mix to ensure a stable energy supply. FPV systems have been widely installed on inland water bodies such as reservoirs and lakes [1–3]. Companies are now targeting offshore waters where space is more abundant and where the integration with wind parks can offer significant economic benefits [4,5]. Several review studies have addressed recent advances and key issues for offshore solar [2,6–8], stating the long-term survivability in harsh environments as a main challenge.
A good understanding of the hydrodynamic behaviour of an FPV design is essential to assess the structural and mooring integrity and to quantify power losses [8–10]. FPV designers have adopted different strategies to survive in offshore conditions. Designs can be classified based on the PV position (directly at waterline or elevated) and on the elastic properties of a single FPV floater (rigid or flexible) [7]. Rigid FPV floaters are typically modular and interconnected, forming a very large floating structure (VLFS) whose elasticity is governed by the stiffness of the connectors. For such modular FPV concepts—the topic

of the present study—a careful assessment of the hydrodynamic loads on the connectors is required, since they are prone to fatigue and survival damage [8].
The hydrodynamic design performance can be studied numerically or experimentally (through scaled model testing in a wave basin). The complex mechanical couplings between modules and the large number of modules/degrees of freedom in the system make it practically infeasible to perform scale model tests for an entire farm. Therefore, the design performance has to be evaluated using a combination of (1) basin tests on a down-sized simplified version of the system; (2) numerical model validation using basin tests; (3) numerical simulations on the complete system using the validated model.
Researchers have developed different numerical approaches for simulating the waveinduced FPV loads and motions. For modular interconnected FPV designs, these numerical approaches can be categorized depending on the treatment of the modules (single- versus multi-body).
A single-body approach computes the global response of a modular array by treating it as a single element with flexible properties (e.g., thin plate or beam element) with a stiffness equivalent to that of the global connector layout [11–13]. This approach copies hydro-elastic methods developed for continuous flexible (membrane-type) FPV designs (e.g., [14–16]) and other VLFSs [17]. While the approach is computationally efficient and allows simulations for large arrays (>1000 PV modules), it requires simplifications and assumptions on the uniformity of elastic properties [13].
In a multi-body (piece-wise flexible) approach, FPV modules are treated as individual rigid elements and the connectors are modelled as numerical stiffness joints [18–20]. This offers the advantage that few assumptions are made on the geometric, mass and elastic properties of modules and connectors. The hydrodynamic interaction between FPV modules should be considered when computing the wave-exciting forces, added mass and damping on each body through linear wave diffraction [18]. A better representation of non-linear effects, for instance due to mooring lines, can be achieved through time domain [18,21], smoothed particle hydrodynamics (SPH) [22] or computational fluid dynamics (CFD) [23] simulations, but the high computational costs make these models less suitable for large farms.
Past studies on modular FPV farms have shown that the global hydro-elastic response is governed by the normalized array length to wavelength and the module length to wavelength, in combination with the natural frequencies of an array [19,24]. Vertical (heave) and rotational (pitch) motions of FPV modules typically vary across an array, depending on shielding properties by the fore floater and viscous energy losses [20,24]. For waves much longer than the length of a floater, shielding within an array is minor and the FPV modules are expected to follow the water surface in terms of both heave and pitch [25–27]. Coupled horizontal array motions and axial loads can be predicted analytically for head waves, provided that the axial connector stiffness is high and dynamic amplification can be neglected [19]. In this case, axial connector loads scale to floater draft, width, and wave amplitude. The number of FPV modules does not affect the maximum connector loads, but it does govern the number of horizontal mode shapes and thus affects the locations of the most loaded connectors [19].
Notwithstanding these relevant insights, some topics have yet remained unexplored. Predominantly, past studies have focused on small scale farms (up to tens of floaters), mostly in an academic context (i.e., wave flume setups with head waves only). The FPV sector requires numerical tools for simulating much larger farms to support their upscaling ambitions [18]. Moreover, there is a need for insights from assessments of realistic FPV designs including (surface) mooring arrangements [28].

This paper aims to extend insights into the hydrodynamic performance of large offshore solar farms (>1000 FPV modules) through numerical simulations of a conceptual 2 MWp FPV farm with floating breakwater protection (introduced in Section 2). A potential flow code (DIFFRAC), validated for a small FPV array, is improved to enable simulations of a large number of bodies on a high-performance computer (methods described in Section 3) and is validated using basin tests of a down-sized version of the FPV farm (Section 4). Section 5 presents the global FPV response and connector loads of the 2 MWp farm and assesses the effectiveness of the floating breakwaters. Section 6 discusses the numerical approach and presents recommendations for design improvement and further research, followed by the study’s conclusions in Section 7.
## 2. Design of the Conceptual 2 MWp FPV Farm
### 2.1. Sign Convention
Throughout this study, a right-handed coordinate system is used, consistent with [27]. The origin of the global coordinate system is located in the centre of the farm and at waterline. Motions are defined in the body-fixed system (at centre of gravity, CoG). Translations into longitudinal (x), transverse (y) and vertical (z) directions are termed surge, sway, and heave. Rotations around the x, y, and z axes are termed roll (ϕ), pitch (θ), and yaw (ψ).
### 2.2. Global Design of 2 MWp Farm
The present study is part of the Horizon Europe project SUREWAVE that aims to upscale FPV for offshore environments. Within this project, a conceptual design for a 2 MWp FPV farm was developed for the purpose of research and technology advancement. The project adopted an existing FPV design (courtesy of Sunlit Sea, Norway) consisting of interconnected shallow-draft floaters that passed demonstrations in inland waters. For upscaling to offshore environments, the FPV system is integrated with a protective ring of external floating breakwaters (FBWs) that reduce direct wave loads on the FPV modules. In the design, it was anticipated that the FBWs are especially effective in terms of blocking short waves which were assumed to drive relative motions and loads onto connectors between FPV modules.
Figure 1 presents the conceptual FPV farm designed in the project, consisting of 3660 connected FPV modules that amount to 2 MWp power, cover an area of 12,936 m2, and which are protected by a ring of 32 interconnected FBWs. The base size of the FPV arrays is 14 × 14 modules but smaller arrays are used on the outside edges to fit them into the breakwater ring. Arrays are connected to other arrays by means of a surface mooring system that consists of synthetic lines and transition pieces (Figure 1). The arrays on the outside edge are connected to a ring of transition elements which are in turn connected to the breakwater ring (Figure 2a). The surface mooring has high horizontal stiffness to prevent collisions between FPV arrays or between FPV modules and FBWs.
### 2.3. Floating Breakwaters
Floating breakwaters (FBWs) are floating structures that attenuate the transmitted wave energy through wave reflection and dissipation by overtopping and viscous losses. The present study considers pontoon-type FBWs built from concrete (Figure 2a). Such a pontoon-type design is common and has been studied in terms of attenuation performance, motions and structural aspects [29–33]. The FBWs may also reduce wind loads on nearby FPV modules [34]. Table 1 presents the main particulars of a single FBW.

Figure 1. Top view illustration of the conceptual 2 MWp farm with FPV arrays, FBW ring and surface mooring (courtesy of CLEMENT Germany GmbH). Blue lines mark transition elements; red lines mark the polyester surface mooring ropes. Arrows mark angles of wave incidence; a wave direction of 0 deg is henceforth referred to as normal incidence (with respect to the FPV farm); the other directions are referred to as oblique incident.

(a)

(b)

Figure 2. (a) Connection between FBW and FPV with surface mooring ring; (b) illustration of FBW interconnection (courtesy of CLEMENT Germany GmbH).

Table 1. Dimensions and mass properties of floating breakwater.
Designation
Length Width Height Draft Mass Vertical CoG w.r.t. keel Roll radius of gyration Pitch radius of gyration Yaw radius of gyration

Value
20.00 m 5.00 m 2.50 m 2.03 m 123 t 1.59 m 1.81 m 6.01 m 6.21 m

In the 2 MWp design, 32 FBWs are interconnected through ropes and polymer fenders, as illustrated in Figures 1 and 2b. This leaves the FBWs free to pitch relative to each other, but other motions are restricted by the stiffness of the connections. Catenary chains moor

the breakwater ring to the seabed. The effect of the bottom mooring on wave-frequent motions is small and is therefore not further considered in the present study.
### 2.4. FPV Modules and Marine Growth

Throughout this work, the term floating PV module refers to the assembly of a 0.5 kWp
capacity PV panel mounted on top of pressed 1.88 m × 1.88 m aluminum sheets that provide buoyancy and structural support (Figure 3). Table 2 presents the main particulars of an FPV module, including a marine growth layer of 60 mm thickness and 1325 kg/m3 density following DNV-GL [9,35]. The marine growth amounts to a total mass of 281 kg (80 kg/m2), forming a significant fraction of the total floater mass (346 kg). It is noted that the actual marine growth varies with field sites, time since installation, anti-fouling and cleaning measures.

Figure 3. Design of Floating PV module (courtesy of SunlitSea).

Table 2. Dimensions and mass properties of FPV module, including 0.06 m of marine growth.

Designation
Length Width Height Draft Mass Vertical position CoG w.r.t. keel Roll/pitch radius of gyration Yaw radius of gyration

Value
1.88 m 1.88 m 0.14 m 0.10 m 346 kg 0.10 m 0.48 m 0.62 m

### 2.5. FPV Connections
The FPV modules are assembled into arrays using polyurethane connectors. A first generation design of these connectors is shown in Figure 3 and was used and discussed in a wave basin study [27]. These basin tests revealed frequent connector buckling due to a lack of compressive stiffness. This motivated a new design of the polyurethane connector, longer and thicker than the first generation, hence with higher stiffness in all degrees of freedom. This new design was used in the present study.
Within an array, adjacent FPV modules are connected through a pair of connectors. Table 3 presents the stiffness of a connection, provided by a pair of connectors in each degree of freedom (DoF). The values are based on load-elongation tests, except for C22 which is estimated to be of order 100 · C11 based on its dimensions and solid mounting. The connectors introduce much flexibility in terms of pitch between modules (low C55) but are relatively stiff in the other rotational DoFs (C44, C66). The transverse stiffness C22 is much higher than in axial and vertical directions.

Table 3. 6DoF connection stiffness of a pair of polyurethane connectors between FPV modules.

Designation
Axial Shear, transverse
Shear, vertical Torsional (roll) Bending (pitch) Bending (yaw)

Symbol
C11 C22 C33 C44 C55 C66

Value
3.9 × 103 kN/m 387 × 103 kN/m 22 × 103 kN/m
185 kNm/rad 0.31 kNm/rad 2.4 × 103 kNm/rad

## 3. Methods
### 3.1. Linear Diffraction Model
For the FPV farm of interest, the wave attenuation by the breakwater and the buildup of standing waves within the breakwater ring are of key interest. For these hydrodynamic processes, wave diffraction and radiation are of high importance. Therefore, we adopt a linear multi-body diffraction solver, DIFFRAC [36], which is developed by the Maritime Research Institute Netherlands (MARIN) and is available following subscription.
Diffraction theory is based on potential flow, so it neglects viscous effects and vorticity. Viscous effects can be added as damping in the equation of motions or as dissipation on the water surface [36,37]. The theory further assumes that motions of waves and floating structures are small, so boundary conditions on the floats and on the free surface can be linearized. A Boundary Element Method (BEM) is used to solve the Laplace equation and boundary conditions on free surface, seabed and surfaces of submerged bodies.
To simulate modular connected arrays, floating bodies are each represented as a mass element (mass and rotational inertia) with a surface representation of the float inside the water, subdivided into mesh elements, to compute hydrodynamic loads. The bodies are interconnected through numerical joints with 6-DoF stiffness. The model solves the linearized equation of motion considering (added) mass, damping, wave exciting forces, and spring terms due to hydrostatics, connectors and mooring. Appendix A presents a more detailed description of linear diffraction theory.
The diffraction model has been previously validated for shallow-draft interconnected floaters, e.g., a floating island with 87 modules [38] and an FPV system comprising up to 12 floaters [19]. These studies showed good agreement with basin measurements in terms of motions as well as connector loads. For the present study, before scaling up to the 2 MWp farm, the model was further validated to ensure a good reproduction of the FBW motions and attenuation and of the FPV module motions (Section 4).
### 3.2. Numerical Model of 2MW Farm
Following validation (Section 4), the numerical model was extended and applied to the 2 MWp farm. Each FPV module is modelled through 45 panel mesh elements and each FBW through 1500 elements, leading to a total of 212,700 mesh elements for the combined mesh (Figure 4). The connections between FPV modules were modelled as 6DoF stiffness joints (see values in Section 2.4). These joints were also used to model the surface mooring (shown in Figures 1 and 2a) and the connections between FBWs (see Figure 2b). The connections between FBWs were modelled as springs with high stiffness in all DoFs except pitch, allowing relative pitch between FBWs but restricting the other relative motions. No mechanical damping on the stiffness joints was considered. The total (potential plus viscous contributions) heave and roll damping for each FBW was derived from decay tests in the basin [27], amounting to 8.9% (heave) and 3.4% (roll) of critical damping.

Figure 4. Boundary element mesh on FPV modules and ring of FBWs.
It is expected that standing waves inside the closed breakwater ring may start to develop at certain frequencies [39], as is also observed in floating fish farms [40,41]. These standing waves are exaggerated in linear diffraction theory and additional free-surface wave damping, to account for viscous losses, should be applied to obtain realistic wave amplitudes (see also Section 3.1). This is also common practice, for example, in vessel side-by-side simulations [36,42]. Therefore, a free surface damping lid was applied between the breakwater ring and the FPV system and between the FPV arrays (for its definition, see [42]). A non-dimensional damping value of ε = 0.025 was used, based on earlier research on the tuning of diffraction theory results to experimental data for vessels in close proximity, where similar standing waves develop [36].
After computing the source strength vectors, velocities and pressures are calculated on all surface mesh elements (Appendix A). The diffraction and radiation potential result in wave forces, added mass and damping coefficients, including interaction terms between floats. These are subsequently used to compute the motions of the FPV modules and FBWs and the loads on the connections and surface mooring.
The challenge in these simulations is the large number of mesh elements and the large number of degrees of freedom (DoFs). Each floating body can move in 6 DoFs, resulting in a total of 22,152 DoFs. For each DoF, a radiation potential has to be calculated, resulting in an additional right-hand-side vector in the (linear) system of equations. For such a large number of DoFs and right-hand-sides in the linear system of equations, the most efficient solver is a direct solver (LU-decomposition). The LU-decomposition has to be made once (per wave frequency) and the calculation of the solution vector (source strength on mesh elements) for each right-hand-side is relatively cheap. The direct solver requires the matrix to be kept in shared memory, so the size of the problem is restricted by the memory of a single compute node of the high-performance computer used for the simulations. Different wave frequencies can be run in parallel on multiple nodes.
The diffraction analysis was run for a wave frequency range from 0.1 rad/s to 3.0 rad/s with a step of 0.1 rad/s, and for multiple wave directions with a wave direction step of 15 degrees (see Figure 1). Simulations were performed with and without the breakwater ring to quantify its effect on the wave transmission and the resulting FPV motions, connection loads and wave drift loads. The simulations without FBW ring still included the surface mooring elements that interconnect the FPV arrays, but the connections to the FBWs were removed.
3.3. Post-Processing
The diffraction calculations result in linear response amplitude operators (RAOs) of floater motions and loads in mooring and FPV connections for unit amplitude waves per wave frequency. For design assessment in a certain wave condition, the RAOs can be combined with the wave spectrum to compute a response spectrum. This can subsequently

Hs [m] Tp [s]

be used to compute the most probable maximum (MPM) value of the response parameter using the following equations:

m0 = Sw(ω)·RAO(ω)2·dω

(1)

MPM = 2·ln N·m0

(2)

Here, Sw(ω) is the wave spectrum; m0 is the zero-order spectral moment of the response spectrum; and N represents the number of wave cycles in a 3 h sea state (N = 10,800/Tz), where Tz is the zero up-crossing period.
In this study, the RAOs of the connection loads between FPV modules were translated to MPM loads along the 50-year return period wave contour at a projected installation site in the Mediterranean Sea (Table 4). Although this linear approach does not account for nonlinear processes that occur in harsh sea states (wave overwash, wave breaking and nonlinear mooring loads), the obtained MPMs still shed insight into the order of magnitude of connection loads for varying sea states and incidence angles.

Table 4. Sea states along 50-year return period contour: significant wave height Hs and peak period Tp. Adopted from [43].
0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 1.2 1.9 2.7 3.6 4.5 5.4 6.2 7.0 7.8 8.6 9.3 10.0 10.8

## 4. Numerical Model Validation
The model was validated by comparing against wave basin tests at geometric scale 1:10 of a simplified, down-sized version of the FPV farm, comprising a 3 × 5 array of FPV modules with an FBW that covers the width of the rectangular basin. A first test series was carried out with FPV connectors that lacked sufficient compressive stiffness, resulting in frequent buckling [27]. A second test series was carried out with an improved connector design with higher compressive stiffness (see Section 2.5). Results of this second campaign (measured motions of FPV modules and breakwater) are used for numerical model validation. The FBW and FPV model, basin setup, environmental conditions and data analysis were the same in both test series and are described by van der Zanden et al. [27]. For the present validation, the RAOs from the white noise wave condition (see [27]) were used. The diffraction analysis considered the basin walls through a panel mesh.
Figure 5 compares the measured and computed motions of the FBW. Apart from a slight mismatch in heave motions at frequencies around and above the heave natural frequency (1.7 rad/s), which is likely caused by wave overwash, the results match closely.
The motions in head seas of the five FPV modules along the centre of the array are presented in Figure 6 (without FBW) and Figure 7 (with FBW). The secondary horizontal axes denote the normalized array length over wavelength La/λ (with La = 10.0 m). The surge RAOs in head seas are approximately 0 at La/λ = 1, consistent with [19]. The pitch RAOs are normalized by wave steepness kai, where k = 2π/λ is the wave number and ai is the incident wave amplitude. The normalized heave and pitch RAOs without FBW (Figure 6b,c) of approximately 1 indicate that the FPV modules tend to follow the water surface. With FBW, the motion response at ω > 1.3 rad/s is clearly reduced (compare Figure 6b,c to Figure 7b,c) due to the wave attenuation by the FBW. For a more detailed discussion of the hydrodynamic behaviour, see [27].

Figure 5. Motion RAOs of floating breakwater, basin test (solid black) and numerical (dashed red) results: (a) surge; (b) heave; (c) roll.

Figure 6. Motion RAOs in head seas without FBW, DIFFRAC (dashed) and basin results (solid) with different colours marking the five instrumented FPV modules (FPV 1 to FPV 5 is fore to aft): (a) surge; (b) heave; (c) pitch.
Figure 7. Motion RAOs in head seas with FBW, DIFFRAC (dashed) and basin results (solid) with different colours marking the five instrumented FPV modules (see legend in Figure 6): (a) surge; (b) heave; (c) pitch.
For both setups (without and with FBW), the numerical results closely follow the measurements. For very short waves (ω > 2 rad/s), the numerical motion amplitudes are

higher than the experiments. This suggests that the diffraction analysis underestimates the attenuation by the FBW, possibly because viscous losses are not considered, and that it overestimates motions and connector loads for these high frequencies (i.e., results can be considered conservative).
Finally, Figure 8 extends the comparison to oblique waves and additional DoFs. For this case, waves are at normal incidence onto the FBW but are at a 45 deg oblique angle with respect to the FPV array (see setup in [27]). Again, measurements and simulations are generally close, with a slight but distinct overestimation by the numerical model for ω > 2 rad/s. The high yaw amplitudes in the basin tests for ω < 1 rad/s are explained by dynamic amplification through the soft-mooring layout that keeps the model in place in the basin and which was not included in the diffraction analysis. The increase in measured roll and pitch response towards low frequencies (ω < 0.8 rad/s) is attributed to measurement uncertainties that are amplified in the present visualization when the wave number k is low.

Figure 8. Motion RAOs in quartering seas (45 deg) without FBW, DIFFRAC (dashed) and basin results (solid) with different colours marking the five instrumented FPV modules (see legend in Figure 6): (a) surge; (b) heave; (c) pitch; (d) roll; (e) pitch; (f) yaw.
## 5. Results

2 MWp Farm
### 5.1. FPV Module Motions

The present section discusses the motions of the 2 MWp farm. Figure 9 visualizes the
motions in time domain for normal incident regular waves without and with FBW ring for wave frequency ω = 1.5 rad/s. The wavelength λ = 27 m corresponds approximately to the length of one 14 × 14 array. Without FBW (Figure 9a), the FPV modules follow the water surface as wave shielding within the farm is minor at this frequency. With FBW ring (Figure 9b), the vertical motions are on average somewhat reduced. Local nodal patterns can be identified due to interference of incident, diffracted and radiated waves (see dashed marking).

(a)

(b)

Figure 9. Motion response for unit amplitude waves, ω = 1.5 rad/s and 0 deg heading. (a) Without floating breakwater ring; (b) with floating breakwater ring. Colour code indicates the dynamic fluid pressure; the same colour scaling is used in panels (a,b). Black arrows indicate the wave direction; dashed circles indicate anti-nodes of standing waves.

To shed more insights into the wave-attenuating performance and wave patterns inside the FBW ring, the RAOs of the vertical module motions are explored. Figure 10 shows the vertical motion amplitude az, normalized by the undisturbed wave amplitude ai, of all floaters with and without FBW ring, for the same wave frequency ω = 1.5 rad/s as in Figure 9. Without FBW ring, the FPV modules move more or less up and down with the waves at this wave frequency, resulting in RAOs close to 1 (Figure 10a). With FBW ring, the FPV vertical motions are on average reduced but are locally amplified at anti-nodes of the standing wave pattern that develops due to interference of the undisturbed incident waves and the waves that are diffracted and radiated by the FBW ring (Figure 10b). The high amplifications at x = 50–70 m relate to wave reflection at the inner side of the concave FBW ring. The distance between anti-nodes is approximately equal to λ/2.

(a)

(b)

Figure 10. RAOs of vertical motions of floating bodies for normal incident waves (0 deg), ω = 1.5 rad/s. (a) Without FBW ring; (b) with FBW ring.

The coloured markers on the centre of FBWs in Figure 10b denote each FBW’s heave response. It follows that the FBWs aligned with the incident wave direction (around x = 0, y = ±89 m) hardly move in vertical direction (az/ai ≈ 0), whereas az/ai > 1 for the perpendicular FBWs (x = ±89 m, y = 0). This illustrates that the interconnected rigid FBWs form a flexible ring, which at this frequency bends out-of-plane.
Figure 11 extends the analysis of vertical motions to different wave frequencies. The figure presents the normalized heave RAO (az/ai) of the FPV modules along the centreline of the farm (x position denoted by vertical axis). The horizontal axis denotes the length of the interconnected FPV arrays along the centreline (La = 153.2 m), normalized by wavelength λ, with the secondary axis denoting the wave frequency ω for reference.

Figure 11. Contour of vertical motion RAOs along the centreline of the farm (y = 2.52 m) for calculation with FBW, wave incidence 180 deg. Vertical axis denotes x position normalized by array length La; horizontal axis denotes the relative array to wavelength La/λ, with secondary axes depicting the wave frequency for reference.
Three regimes of FPV motions can be classified, each dependent on the attenuation performance of the FBW ring. For long waves (La/λ < 2, ω < 1.0 rad/s), the FBW ring is hardly effective and FPV modules across the farm follow the water surface (az/ai ≈ 1 m/m). In an intermediate regime (2 < La/λ < 8), the FBW ring is partially effective: motion amplitudes are locally reduced, but at other locations enhanced as wave diffraction and radiation lead to standing waves inside the ring. The number of nodes and anti-nodes increases as the wavelength reduces. Finally, (very) short waves (La/λ > 9) lead to a reduction in FPV motions by 60–80% and standing wave modes are less distinct.
### 5.2. RAOs of Connection Loads

#### 5.2.1. Horizontal Loads
The connectors between FPV modules are susceptible to fatigue loading and exceedance of ultimate strength and are therefore explored in detail. Figure 12 presents the RAOs of connection loads in earth-fixed surge direction for ω = 1.5 rad/s, without and with FBW. Following [19], the RAOs are normalized by 2ρgBT, where ρ = 1025 kg/m3 is the sea water density; B is the FPV module width; and T is the FPV draft. The presented loads are the forces on the full connection between FPV modules (i.e., on the pair of polyurethane connectors).

(a)

(b)

Figure 12. Normalized RAOs of horizontal connection loads for ω = 1.5 rad/s (λ = 27.3 m, La/λ = 5.6) and 0 deg wave incidence: (a) without FBW; (b) with FBW.

For any floater or array length, in absence of nonlinear or dynamic amplification effects, normalized axial connection loads Fx/2ρgBTai within an array are expected to vary between 0 and 1 [19]. For the situation without FBW (Figure 12a), the results are consistent with this prediction. The figure further shows a pattern of local minima and maxima in axial connection loads. The number of maxima is approximately equal to La/λ (=5.6), which is again consistent with the theory described in [19]. The stiff surface mooring transmits loads between the 14 × 14 FPV arrays.
The layout with FBW ring changes the connection loads strongly (Figure 12b). For the presented frequency, axial loads are locally reduced but increase at other locations, particularly at the edges where the FPV arrays are connected to the breakwaters. The spatial distribution of these loads shows little relation to the vertical FPV module motions (see Figure 10b). This implies that the axial load response is not governed by the standing waves in the ring (in spite of their expected effect on wave excitation). Likely, other factors such as the change in horizontal vibration modes due to the surface mooring connections to the FBW ring have a larger effect on the axial connection load response.
The analysis of axial loads is extended to other frequencies through Figure 13, through a similar data representation as Figure 11 and as [19]. Without FBW ring (Figure 13a), for La/λ = 1, a single maximum of Fx/2ρgBTai = 1 is found in the centre of the farm (x = 0). When La/λ increases, higher mode numbers are excited, leading to an increased number of peaks. This peak count equals the value of La/λ (most evident for La/λ = 1, 2, 3, 5, and 6). The normalized load amplitudes remain in a range of Fx/2ρgBTai = 0 to 1. These observations are all consistent with the theory and analytical formulations by [19] for stiff connections.

(a)

(b)

Figure 13. Contour of normalized loads on FPV connections near centreline of the farm (y = 2.52 m). Vertical axes denote x position normalized by array length La; horizontal axes denote the array to wavelength, with secondary axes depicting the wave frequency for reference. (a) Without FBW ring; (b) with FBW ring.

Figure 13a reveals a change in axial load response for La/λ > 7, with a normalized response that is well above 1 along the full array for La/λ ≈ 9 (ω = 1.9 rad/s). Model analysis of the system showed that this frequency corresponds to the PV farm’s first axial compression mode in x direction. Consistent with [19], wave excitation of this axial vibration mode leads to dynamic amplification (resonance) and results in high connector loads throughout the farm. Because no damping is applied on the connections, the resonant load response may be overestimated by the model.
With FBW ring (Figure 13b), the axial loads reduce for La/λ < 4 (compared to the situation without FBW). Because the attenuation performance of the FBW ring is limited at these wavelengths, this reduction in loads is attributed to the inclusion of the surface mooring connection between FPV arrays and FBW ring, which increases the horizontal stiffness and the natural frequencies of axial vibration modes. The higher surface mooring stiffness also explains why the main resonance peak in connection loads shifts towards higher frequencies, from La/λ ≈ 9 (without FBW) to La/λ ≈ 10 (with FBW).
To study the FBW effectiveness on FPV connection loads for the full farm and for different angles of wave incidence, Figure 14 presents the spatially averaged Fx RAOs without and with FBW.
The FBW ring and its surface mooring reduce axial loads by ~20% for ω = 0.5 to 0.8 rad/s (compare dashed to solid lines). For ω > 1.0 rad/s, the axial load response varies distinctly with wave heading. Normal incident waves (0 deg) lead in the situation without FBW ring to resonant amplifications at ω = 1.9, 2.4 and 2.7 rad/s. With FBW ring, these peaks reduce in magnitude and shift to higher frequencies. Oblique incident waves generally lead to higher axial loads than normal incident waves (except at resonant frequencies), with 45 deg incidence leading to the greatest loads. The FBW ring leads to a

reduction in spatially averaged axial connection loads of a factor of 2 to 3 for oblique waves at these high wave frequencies.

Figure 14. RAOs of spatially averaged connection loads Fx for varying angle of incidence; without FBW (solid) and with FBW (dashed).
#### 5.2.2. Vertical Loads
Figure 15 presents the spatial distribution of the FPV connection load RAOs in vertical direction (Fz). For consistency with the axial loads described in the previous section, the RAOs are again normalized by 2ρgBTai. Because the vertical load in connectors is small for waves much longer than the FPV module length, results are shown here for a high ω of 2.0 rad/s. Later, results are presented for a wider range of frequencies.

(a) Figure 15. Cont.

(b)

(c)

(d)

Figure 15. Contour of normalized vertical loads Fz on FPV connections, ω = 2.0 rad/s (λ = 15.4 m). (a) 0 deg incidence, without FBW ring; (b) 0 deg incidence, with FBW ring; (c) 45 deg incidence, without FBW ring; (d) 45 deg incidence, with FBW ring.

Normal incident waves without FBW ring lead to small Fz loads (Figure 15a). This is explained by the low pitch stiffness of the connectors between FPV modules, allowing an almost free rotation that results in a good wave-following capability of the modules. Quartering waves, however, result in high vertical loads on connections (Figure 15c). For this heading, motions of the individual FPV modules are restricted due to the torsional stiffness introduced by the pairs of connectors, which enhances stresses in multiple directions including the vertical direction.
With FBW ring, the vertical loads vary spatially leading to local maxima and minima in response (Figure 15b,d). These results illustrate that in contrast to the axial loads (see previous section), the vertical loads are affected by standing waves inside the FBW ring. On average, the vertical loads increase slightly for normal incidence waves but decrease substantially for 45 deg incidence for this wave frequency.
The spatially averaged vertical FPV connection loads for varying wave frequency are shown in Figure 16. Without FBW (solid lines), the vertical loads are small for ω < 1.0 rad/s and gradually increase towards higher frequencies. This trend is consistent with the results by [12] and is explained as waves that are much longer than the floater length (i.e., λ/Lf >> 1) lead to small phase differences in vertical wave excitation between floaters; the relative vertical motions between FPV modules are naturally small and so are the vertical loads on the connections.

Figure 16. RAOs of spatially averaged vertical connection loads Fz for varying angle of incidence; without FBW (solid) and with FBW (dashed).
The dashed lines in Figure 16 represent the loads with FBW. For oblique incident waves (15, 30, 45 deg), the average vertical loads for ω > 1.5 rad/s with FBW are reduced by up to a factor of 3 compared to the setup without FBW. For normal incident waves, the loads increase slightly, but the magnitudes are small compared to the other headings.
#### 5.2.3. Overturning Moments

Next to translational loads, the wave-induced moments are also relevant for assessing
the structural integrity of the connections. To understand their spatial distribution, Figure 17 presents RAOs of overturning moments along the horizontal plane (Mxy) on the connections for ω = 1.5 rad/s and oblique (45 deg) incidence. A similar normalization to that for the translational loads is adopted (see Section 5.2.1), now also including the floater length Lf.
Without FBW (Figure 17a), loads for each 14 × 14 array follow a similar spatial distribution; moments are clearly smaller for the connections to outwards FPV modules than for the connectors further inward. This is explained as the overturning motions of the inward modules (which are each connected to four other modules) are more restrained than those of the outer modules (which are connected to two or three other modules). Figure 17b shows the Mxy distribution with FBW ring, revealing a global load reduction but local amplifications. Further analysis showed that these peaks in Mxy are located at nodal points of the standing wave.
Figure 18 presents the spatially averaged roll moments on the FPV connections for varying angles of incidence, without and with FBW ring. Moments increase with wave frequency and are higher for oblique than normal incidence waves. These results are qualitatively similar to the vertical load RAOs presented in Section 5.2.2 and to the results by [12]. The FBW ring is effective in reducing moments at high wave frequencies (ω > 1.5 rad/s), which is again similar to results for vertical connection loads (c.f. Figure 16).

(a)

(b)

Figure 17. Contour of Mxy loads on connections, ω = 1.5 rad/s, 45 deg incidence. (a) Without FBW ring; (b) with FBW ring.

Figure 18. RAOs of spatially averaged roll moments Mx onto connections for varying angle of incidence; without FBW (solid) and with FBW (dashed).
### 5.3. Maximum Connection Loads in Irregular Seas

The previous sections showed response amplitudes for regular waves with unit am-
plitude. To study connection loads in the more realistic case of irregular seas, this section presents the most probable maxima (MPMs) along the 50 y return period wave contour at a Mediterranean Sea site following the methods explained in Section 3.3. Because no mechanical connector damping was assumed, the obtained MPM loads are expected to be conservative, especially in the axial direction that was demonstrated to be affected by resonant amplification (Section 5.2.1).
Figure 19 presents the MPM axial loads for one sea state (normal incident waves with Hs = 4.0 m and Tp = 7.0 s), revealing distinct spatial variation. Without FBWs, the connections in the centre of the farm receive the greatest loads. With FBW ring, the loading

generally reduces for the FPV connections in the middle of the farm but increases for the outward FPV connections. The latter is consistent with results discussed in Section 5.2.1.

(a)

(b)

Figure 19. MPM axial connection loads for normal (0 deg) wave incidence, Hs = 4.0 m and Tp = 7.0 s: (a) without FBW; (b) with FBW.

The MPM loads are further explored through Figure 20, which presents connection loads for different DoFs and wave headings. The horizontal axes represent the sea states, denoted here by the peak period; note that a higher Tp also means higher Hs. The colour contours in each panel mark the envelope of spatial minimum to maximum connection loads; the solid lines mark the spatial mean.
For the axial loads (Figure 20a,b), the spatially averaged MPM loads without FBW protection (blue line) increase from Tp ≈ 1 to 4 s, and are roughly constant for Tp = 4 to 11 s despite these waves being up to a factor of 4 higher (Table 4). The reason why loads do not increase for higher Tp is that these longer waves do not lead to a higher excitation of the main horizontal vibration modes in the FPV farm (as described in Section 5.2.1). Compared to the results without FBW ring (blue lines), the spatially averaged MPM axial loads with FBW ring (green lines) are similar for 0 deg incidence but they reduce by 20–50% for 45 deg incidence.
For both incident angles the spatial maximum MPM axial loads, represented by the contour envelope in Figure 20a,b, increase for the configuration with FBW ring, meaning that some connections receive greater loads and are more likely to break than without FBW ring. This is consistent with the results in Figure 19, which showed an increase in loads for the outward FPV modules. Optimization of the surface mooring between FPV arrays and FBW ring can alleviate these large loads. A simulation with softer surface mooring, performed as a sensitivity check, showed that a lower surface mooring stiffness reduces the spatial maximum and spatial mean MPM loads, but also leads to a higher risk of collision between FPV arrays and between FBW and FBW ring due to increased horizontal relative motions.

(a)

(b)

(c)

(d)

(e)

(f)

Figure 20. Most Probable Maximum (MPM) FPV connection loads along 50-y return period contour at Mediterranean Sea location, for 0 deg (left) and 45 deg (right) incidence. (a,b) Axial loads Fx; (c,d) vertical loads Fz; (e,f) overturning moments Mx. Colour coding indicates FBW presence (blue: without FBW; green: with FBW). The contour surface marks the envelope of spatial minimum to maximum loads; solid lines mark the spatially averaged MPM.

The vertical loads and overturning moments show similar trends (Figure 20c–f). Despite higher wave height, the longest waves do not lead to the greatest loads. Instead, the greatest Fz and Mx loads occur for sea states with relatively short waves (Tp = 3–5 s). This is consistent with the large response amplitudes for high ω as discussed in Sections 5.2.2 and 5.2.3. Compared to the results without FBW ring, the setup with FBW

ring leads to some increase in Fz and Mx loads for normal incident waves (Figure 20c,e) but to a clear reduction for 45 deg waves (Figure 20d,f). For the latter, the spatially averaged loads reduce by 50% for Tp ≈ 4 s and 30% for Tp ≈ 10 s. Hence, the FBW ring and surface mooring design is more effective in reducing the vertical loads and overturning moments than in reducing the axial connection loads.
## 6. Discussion
The results above are obtained from linear wave diffraction calculations (potential flow). The diffraction code does not resolve nonlinear processes such as wave breaking, overwash, viscous energy dissipation due to friction, or non-linear dynamics of the mooring arrangement or FPV connections. While these processes could be included in time domain, SPH or CFD simulations, the simulation of such a large number of bodies is generally not feasible or would be extremely computationally expensive with such higher fidelity tools. Hence, although diffraction calculations are considered low-fidelity, they are at present stage the best available tool to study the wave-induced response of such a large number of floating bodies.
For the present 2 MWp design, the configuration with FBW ring reduces FPV motions and connector loads through wave attenuation by the FBWs, and because the surface mooring connection between FPV arrays and FBWs reduces the horizontal motion response at dominant wave frequencies. At the same time, the FBW ring introduces standing wave modes that locally enhance FPV module motions and vertical loads and moments on the FPV connections. Because the FBWs are slim compared to the array size, they hardly attenuate the waves with frequencies corresponding to the lowest horizontal motion modes of the FPV array. The FBW ring is instead more effective in attenuating the high-frequency content of the incident wave spectrum, which does lead to a distinct reduction in maximum vertical loads and overturning moments on the FPV connectors.
The simulated conceptual farm design leaves room for improvement. The axial connector loads, which are a critical design element, could be reduced by lowering the ratio of the array size to FBW width. This would reduce the transmission of waves with lengths that excite the first horizontal modes of the FPV array. Furthermore, optimization of the horizontal stiffness of FPV connectors and surface mooring can shift axial mode shapes away from frequencies with high wave excitation, hence also contributing to the reduction in connector loads. When reducing the surface mooring stiffness, it needs to be investigated if the gap between the breakwater ring and the FPV field is always maintained and collisions are avoided.
The axial connector loads scale linearly to floater draft. A reduction in FPV mass would reduce connector loads, but may be difficult to realize for designers. For lightweight FPV modules, marine growth forms a significant contribution to the total mass. Field observations on fouling on FPV farms (e.g., [44,45]) are key to obtaining realistic marine growth values and improving design guidelines. For reference, field observations of a near-shore FPV pilot in the Dutch North Sea [45] found a marine growth mass that is considerably lower than what is used in the present study based on class guidelines. The marine growth assumption, but also the exclusion of mechanical damping and of viscous attenuation by the FBWs, may have led to conservative estimates of connector loads in the present study.
Even after design improvement, it is not evident that the proposed FBW ring solution would be economically viable. The FBW ring attenuates high-frequency wave energy, leading to reduced FPV module motions and lower dynamic (fatigue) and survival loads on FPV connectors and power cables. Wave-frequent structural loads (e.g., bending moments) on FPV floaters are also reduced, although it is noted that such loads are small for

the simulated floaters as they are short compared to incident wave lengths (see [10,17]). Furthermore, the FBWs reduce the crest heights of steep and breaking waves [27], which likely reduces the occurrence and intensity of overwash and high-frequency slamming impacts that form structural risks for the PV panels and electric components (inverters, transformers). Hence, the wave-attenuating performance of the FBW ring increases the lifetime of system components and reduces operation and maintenance costs.
In addition, the FBW ring is expected to positively affect the power uptake of the FPV farm. Firstly, because the reduced risk of component damage improves the energy production reliability. Secondly, the FPV panel efficiency improves when overturning motions in steep seas are reduced [46]. However, it is noted that such motion-induced power losses may be small at annual basis [10].
On the other hand, the FBW ring introduces higher costs for materials (FBWs, connections between FBWs, surface mooring), installation, and decommissioning. Moreover, the FBW ring receives substantially higher wave drift, wind and current forces than the FPV farm, which drives up the costs of the seabed mooring. A quantitative analysis of the lifecycle costs and energy yield is recommended to evaluate the economic viability of the simulated concept.
Future studies may focus on advancing higher-fidelity tools (time-domain simulations, SPH, CFD) to enable the assessment of such large farms with better accuracy. Alternatively, multi-fidelity approaches could be considered, combining high-fidelity simulations for detailed assessment of small arrays with lower fidelity modelling of the larger farm. In addition, the validation of numerical models for large FPV farms (hundreds to thousands of FPV modules) using basin or field data is recommended. Particular topics of relevance are the amount of viscous energy dissipation in large farms and the mechanical damping in FPV connections.
## 7. Conclusions
A wave diffraction model (DIFFRAC) was extended to enable the hydrodynamic modelling of large floating PV (FPV) farms. The applicability of the model was demonstrated through simulations of a 2 MWp offshore FPV farm without and with a protective ring of floating breakwaters (FBWs). The simulations shed insights into the wave-induced motions and the spatial distribution of loads and moments on FPV connectors for varying wave frequencies and incident angles. Results were also used to shed insights into the effectiveness of the FBW ring solution in steep (50-year return period) sea states.
Three wave frequency regimes of the FPV farm’s motions inside the FBW ring are distinguished: (i) a low-frequency regime in which the FBW is hardly effective and FPV modules tend to follow the water surface; (ii) an intermediate regime in which the FBW is partially effective and standing waves (sloshing) are formed in the FBW ring; (iii) a high-frequency regime in which the FBW attenuates the majority of wave energy and FPV module motions are clearly reduced.
Axial loads on the connectors are affected by wavelength to farm size and by resonant amplification of axial motions. The axial connector loads are not evidently affected by standing wave modes. The FBW ring with surface mooring reduces axial loads for some frequencies but leads to a local and global increase in response at other frequencies. In irregular seas, spatially averaged axial connector loads are reduced by up to 20%.
The responses of vertical load and overturning moments on connectors are largest for high wave frequencies. The FBW ring is effective in attenuating wave energy at these frequencies and, as such, in reducing vertical loads and overturning moments on FPV connectors. In irregular seas, this reduction amounts to up to 50%.

The FBW ring configuration offers a reduction in fatigue and survival loads onto FPV modules and connectors and leaves room for further design improvement. It is not evident that these reductions outweigh the additional costs for material, mooring, installation and decommissioning.
In future studies, better estimates for viscous wave and mechanical damping inside the farm are needed to prevent overly conservative outcomes. Validation data for large farms (basin tests or field pilots) or advanced numerical modelling (CFD) may support in accomplishing this.

Author Contributions: Conceptualization, T.B., N.B. and J.v.d.Z.; methodology, T.B., N.B. and J.v.d.Z.; software, T.B.; validation, N.B. and J.v.d.Z.; formal analysis, T.B., N.B. and J.v.d.Z.; investigation, T.B., N.B. and J.v.d.Z.; resources, T.B. and J.v.d.Z.; data curation, J.v.d.Z.; writing—original draft preparation, T.B. and J.v.d.Z.; writing—review and editing, T.B., N.B. and J.v.d.Z.; visualization, T.B. and J.v.d.Z.; supervision, T.B. and J.v.d.Z.; project administration, J.v.d.Z.; funding acquisition, T.B. and J.v.d.Z. All authors have read and agreed to the published version of the manuscript.
Funding: The present study is part of the SUREWAVE project, Funded by the European Union with GA No. 101083342. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them.
Data Availability Statement: The numerical results supporting the conclusions of this article will be made available by the authors on request. Basin test data from [27] that have been used for validation are publicly available on https://zenodo.org/doi/10.5281/zenodo.10960432 (accessed on 1 March 2026).
Acknowledgments: The authors gratefully acknowledge the discussions with project partners throughout the SUREWAVE project, which helped maturing the approach and results presented in this paper. We thank the two anonymous reviewers for their constructive feedback.
Conflicts of Interest: The authors declare no conflicts of interest.

## Abbreviations
The following abbreviations are used in this manuscript:

CFD CoG BEM DoF FBW (F)PV JONSWAP MPM RAO RMS SPH VLFS

computational fluid dynamics centre of gravity boundary element method degree of freedom floating breakwater (floating) photovoltaics Joint North Sea wave project most probable maximum response amplitude operator root mean square smoothed particle hydrodynamics very large floating structure

## Appendix A. Linear Diffraction Theory
Linear multi-body diffraction theory is used to simulate the response of the FPV system to waves. Because of the linearity assumption, the velocity potential can be split up into individual potentials describing incident waves, radiated waves (added mass,

damping effects) and diffracted waves. The potential is then a superposition of these

individual potentials:

NDoF

∑ φ = φinc + φdif +

φrad,i

i=1

(A1)

where NDoF is the number of degrees of freedom in the system (i.e., 6 times the number of floats). Due to the assumption of linearity, a transformation can be made from time domain to frequency domain through a Fourier transform:

φˆ(ω) = φ(t)e−iωt

(A2)

where ω is the frequency of the incident waves. A boundary element method (BEM) is used where each velocity potential (except the incident wave potential, which is known) is described as a surface integral of source strengths and a Green function G:

→
φˆ x , ω =

→

→→

σ ξ , ω G x , ξ , ω dSξ

S

(A3)

The zero-speed Green function is used [47], which satisfies the linearized condition on the free surface and the no-flux condition on the seabed. The surface S on which sources are distributed is then reduced to the surfaces of the floats. These surfaces are discretized into N surface mesh elements and the source strengths are assumed constant on each mesh element. This results in the discretized version of equation (6):

→
φˆ x , ω

N
= ∑ σi

→→
G x , ξ , ω dSξ

i=1 Si

(A4)

The magnitude of the source strengths on the mesh elements follows from applying the boundary condition for the radiation and diffraction potentials (no flux: water cannot go through the surface mesh) in the middle of each of the surface mesh elements. From the source strengths, pressures and velocities on surface mesh elements can be calculated. These are used to calculate wave forces and added mass and damping coefficients (A, B) which are then fed into the equation of motion of the floats to calculate the motion response:

−(M + A)ω2 − iBω + Chydro + Cmoor

→
x

=

→
F

(A5)

→
Here, x is a vector with the 6DoF motion response of all floats; M, A, B, Chydro are matrices with the dry inertia of the system, added mass, damping and hydrostatic restoring;
→
F is a collection of external forces (e.g., wave forces). Cmoor is the stiffness matrix due to the surface mooring and interconnectors between the FPV modules. Connector and
surface mooring loads can be obtained by calculating relative motions between floats and
multiplying with the appropriate stiffness.

## References
1. Sahu, A.; Yadav, N.; Sudhakar, K. Floating Photovoltaic Power Plant: A Review. Renew. Sustain. Energy Rev. 2016, 66, 815–824. [CrossRef]
2. Vo, T.T.E.; Ko, H.; Huh, J.; Park, N. Overview of Possibilities of Solar Floating Photovoltaic Systems in the OffShore Industry. Energies 2021, 14, 6988. [CrossRef]
3. Ghosh, A. A Comprehensive Review of Water Based PV: Flotavoltaics, under Water, Offshore & Canal Top. Ocean Eng. 2023, 281, 115044. [CrossRef]

4. Golroodbari, S.Z.M.; Vaartjes, D.F.; Meit, J.B.L.; van Hoeken, A.P.; Eberveld, M.; Jonker, H.; van Sark, W.G.J.H.M. Pooling the Cable: A Techno-Economic Feasibility Study of Integrating Offshore Floating Photovoltaic Solar Technology Within an Offshore Wind Park. Sol. Energy 2021, 219, 65–74. [CrossRef]
5. Abid, M.; Abid, Z.; Sagin, J.; Murtaza, R.; Sarbassov, D.; Shabbir, M. Prospects of Floating Photovoltaic Technology and Its Implementation in Central and South Asian Countries. Int. J. Environ. Sci. Technol. 2019, 16, 1755–1762. [CrossRef]
6. Liu, G.; Guo, J.; Peng, H.; Ping, H.; Ma, Q. Review of Recent Offshore Floating Photovoltaic Systems. J. Mar. Sci. Eng. 2024, 12, 1942. [CrossRef]
7. Claus, R.; López, M. Key Issues in the Design of Floating Photovoltaic Structures for the Marine Environment. Renew. Sustain. Energy Rev. 2022, 164, 112502. [CrossRef]
8. Shi, W.; Yan, C.; Ren, Z.; Yuan, Z.; Liu, Y.; Zheng, S.; Li, X.; Han, X. Review on the Development of Marine Floating Photovoltaic Systems. Ocean Eng. 2023, 286, 115560. [CrossRef]
9. DNV-GL. Recommended Practice: Design, Development and Operation of Floating Solar Photovoltaic Systems; DNVGL-RP-0584; DNV-GL: Høvik, Norway, 2021.
10. Alcañiz, A.; Agarwal, S.; Tiwald, P.; Isabella, O.; Ziar, H.; Colomés, O. Assessment of Power Losses and Structural Response of Offshore Floating Solar Platform. Energy 2025, 335, 137656. [CrossRef]
11. Tay, Z.Y. Three-Dimensional Hydroelasticity of Multi-Connected Modular Offshore Floating Solar Photovoltaic Farm. J. Mar. Sci. Eng. 2023, 11, 1968. [CrossRef]
12. Li, Z.; Chen, D.; Feng, X. Hydroelastic and Expansibility Analysis of a Modular Floating Photovoltaic System with MultiDirectional Hinge Connections. Ocean Eng. 2023, 289, 116218. [CrossRef]
13. Sree, D.K.K.; Law, A.W.-K.; Pang, D.S.C.; Tan, S.T.; Wang, C.L.; Kew, J.H.; Seow, W.K.; Lim, V.H. Fluid-Structural Analysis of Modular Floating Solar Farms under Wave Motion. Sol. Energy 2022, 233, 161–181. [CrossRef]
14. Zhang, Y.; Zhang, X.; Chen, Y.; Tian, X.; Li, X. A Frequency-Domain Hydroelastic Analysis of a Membrane-Based Offshore Floating Photovoltaic Platform in Regular Waves. J. Fluids Struct. 2024, 127, 104125. [CrossRef]
15. Xu, P.; Wellens, P.R. Theoretical Analysis of Nonlinear Fluid–Structure Interaction between Large-Scale Polymer Offshore Floating Photovoltaics and Waves. Ocean Eng. 2022, 249, 110829. [CrossRef]
16. Otto, W.J.; Bunnik, T.H.J.; Kaydihan, L. Hydro-Elastic Behavior of an Inflatable Mattress in Waves. In Proceedings of the 9th International Conference on Hydroelasticity in Marine Technology, Rome, Italy, 10–13 July 2022.
17. Zhang, M.; Schreier, S. Review of Wave Interaction with Continuous Flexible Floating Structures. Ocean Eng. 2022, 264, 112404. [CrossRef]
18. Ikhennicheu, M.; Blanc, A.; Danglade, B.; Gilloteaux, J.-C. OrcaFlex Modelling of a Multi-Body Floating Solar Island Subjected to Waves. Energies 2022, 15, 9260. [CrossRef]
19. Otto, W.; Kluwer, T.; Hirdaris, S. Wave Induced Response of Shallow Draft Interconnected Pontoons. In Proceedings of the ASME 2025 44th International Conference on Ocean, Offshore and Arctic Engineering, Vancouver, BC, Canada, 22–27 June 2025; American Society of Mechanical Engineers: New York, NY, USA, 2025; Volume 5, p. V005T09A071.
20. Li, Y.; Ren, N.; Li, X.; Ou, J. Hydrodynamic Analysis of a Novel Modular Floating Structure System Integrated with Floating Artificial Reefs and Wave Energy Converters. J. Mar. Sci. Eng. 2022, 10, 1091. [CrossRef]
21. Saitov, K.; Jiang, Z. Advancing Offshore Solar Energy Generation: Numerical Modelling and Calibration of a Floating Solar Array against Model Tests. Sol. Energy 2025, 288, 113225. [CrossRef]
22. Cai, G.; Luo, M.; Rubinato, M.; Zhan, Y.; Khayyer, A. Simulation of Multi-Body Floating Structures under Wave Actions Using DualSPHysics+. Ocean Eng. 2026, 349, 124073. [CrossRef]
23. Zhang, G.; Bao, F.; Jiang, C.; El Moctar, O.; Xu, Z.; Zhou, B. Hydrodynamic Performance of Floating Solar Arrays with Articulated Modules for Optimal Wave Adaptation. Appl. Ocean Res. 2025, 164, 104762. [CrossRef]
24. Wei, Y.; Zou, D.; Zhang, D.; Zhang, C.; Ou, B.; Riyadi, S.; Utama, I.K.A.P.; Hetharia, W.; Wood, T.; Huang, L. Motion Characteristics of a Modularized Floating Solar Farm in Waves. Phys. Fluids 2024, 36, 033320. [CrossRef]
25. Lee, J.-H.; Paik, K.-J.; Lee, S.-H.; Hwangbo, J.; Ha, T.-H. Experimental and Numerical Study on the Characteristics of Motion and Load for a Floating Solar Power Farm under Regular Waves. J. Mar. Sci. Eng. 2022, 10, 565. [CrossRef]
26. Delacroix, S.; Bourdier, S.; Soulard, T.; Elzaabalawy, H.; Vasilenko, P. Experimental Modelling of a Floating Solar Power Plant Array under Wave Forcing. Energies 2023, 16, 5198. [CrossRef]
27. van der Zanden, J.; Bunnik, T.; Cortés, A.; Delhaye, V.; Kegelart, G.; Pehlke, T.; Panjwani, B. Wave Basin Tests of a Multi-Body Floating PV System Sheltered by a Floating Breakwater. Energies 2024, 17, 2059. [CrossRef]
28. Zhang, F.; Shi, W.; Wang, Q. A Study on the Hydrodynamics and Coupling Effects of the Multibody Floating Photovoltaic (FPV) Concept. J. Mar. Sci. Eng. 2023, 11, 1491. [CrossRef]
29. McCartney, B.L. Floating Breakwater Design. J. Waterw. Port Coast. Ocean Eng. 1985, 111, 304–318. 30. Ruol, P.; Martinelli, L.; Pezzutto, P. Formula to Predict Transmission for π-Type Floating Breakwaters. J. Waterw. Port Coast. Ocean
Eng. 2013, 139, 1–8. [CrossRef]

31. Martinelli, L.; Ruol, P.; Zanuttigh, B. Wave Basin Experiments on Floating Breakwaters with Different Layouts. Appl. Ocean Res. 2008, 30, 199–207. [CrossRef]
32. Gesraha, M.R. Analysis of Shaped Floating Breakwater in Oblique Waves: I. Impervious Rigid Wave Boards. Appl. Ocean Res. 2006, 28, 327–338. [CrossRef]
33. Peña, E.; Ferreras, J.; Sanchez-Tembleque, F. Experimental Study on Wave Transmission Coefficient, Mooring Lines and Module Connector Forces with Different Designs of Floating Breakwaters. Ocean Eng. 2011, 38, 1150–1160. [CrossRef]
34. Panjwani, B. Assessment of Breakwater as a Protection System against Aerodynamic Loads Acting on the Floating PV System. Energies 2024, 17, 4873. [CrossRef]
35. DNV-GL. Recommended Practice: Environmental Conditions and Environmental Loads; DNVGL-RP-C205; DNV-GL: Høvik, Norway, 2014.
36. Bunnik, T.; Pauw, W.; Voogt, A. Hydrodynamic Analysis for Side-by-Side Offloading. In Proceedings of the Nineteenth (2009) International Offshore and Polar Engineering Conference; ISOPE: Mountain View, CA, USA, 2009.
37. Pauw, W.H.; Huijsmans, R.H.M.; Voogt, A. Advances in the Hydrodynamics of Side-by-Side Moored Vessels. In Proceedings of the ASME 2007 26th International Conference on Offshore Mechanics and Arctic Engineering, San Diego, CA, USA, 10–15 June 2007; ASMEDC: New York, NY, USA, 2009; Volume 4, pp. 597–603.
38. Waals, O.J.; Bunnik, T.H.J.; Otto, W.J. Model Tests and Numerical Analysis for a Floating Mega Island. In Proceedings of the ASME 2018 37th International Conference on Ocean, Offshore and Arctic Engineering, Madrid, Spain, 17–22 June 2018; American Society of Mechanical Engineers: New York, NY, USA, 2018; Volume 1, p. V001T01A016.
39. Park, J.C.; Wang, C.M. Hydrodynamic Behaviour of a Floating Polygonal Platform Centrally Placed within a Polygonal Ring Structure under Wave Action. J. Mar. Sci. Eng. 2022, 10, 1430. [CrossRef]
40. Faltinsen, O.M.; Shen, Y. Wave and Current Effects on Floating Fish Farms: Keynote Contribution for the International Workshop on Wave Loads and Motions of Ships and Offshore Structures, Harbin, China, 5–7 November 2017. J. Mar. Sci. Appl. 2018, 17, 284–296. [CrossRef]
41. van der Plas, P.; Serraris, J.W.; Helder, J.A.; Hanssen, F.-C.W.; Bjar, L.F.; Krogenes, K.O. Reconstruction of Fish Farm Model Tests in CFD for Detailed Analysis of Internal Sloshing and Wave Loading in Extreme Sea States. In Proceedings of the ASME 2022 41st International Conference on Ocean, Offshore and Arctic Engineering, Hamburg, Germany, 5–10 June 2022; American Society of Mechanical Engineers: New York, NY, USA, 2022; Volume 7, p. V007T08A055.
42. Chen, X.B. Hydrodynamic Analysis for Offshore LNG Terminals. In Proceedings of the 2nd Offshore Hydrodynamics Symposium, Rio de Janeiro, Brazil, 16–19 October 2005.
43. Riise, B.; Delhaye, V.; van der Zanden, J.; Bunnik, T.; Panjwani, B. Use Case Scenario Basis for Typical, Rough Location. SUREWAVE D2.1. 2023. Available online: https://surewave.eu/pdf/D2_1_Use-case_scenario_basis_for_typical_rough_locations.pdf (accessed on 1 March 2026).
44. Mavraki, N.; Bos, O.G.; Vlaswinkel, B.M.; Roos, P.; de Groot, W.; van der Weide, B.; Bittner, O.; Coolen, J.W.P. Fouling Community Composition on a Pilot Floating Solar-Energy Installation in the Coastal Dutch North Sea. Front. Mar. Sci. 2023, 10, 1223766. [CrossRef]
45. Mavraki, N.; Bos, O.G.; van der Weide, B.; Bittner, O.; Vlaswinkel, B.M.; Nalmpanti, M.; Coolen, J.W.P. Inventory of the Biofouling Community on the First Offshore Solar Energy Farm in the North Sea. J. Sea Res. 2025, 208, 102627. [CrossRef]
46. Huang, L.; Yang, Y.; Khojasteh, D.; Ou, B.; Luo, Z. Floating Solar Power Loss Due to Motions Induced by Ocean Waves: An Experimental Study. Ocean Eng. 2024, 312, 118988. [CrossRef]
47. Newman, J.N. Algorithms for the Free-Surface Green Function. J. Eng. Math. 1985, 19, 57–67. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.