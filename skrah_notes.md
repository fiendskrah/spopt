# Spopt notes

## Binder (using chrome on linux)
```Your session is taking longer than usual to start!``` 
server launch ~ 6 mins 30 secs
"/docs/notesbooks/" and "/notebooks" - redundancy?

### "/notebooks/azp.ipynb"
very light on narrative
summary or excerpt from Openshaw and Rao (1995)?
comments on code or summary after cell?
what does AZP stand for?

`Cluster 32 Mexican states into 8 regions using AZP algorithm (Openshaw, S. and
Rao, L. (1995)).` 

cell 8 narrative - the azp function and its parameters (what can you do?)
a side-by-side of before and after in the last cell

The full list of parameters for the AZP class can be found on the
[AZP API
page](https://pysal.org/spopt/generated/spopt.region.AZP.html#spopt.region.AZP)

### "/notebooks/maxp.ipynb"

https://splot.readthedocs.io/en/stable/users/tutorials/region.html

https://pysal.org/spopt/generated/spopt.region.MaxPHeuristic.html#spopt.region.MaxPHeuristic

cell 7 - the maxP function and its parameters (what can you do?)

Cell 8 - # How many regions do we have?

The full list of parameters for the MaxPHeuristic class can be found on the [MaxPHeuristic API
page](https://pysal.org/spopt/generated/spopt.region.MaxPHeuristic.html#spopt.region.MaxPHeuristic)

### "/notebooks/reg-k-means.ipynb"

No narrative
This one is pretty opaque to me. I'm unsure of the purpose of the k-means functions
and I can't really interpret how the array is changing. 

The full list of parameters for the RegionKMeans class can be found on the
[RegionKMeans API
page](https://pysal.org/spopt/generated/spopt.region.RegionKMeansHeuristic.html#spopt.region.RegionKMeansHeuristic)
### "/notebooks/skater.ipynb"

"Cluster 77 communities into 10 regions such that each region consists of at
least 3 communities and homogeneity in the number of Airbnb spots in communities
is maximized."

This one is good. Some detail about how the airbnb's are dispersed acrosss the
communities could be nice. a legend or .head() or something?

The full list of parameters for the Skater class can be found on the
[Skater API
page](https://pysal.org/spopt/generated/spopt.region.Skater.html#spopt.region.Skater)

### "/notebooks/ward.ipynb"

what is the constraint and why?

The full list of parameters for the WardSpatial class can be found on the
[WardSpatial API
page[(https://pysal.org/spopt/generated/spopt.region.WardSpatial.html#spopt.region.WardSpatial)

## link to api page for specific parameters. 

The full list of parameters for the Spenc class can be found on the
[Spenc API
page](https://pysal.org/spopt/generated/spopt.region.Spenc.html#spopt.region.Spenc)



# notes 1/27

urban institute meeting 
    API - being developed/reworked by UI
    and vice president for general research purposes.

they're doing lots of restructuring
pushes roadmap back - can't build on API until it's more stable

school research papers line up with gate's goals.

regulating shcool redistrciting - optimization problem?

Table - for census, what is available at what level (blocks, groups, tracts)

kick the tires on this: https://github.com/pysal/tobler/blob/master/notebooks/binary_dasymetric.ipynb