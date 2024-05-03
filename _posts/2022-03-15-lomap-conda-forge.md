---
layout: post
title: "Lomap 2.0 released on conda-forge"
categories: release
---

We've released [Lomap](http://github.com/OpenFreeEnergy/Lomap) 2.0 on
conda-forge. Lomap is a useful tool for creating atom mappings between
two lignand molecules, and we've taken responsibility for maintaining it,
since it was no longer actively developed by the academic team that
created it (David Mobley's group at University of California, Irvine).

One of our first maintenance tasks has been to make it easier for users to
install Lomap. Therefore, we've made it possible to install Lomap using
`conda`.  To distinguish this line from the previous versions of Lomap, we're
referring to this package as `lomap2`. It can be installed  with the command:

`conda install -c conda-forge lomap2`
