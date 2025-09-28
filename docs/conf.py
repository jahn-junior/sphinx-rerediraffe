from __future__ import annotations

copyright = (
    "2020, FIRST",
    "2025-%Y, the Sphinx developers",
)

master_doc = "index"
project = "sphinxext-rediraffe"

exclude_patterns = ["_build"]

html_theme = "furo"
html_logo = "../assets/rediraffe_logo_128.png"

extensions = ["myst_parser", "sphinxext.rediraffe"]

rediraffe_redirects = {"other.md": "index.md", "other2.md": "other.md"}
