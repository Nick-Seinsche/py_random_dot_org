Random.org API Wrapper
======================
.. image:: https://img.shields.io/badge/Version-1.0.2-blue
   :target: https://github.com/Nick-Seinsche/py_random_dot_org/releases/tag/v1.0.2
   :alt: Version 1.0.2

.. image:: https://img.shields.io/github/actions/workflow/status/Nick-Seinsche/py_random_dot_org/.github%2Fworkflows%2Fpublish-pypi.yml
   :alt: GitHub Actions Workflow Status

.. image:: https://img.shields.io/badge/ReadTheDocs-Documentation-orange
   :target: https://nick-seinsche.github.io/py_random_dot_org/
   :alt: ReadTheDocs Documentation

.. image:: https://img.shields.io/badge/PYPI-Package-red
   :target: https://pypi.org/project/py-random-dot-org/
   :alt: PYPI PAckage



This Python module provides a wrapper for the `Random.org API`_ to generate various types of random data such as integers,
sequences, decimal fractions, Gaussian numbers, strings, UUIDs, and random blobs.

Features
--------

- Generate random integers, integer sequences, decimal fractions, and Gaussian-distributed numbers.
- Generate random strings, UUIDs, and blobs.
- Retrieve API usage statistics, including remaining bits and requests.

Installation and Setup
----------------------

1. Install the package from PYPI:
   ::

       pip install py-random-dot-org

2. Visit https://api.random.org/ and fetch an api key.

Usage
-----

1. Import the ``BasicApi`` class and initialize it with your Random.org API key:
   ::

       from basic_api import BasicApi

       api = BasicApi(api_key="your_api_key")

2. Call the available methods to generate random data. For example, to generate random integers:
   ::

       random_integers = api.generate_integers(num=5, minimum=1, maximum=100)
       print(random_integers)

3. You can also check your API usage:
   ::

       usage_stats = api.get_usage()
       print(usage_stats)

Running Tests
-------------

The project includes tests written using ``pytest``. To run the tests:

1. Install ``pytest``:
   ::

       pip install pytest

2. Run the tests:
   ::

       pytest

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.

.. _Random.org API: https://api.random.org/
