# Test Utility Functions

# This file contains utility functions and helpers for testing.


def assert_equal(a, b):
    """Asserts that two values are equal."""
    assert a == b, f"Expected {a} to be equal to {b}"


def assert_raises(exception_type, func, *args, **kwargs):
    """Asserts that a specific exception is raised when calling a function."""
    try:
        func(*args, **kwargs)
    except exception_type:
        return
    except Exception as e:
        raise AssertionError(
            f"Expected {exception_type} but got {type(e).__name__}"
        ) from e
    else:
        raise AssertionError(f"Expected {exception_type} but no exception was raised")


# Add more utility functions and helpers as needed.
