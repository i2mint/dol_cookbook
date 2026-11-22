# dol_cookbook.recipe_json_values

Recipe: store Python objects as JSON text.

`ValueCodecs.json()` encodes values on write and decodes on read.

```pycon
>>> from dol import ValueCodecs
>>> backend = {}
>>> store = ValueCodecs.json()(backend)
>>> store["config"] = {"retries": 3, "tags": ["a", "b"]}
>>> backend["config"]
'{"retries": 3, "tags": ["a", "b"]}'
>>> store["config"]["tags"]
['a', 'b']
```

Codecs compose with `+`: add `str_to_bytes` to hold bytes instead of text.

```pycon
>>> bstore = (ValueCodecs.json() + ValueCodecs.str_to_bytes())({})
>>> bstore["x"] = [1, 2]
>>> list(bstore)
['x']
```
