import os
import time

from .utils import *
class Stopwatch:
  """
  A simple stopwatch class that can be used to time code execution.
  """
  def __init__(self, name: str="stw", verbose: bool=False):
    """
    Initialize the stopwatch.

    Args:
      `name`: Name for this stopwatch instance, used in verbose output.
      `verbose`: Whether to automatically print output for every function call.
    """
    self._start_time = self.now()
    self._laps = []
    self._last_lap_time = self.now()
    self._verbose = verbose
    self._name = name
    
  def now(self) -> float:
    """
    Get the current system time.

    Returns:
      `current_time`: The current time in seconds
    """
    return time.perf_counter()
  
  @property
  def laps(self) -> list[tuple[str, float, float, float]]:
    """
    Get the list of recorded laps.
    
    Returns:
      `list[tuple[str, float, float, float]]`: A list of tuples containing 
      (lap_name, timestamp, total_time, lap_time) for each recorded lap.
    """
    return self._laps

  def lap(self, lap_name: str=None) -> tuple[float, float]:
    """
    Record a lap in the stopwatch.

    If initialized with `verbose=True`, prints the lap time and total time since the stopwatch was started.

    Args:
      `lap_name`: The name of the lap. If not provided, the name will be "lap n" where n is the lap number.

    Returns:
      `tuple[float, float]`: A tuple containing (total_time, lap_time) - the time it took to complete the lap, 
      and total time since the stopwatch was started.
    """

    # default lap name
    if lap_name is None:
      lap_name = f"lap {len(self._laps) + 1}"

    cur_time = self.now()

    total_time = cur_time - self._start_time
    lap_time = cur_time - self._last_lap_time
    self._last_lap_time = cur_time

    self._laps.append((lap_name, cur_time, total_time, lap_time))

    if self._verbose:
      line = f"[{self._name}] {lap_name}: {human_readable(lap_time)} "
      if len(self._laps) > 1:
        line += f"| total: {human_readable(total_time)}"
      print(line)

    return total_time, lap_time
  
  # getters

  def get_lap(self, index: int=None, name: str=None) -> tuple[float, float, float]:
    """
    Get a lap by index or name.
    
    > Please provide only one of index or name!

    Args:
      `index`: The index of the lap to get.
      `name`: The name of the lap to get.

    Returns:
      `tuple[float, float, float]`: A tuple containing (timestamp, total_time, lap_time) for the requested lap.
    """
    if index is not None and name is not None:
      raise ValueError("Only one of index or name can be provided")
    
    if index is not None:
      if index >= len(self._laps) or index < 0:
        raise ValueError(f"No lap with the given index {index} exists")
      
      return self._laps[index][1:]
    
    if name is not None:
      for lap in self._laps:
        if lap[0] == name:
          return lap[1:]
        
      raise ValueError("No lap with the given name")
    
    raise ValueError("Either index or name must be provided")

  
  def elapsed_total(self, name: str=None) -> float:
    """
    Get the total time since the stopwatch was started until the lap.

    Args:
      `name`: The name of the lap to get the time until. If not provided, the time until the last lap will be returned.

    Returns:
      `total_time`: The total time since the stopwatch was started
    """
    if name is None:
      return self._last_lap_time - self._start_time
    
    timestamp, total_time, lap_time = self.get_lap(name=name)
    return total_time
  

  def elapsed_since_lap(self, name: str=None) -> float:
    """
    Get the time elapsed since the last lap.

    Args:
      `name`: The name of the lap to get the time elapsed since. If not provided, the time elapsed since the last lap will be returned.

    Returns:
      `elapsed_time`: The time elapsed since the last lap.
    """
    if name is None:
      return self.now() - self._last_lap_time
    
    lap = self.get_lap(name=name)
    return self.now() - lap[1]
  

  # representations
  
  
  def __str__(self) -> str:
    """
    Get a string representation of the stopwatch.

    Returns:
      `str`: The string representation of the stopwatch.
    """
    s = f"Stopwatch({self._name}"
    s += f", total_time={human_readable(self.elapsed_total())}"
    if len(self._laps) != 0:
      s +=  f", elapsed_until_last_lap={human_readable(self.elapsed_total())}"
    s += ")"
    return s
  
  def __repr__(self) -> str:
    """
    Get a string representation of the stopwatch.

    Returns:
      `str`: The string representation of the stopwatch.
    """
    return str(self)

  # context manager support

  def __enter__(self):
    self.lap("start")
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.lap("done")

  # function timing support

  def time_function(self, func, *args, **kwargs) -> tuple[float, any]:
    """
    Time the execution of a function.

    Args:
      `func`: The function to time
      `*args`: The positional arguments to pass to the function
      `**kwargs`: The keyword arguments to pass to the function

    Returns:
      `tuple[float, any]`: A tuple containing (elapsed_time, result) where elapsed_time is the time it took 
                          to execute the function and result is the return value of the function
    """
    self.lap(f"start {func.__name__}")
    result = func(*args, **kwargs)
    total_time, lap_time = self.lap(f"done {func.__name__}")
    return lap_time, result
  
  # diagram printing3
  def print_diagram(self):
    """
    Print a visual diagram of the stopwatch laps.
    
    This displays a visual representation of lap times with proportional spacing
    and labeled duration, making it easy to compare relative lap times.
    
    Returns:
      None
    """
    shading = ["░", "▒", "▓", "▚", "▐"]

    try:
      width = min(os.get_terminal_size().columns, 200)
    except OSError:
      width = 200
      
    segment_width_s = (width - len(self._laps) + 1) / self.elapsed_total()
    line1 = "│"
    line2 = " "
    for i, (name, time_at, total_time, lap_time) in enumerate(self._laps):
      width = int(lap_time * segment_width_s)
      shading_char = shading[i % len(shading)]
      line1 += shading_char * width
      line1 += "│"

      label = f"{name} ({human_readable(lap_time)})"
      padding_before = (width - len(label)) // 2
      padding_after = width - len(label) - padding_before
      line2 += " " * padding_before + label + " " * padding_after + " "

    print(f" {self._name} ({human_readable(self.elapsed_total())})")
    print(line1)
    print(line2)


