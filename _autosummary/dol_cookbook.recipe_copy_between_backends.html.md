# dol_cookbook.recipe_copy_between_backends

Recipe: copy data between two backends that use different formats.

A source backend holds pickles under `.pkl` keys; the target should receive
gzipped csv under `.csv.gz` keys. Both sides are wrapped so that, from the
outside, they look like the same `{name: rows}` mapping, and `update` copies.

```pycon
>>> import pickle
>>> from dol import ValueCodecs, KeyCodecs, Pipe
>>> src_backend = {
...     "file_1.pkl": pickle.dumps([["A", "B"], ["one", "two"]]),
...     "file_2.pkl": pickle.dumps([["apple", "pie"]]),
... }
>>> targ_backend = {}
>>> src = Pipe(KeyCodecs.suffixed(".pkl"), ValueCodecs.pickle())(src_backend)
>>> targ = Pipe(
...     KeyCodecs.suffixed(".csv.gz"),
...     ValueCodecs.csv() + ValueCodecs.str_to_bytes() + ValueCodecs.gzip(),
... )(targ_backend)
>>> targ.update(src)
>>> list(targ_backend)
['file_1.csv.gz', 'file_2.csv.gz']
>>> list(src) == list(targ)
True
>>> targ["file_1"] == src["file_1"]
True
```

Swap the dicts for `dol.Files(folder)` (or any other store) and nothing else changes.
