from .stopwatch import Stopwatch

def stopwatch(func: callable):
  """
  A decorator to time the execution of a function.

  This decorator wraps the function with a Stopwatch instance using the
  function's name and outputs timing information.

  Args:
    `func`: The function to time.

  Returns:
    `wrapper`: The wrapped function that returns the original function's result.
  """
  def wrapper(*args, **kwargs):
    sw = Stopwatch(name=func.__name__, verbose=True)
    result = func(*args, **kwargs)
    sw.lap("done")
    return result
  
  return wrapper
