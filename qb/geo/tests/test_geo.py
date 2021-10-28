from numpy.testing import assert_almost_equal
from qb.geo import area, distance, AreaUnit, DistanceUnit


def test_distance():
    p1 = (10.0, 15.2)
    p2 = (11.2, 28.3)

    assert_almost_equal(
        distance(p1, p2, unit=DistanceUnit.METERS),
        1437867.76,
        decimal=2
    )


def test_area():
    p1 = (10.0, 15.2)
    p2 = (11.2, 28.3)
    p3 = (13.2, 15.4)

    desired = 263677089187.0281
    assert_almost_equal(area(p1, p2, p3, unit=AreaUnit.METERS2), desired, decimal=2)
