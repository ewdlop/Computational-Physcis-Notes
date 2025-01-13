```text
scalar_field/
├── core/
│   ├── __init__.py
│   ├── classical/
│   │   ├── __init__.py
│   │   ├── klein_gordon.py        # Klein-Gordon equation
│   │   ├── noether_currents.py    # Conservation laws
│   │   └── equations_motion.py    # Field equations
│   └── quantum/
│       ├── __init__.py
│       ├── creation_operators.py   # a, a† operators
│       ├── vacuum.py              # Vacuum state
│       └── coherent_states.py     # Coherent states
├── interactions/
│   ├── __init__.py
│   ├── vertices/
│   │   ├── __init__.py
│   │   ├── phi2_coupling.py       # Mass term
│   │   ├── phi3_coupling.py       # Cubic interaction
│   │   └── phi4_coupling.py       # Quartic interaction
│   └── potentials/
│       ├── __init__.py
│       ├── mexican_hat.py         # SSB potential
│       ├── sine_gordon.py         # Sine-Gordon model
│       └── higgs_potential.py     # Higgs mechanism
├── quantum_corrections/
│   ├── __init__.py
│   ├── propagators/
│   │   ├── __init__.py
│   │   ├── free_propagator.py     # Free field
│   │   └── dressed_propagator.py  # With interactions
│   ├── loops/
│   │   ├── __init__.py
│   │   ├── one_loop.py           # One-loop diagrams
│   │   ├── two_loop.py           # Two-loop diagrams
│   │   └── bubble_sum.py         # Bubble resummation
│   └── effective_action/
│       ├── __init__.py
│       ├── coleman_weinberg.py    # Effective potential
│       └── wilsonian.py          # Wilsonian RG
└── applications/
    ├── __init__.py
    ├── phase_transitions/
    │   ├── __init__.py
    │   ├── second_order.py       # Second-order transitions
    │   └── first_order.py        # First-order transitions
    └── solitons/
        ├── __init__.py
        ├── kinks.py              # Topological solitons
        └── breathers.py          # Dynamic solitons
```
---------------

```text
qcd/
├── core/
│   ├── __init__.py
│   ├── gauge_sector/
│   │   ├── __init__.py
│   │   ├── gluon_field.py       # Gluon fields
│   │   ├── field_strength.py    # Field strength tensor
│   │   └── ghost_fields.py      # Faddeev-Popov ghosts
│   └── matter_sector/
│       ├── __init__.py
│       ├── quark_field.py       # Quark fields
│       └── color_charge.py      # Color algebra
├── symmetries/
│   ├── __init__.py
│   ├── gauge/
│   │   ├── __init__.py
│   │   ├── su3_generators.py    # Gell-Mann matrices
│   │   └── gauge_transform.py   # Gauge transformations
│   └── global/
│       ├── __init__.py
│       ├── chiral_symmetry.py   # Chiral symmetry
│       └── flavor_symmetry.py   # Flavor SU(3)
├── dynamics/
│   ├── __init__.py
│   ├── vertices/
│   │   ├── __init__.py
│   │   ├── quark_gluon.py      # Quark-gluon vertex
│   │   ├── three_gluon.py      # Triple gluon vertex
│   │   └── four_gluon.py       # Four gluon vertex
│   └── propagators/
│       ├── __init__.py
│       ├── gluon_prop.py       # Gluon propagator
│       └── quark_prop.py       # Quark propagator
├── confinement/
│   ├── __init__.py
│   ├── wilson_loop.py          # Wilson loops
│   ├── string_tension.py       # String tension
│   └── potential.py            # Static potential
└── phenomenology/
    ├── __init__.py
    ├── hadronization/
    │   ├── __init__.py
    │   ├── fragmentation.py    # Fragmentation
    │   └── color_flow.py       # Color connections
    └── jets/
        ├── __init__.py
        ├── parton_shower.py    # Parton evolution
        └── clustering.py       # Jet algorithms
```
-----

```text
qed
qed/
├── core/
│   ├── __init__.py
│   ├── gauge_sector/
│   │   ├── __init__.py
│   │   ├── photon_field.py     # Photon field
│   │   ├── gauge_fixing.py     # Gauge conditions
│   │   └── potentials.py       # EM potentials
│   └── matter_sector/
│       ├── __init__.py
│       ├── dirac_field.py      # Electron field
│       └── current.py          # EM current
├── interactions/
│   ├── __init__.py
│   ├── vertices/
│   │   ├── __init__.py
│   │   ├── basic_vertex.py     # QED vertex
│   │   └── form_factors.py     # EM form factors
│   └── processes/
│       ├── __init__.py
│       ├── compton.py          # Compton scattering
│       └── pair_production.py  # e+e- production
├── radiative_corrections/
│   ├── __init__.py
│   ├── self_energy/
│   │   ├── __init__.py
│   │   ├── electron.py        # Electron self-energy
│   │   └── photon.py         # Vacuum polarization
│   └── vertex/
│       ├── __init__.py
│       ├── corrections.py     # Vertex corrections
│       └── ward_identity.py   # Ward identities
└── applications/
    ├── __init__.py
    ├── atomic/
    │   ├── __init__.py
    │   ├── levels.py          # Energy levels
    │   └── transitions.py     # Atomic transitions
    └── beam_physics/
        ├── __init__.py
        ├── radiation.py       # Synchrotron radiation
        └── scattering.py      # Beam scattering
```
---

```text
nuclear_physics/
├── README.md
├── setup.py
├── requirements.txt
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_models.py
│   └── test_interactions.py
├── docs/
│   ├── api_reference.md
│   ├── theory_background.md
│   └── examples/
│       ├── shell_model.ipynb
│       └── collective_motion.ipynb
└── src/
    ├── __init__.py
    ├── core/
    │   ├── __init__.py
    │   ├── quantum_numbers.py
    │   ├── angular_momentum.py
    │   └── radial_functions.py
    ├── models/
    │   ├── __init__.py
    │   ├── shell_model.py
    │   ├── collective_model.py
    │   └── cluster_model.py
    ├── interactions/
    │   ├── __init__.py
    │   ├── nucleon_nucleon.py
    │   ├── three_body.py
    │   └── effective_force.py
    ├── structure/
    │   ├── __init__.py
    │   ├── density_matrices.py
    │   ├── transitions.py
    │   └── correlations.py
    ├── potential/
    │   ├── __init__.py
    │   ├── woods_saxon.py
    │   ├── harmonic_oscillator.py
    │   └── nuclear_force.py
    └── utils/
        ├── __init__.py
        ├── constants.py
        └── numerical.py
```
---

```text
gravity/
├── core/
│   ├── __init__.py
│   ├── geometry/
│   │   ├── __init__.py
│   │   ├── metric.py          # Metric tensor
│   │   ├── connection.py      # Christoffel symbols
│   │   └── curvature.py       # Riemann tensor
│   └── dynamics/
│       ├── __init__.py
│       ├── einstein_eqs.py    # Field equations
│       └── energy_tensor.py   # Energy-momentum tensor
├── classical_solutions/
│   ├── __init__.py
│   ├── vacuum/
│   │   ├── __init__.py
│   │   ├── schwarzschild.py   # Schwarzschild solution
│   │   └── kerr.py           # Kerr solution
│   └── cosmological/
│       ├── __init__.py
│       ├── flrw.py           # FLRW metrics
│       └── de_sitter.py      # de Sitter space
├── quantum_gravity/
│   ├── __init__.py
│   ├── linearized/
│   │   ├── __init__.py
│   │   ├── graviton.py       # Graviton field
│   │   └── propagator.py     # Graviton propagator
│   └── loops/
│       ├── __init__.py
│       ├── divergences.py    # UV divergences
│       └── effective.py      # Effective action
└── applications/
    ├── __init__.py
    ├── black_holes/
    │   ├── __init__.py
    │   ├── thermodynamics.py # BH thermodynamics
    │   └── radiation.py      # Hawking radiation
    └── cosmology/
        ├── __init__.py
        ├── inflation.py      # Inflationary theory
        └── perturbations.py  # Cosmic perturbations
```

---

```text
electroweak/
├── core/
│   ├── __init__.py
│   ├── fields/
│   │   ├── __init__.py
│   │   ├── gauge_bosons/
│   │   │   ├── w_boson.py       # W± fields
│   │   │   ├── z_boson.py       # Z0 field
│   │   │   └── photon.py        # Electromagnetic field
│   │   ├── fermions/
│   │   │   ├── leptons.py       # e,μ,τ and neutrinos
│   │   │   └── quarks.py        # Quark fields
│   │   └── scalar/
│   │       └── higgs.py         # Higgs field
│   └── symmetries/
│       ├── su2.py               # SU(2) weak isospin
│       └── u1.py                # U(1) hypercharge
├── interactions/
│   ├── __init__.py
│   ├── vertices/
│   │   ├── charged_current.py   # W± interactions
│   │   ├── neutral_current.py   # Z0 and γ interactions
│   │   └── higgs_coupling.py    # Yukawa couplings
│   ├── propagators/
│   │   ├── vector_bosons.py     # Gauge boson propagators
│   │   ├── fermions.py          # Fermion propagators
│   │   └── scalar.py            # Higgs propagator
│   └── mixing/
│       ├── weinberg.py          # Weinberg angle
│       └── mass_matrices.py     # Mass generation
├── symmetry_breaking/
│   ├── __init__.py
│   ├── higgs_mechanism/
│   │   ├── vacuum.py            # Vacuum expectation value
│   │   ├── goldstone.py         # Goldstone bosons
│   │   └── mass_generation.py   # Particle masses
│   └── currents/
│       ├── conservation.py      # Conserved currents
│       └── anomalies.py         # Quantum anomalies
├── quantum_corrections/
│   ├── __init__.py
│   ├── loops/
│   │   ├── one_loop/
│   │   │   ├── vertex.py        # Vertex corrections
│   │   │   ├── self_energy.py   # Self-energy diagrams
│   │   │   └── vacuum_pol.py    # Vacuum polarization
│   │   └── two_loop/
│   │       └── corrections.py    # Higher order terms
│   ├── renormalization/
│   │   ├── counterterms.py      # Renormalization terms
│   │   ├── beta_functions.py    # RG functions
│   │   └── ward_identities.py   # Ward-Takahashi
│   └── effective_action/
│       ├── schwinger.py         # Schwinger's action
│       └── wilson.py            # Wilson's approach
├── phenomenology/
│   ├── __init__.py
│   ├── processes/
│   │   ├── decay.py             # Particle decays
│   │   ├── scattering.py        # Cross sections
│   │   └── production.py        # Particle production
│   ├── parameters/
│   │   ├── coupling.py          # Coupling constants
│   │   ├── mixing_angles.py     # Mixing parameters
│   │   └── masses.py            # Physical masses
│   └── predictions/
│       ├── rates.py             # Decay rates
│       └── cross_sections.py    # σ(e+e-→anything)
└── utils/
    ├── __init__.py
    ├── constants.py             # Physical constants
    ├── tensors.py              # Tensor operations
    ├── dirac.py                # Dirac algebra
    └── numerical/
        ├── integration.py       # Loop integrals
        └── monte_carlo.py       # MC simulations
```
