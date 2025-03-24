# Website for OpenFreeEnergy

## Build with conda

To build the website locally, you'll create a
[conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation)
environment and install the website's bundle within that. Once you have conda
installed, and this repo cloned, the commands to run (from within the root
directory of this repo) are:

```bash
conda env create --file environment.yml
conda activate ofe-website
bundle install
```

From there you can launch a local web server with

```bash
bundle exec jekyll serve
```

or, if you want to have the website automatically update as you make changes:

```bash
bundle exec jekyll serve --watch
```

## Build with docker

If you have docker installed, you don't need to install anything else to build the website and view it.

Run:

```bash
docker run -p 4000:4000 -v $(pwd):/site bretfisher/jekyll-serve
```

And then go to http://0.0.0.0:4000 to view the website.
It will create the website in the  `_site` folder and it will be owned by root.
To remove the folder run `sudo rm -fr _site/`.

## Contents

* [Adding news items](#adding-news-items)
* [Adding new team members](#adding-new-team-members)
* [Adding new packages to our projects
page](#adding-new-packages-to-our-projects-page)
* [Tracking upstream changes](#tracking-upstream-changes)

## Adding news items

News items are stored in the `_posts/` directory. Each item is a file. That
file must be named in the format `YYYY-MM-DD-TITLE` where `YYYY-MM-DD` gives
the year month and day for the post. With this, it is possible to backdate posts.
<!-- TODO: mention URL; but maybe after adjusting it -->

The file will is Markdown format with YAML frontmatter. The YAML frontmatter
should include the following:

* `layout: post`: News items should use the `post` layout.
* `title`: The title of the post.
* `categories`: space-separated list of categories. Categories we encourage are
  names of specific software packages (e.g., `gufe`, `openfe`, `lomap`) and
  types of news item (e.g., `releases`, `presentations`, `hirings`).

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


## Adding new packages to our projects page

The details for these are in files in `_projects/`. Make a copy of
`_defaults.md`. Note that these are markdown files with YAML frontmatter
(although all you do is fill in the YAML). Fill in each of the fields. `role`
can be one of `flagship`, `developers`, `maintainers`. Within each role,
projects are listed alphabetically by filename.

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


