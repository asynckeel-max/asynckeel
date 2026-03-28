# Test Utility Functions


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
        msg = f"Expected {exception_type} but got {type(e).__name__}"
        raise AssertionError(msg) from e
    else:
        msg = f"Expected {exception_type} but no exception was raised"
        raise AssertionError(msg)
