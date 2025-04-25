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

```
$ openfe gather replicate_*/*ejm_4*  --report=raw
```

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

**NOTE**: If you absolutely love looking at tab-delimited tables (or if you pipe stdout output as a part of your workflow), you can always add the `--tsv` option when running `openfe gather`.

### 3. Info about failed simulations is now included in reports

Alchemical networks can become large and complex, and so an alchemical network will often be in an incomplete state with any number of results JSONs missing, invalid, or containing results of a failed simulation.
Our goal is to pass through as much useful information about the current state of the resulting alchemical network in a concise and comprehensible way.

Prior to v1.4.0, openfe would simply omit any invalid edges.
As of v1.4.0, `openfe gather` outputs every leg that it is able to detect a pair of ligand names and a leg run type (complex, solvent, or vacuum) for.
If it is unable to determine a calculated value, it will simply mark `Error` instead.

Using the same example as above, but with the `solvent` leg of the `lig_ejm_31` to `lig_ejm_42` leg failed, the resulting table would be:

``` bash

 $ openfe gather replicate_0/*ejm_4*  --report=raw
  ┌─────────┬────────────┬────────────┬─────────────────┬──────────────────┐
  │         │            │            │ DG(i->j)        │ MBAR uncertainty │
  │ leg     │ ligand_i   │ ligand_j   │ (kcal/mol)      │ (kcal/mol)       │
  ├─────────┼────────────┼────────────┼─────────────────┼──────────────────┤
  │ complex │ lig_ejm_31 │ lig_ejm_42 │ -14.9           │ 0.8              │
  │ solvent │ lig_ejm_31 │ lig_ejm_42 │ Error           │ Error            │
  │ complex │ lig_ejm_31 │ lig_ejm_46 │ -40.7           │ 0.8              │
  │ solvent │ lig_ejm_31 │ lig_ejm_46 │ -39.9           │ 0.8              │
  ...

```

Additionally, openfe will detect a few common failure modes and list the failed files and their detected failure mode before returning the table.
This should make it more feasible to keep track of failed simulations.

Some types of warnings include:
  - missing ligand names and/or simulation type (these JSONs won't be included in the reported table)
  - missing `'estimate'` or `'uncertainty'` keys in a JSON
  - all `'unit results'` contain `Exception`s, and so the simulation has failed.

**NOTE**: Since it is only aware of the results JSONs passed in on the CLI, **openfe still has no awareness of results JSONs that are entirely missing**.


### 4. Errors are caught up-front with clearer messages

Our goal for openfe's error handling is 1) timeliness - catch errors or invalid states as early in the runtime as possible, and 2) clarity - relay the breaking behavior to the user clearly and without extraneous information.
We found the following opportunities for improving our error handling with timeliness and clarity in mind:

- If the input(s) to `openfe gather ` contain no valid results (or you make a typo), ``openfe gather`` will now output an error, instead of an empty table.  This is especially helpful for if you use `-o filename.tsv`, since with the prior behavior you wouldn't be aware that it was unsuccessful until you opened the file and saw no results were recorded.
-  When performing ``report=dg`` calculations, there must be two or more repeats of every leg in order to have a non-zero uncertainty. Instead of waiting for cinnabar to fail and throw a confusing `numpy` error, we catch this up-front and let you know you need more repeats for a valid calculation.
- If a results network has fewer than 3 edges *or* is disconnected, ``report=dg`` will fail and prompt for more legs or repeats, but both `raw` and `ddg` values may be computed.


Our hope is that these improvements made to the openfe gather CLI functionality will make analyzing and troubleshooting free energy calculation results a bit easier.

Many of these changes were in response to [issues raised by users]([https://github.com/OpenFreeEnergy/openfe/issues), and more feedback is always welcome - no matter how small!
