import pytest

from calculator import simple_calculator


@pytest.mark.parametrize("num_1, num_2, operation, expected_result", [(3, 3, "+", 6),
                                                                      (10, 2, '/', 5),
                                                                      (15, 5, "+", 20),
                                                                      (12, 4, "-", 8)])
def test_simple_calculator(num_1, num_2, operation, expected_result):
    result = simple_calculator(num_1, num_2, operation)
    assert result == expected_result
