from my_funcs.test import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5), (20, 4, 5), (100, 10, 10)])
def test_division_great(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, divide", [(ZeroDivisionError, 0), (TypeError, "2")])
def test_zero_division(expected_exception, divide):
    with pytest.raises(expected_exception):
        division(100, divide)

