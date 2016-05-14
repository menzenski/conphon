========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/conphon/badge/?style=flat
    :target: https://readthedocs.org/projects/conphon
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/menzenski/conphon.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/menzenski/conphon

.. |requires| image:: https://requires.io/github/menzenski/conphon/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/menzenski/conphon/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/menzenski/conphon/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/menzenski/conphon

.. |codecov| image:: https://codecov.io/github/menzenski/conphon/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/menzenski/conphon

.. |landscape| image:: https://landscape.io/github/menzenski/conphon/master/landscape.svg?style=flat
    :target: https://landscape.io/github/menzenski/conphon/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg?style=flat
    :target: https://www.codacy.com/app/menzenski/conphon
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/menzenski/conphon/badges/gpa.svg
   :target: https://codeclimate.com/github/menzenski/conphon
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/conphon.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/conphon

.. |downloads| image:: https://img.shields.io/pypi/dm/conphon.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/conphon

.. |wheel| image:: https://img.shields.io/pypi/wheel/conphon.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/conphon

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/conphon.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/conphon

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/conphon.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/conphon

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/menzenski/conphon/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/menzenski/conphon/


.. end-badges

A package for applying sound change rules to linguistic data.

* Free software: MIT license

Installation
============

::

    pip install conphon

Documentation
=============

https://conphon.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
