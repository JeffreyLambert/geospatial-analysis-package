import requests


class arcGIS:
    """ Tools for making requests to arcGIS REST API

    The arcGIS class provides a wrapper for making requests to the arcGIS REST API.

    Example::

        gis = arcGIS()
        gis.geocode('211 Mains St, San Francisco, CA 94105')

        lon, lat = gis.lonlat

    """