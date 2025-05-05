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

* Recording laps with named checkpoints
* Timing function execution
* Visualizing timing comparisons
* Using context managers for timing blocks of code
* Human-readable time formatting

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
   with Stopwatch(name="example", verbose=True) as sw:
       # Your code here
       sw.lap("operation1")  # Record a lap
       # More code here
       sw.lap("operation2")  # Record another lap
       
       # Print a visual diagram of the timing
       sw.print_diagram()

   # Using the stopwatch decorator
   from stw import stopwatch
   
   @stopwatch
   def process_data(items):
       # Function will be automatically timed
       return sum(items)
       
   result = process_data([1, 2, 3, 4, 5])

See the :ref:`examples` section for more usage examples and the :ref:`api` section for detailed API documentation.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
