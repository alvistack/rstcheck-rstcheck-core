=============
rstcheck-core
=============

+-------------------+---------------------------------------------------------------------------------------------+
| **General**       | |maintenance_y| |license| |semver|                                                          |
|                   +---------------------------------------------------------------------------------------------+
|                   | |rtd|                                                                                       |
+-------------------+---------------------------------------------------------------------------------------------+
| **CI**            | |gha_tests| |gha_docu| |gha_qa|                                                             |
+-------------------+---------------------------------------------------------------------------------------------+
| **PyPI**          | |pypi_release| |pypi_py_versions| |pypi_implementations|                                    |
|                   +---------------------------------------------------------------------------------------------+
|                   | |pypi_format| |pypi_downloads|                                                              |
+-------------------+---------------------------------------------------------------------------------------------+
| **Github**        | |gh_tag| |gh_last_commit|                                                                   |
|                   +---------------------------------------------------------------------------------------------+
|                   | |gh_stars| |gh_forks| |gh_contributors| |gh_watchers|                                       |
+-------------------+---------------------------------------------------------------------------------------------+


Library for checking syntax of reStructuredText and code blocks nested within it.

See the full documentation at `read-the-docs`_


.. contents::


Installation
============

From pip

.. code:: shell

    $ pip install rstcheck_core

To use pyproject.toml for configuration::

    $ pip install rstcheck_core[toml]

To add sphinx support::

    $ pip install rstcheck_core[sphinx]


Supported languages in code blocks
==================================

- Bash
- Doctest
- C (C99)
- C++ (C++11)
- JSON
- XML
- Python
- reStructuredText


.. _read-the-docs: https://rstcheck-core.readthedocs.io


.. General

.. |maintenance_n| image:: https://img.shields.io/badge/Maintenance%20Intended-✖-red.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - not intended

.. |maintenance_y| image:: https://img.shields.io/badge/Maintenance%20Intended-✔-green.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - intended

.. |license| image:: https://img.shields.io/github/license/rstcheck/rstcheck-core.svg?style=flat-square&label=License
    :target: https://github.com/rstcheck/rstcheck/blob/main/LICENSE
    :alt: License

.. |semver| image:: https://img.shields.io/badge/Semantic%20Versioning-2.0.0-brightgreen.svg?style=flat-square
    :target: https://semver.org/
    :alt: Semantic Versioning - 2.0.0

.. |rtd| image:: https://img.shields.io/readthedocs/rstcheck-core/latest.svg?style=flat-square&logo=read-the-docs&logoColor=white&label=Read%20the%20Docs
    :target: https://rstcheck-core.readthedocs.io/en/latest/
    :alt: Read the Docs - Build Status (latest)


.. CI


.. |gha_tests| image:: https://img.shields.io/github/workflow/status/rstcheck/rstcheck-core/Test%20code/main?style=flat-square&logo=github&label=Test%20code
    :target: https://github.com/rstcheck/rstcheck-core/actions/workflows/test.yaml
    :alt: Test status

.. |gha_docu| image:: https://img.shields.io/github/workflow/status/rstcheck/rstcheck-core/Test%20documentation/main?style=flat-square&logo=github&label=Test%20documentation
    :target: https://github.com/rstcheck/rstcheck-core/actions/workflows/documentation.yaml
    :alt: Documentation status

.. |gha_qa| image:: https://img.shields.io/github/workflow/status/rstcheck/rstcheck-core/QA/main?style=flat-square&logo=github&label=QA
    :target: https://github.com/rstcheck/rstcheck-core/actions/workflows/qa.yaml
    :alt: QA status


.. PyPI

.. |pypi_release| image:: https://img.shields.io/pypi/v/rstcheck-core.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck-core/
    :alt: PyPI - Package latest release

.. |pypi_py_versions| image:: https://img.shields.io/pypi/pyversions/rstcheck-core.svg?style=flat-square&logo=python&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck-core/
    :alt: PyPI - Supported Python Versions

.. |pypi_implementations| image:: https://img.shields.io/pypi/implementation/rstcheck-core.svg?style=flat-square&logo=python&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck-core/
    :alt: PyPI - Supported Implementations

.. |pypi_format| image:: https://img.shields.io/pypi/format/rstcheck-core.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck-core/
    :alt: PyPI - Format

.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/rstcheck-core.svg?style=flat-square&logo=pypi&logoColor=FBE072
    :target: https://pypi.org/project/rstcheck-core/
    :alt: PyPI - Monthly downloads



.. GitHub

.. |gh_tag| image:: https://img.shields.io/github/v/tag/rstcheck/rstcheck-core.svg?sort=semver&style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck-core/tags
    :alt: Github - Latest Release

.. |gh_last_commit| image:: https://img.shields.io/github/last-commit/rstcheck/rstcheck-core.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck-core/commits/main
    :alt: GitHub - Last Commit

.. |gh_stars| image:: https://img.shields.io/github/stars/rstcheck/rstcheck-core.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck-core/stargazers
    :alt: Github - Stars

.. |gh_forks| image:: https://img.shields.io/github/forks/rstcheck/rstcheck-core.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck-core/network/members
    :alt: Github - Forks

.. |gh_contributors| image:: https://img.shields.io/github/contributors/rstcheck/rstcheck-core.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck-core/graphs/contributors
    :alt: Github - Contributors

.. |gh_watchers| image:: https://img.shields.io/github/watchers/rstcheck/rstcheck-core.svg?style=flat-square&logo=github
    :target: https://github.com/rstcheck/rstcheck-core/watchers/
    :alt: Github - Watchers
