from shapely.geometry import Point as ShapelyPoint


class Point:
    def __init__(self, id, lon, lat, name=None, tag=None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        
        self.id = id
        self.geometry = ShapelyPoint(lon, lat)
        self.name = name
        self.tag = tag
  
    def to_tuple (self):
        return (self.geometry.x, self.geometry.y)
    
    def distance_to(self, other):
        return self.geometry.distance(other.geometry)
    
