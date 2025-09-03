import geopandas as gpd
import pandas, numpy, pyvrp, sys
sys.path.insert(0, '/home/dylan/projects/gsoc2025/spopt/') # active development
import spopt
from spopt.route import engine, heuristic, utils
from spopt.route.heuristic import LastMile
from pyvrp.stop import MaxIterations

import pytest

def test_lastmile_route():
        trucks = pandas.DataFrame(
        [['big', 'lng',      2000,    280, .004,  .50, 5],
        ['big', 'electric', 2000,    480, .002,  .50, 5],
        ['med', 'lng',      800, 280*.66, .0001, .63, 10],
        ['med', 'electric', 800, 480*.66, .004,  .50, 10],
        ['smo', 'lng',      400, 280*0.4, .002,  .50, 20],
        ['smo', 'electric', 400, 480*0.4, .0001, .63, 20],
        ],
        columns = [
            'namesize', 'namefuel', 'capacity', 
            'fixed_cost', 'cost_per_meter', 'cost_per_minute', 'n_truck'
            ]
    )

    gdf = gpd.read_file('/home/dylan/projects/gsoc2025/spopt/notebooks/gsoc2025/data/dublinpubs.geojson')
    clients = gdf.iloc[1:,:].reset_index(drop=True)
    clients = clients.set_index(clients.osmid.astype(str))
    depot = gdf.iloc[0,:]

    print('initializing model')
    m = LastMile(
        depot_location=(depot.longitude.item(), depot.latitude.item()),
        depot_open=pandas.Timestamp("2030-01-02 07:00:00"),
        depot_close=pandas.Timestamp("2030-01-02 20:00:00"),
        depot_name=depot['name'],
    )

    print("adding clients")
    m.add_clients(
        locations = clients.geometry, 
        delivery = clients.demand,
        pickup = clients.supply,
        time_windows=None,
        service_times=(numpy.log(clients.demand)**2).astype(int)
    )

    print("adding trucks")
    m.add_trucks_from_frame(
        trucks, 
    )

    m.solve(stop=MaxIterations(50_000), seed=0, display=False)
    
    assert m.result_.is_feasible()
    expected_solution = 174870190
    assert m.result_.cost() == pytest.approx(expected_solution, rel=1e-9)
