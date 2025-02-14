STW Documentation
================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   api

Overview
--------

STW (Stopwatch) is a lightweight Python stopwatch library for timing code execution with precision.
It provides features for lap timing, function execution timing, and context manager support.

Quick Start
----------

Installation
~~~~~~~~~~~

.. code-block:: bash

   pip install stw

Basic Usage
~~~~~~~~~~

.. code-block:: python

   from stw import Stopwatch

   # Simple timing
   with Stopwatch() as sw:
       # Your code here
       elapsed = sw.elapsed_time()

See the full documentation for more examples and detailed API reference.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
