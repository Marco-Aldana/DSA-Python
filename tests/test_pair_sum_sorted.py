import pytest
from solutions.pair_sum_sorted import testing_pytest_integration

@pytest.mark.parametrize("num1, num2, result",[
    (2,2,4),
    (3,5,8),
    (0,0,0),
])
def test_sumilla_sums_2_positive_numbers(num1, num2, result):
    assert testing_pytest_integration(num1, num2) == result
    