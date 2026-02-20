#from spatial import Point

#p = Point("A", 121.0, 14.6)
#print("BBox:", p.bbox())
#print("Tuple:", p.to_tuple())

#q = Point("X", 122.0, 14.0)
#print("BBox:", q.bbox())
#print("Tuple:", q.to_tuple())

from shapely.geometry import Polygon
from spatial import Parcel

# a simple rectangle polygon sample
geom = Polygon([
    (0,0),
    (10,0),
    (10,5),
    (0,5)
])

#Dictionary for added structure
attrs = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}

parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs)

print("Parcel BBox:", parcel.bbox())
print("Parcel Zone:", parcel.attributes["zone"])
