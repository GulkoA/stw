.. _api:

API Reference
============

.. currentmodule:: stw.stopwatch

.. automodule:: stw.stopwatch
   :members:
   :undoc-members:
   :special-members: __init__, __enter__, __exit__
   :show-inheritance:
   :member-order: bysource

Error Handling
-------------

The Stopwatch class raises the following exceptions:

* ``RuntimeError``: When performing operations on an unstarted stopwatch
* ``ValueError``: When accessing invalid laps or providing invalid arguments
