from spatial import Point, Parcel
from shapely.geometry import Polygon
import json


# print("\n--- Challenge 2 ---\n")
# ------------------------------
# Challenge 1
# ------------------------------
#   row = {"id": "A", "lon": 121.0, "lat": 14.6, "name": "Gate", "tag": "POI"}

#   try: 
#       p = Point.from_dict(row)
#       print("Valid Point created successfully:")
#       print(p.as_dict())
#   except ValueError as e:
#       print ("Error creating Point from valid data:", e)

#   row_invalid = {"id": "B", "lon": 999.0, "lat":15.5, "name": "Point B","tag": "POI"}

#   try:
#       r_invalid = Point.from_dict(row_invalid)
#       print("Invalid Point created successfully:")
#       print(r_invalid.as_dict())
#   except ValueError as e:
#   print("Error creating Point from invalid data:", e)


# ------------------------------
# Challenge 2
# ------------------------------

print("\n--- Challenge 2 ---\n")

row = {"id": "A","name": "Gate", "tag": "POI", "geometry": (121.0, 14.6)}

try:
    print("Valid Point created successfully:")

    p = Point.from_dict(row)
    data = p.as_dict()
    data["geometry"] = str(data["geometry"])
    data["bbox"] = str(data["bbox"])

    print(json.dumps(data, indent=3))

except ValueError as e:
    print ("Error creating Point from valid data:", e)

print("\n--- Parcel Test ---")

geom = Polygon([
    (0,0),
    (10,0),
    (10,5),
    (0,5)
 ])

attrs = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}

parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs)
parcel_data = parcel.as_dict()
parcel_data["bbox"] = str(parcel_data["bbox"])
print(json.dumps(parcel_data, indent=3))



# ------------------------------
# Challenge 3
# ------------------------------

print("\n--- Challenge 3 ---\n")

geom = Polygon([
    (121.0, 14.0),
    (121.0, 15.0),
    (122.0, 15.0),
    (122.0, 14.0)
])

attrs = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}

parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs)
point_in = Point.from_dict({"id": "A", "geometry": (121.5, 14.5), "name": "Inside", "tag": "POI"})
point_out = Point.from_dict({"id": "B", "geometry": (122.4, 14.3), "name": "Outside", "tag": "POI"})
print(f"point_in.intersects(parcel): {point_in.intersects(parcel)}") 
print(f"point_out.intersects(parcel): {point_out.intersects(parcel)}") 
