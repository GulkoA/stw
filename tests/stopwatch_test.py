import pytest
import time
from src.stw import Stopwatch, stopwatch, human_readable

@pytest.fixture
def sw():
    """Provides a fresh stopwatch instance for each test"""
    return Stopwatch()

# Basic functionality tests
def test_init():
    """Test initialization of the stopwatch"""
    # Default initialization
    sw = Stopwatch()
    assert len(sw._laps) == 0
    assert sw._name == "stw"
    assert not sw._verbose
    
    # Named initialization
    sw = Stopwatch(name="test_timer")
    assert sw._name == "test_timer"
    
    # Verbose initialization
    sw = Stopwatch(verbose=True)
    assert sw._verbose

def test_lap_functionality(sw):
    """Test the lap functionality"""
    # Record a lap
    total_time, lap_time = sw.lap("first")
    assert lap_time > 0
    assert total_time > 0
    assert len(sw.laps) == 1
    assert sw.laps[0][0] == "first"
    
    # Record another lap
    time.sleep(0.1)
    total_time, lap_time = sw.lap("second")
    assert lap_time >= 0.1
    assert total_time > 0
    assert len(sw.laps) == 2
    
    # Auto-naming
    total_time, lap_time = sw.lap()
    assert sw.laps[2][0] == "lap 3"

def test_get_lap(sw):
    """Test retrieving lap information"""
    sw.lap("test_lap")
    time.sleep(0.1)
    sw.lap("second_lap")
    
    # Get by name
    timestamp, total_time, lap_time = sw.get_lap(name="test_lap")
    assert timestamp > 0
    assert total_time > 0
    assert lap_time > 0
    
    # Get by index
    timestamp, total_time, lap_time = sw.get_lap(index=0)
    assert timestamp > 0
    assert total_time > 0
    assert lap_time > 0
    
    # Error cases
    with pytest.raises(ValueError):
        sw.get_lap(index=0, name="test_lap")
    
    with pytest.raises(ValueError):
        sw.get_lap()
    
    with pytest.raises(ValueError):
        sw.get_lap(name="nonexistent")
    
    with pytest.raises(ValueError):
        sw.get_lap(index=2)  # Out of bounds

def test_elapsed_time_methods(sw):
    """Test the various elapsed time methods"""
    # Record some laps with delays
    sw.lap("first")
    time.sleep(0.1)
    sw.lap("second")
    time.sleep(0.2)
    sw.lap("third")
    
    # Test elapsed_total
    total = sw.elapsed_total()
    assert total > 0.3
    
    # Test elapsed_total with specific lap
    total_until_second = sw.elapsed_total("second")
    assert 0.1 <= total_until_second < total
    
    # Test elapsed_since_lap
    time.sleep(0.1)
    since_third = sw.elapsed_since_lap()  # Default to last lap
    assert since_third >= 0.1
    
    since_first = sw.elapsed_since_lap("first")
    assert since_first >= 0.4  # first + 0.1 + second + 0.2 + third + 0.1

def test_context_manager():
    """Test using stopwatch as a context manager"""
    with Stopwatch(name="context_test") as sw:
        time.sleep(0.1)
        assert len(sw.laps) == 1
        assert sw.laps[0][0] == "start"
        
        total_time, lap_time = sw.lap("middle")
        assert lap_time >= 0.1
    
    # After exiting context
    assert len(sw.laps) == 3
    assert sw.laps[2][0] == "done"
    total_duration = sw.elapsed_total()
    assert total_duration >= 0.1

def test_nested_stopwatches():
    """Test nested stopwatch usage from README example"""
    with Stopwatch(name="outer") as outer:
        time.sleep(0.1)
        
        with Stopwatch(name="inner") as inner:
            time.sleep(0.1)
            
        # Inner should have completed
        assert len(inner.laps) >= 2
        assert inner.elapsed_total() >= 0.1
        
        # Outer continues
        time.sleep(0.1)
    
    # Outer should include all time
    assert outer.elapsed_total() >= 0.3

def test_time_function(sw):
    """Test timing function execution"""
    def example_function(a, b):
        time.sleep(0.1)
        return a + b
    
    # Basic test
    time_taken, result = sw.time_function(example_function, 2, 3)
    assert time_taken >= 0.1
    assert result == 5
    assert len(sw.laps) == 2
    assert "start" in sw.laps[0][0]
    assert "done" in sw.laps[1][0]

def test_stopwatch_decorator():
    """Test the @stopwatch decorator"""
    @stopwatch
    def decorated_function(x, y):
        time.sleep(0.1)
        return x * y
    
    # When called, should automatically time and return result
    result = decorated_function(6, 7)
    assert result == 42  # Function should return normally

def test_human_readable():
    """Test the human_readable function"""
    # Test seconds only
    assert human_readable(5.25) == "5.25s"
    
    # Test minutes and seconds
    assert human_readable(65.5) == "1m 5.50s"
    
    # Test hours, minutes, seconds
    assert human_readable(3725.75) == "1h 2m 5.75s"

def test_print_diagram(sw, capsys):
    """Test the diagram printing functionality"""
    # Record some laps
    sw.lap("first")
    time.sleep(0.1)
    sw.lap("second")
    time.sleep(0.2)
    sw.lap("third")
    
    # Print the diagram
    sw.print_diagram()
    
    # Capture the output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify basic elements appear in output
    assert sw._name in output
    assert "first" in output
    assert "second" in output
    assert "third" in output
    assert "│" in output  # Diagram boundary character

def test_string_representation(sw):
    """Test string representation methods"""
    # Initial representation
    sw.lap("first")
    s = str(sw)
    assert sw._name in s
    assert "total_time" in s
    
    # With multiple laps
    sw.lap("second")
    s = str(sw)
    assert "elapsed_until_last_lap" in s

def test_readme_examples():
    """Test the examples shown in the README file"""
    # Quick start example
    sw = Stopwatch(name="quickstart")
    sw.lap("begin")
    time.sleep(0.1)
    sw.lap("end")
    total = sw.elapsed_total()
    assert total >= 0.1
    
    # Database operations example
    sw = Stopwatch(name="database-ops")
    sw.lap("begin")
    time.sleep(0.1)
    total_time, lap_time = sw.lap("query")
    assert lap_time >= 0.1
    time.sleep(0.1)
    total_time, lap_time = sw.lap("processing")
    assert lap_time >= 0.1
    assert total_time >= 0.2
    
    # Function benchmarking example
    def calculation(n, factor=2):
        time.sleep(n * 0.01)
        return n * factor
    
    sw = Stopwatch()
    time_taken, result = sw.time_function(calculation, 5, factor=3)
    assert time_taken >= 0.05
    assert result == 15
