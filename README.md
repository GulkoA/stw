# stw ⏱️

A lightweight Python stopwatch library for timing code execution with precision. Features include lap timing, function execution timing, and context manager support.

Docs can be found [here](https://stw.readthedocs.io/en/latest/).

[![PyPI version](https://badge.fury.io/py/stw.svg)](https://badge.fury.io/py/stw)

## Features

- Simple start/stop timing
- Lap timing with named laps
- Function execution timing
- Context manager support
- Elapsed time tracking
- Lap time analysis
- String representations for debugging

## Installation

```bash
pip install stw
```

## Usage

### Basic Timing

```python
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
```

### Lap Timing

```python
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
```

### Function Timing

```python
from stw import Stopwatch

def expensive_operation(x, y, multiplier=1):
    # ... some time-consuming code ...
    return (x + y) * multiplier

sw = Stopwatch()

# Time function with arguments
time_taken, result = sw.time_function(
    expensive_operation, 
    2, 
    3, 
    multiplier=2
)
print(f"Function took {time_taken:.2f} seconds and returned {result}")
```

### Advanced Usage

```python
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
```

## API Reference

### Constructor

- `Stopwatch(start=False)`: Create a new stopwatch instance
    - `start`: Whether to start timing immediately

### Methods

- `start()`: Start the stopwatch
- `stop() -> float`: Stop the stopwatch and return total time
- `lap(name=None) -> tuple[float, float]`: Record a lap, returns (lap_time, total_time)
- `get_lap(index=None, name=None) -> tuple[float, float]`: Get lap timing by index or name
- `elapsed_time() -> float`: Get current total elapsed time
- `elapsed_since_lap(name=None) -> float`: Get time elapsed since specific lap
- `time_function(func, *args, **kwargs) -> tuple[float, any]`: Time a function execution

### Properties

- `is_running -> bool`: Check if stopwatch is currently running
- `laps -> list[tuple[str, float, float]]`: Access recorded laps

## Error Handling

The library raises appropriate exceptions for invalid operations:

- `RuntimeError`: When stopping/lapping before starting
- `ValueError`: When accessing invalid laps or providing invalid arguments

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
