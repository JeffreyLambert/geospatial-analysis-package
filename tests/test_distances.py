import pytest
import numpy as np
from geospatial.distances import Haversine

location_pairs = [
        (47.620422, -122.349358)  # Seattle Space Needle
        , (37.8196, -122.4785)  # San Francisco Golden gate bridge
        , (41.882702, -87.619392)  # Millennium Park, Chicago IL
        , (41.0, np.nan)
    ]


@pytest.mark.parametrize("test_input,expected",
                         [
                             # Test that distance to self is zero
                             ([location_pairs[0], location_pairs[0]], 0),
                             # Test that missing location returns nan
                             ([location_pairs[0], (np.nan, np.nan)], np.nan),
                             # Test that incomplete pair returns nan
                             ([location_pairs[0], location_pairs[3]], np.nan)
                          ])
def test_returns_distance_of_zero_or_nan(test_input, expected):
    lat_1, lon_1 = test_input[0]
    lat_2, lon_2 = test_input[1]
    hvs = Haversine(lat_1=lat_1, lat_2=lat_2, lon_1=lon_1, lon_2=lon_2)
    np.testing.assert_equal(hvs.km, expected)
    np.testing.assert_equal(hvs.miles, expected)


def test_pair_order_does_not_matter():
    lat_1, lon_1 = location_pairs[0]
    lat_2, lon_2 = location_pairs[1]
    hvs1 = Haversine(lat_1=lat_1, lat_2=lat_2, lon_1=lon_1, lon_2=lon_2)
    hvs2 = Haversine(lat_1=lat_2, lat_2=lat_1, lon_1=lon_2, lon_2=lon_1)
    assert hvs1.km == hvs2.km
    assert hvs1.miles == hvs2.miles


@pytest.mark.parametrize(
    "test_input,expected_km,expected_miles",
    [
        ([location_pairs[0], location_pairs[1]], 1089.85230, 677.20262),
        ([location_pairs[0], location_pairs[2]], 2790.72129, 1734.07328)
    ]
)
def test_returns_correct_distance(test_input, expected_km, expected_miles):
    lat_1, lon_1 = test_input[0]
    lat_2, lon_2 = test_input[1]
    hvs = Haversine(lat_1=lat_1, lat_2=lat_2, lon_1=lon_1, lon_2=lon_2)
    assert round(hvs.km, 5) == expected_km
    assert round(hvs.miles, 5) == expected_miles
