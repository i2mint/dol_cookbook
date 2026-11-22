# dol_cookbook.recipe_translate_keys

Recipe: show friendly keys over a backend with awkward ones.

`wrap_kvs` takes a `key_decoder` (backend key to outer key) and a
`key_encoder` (outer key to backend key); they must be inverses.

```pycon
>>> from dol import wrap_kvs
>>> backend = {"user_1.json": 1, "user_2.json": 2}
>>> users = wrap_kvs(
...     backend,
...     key_decoder=lambda k: k.removesuffix(".json"),
...     key_encoder=lambda k: k + ".json",
... )
>>> list(users)
['user_1', 'user_2']
>>> users["user_2"]
2
>>> users["user_3"] = 3
>>> sorted(backend)
['user_1.json', 'user_2.json', 'user_3.json']
```

For the common cases there are ready-made codecs: `KeyCodecs.suffixed('.json')`
does the same as the lambdas above.
