.. _examples:

Usage Examples
=============

Basic Timing
-----------

.. code-block:: python

    from stw import Stopwatch

    # Simple start/stop
    sw = Stopwatch()
    sw.start()
    # ... your code here ...
    elapsed = sw.stop()
    print(f"Operation took {elapsed:.2f} seconds")

    # Auto-start initialization
    sw = Stopwatch(start=True)
    # ... your code here ...
    elapsed = sw.stop()

Lap Timing
---------

.. code-block:: python

    sw = Stopwatch(start=True)

    # Named laps
    sw.lap("database_query")
    sw.lap("data_processing")

    # Get lap information
    db_time, db_total = sw.get_lap(name="database_query")
    time_since_db = sw.elapsed_since_lap("database_query")

Function Timing
-------------

.. code-block:: python

    def expensive_operation(x, y, multiplier=1):
        return (x + y) * multiplier

    sw = Stopwatch()
    time_taken, result = sw.time_function(
        expensive_operation, 
        2, 
        3, 
        multiplier=2
    )

Context Manager
-------------

.. code-block:: python

    with Stopwatch() as sw:
        # ... your code here ...
        current_time = sw.elapsed_time()
