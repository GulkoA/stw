import time

class Stopwatch:
  """
  A simple stopwatch class that can be used to time code execution.
  """

  def __init__(self, start=False):
    """
    Initialize the stopwatch.

    Args:
      `start`: Whether to start the stopwatch immediately upon initialization.
    """
    self._start_time = None
    self._end_time = None
    self._laps = []
    self._last_lap_time = None
    self._is_running = False

    if start:
      self.start()

  @property
  def is_running(self) -> bool:
    return self._is_running
  
  @property
  def laps(self) -> list[tuple[str, float, float]]:
    return self._laps

  def start(self) -> None:
    """
    Start the stopwatch.
    """
    self._start_time = time.time()
    self._last_lap_time = self._start_time
    self._is_running = True
    self._end_time = None

  def lap(self, name: str=None) -> tuple[float, float]:
    """
    Record a lap in the stopwatch.

    Args:
      `name`: The name of the lap. If not provided, the name will be "lap n" where n is the lap number.

    Returns:
      `lap_time`: The time it took to complete the lap.

      `total_time`: The total time since the stopwatch was started
    """
    if not self.is_running:
      raise RuntimeError("Stopwatch is not running, cannot record a lap")
    if name is None:
      name = f"lap {len(self._laps) + 1}"

    cur_time = time.time()
    lap_time = cur_time - self._last_lap_time
    total_time = cur_time - self._start_time

    self._laps.append((name, lap_time, total_time))

    self._last_lap_time = cur_time
    return lap_time, total_time

  def get_lap(self, index: int=None, name: str=None) -> tuple[float, float]:
    """
    Get a lap by index or name.
    
    > Please provide only one of index or name!

    Args:
      `index`: The index of the lap to get.

      `name`: The name of the lap to get.

    Returns:
      `lap_time`: The time it took to complete the lap

      `total_time`: The total time since the stopwatch was started.
    """
    if index is not None and name is not None:
      raise ValueError("Only one of index or name can be provided")
    
    if index is not None:
      if index >= len(self._laps) or index < 0:
        raise ValueError(f"No lap with the given index {index} exists")
      
      return self._laps[index][1], self._laps[index][2]
    
    if name is not None:
      for lap in self._laps:
        if lap[0] == name:
          return lap[1], lap[2]
        
      raise ValueError("No lap with the given name")
    
    raise ValueError("Either index or name must be provided")

  def stop(self) -> float:
    """
    Stop the stopwatch.

    Returns:
      `total_time`: The total time since the stopwatch was started
    """
    if not self.is_running:
      raise RuntimeError("Stopwatch is not running, cannot stop")
    self._end_time = time.time()
    self._is_running = False
    return self._end_time - self._start_time
  
  def elapsed_time(self) -> float:
    """
    Get the total time since the stopwatch was started is running, or the time it took to complete if it is stopped.

    Returns:
      `total_time`: The total time since the stopwatch was started
    """
    if self.is_running:
      return time.time() - self._start_time
    if self._end_time is not None:
      return self._end_time - self._start_time
    raise ValueError("Stopwatch has not been started yet")

  def elapsed_since_lap(self, name: str=None) -> float:
    """
    Get the time elapsed since the last lap.

    Args:
      `name`: The name of the lap to get the time elapsed since. If not provided, the time elapsed since the last lap will be returned.

    Returns:
      `elapsed_time`: The time elapsed since the last lap.
    """
    if name is None:
      if len(self._laps) == 0:
        raise ValueError("No laps have been recorded yet")
      return time.time() - self._last_lap_time
    
    for lap in self._laps:
      if lap[0] == name:
        return time.time() - lap[1]
      
    raise ValueError("No lap with the given name")
  
  # representations
  
  
  def __str__(self) -> str:
    """
    Get a string representation of the stopwatch.

    Returns:
      `str`: The string representation of the stopwatch.
    """
    s = f"Stopwatch(running={self.is_running}"
    if self.is_running or self._end_time is not None:
      s += f", elapsed_time={self.elapsed_time()}"
    if len(self._laps) != 0:
      s +=  f", elapsed_since_lap={self.elapsed_since_lap()}"
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
    self.start()
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.stop()

  # function timing support

  def time_function(self, func, *args, **kwargs):
    """
    Time the execution of a function.

    Args:
      `func`: The function to time
      `*args`: The positional arguments to pass to the function
      `**kwargs`: The keyword arguments to pass to the function

    Returns:
      `elapsed_time`: The time it took to execute the function
      `result`: The return value of the function
    """
    self.start()
    result = func(*args, **kwargs)
    elapsed_time = self.stop()
    return elapsed_time, result
  