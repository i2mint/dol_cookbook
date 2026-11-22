# dol_cookbook

Worked recipes for [dol](https://github.com/i2mint/dol), the data-object-layer toolkit. Every recipe is a module whose docstring is runnable doctest, so CI verifies it.

To install: `pip install dol_cookbook`

## Recipes

- `dol_cookbook.recipe_copy_between_backends`: copy between a pickle backend and a gzipped-csv backend through wrapped stores.
- `dol_cookbook.recipe_filter_keys`: show only some keys (`filt_iter`).
- `dol_cookbook.recipe_translate_keys`: friendly keys over awkward ones (`wrap_kvs`, `KeyCodecs`).
- `dol_cookbook.recipe_json_values`: values stored as JSON text (`ValueCodecs`).
- `dol_cookbook.recipe_files_as_text`: a folder as a `{filename: text}` mapping (`Files`, `TextFiles`).
- `dol_cookbook.recipe_cached_keys`: list a slow store once (`cached_keys`).
- `dol_cookbook.pipes`: useful `Pipe` compositions, such as `get_rows_iterator` for DataFrames.

Read a recipe in the source, or in a Python session: `import dol_cookbook.recipe_filter_keys as r; help(r)`.
