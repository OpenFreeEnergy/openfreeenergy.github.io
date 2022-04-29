# Website for OpenFreeEnergy

The get this started within a conda environment, first create an environment
from the included `environment.yml` file. Then you will need to run `bundle
install`. From there, you can launch a local server using `bundle exec jekyll
serve`. Use the `--watch` argument to `jekyll serve` if you want website to
automatically update as you make changes.

## Tracking upstream changes

It turns out this theme is poorly designed for customization. So I'm keeping in
here our overrides along with the diff of the original, which will hopefully
make future maintenance updates a little easier.

When creating a diff, it should always be

```
diff installed_file our_file > _file.diff
```

This way, we can check whether updated versions of the theme made changes to
the files that we have changed -- if that diff is exactly the saved diff, then
no changes have been made upstream.

You can find the location of the installed file with:

```
bundle info --path jekyll-theme-hydra
```

## Adding new packages to our projects page

The details for these are in files in `_projects/`. Make a copy of
`_defaults.md`. Note that these are markdown files with YAML frontmatter
(although all you do is fill in the YAML). Fill in each of the fields. `role`
can be one of `flagship`, `developers`, `maintainers`. Within each role,
projects are listed alphabetically by filename.
