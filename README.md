# Website for OpenFreeEnergy

The get this started within a [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation) environment, first create an environment from the included `environment.yml` file (`conda env create --file environment.yml`). 
Then you will need to run `bundle install`. 
From there, you can launch a local server using `bundle exec jekyll serve`. 
Use the `--watch` argument to `jekyll serve` if you want website to automatically update as you make changes.

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

## Adding new team members

Each team member has a file that is just a markdown file with YAML frontmatter.
Only the frontmatter is filled in. The frontmatter includes the following fields:

* `name`: Full name as you want it on the website
* `position`: Title at OpenFreeEnergy
* `image_path`: URL or path to an image. We frequently use our GitHub avatars
  (in which case this should be the whole https URI). If using a file, place it
  in the `assets/images/team/` directory. In that case, note that the
  `image_path` should have a preceding slash (i.e.,
  `/assets/images/team/image.jpg`)
* `github`: You GitHub username
* `scholar` [optional]: A link to your Google Scholar profile. Should include
  everything that comes after `https://scholar.google.com/` in your profile's
  URL. Leave this blank if you don't want to include your Google Scholar link.
* `blurb`: A brief paragraph describing yourself.

You can copy `_team/_defaults.md` to get a template. You can see the rendered
versions at https://openfree.energy/team/.
