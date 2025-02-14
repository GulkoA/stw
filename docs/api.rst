.. _api:

API Reference
============

Stopwatch Class
--------------

.. autoclass:: stw.Stopwatch
   :members:
   :special-members: __init__, __enter__, __exit__
   :show-inheritance:

Core Methods
~~~~~~~~~~~

.. automethod:: stw.Stopwatch.start

.. automethod:: stw.Stopwatch.stop

.. automethod:: stw.Stopwatch.lap

.. automethod:: stw.Stopwatch.get_lap

.. automethod:: stw.Stopwatch.elapsed_time

.. automethod:: stw.Stopwatch.elapsed_since_lap

.. automethod:: stw.Stopwatch.time_function

Properties
~~~~~~~~~

.. autoproperty:: stw.Stopwatch.is_running

.. autoproperty:: stw.Stopwatch.laps

Error Handling
-------------

The Stopwatch class raises the following exceptions:

* ``RuntimeError``: When performing operations on an unstarted stopwatch
* ``ValueError``: When accessing invalid laps or providing invalid arguments
