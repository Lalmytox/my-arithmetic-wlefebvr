from importlib.metadata import version as get_version

project = "my-arithmetic-wlefebvr"
author = "W. Lefebvre"
release = get_version("my-arithmetic-wlefebvr")   # version issue de hatch-vcs

extensions = [
    "sphinx.ext.autodoc",    # lit les docstrings du code
    "sphinx.ext.napoleon",   # comprend le format numpy
    "sphinx.ext.viewcode",   # lien vers le code source
]
napoleon_google_docstring = False
napoleon_numpy_docstring = True

html_theme = "sphinx_rtd_theme"