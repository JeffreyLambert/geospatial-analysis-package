import requests


class arcGIS:
    """ Tools for making requests to arcGIS REST API

    The arcGIS class provides a wrapper for making requests to the arcGIS REST API.

    Example::

        gis = arcGIS()
        gis.geocode('211 Mains St, San Francisco, CA 94105')

        lon, lat = gis.lonlat

    """


    def __init__(self):
        """Initializes arcGIS class"""
        self.api_url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"


    def geocode(self, address: str, f: str = 'json') -> tuple:
        """
        Return a longitude and latitude tuple for a given street address.

        :param str address: Full address string to be geocoded.  Should contain
            street address, city, state, and zip.
        :param str f: response type which can be either 'json' or 'pjson'.  Default is 'json'.
        :return: longitude, latitude tuple.
        """

        assert (f in ['json', 'pjson']), "f must be 'json' or 'pjson'"
        assert (type(address) == str), "Address must be a string"

        url_params = dict(
            f=f,
            singleLine=address,
            outFields='Match_addr,Addr_type'
        )

        response = requests.get(
            self.api_url
            , params=url_params
        )

        assert (response.status_code == 200), f"Connection to ArcGIS failed with error code {response.status_code}"

        try:
            coordinates = response.json()['candidates'][0]['location']
            lat = coordinates['y']
            lon = coordinates['x']

            return lon, lat

        except AssertionError as error:
            print(error)
            print('No response was retrieved')
