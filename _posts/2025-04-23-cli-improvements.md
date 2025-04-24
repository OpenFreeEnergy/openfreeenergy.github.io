---
layout: post
title: "Usability Improvements to the CLI"
categories: release
---


### 1. Pass in lists of filepaths, not just a single directory

you have several results directories available,
but only want to process the results of a subset for now:

```
$ openfe gather results_*_trial2/
```

you have several results directories available, but only want to process the results of a subset for now:

``` bash
$ openfe gather results/*solvent*.json --report=raw
```

### 2. Improved table formatting


``` bash
 $ openfe gather replicate_0/*ejm_4*  --report=raw
┌─────────┬────────────┬────────────┬─────────────────┬──────────────────┐
│         │            │            │ DG(i->j)        │ MBAR uncertainty │
│ leg     │ ligand_i   │ ligand_j   │ (kcal/mol)      │ (kcal/mol)       │
├─────────┼────────────┼────────────┼─────────────────┼──────────────────┤
│ complex │ lig_ejm_31 │ lig_ejm_42 │ -14.9           │ 0.8              │
│ solvent │ lig_ejm_31 │ lig_ejm_42 │ -15.7           │ 0.8              │
│ complex │ lig_ejm_31 │ lig_ejm_46 │ -40.7           │ 0.8              │
│ solvent │ lig_ejm_31 │ lig_ejm_46 │ -39.9           │ 0.8              │
│ complex │ lig_ejm_31 │ lig_ejm_47 │ -27.8           │ 0.8              │
│ solvent │ lig_ejm_31 │ lig_ejm_47 │ -27.8           │ 0.8              │
│ complex │ lig_ejm_31 │ lig_ejm_48 │ -16.0           │ 0.8              │
│ solvent │ lig_ejm_31 │ lig_ejm_48 │ -16.8           │ 0.8              │
│ complex │ lig_ejm_42 │ lig_ejm_43 │ -19.0           │ 0.8              │
│ solvent │ lig_ejm_42 │ lig_ejm_43 │ -20.3           │ 0.8              │
│ complex │ lig_ejm_46 │ lig_jmc_23 │ 17.3            │ 0.8              │
│ solvent │ lig_ejm_46 │ lig_jmc_23 │ 17.1            │ 0.8              │
│ complex │ lig_ejm_46 │ lig_jmc_27 │ 15.8            │ 0.8              │
│ solvent │ lig_ejm_46 │ lig_jmc_27 │ 15.9            │ 0.8              │
│ complex │ lig_ejm_46 │ lig_jmc_28 │ 23.1            │ 0.8              │
│ solvent │ lig_ejm_46 │ lig_jmc_28 │ 23.3            │ 0.8              │
└─────────┴────────────┴────────────┴─────────────────┴──────────────────┘
```