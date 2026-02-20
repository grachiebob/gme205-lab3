from spatial import Point

p = Point("A", 121.0, 14.6)
print(p.id, p.geometry.x, p.geometry.y)
print(p.to_tuple())

q = Point("X", 122.0, 14.0)
print(q.id, q.geometry.x, q.geometry.y)
print(q.to_tuple())

# ----------------------------------
# Distance Test
# ----------------------------------

print("------------------------------")
print("Distance Test")

p = Point("A", 121.0, 14.6)
print(p.id, p.geometry.x, p.geometry.y)

q = Point("B", 129.0, 17.0)
print(q.id, q.geometry.x, q.geometry.y)

print(p.distance_to(q))