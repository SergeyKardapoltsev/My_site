import os
import sys
from typing import Any, Dict

# add the demo python code to the path, so that it can be used to demonstrate
# source links
sys.path.append(os.path.abspath("./kitchen-sink/demo_py"))

project = 'kardapoltsev'
copyright = '2024, SergeyKardapoltsev'
author = 'SergeyKardapoltsev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'scrolls'
html_static_path = ['_static']