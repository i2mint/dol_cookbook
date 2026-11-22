# dol_cookbook.recipe_filter_keys

Recipe: expose only some of a store’s keys.

`filt_iter` restricts which keys a store shows; the backend is untouched.

```pycon
>>> from dol import filt_iter
>>> backend = {"a.json": "{}", "b.txt": "hi", "c.json": "[]"}
>>> only_json = filt_iter(backend, filt=lambda k: k.endswith(".json"))
>>> list(only_json)
['a.json', 'c.json']
>>> "b.txt" in only_json
False
```

It also works as a decorator factory, to make a reusable filter:

```pycon
>>> json_only = filt_iter(filt=lambda k: k.endswith(".json"))
>>> sorted(json_only(backend))
['a.json', 'c.json']
```
