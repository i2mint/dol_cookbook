# dol_cookbook.recipe_files_as_text

Recipe: a folder as a `{filename: text}` mapping.

`Files` reads and writes bytes; `TextFiles` reads and writes text.

```pycon
>>> import tempfile
>>> from dol import Files, TextFiles
>>> folder = tempfile.mkdtemp()
>>> raw = Files(folder)
>>> raw["note.txt"] = b"hello"
>>> list(raw)
['note.txt']
>>> text = TextFiles(folder)
>>> text["note.txt"]
'hello'
>>> text["other.txt"] = "world"
>>> sorted(text)
['note.txt', 'other.txt']
>>> del text["other.txt"]
>>> list(text)
['note.txt']
```
