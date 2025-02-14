Welcome to STW Documentation
===========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   api
   examples

About STW
---------

STW (Stopwatch) is a lightweight Python stopwatch library for timing code execution with precision.
It provides a simple yet powerful interface for:

* Basic timing operations
* Lap timing with named laps
* Function execution timing
* Context manager support

Quick Start
----------

Installation
~~~~~~~~~~~

.. code-block:: bash

   pip install stw

Basic Example
~~~~~~~~~~~~

.. code-block:: python

   from stw import Stopwatch

   # Using context manager
   with Stopwatch() as sw:
       # Your code here
       print(f"Operation took {sw.elapsed_time():.2f} seconds")

   # Using lap timing
   sw = Stopwatch(start=True)
   sw.lap("operation1")
   sw.lap("operation2")
   print(sw.elapsed_since_lap("operation1"))

See the :ref:`examples` section for more usage examples and the :ref:`api` section for detailed API documentation.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
