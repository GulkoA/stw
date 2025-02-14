.. _api:

API Reference
============

.. currentmodule:: stw

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:
   
   stw.Stopwatch

Class Documentation
-----------------

.. autoclass:: Stopwatch
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
