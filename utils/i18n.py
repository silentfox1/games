# -*- coding: utf-8 -*-

from markdown2 import Markdown

def get(game, language, key):
    l10n_value = game["tr"].get(language, {}).get(key)
    if l10n_value is not None:
        return l10n_value
    else:
        return game[key]

def get_desc(game, language):
    desc = get(game, language, "description")
    if "description-format" not in game:
        return desc.replace("\n", "<br>")
    elif game["description-format"] == "markdown":
        markdowner = Markdown(extras=["strike"])
        return markdowner.convert(desc)
    else:
        raise ValueError("description format invaild")

