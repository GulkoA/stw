.. _readme:

Introduction
===========

STW (Stopwatch) ⏱️
------------------

A lightweight Python stopwatch library for timing code execution with precision.
Features include lap timing, function execution timing, and context manager support.

Features
--------

- Simple start/stop timing
- Lap timing with named laps
- Function execution timing
- Context manager support
- Elapsed time tracking
- Lap time analysis
- String representations for debugging

Installation
-----------

.. code-block:: bash

   pip install stw

For detailed usage examples, see the :ref:`examples` section.
For API documentation, see the :ref:`api` section.

Error Handling
-------------

The library raises appropriate exceptions for invalid operations:

* ``RuntimeError``: When stopping/lapping before starting
* ``ValueError``: When accessing invalid laps or providing invalid arguments

License
-------

MIT License