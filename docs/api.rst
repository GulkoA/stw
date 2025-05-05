.. _api:

API Reference
============

.. currentmodule:: stw

Top Level Functions
-----------------

.. autofunction:: stw.stopwatch.human_readable
.. autofunction:: stw.stopwatch.stopwatch

Stopwatch Class
-------------

.. autoclass:: stw.stopwatch.Stopwatch
   :members:
   :undoc-members:
   :special-members: __init__, __enter__, __exit__
   :show-inheritance:
   :member-order: bysource

Error Handling
-------------

The Stopwatch class raises the following exceptions:

* ``ValueError``: When accessing invalid laps or providing invalid arguments
