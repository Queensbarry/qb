import numpy as np
from numpy.testing import assert_equal, assert_raises
from qb.statistics.tool import check_two_array


def test_check_two_array():
    a = [1, 2, 3]
    b = [1, 2, 3, 4]

    assert_equal(check_two_array(a, b), (a, b))
    with assert_raises(ValueError):
        check_two_array(a, b, is_same_shape=True)

    c = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    d = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    assert_equal(check_two_array(c, d, is_same_size=True), (c, d))
    with assert_raises(ValueError):
        check_two_array(a, b, is_same_shape=True)

    e = [
        [1, np.nan, 3],
        [4, 5, 6]
    ]
    f = [
        [9, 2, 3],
        [4, np.nan, 6]
    ]
    e_desired = [1, 3, 4, 6]
    f_desired = [9, 3, 4, 6]
    assert_equal(check_two_array(e, f, is_clean_same_time=True), (e_desired, f_desired))

    with assert_raises(RuntimeWarning):
        check_two_array(e, f, is_clean_same_time=True, is_nan_warning=True, nan_warning_criterion=0.01)
