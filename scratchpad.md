# Glob redirect scratchpad

## The basic idea

When you rename a directory in the project source, you end up with a long list of
redirects like:

```
"old/<page-1>" "new/<page-1>"
"old/<page-2>" "new/<page-2>"
...
"old/<page-n>" "new/<page-n>"
```

I'd like to be able to glob redirects so this can be reduced to something like:

```
"old/*" "new"
```

## Edge cases

### Many-to-many or many-to-one

**Problem**: If I add the following redirect, how are the files in the source directory
redirected?

```
"old/*" "new"
```

`old/path/to/file' -> 

**Solution**: If `new` is a directory, it should act like the `mv` command, mapping all
of the source files to an equivalent path in the destination directory. If `new` isn't a
directory, it should map all of the globbed sources to the destination.

Could this be further disambiguated?

### Duplicate sources

**Problem**: What if I want to glob a bunch of redirects, but I want to change specific
paths within that glob? Rediraffe doesn't support duplicate keys in the redirect dict.

**Solution**: Override specific paths in the group with tabbed entries.

```
"old/* new/"
  "old/foo" "new/bar"
  "old/bar" "other/baz"
```

## Pseudocode implementation

This logic should be implemented in the `create_graph` function.

```
if line ends with '*'
    create temporary dict

    if dest exists
        if dest is a dir
            for file in source files
                add 'source/path -> dest/path' to dict
        else
            for file in source files
                add 'source/path -> dest' to dict

    while next line starts with whitespace
        if line starts with `source`
            replace existing destination with specified

    append temp to final one
```
