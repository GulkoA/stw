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

    # Using context manager
    with Stopwatch() as sw:
        # ... your code here ...
        print(f"Current time: {sw.elapsed_time():.2f}")

Lap Timing
---------

.. code-block:: python

    sw = Stopwatch(start=True)

    # Record named laps
    lap_time, total_time = sw.lap("database_query")
    lap_time, total_time = sw.lap("data_processing")

    # Auto-named laps
    lap_time, total_time = sw.lap()  # Named "lap 1"
    lap_time, total_time = sw.lap()  # Named "lap 2"

    # Get lap information
    # By name
    db_lap_time, db_total = sw.get_lap(name="database_query")

    # By index
    first_lap_time, first_total = sw.get_lap(index=0)

    # Get time since last lap
    time_since_last = sw.elapsed_since_lap()

    # Get time since specific lap
    time_since_db = sw.elapsed_since_lap("database_query")

Function Timing
-------------

.. code-block:: python

    def expensive_operation(x, y, multiplier=1):
        # ... some time-consuming code ...
        return (x + y) * multiplier

    sw = Stopwatch()
    time_taken, result = sw.time_function(
        expensive_operation, 
        2, 
        3, 
        multiplier=2
    )
    print(f"Function took {time_taken:.2f} seconds and returned {result}")

Advanced Usage
------------

.. code-block:: python

    # Nested timing
    with Stopwatch() as outer:
        # ... some code ...
        with Stopwatch() as inner:
            # ... nested operation ...
            inner_time = inner.elapsed_time()
        outer_time = outer.elapsed_time()

    # String representation for debugging
    sw = Stopwatch(start=True)
    sw.lap("first")
    print(sw)  # Outputs: Stopwatch(running=True, elapsed_time=0.001, elapsed_since_lap=0.001)
