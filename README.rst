========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/spec-synthase/badge/?style=flat
    :target: https://readthedocs.org/projects/spec-synthase
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ex-dev/spec-synthase.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ex-dev/spec-synthase

.. |coveralls| image:: https://coveralls.io/repos/ex-dev/spec-synthase/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ex-dev/spec-synthase

.. |version| image:: https://img.shields.io/pypi/v/spec-synthase.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/spec-synthase

.. |commits-since| image:: https://img.shields.io/github/commits-since/ex-dev/spec-synthase/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ex-dev/spec-synthase/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/spec-synthase.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/spec-synthase

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/spec-synthase.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/spec-synthase

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/spec-synthase.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/spec-synthase


.. end-badges

spec-synthase is a tool to help deal with big swagger files, by building the swagger specification files from little
spec files.

* Free software: MPL2 license

Installation
============

::

    pip install spec-synthase

Documentation
=============

https://spec-synthase.readthedocs.io/

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
