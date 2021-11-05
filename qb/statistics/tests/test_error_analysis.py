from numpy.testing import assert_almost_equal
from qb.statistics.error_analysis import me


def test_me():
    f = [1.2, 2.3, 3.4, 4.5, 5.6]
    o = [1.2, 2.4, 3.3, 4.4, 5.6]

    assert_almost_equal(me(f, o), 0.0199, decimal=4)

    f = [
        [1.2, 2.3, 3.4, 4.5, 5.6],
        [1.2, 2.4, 3.3, 4.4, 5.6]
    ]
    o = [
        [1.2, 2.4, 3.3, 4.4, 5.6],
        [1.2, 2.3, 3.4, 4.5, 5.6]
    ]
    assert_almost_equal(me(f, o), 0.0, decimal=4)
