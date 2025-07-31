import routingpy
from routingpy import OSRM, Valhalla

import os
import numpy
import requests
import warnings
import geopandas
import pandas
import shapely
from sklearn import metrics


def build_specific_route(waypoints,
                         return_durations=True,
                         **kwargs):
    
    '''
    Parameters
    ----------
    
    waypoints : list, required
         A list of coordinate pairs between which to path a vehicular route.
         The coordinates are also expected as a list.
         e.g.: [[-6.2288162, 53.365756], [-6.2652379, 53.330686]].
    
    return_durations : boolean, required
         Set to ``True`` to return durations for each leg.
         Default is ``True``.

    routing : dictionary, optional
        Specifies which engine and associated parameters to utilize for the request.
        Supported engines:
            OSRM - Open Source Routing Machine


    Returns
    -------
    
    route_shape : geometry
        A linestring reflecting the shortest path between the inputed waypoints.

    leg_duration : numpy.array
        An array of the durations on each leg of the route.
    '''
    engine = kwargs.get("routing")
    
    # Step 1: Get directions
    directions = engine.directions(
        locations=waypoints,
        geometries='geojson',
        annotations=True
    )

    # Step 2: Extract geometry and durations
    route_coords = directions.geometry  # List of (lon, lat)
    route_shape = shapely.LineString(route_coords)

    # Step 3: Durations per leg
    legs = directions.raw['routes'][0]['legs']
    leg_durations = numpy.array([leg['duration'] for leg in legs])

    # Step 4: Validate leg count (len(legs) == len(waypoints) - 1)
    numpy.testing.assert_array_equal(
        len(legs),
        len(waypoints) - 1
    )

    if return_durations:
        return route_shape, leg_durations
    else:
        return route_shape


def build_route_table(demand_sites,
                      candidate_depots,
                      cost='distance',
                      **kwargs):
    
    '''
    parameters:
    demand_sites = a list of coordinates pairs for clients. The coordinates are also expected 
    as a list, e.g.: [[-6.2288162, 53.365756], [-6.2652379, 53.330686]]
    
    candidate_depots = a list of coordinate pairs for depot(s).The coordinates are also expected 
    as a list, e.g.: [[-6.2288162, 53.365756]
    
    returns tuple (distance_matrix, duration_matrix)

    
    '''
    engine = kwargs.get("routing")
    routing_kws = kwargs.get("routing_kws", {})
                       
    candidate_series = pandas.Series([tuple(coord) for coord in candidate_depots])
    demand_series = pandas.Series([tuple(coord) for coord in demand_sites])
    all_points = pandas.concat((candidate_series, demand_series)).reset_index(drop=True)
    
    # Set annotation type
    if cost == 'distance':
        annotations = ['distance']
    elif cost == 'duration':
        annotations = ['duration']
    elif cost == 'both':
        annotations = ['distance', 'duration']
    else:
        raise ValueError(f"Unsupported cost type '{cost}'")

    print("Extra kwargs:")
    print(kwargs)
    if isinstance(engine, OSRM):
        
        result = engine.matrix(
            locations=all_points,
            annotations=annotations,
        )

    elif isinstance(engine, Valhalla):
        profile = routing_kws.get("profile")
        print(profile)
        result = engine.matrix(
            locations=all_points,
            annotations=annotations,
            profile=profile
        )
        
    else:
        raise ValueError(f"Unsupported engine '{engine}'")
    
    # Parse outputs
    distances = numpy.asarray(result.distances).astype(float) if 'distance' in annotations else None
    durations = numpy.asarray(result.durations).astype(float) if 'duration' in annotations else None

    return (distances, durations)
