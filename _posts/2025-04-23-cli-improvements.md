---
layout: post
title: "Usability Improvements to the CLI"
categories: release
---

New in openfe v1.4.0 are several new quality-of-life improvements to our command line, specifically the ``openfe gather`` command.

When gathering results data, it's likely you'll be interacting with incomplete or failed simulation results, and the improvements in v1.4.0 make this handling more transparent and intuitive.

### 1. Pass in lists of filepaths, not just a single directory
Prior to v1.4.0, ``openfe gather`` took in a single directory, and searched through all files in that directory.
This is great if you're running a simple workflow where all the simulations are complete and stored in a single directory - but that's not what real life workflows look like.

Now in v1.4.0, you can pass any combination of files and directories into ``openfe gather``. This includes wildcards and any other linux file operations you can dream up.

For example, if you just want to check the results of a subset of ligands, across all of your simulation replicates, you can do this with a simple command:


`$ openfe gather replicate_*/*ejm_4*  --report=raw`


Similarly, this also makes it simple to check the results of a single result JSON file:


```
$ openfe gather rbfe_lig_ejm_31_complex_lig_ejm_42_complex.json  --report=raw
```



### 2. Improved table formatting

Also new in v1.4.0, we've updated our table formatting for improved readability.
This formatting is only applied when writing to the terminal's stdout, such that if you pass a file name to `-o`, that file will still be tab-delimited as before.

An example of how a results table might look as of v1.4.0:

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

NOTE: If you absolutely love looking at tab-delimited tables (or if you pipe stdout output as a part of your workflow), you can always add the `--tsv` option when running `openfe gather`.

### 3. Info about failed simulations is now included in reports

Alchemical networks can become large and complex, and so an alchemical network will often be in an incomplete state with any number of results JSONs missing, invalid, or containing results of a failed simulation.
Our goal is to pass through as much useful information about the current state of the resulting alchemical network in a concise and comprehensible way.

As of v1.4.0, `openfe gather`'s output includes every leg that



### 4. Errors are caught up-front with clearer messages