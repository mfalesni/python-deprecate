# -*- coding: utf-8 -*-
import pkg_resources
__distribution = pkg_resources.get_distribution('deprecate')

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = __distribution.project_name
copyright = u'2015, Milan Falešník'
author = u'Milan Falešník'


# The short X.Y version.
version = u'1.x'
# The full version, including alpha/beta/rc tags.
release = __distribution.version
version = '.'.join(release.split('.')[:2])

exclude_patterns = []

pygments_style = 'sphinx'
todo_include_todos = False


html_theme = 'haiku'
html_static_path = ['_static']

htmlhelp_basename = 'deprecatedoc'
