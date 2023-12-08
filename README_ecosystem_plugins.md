# Managing the ecosystem catalog

A subset of this website is devoted to providing a catalog of software that
makes up the broader Open Free Energy ecosystem. This is intended to be a
central clearinghouse where users can find different modular tools that can be
plugged into an Open Free Energy workflow. This page documents that part of the
website.

## Adding a new catalog entry

External contributors are most likely to want to add a new catalog entry,
representing some useful code that they have created and wish to share. Adding
new entries is intended to be as easy as possible.

Basically, all you need to do is fork and clone this repo, and add a new item
under the `_ecosystem/` directory. This will be a Markdown file with YAML
frontmatter.  Copy the `_ecosystem/_defaults.md` file to get a template that
you can work from.

Add that file in a branch on your fork, and make a pull request to have your
new entry added to the catalog!

## Customizing ecosystem configuration

The general idea  here is that catalog entries represent different "categories"
of object, with the objects within a category being modular replacements for
each other. As an example, "protocol" is one of the categories for Open Free
Energy.

Details of the ecosystem configuration are in the `_config.yaml` for the site.
In particular, custom configuration the ecosystem tools are under the
`ecosystem_catalog` top-level heading. This allows you to change, e.g., the
allowed categories.

Some aspects of configuration are based on Jekyll's standard configuration
tools. In particular, note that `ecosystem` is one the Jekyll `collections`,
and note that we can set the default layout for ecosystem entries within the
standard `defaults` configuration heading.

## Changing the presentation of catalog entries

Catalog entries are shown in two different styles:

1. Full-page mode, where a full web page is dedicated to each entry. This is
   intended to provide sufficient details for a reader to learn more about the
   entry. You can customize this mode in `_layouts/ecosystem-entry.html`. 
2. Summary mode (cards), where a brief summary of each entry is provided, e.g.,
   as part of a list of other catalog entries. You can customize this mode in
   `_includes/ecosystem-summary.html`.
