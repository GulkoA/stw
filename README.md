# stw ⏱️

A lightweight Python stopwatch library for timing code execution with precision. Whether you need to benchmark performance, time specific operations, or track code execution, `stw` provides a simple yet powerful interface.

[![PyPI version](https://badge.fury.io/py/stw.svg)](https://badge.fury.io/py/stw)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://stw.readthedocs.io/en/latest/)

## Key Features

- 🔄 Simple start/stop timing
- 🏁 Lap timing with named checkpoints
- ⚡ Function execution benchmarking
- 📊 Visual lap time diagrams
- 🧩 Context manager support (`with` statement)
- 📈 Elapsed time tracking
- 🔍 Human-readable time formatting

## Installation

```bash
pip install stw
```

## Quick Start

```python
from stw import Stopwatch

# Basic timing
sw = Stopwatch(name="quickstart")
sw.lap("begin")  # records a lap named "begin"
# ... your code here ...
sw.lap("end")
print(f"Total time: {sw.elapsed_total()}s")
```

## Usage Examples

### Basic Timing

```python
from stw import Stopwatch
import time

# Method 1: Manual start/stop
sw = Stopwatch(name="example1")
sw.lap("start")
time.sleep(1.5)  # simulate work
total_time, lap_time = sw.lap("end")
print(f"Operation took {lap_time[0]:.2f} seconds")  # lap_time

# Method 2: Using context manager (automatically records start/end laps)
with Stopwatch(name="example2", verbose=True) as sw:
    time.sleep(1.2)  # simulate work
    # The elapsed time is automatically printed when exiting the context

```

### Timing Multiple Operations

```python
from stw import Stopwatch
import time

# Create a stopwatch with verbose output
sw = Stopwatch(name="database-ops", verbose=True)

# Record start lap
sw.lap("begin")

# First operation
time.sleep(0.8)  # simulate database query
sw.lap("query")
# Prints: [database-ops] query: 0.80s | total: 0.80s

# Second operation
time.sleep(0.5)  # simulate data processing
sw.lap("processing")
# Prints: [database-ops] processing: 0.50s | total: 1.30s

# Third operation
time.sleep(0.3)  # simulate rendering
sw.lap("render")
# Prints: [database-ops] render: 0.30s | total: 1.60s

# Get time info for a specific operation
timestamp, total_time, lap_time = sw.get_lap(name="query")
print(f"Query operation took {lap_time:.2f}s")

# Print a visual diagram of all operations
sw.print_diagram()
```

### Function Benchmarking

```python
from stw import Stopwatch, stopwatch
import time

# Method 1: Using the time_function method
def expensive_calculation(n, factor=2):
    time.sleep(n * 0.1)  # simulate work
    return n * factor

sw = Stopwatch()
# Time any function with any arguments
time_taken, result = sw.time_function(
    expensive_calculation, 
    5,  # positional arg 
    factor=3  # keyword arg
)
print(f"Calculation took {time_taken:.2f}s and returned {result}")

# Method 2: Using the decorator
@stopwatch
def process_data(items, multiplier=1):
    time.sleep(0.2)  # simulate work
    return sum(items) * multiplier

# Function execution is automatically timed
result = process_data([1, 2, 3, 4], multiplier=2)
# Prints timing information automatically
```

### Nested Timing

```python
from stw import Stopwatch
import time

# Timing nested operations
with Stopwatch(name="outer", verbose=True) as outer:
    time.sleep(0.5)  # some initial work
    
    with Stopwatch(name="inner", verbose=True) as inner:
        time.sleep(0.8)  # nested operation
    
    time.sleep(0.3)  # more outer work
    
    # Access timing information from both stopwatches
    print(f"Inner operation: {inner.elapsed_total():.2f}s")
    print(f"Total with overhead: {outer.elapsed_total():.2f}s")
```

### Advanced Features

```python
from stw import Stopwatch
import time

sw = Stopwatch(name="advanced")

# Record some operations
sw.lap("first")
time.sleep(0.5)
sw.lap("second")
time.sleep(0.8)
sw.lap("third")

# Get time since a specific lap
time_since_second = sw.elapsed_since_lap("second")
print(f"Time since 'second' lap: {time_since_second:.2f}s")

# Get time until a specific lap
time_until_second = sw.elapsed_total("second")
print(f"Time until 'second' lap: {time_until_second:.2f}s")

# Access all recorded laps
for lap_name, timestamp, total_time, lap_time in sw.laps:
    print(f"Lap '{lap_name}': {lap_time:.2f}s (Total: {total_time:.2f}s)")

# Visual representation
print(sw)  # Shows current state with elapsed time
sw.print_diagram()  # Prints a visual diagram of all laps
```

## API Reference

### Constructor

- `Stopwatch(name="stw", verbose=False)`: Create a new stopwatch
  - `name`: Name for this stopwatch (useful for identifying in output)
  - `verbose`: When True, automatically prints lap timings

### Methods

- `lap(lap_name=None) -> tuple[float, float]`: Record a lap, returns (total_time, lap_time)
- `get_lap(index=None, name=None) -> tuple[float, float, float]`: Get (timestamp, total_time, lap_time) by index or name
- `elapsed_until_lap(name=None) -> float`: Get time until the last lap or a specific lap
- `elapsed_since_lap(name=None) -> float`: Get time since the last lap or a specific lap

- `time_function(func, *args, **kwargs) -> tuple[float, any]`: Time a function execution
- `print_diagram()`: Print a visual representation of lap times

### Properties

- `laps -> list[tuple[str, float, float, float]]`: Access all recorded laps
  - Each lap is a tuple of (lap_name, timestamp, total_time, lap_time)

### Decorators

- `@stopwatch`: Decorator to automatically time a function

## Error Handling

The library raises appropriate exceptions for invalid operations:

- `ValueError`: When accessing invalid laps or providing invalid arguments

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
