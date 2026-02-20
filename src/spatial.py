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

class SpatialObject:
    """
    Base class for anything that exists in space.
    Stores goemetry and provides shared spatial behavior.
    """

    def __init__(self, geometry):
        self.geometry = geometry

    def bbox(self):
        """
        Return bounding box as (minx, miny, maxx, maxy).
        """
        return self.geometry.bounds    

class Point(SpatialObject):

    def __init__(self, id, lon, lat, name=None, tag=None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        
        geometry = ShapelyPoint(lon, lat)
        super().__init__(geometry)
        
        self.id = id
        self.name = name
        self.tag = tag

    @classmethod                    # implemeent a class meethod from_dict in Point
    def from_dict(cls, d: dict):
        return cls(
            id=d.get("id"),
            lon=d.get("lon"),
            lat=d.get("lat"),
            name=d.get("name"),
            tag=d.get("tag")
        )
    
    def as_dict(self):
        return {
            "id": self.id,
            "lon": self.geometry.x,
            "lat": self.geometry.y,
            "name": self.name,
            "tag": self.tag   
        }
    
    def to_tuple(self):
        return (self.geometry.x, self.geometry.y)

    def distance_to(self, other):
        return self.geometry.distance(other.geometry)
    
class Parcel(SpatialObject):
    """
    Parcel = spatial oject + sturtcured attributes.
    """

    def __init__(self, parcel_id, geometry, attributes: dict):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.attributes = attributes
