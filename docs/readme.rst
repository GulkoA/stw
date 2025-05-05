.. _readme:

Introduction
===========

STW (Stopwatch) ⏱️
------------------

A lightweight Python stopwatch library for timing code execution with precision. Whether you need to benchmark performance, time specific operations, or track code execution, STW provides a simple yet powerful interface.

Key Features
-----------

- 🔄 Simple start/stop timing
- 🏁 Lap timing with named checkpoints
- ⚡ Function execution benchmarking
- 📊 Visual lap time diagrams
- 🧩 Context manager support (``with`` statement)
- 📈 Elapsed time tracking
- 🔍 Human-readable time formatting

Installation
-----------

.. code-block:: bash

   pip install stw

For detailed usage examples, see the :ref:`examples` section.
For API documentation, see the :ref:`api` section.

Quick Start
----------

.. code-block:: python

   from stw import Stopwatch

   # Basic timing
   sw = Stopwatch(name="quickstart")
   sw.lap("begin")  # records a lap named "begin"
   # ... your code here ...
   sw.lap("end")
   print(f"Total time: {sw.elapsed_total():.2f}s")

Error Handling
-------------

The library raises appropriate exceptions for invalid operations:

* ``ValueError``: When accessing invalid laps or providing invalid arguments

License
-------

MIT License