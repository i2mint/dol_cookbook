"""Recipe: avoid re-listing a slow store.

Listing the keys of a remote store can be slow. ``cached_keys`` lists once and
remembers.

>>> from dol import cached_keys
>>> class Slow(dict):
...     listings = 0
...     def __iter__(self):
...         Slow.listings += 1
...         return super().__iter__()
>>> store = cached_keys(Slow(a=1, b=2))
>>> list(store), list(store), list(store)
(['a', 'b'], ['a', 'b'], ['a', 'b'])
>>> Slow.listings
1
"""
