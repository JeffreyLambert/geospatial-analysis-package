# Geospatial Tools

## Description
This package contains a class which makes it easy to access the 
find address geocode endpoint of the ArcGIS REST API.  It extends this
by adding a class which allows you calculate the distance between
two cartesian geographic coordinates.

## Installation

The package can be installed using the *.tar.gz file located in the
"dist" folder.

```bash
pip install geospatial-tools-0.0.1.tar.gz
```

## Usage

```python
from geospatial.arcgis import arcGIS

gis = arcGIS()
gis.geocode('211 Main St San Francisco, CA 94105')
```

```python
from geospatial.distances import Haversine

hvs = Haversine(lat_1=47.620422, lat_2=37.8196
                lon_1=-122.349358, lon_2=-122.4785)
hvs.miles
```

## Motivation & Details
This python package was born out of a geospatial analysis
I was performing for Charles Schwab.  

This package provides an idea of the work involved with that project.

By geocoding our branch locations,
we were able to calculate the distance from any zip code to the branch of interest.
We then used this information to determine how far from a branch do you need to go
to account for the majority of their assets.  The data captured in this ETL
processed was utilized downstream to aid the branch network target setting process.

The ETL for the geospatial portion of the analysis went as follows:
1. Retrieve locations from SQL database
2. Geocode locations using ArcGIS
3. Calculate the distance (miles) between branches and zip codes
4. Sort the zip codes by distance
5. Calculate the percentage of cumulative assets accounted for
at each zip code
6. Write this analysis to a SQL table in our team HDM

Technologies utilized
- Bash
- SQL
- Python

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Project Status
Development is not continuing on this package.  It is currently meant
only as a project for my Data Science Portfolio.