# stwatch

A lightweight Python stopwatch library for timing code execution with precision. Features include lap timing, function execution timing, and context manager support.

## Installation

```bash
pip install stwatch
```

## Usage

### Simple Timing

```python
from stwatch import Stopwatch

# Basic usage
sw = Stopwatch()
sw.start()
# ... your code here ...
elapsed = sw.stop()
print(f"Operation took {elapsed:.2f} seconds")

# Using context manager
sw = Stopwatch()
with sw:
    # ... your code here ...
    print(f"Current time: {sw.elapsed_time():.2f}")
```

### Timing Functions

```python
from stwatch import Stopwatch

def expensive_operation():
    # ... some time-consuming code ...
    pass

sw = Stopwatch()
time_taken, result = sw.time_function(expensive_operation)
print(f"Function took {time_taken:.2f} seconds")
```


## Lap Timing

```python
sw = Stopwatch(start=True)  # Start immediately

# Record named laps
lap_time, total_time = sw.lap("database_query")
lap_time, total_time = sw.lap("data_processing")

# Get lap info
db_lap_time, db_total = sw.get_lap(name="database_query")
proc_lap_time, proc_total = sw.get_lap(name="data_processing")
```
