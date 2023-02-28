from utils import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (15, -3, -5),
                                                   (10, 2.5, 4)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, divisionable, divider", [(ZeroDivisionError, 10, 0),
                                                                       (TypeError, 20, "2")])
def test_division_with_error(expected_exception, divisionable, divider):
    with pytest.raises(expected_exception):
        division(divisionable, divider)
