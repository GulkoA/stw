def human_readable(seconds: float) -> str:
  """
  Convert seconds to a human-readable format.

  Args:
    `seconds`: The number of seconds to convert.

  Returns:
    `str`: The human-readable format of the seconds.
  """
  s = seconds % 60
  m = (seconds // 60) % 60
  h = (seconds // 3600) % 24

  if m == 0 and h == 0:
    return f"{s:.2f}s"
  elif h == 0:
    return f"{m:.0f}m {s:.2f}s"
  else:
    return f"{h:.0f}h {m:.0f}m {s:.2f}s"