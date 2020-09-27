import pytest
from geospatial.arcgis import arcGIS


@pytest.fixture
def create_object():
    gis = arcGIS()
    return gis


def test_arcgis_initializes(create_object):
    gis = create_object
    assert isinstance(gis, arcGIS)


def test_geocode(create_object):
    gis = create_object
    lon, lat = gis.geocode('211 Mains St, San Francisco, CA 94105')
    assert round(lon, 5) == -122.39270
    assert round(lat, 5) == 37.79059


def test_returns_output_format_error(create_object):
    gis = create_object
    with pytest.raises(Exception):
        assert gis.geocode('211 Main St, San Francisco, CA 94105', f='test')


def test_returns_address_format_error(create_object):
    gis = create_object
    with pytest.raises(Exception):
        assert gis.geocode(1234)


@pytest.fixture
def create_mock_object(mocker):
    gis = arcGIS()
    mocker.patch("geospatial.arcgis.arcGIS.geocode", return_value={})
    return gis


def test_returns_response_code_error(create_mock_object):
    gis = create_mock_object
    with pytest.raises(Exception):
        assert gis.geocode('211 Main St, San Francisco, CA 94105')



