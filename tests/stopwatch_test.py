import pytest
import time
from src.stwatch import Stopwatch

@pytest.fixture
def stopwatch():
    return Stopwatch()

def test_init():
    sw = Stopwatch()
    assert not sw.is_running
    
    sw = Stopwatch(start=True)
    assert sw.is_running

def test_start_stop(stopwatch):
    stopwatch.start()
    assert stopwatch.is_running
    time.sleep(0.1)
    elapsed = stopwatch.stop()
    assert not stopwatch.is_running
    assert elapsed >= 0.1

def test_elapsed_time(stopwatch):
    stopwatch.start()
    time.sleep(0.1)
    running_time = stopwatch.elapsed_time()
    assert running_time >= 0.1
    stopwatch.stop()
    final_time = stopwatch.elapsed_time()
    assert final_time >= 0.1

def test_lap_timing(stopwatch):
    stopwatch.start()
    time.sleep(0.1)
    lap_time, total_time = stopwatch.lap("first")
    assert lap_time >= 0.1
    assert total_time >= 0.1
    
    time.sleep(0.1)
    lap_time, total_time = stopwatch.lap("second")
    assert lap_time >= 0.1
    assert total_time >= 0.2

def test_get_lap(stopwatch):
    stopwatch.start()
    time.sleep(0.1)
    stopwatch.lap("test_lap")
    lap_time, total_time = stopwatch.get_lap(name="test_lap")
    assert lap_time >= 0.1
    assert total_time >= 0.1

    with pytest.raises(ValueError):
        stopwatch.get_lap(index=0, name="test_lap")

def test_context_manager():
    with Stopwatch() as sw:
        assert sw.is_running
        time.sleep(0.1)
    assert not sw.is_running
    assert sw.elapsed_time() >= 0.1

def test_time_function(stopwatch):
    def slow_function():
        time.sleep(0.1)
        return 42

    elapsed, result = stopwatch.time_function(slow_function)
    assert elapsed >= 0.1
    assert result == 42

def test_multiple_stops(stopwatch):
    stopwatch.start()
    time.sleep(0.1)
    stopwatch.stop()
    with pytest.raises(RuntimeError):
        stopwatch.stop()

def test_lap_without_start(stopwatch):
    with pytest.raises(RuntimeError):
        stopwatch.lap()
