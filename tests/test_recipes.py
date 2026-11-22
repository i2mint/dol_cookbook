"""Every recipe module must import and its doctests must run."""

import doctest
import importlib
import pkgutil

import dol_cookbook


def _recipe_names():
    return [
        m.name
        for m in pkgutil.iter_modules(dol_cookbook.__path__)
        if m.name.startswith("recipe_")
    ]


def test_there_are_recipes():
    assert len(_recipe_names()) >= 5


def test_recipe_doctests_pass_and_exist():
    for name in _recipe_names():
        mod = importlib.import_module(f"dol_cookbook.{name}")
        result = doctest.testmod(mod)
        assert result.attempted > 0, name
        assert result.failed == 0, name
