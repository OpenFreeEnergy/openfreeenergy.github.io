It turns out this theme is poorly designed for customization. So I'm keeping in
here our overrides along with the diff of the original, which will hopefully
make future maintenance updates a little easier.

When creating a diff, it should always be

```
diff installed_file our_file > file.diff
```

This way, we can check whether updated versions of the theme made changes to
the files that we have changed -- if that diff is exactly the saved diff, then
no changes have been made upstream.

You can find the location of the installed file with:

```
bundle info --path jekyll-theme-hydra
```
