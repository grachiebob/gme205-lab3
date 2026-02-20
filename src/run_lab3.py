from spatial import Point

row = {"id": "A", "lon": 121.0, "lat": 14.6, "name": "Gate", "tag": "POI"}

try: 
    p = Point.from_dict(row)
    print("Valid Point created successfully:")
    print(p.as_dict())
except ValueError as e:
    print ("Error creating Point from valid data:", e)

row_invalid = {"id": "B", "lon": 999.0, "lat":15.5, "name": "Point B","tag": "POI"}

try:
    r_invalid = Point.from_dict(row_invalid)
    print("Invalid Point created successfully:")
    print(r_invalid.as_dict())
except ValueError as e:
    print("Error creating Point from invalid data:", e)