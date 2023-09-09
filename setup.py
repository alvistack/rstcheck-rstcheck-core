# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rstcheck_core']

package_data = \
{'': ['*']}

modules = \
['AUTHORS']
install_requires = \
['docutils>=0.7,<0.20', 'pydantic>=1.2,<2.0', 'types-docutils>=0.18,<0.20']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.6,<5.0',
                             'typing-extensions>=3.7.4,<5.0'],
 'docs': ['sphinx>=4.0,<6.0',
          'sphinx-autobuild==2021.3.14',
          'm2r2>=0.3.2',
          'sphinx-rtd-theme<1',
          'sphinx-rtd-dark-mode>=1.2.4,<2.0.0',
          'sphinx-autodoc-typehints>=1.15',
          'sphinxcontrib-apidoc>=0.3',
          'sphinxcontrib-spelling>=7.3'],
 'sphinx': ['sphinx>=4.0,<6.0'],
 'testing': ['pytest>=6.0',
             'pytest-cov>=3.0',
             'coverage[toml]>=6.0',
             'coverage-conditional-plugin>=0.5',
             'pytest-sugar>=0.9.5',
             'pytest-randomly>=3.0',
             'pytest-mock>=3.7'],
 'toml:python_version < "3.11"': ['tomli>=2.0,<3.0']}

setup_kwargs = {
    'name': 'rstcheck-core',
    'version': '1.0.3',
    'description': 'Checks syntax of reStructuredText and code blocks nested within it',
    'author': 'Steven Myint',
    'author_email': 'git@stevenmyint.com',
    'maintainer': 'Christian Riedel',
    'maintainer_email': 'cielquan@protonmail.com',
    'url': 'https://github.com/rstcheck/rstcheck-core',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
