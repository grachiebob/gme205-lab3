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
        return (self.geometry.bounds)
    
    def intersects(self, other) -> bool:               #Add an intersects() method to SpatialObject
        return self.geometry.intersects(other.geometry)

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

    @classmethod                    # implement a class method from_dict() in Point
    def from_dict(cls, d: dict):
        lon = d.get("geometry", (None, None))[0]
        lat = d.get("geometry", (None, None))[1]
        if lon is None or lat is None:
            raise ValueError(f"Longitude or Latitude missing in input: {d}")
        
        return cls(
            id=d.get("id"),
            lon=float(lon),
            lat=float(lat),
            name=d.get("name"),
            tag=d.get("tag")
        )
    
    def as_dict(self):              # implement as_dict() in Point
        return {
            "id": self.id,
            "name": self.name,
            "tag": self.tag,
            "geometry": self.to_tuple(),
            "bbox": self.bbox()
        }
    
    def to_tuple(self):
        return (self.geometry.x, self.geometry.y)

    def distance_to(self, other):
        return self.geometry.distance(other.geometry)
    
    
class Parcel(SpatialObject):
    """
    Parcel = spatial object + structured attributes.
    """

    def __init__(self, parcel_id, geometry, attributes: dict):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.attributes = attributes

    def as_dict(self):                      # implement as_dict() in Parcel
        return {
            "parcel_id": self.parcel_id,
            "bbox": self.bbox(),
            "attributes": self.attributes
        }