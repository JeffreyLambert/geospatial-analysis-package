import numpy as np
from math import pi


class Haversine:
    """
    The Haversine class is used to calculate the haversine distance between two geolocation points denoted by
    latitude and longitude.

    The haversine function returns the distance between two points on the surface of a sphere, such as the earth.

    This class receives two pairs of coordinates and returns a class object with attributes for the
    haversine distance available in kilometers and miles.

    Example::

        distances = Haversine(lat_1, lat_2, lon_1, lon_2)
        distances.miles
    """

    def __init__(self, lat_1, lat_2, lon_1, lon_2):
        """

        :param lat_1: Latitude for location 1
        :param lat_2: Latitude for location 2
        :param lon_1: Longitude for location 1
        :param lon_2: Longitude for location 2
        """

        R = 6371000  # Radius of earth

        phi_1 = lat_1 * (pi / 180)
        phi_2 = lat_2 * (pi / 180)

        delta_phi = (lat_2 - lat_1) * (pi / 180)
        delta_lambda = (lon_2 - lon_1) * (pi / 180)

        a = (np.sin(delta_phi / 2) * np.sin(delta_phi / 2)) + \
            (np.cos(phi_1) * np.cos(phi_2)) * \
            (np.sin(delta_lambda / 2) * np.sin(delta_lambda / 2))

        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

        d = R * c  # Distance in meters

        self.km = d / 1000  # Conversion to kilometers
        self.miles = d * 0.000621371  # Conversion to miles
