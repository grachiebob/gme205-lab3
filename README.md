# GmE 205: Laboratory 3
## Spatial Object Systems: Shapely, Inheritance, and Structured Data

### *Description*
This project basically extends Laboratory Exercise 2’s spatial framework by using *Shapely* for geometric objects, introducing a base class with inheritance, and adding structured dictionary attributes, while preserving responsibility boundaries and avoiding a *God Object.* 

### *Dependencies*
* Python 3.14
* Visual Studio Code
* GitHub
* pandas
* matplotlib
* shapely

### *How to set up the virtual environment?*
This is the first thing to do before starting this exercise. Here are the steps to set up a virtual environment:
1. Open the Visual Studio Code.
2. Under the VS Code Terminal tab, select "New Terminal."
3. Run this code:<br>
        `py -m venv .venv`<br>
        `.\.venv\Scripts\activate`<br>

### *Refactor Point to Use Shapely*
In the previous exercise, the CSV file stored the coordinates as raw numbers. This project converts these raw numbers into geometry objects, such as points, while Shapely handles all the spatial and mathematical operations.

#### *Reflection*
The `Point` class does not store raw coordinates or longitude or latitude values (`self.lon`, `self.lat`) as separate attributes. Instead, a `ShapelyPoint` object stores the coordinates assigned to `self.geometry` internally. Some functions or methods used in the previous exercise, such as `to_tuple()`, remain unchanged, wherein users can still call these methods with the same responsibility without needing to know about the internal changes or processes. The spatial processing is assigned to Shapely, which performs geometry operations, such as the `distance_to()` function. The `Point` class do not need to use formulas manually, since Shapely automatically computes them.

### *Designing a Spatial Hierarchy*
These objects share a common structure through a base class (`SpatialObject`). For instance, instead of each shape carrying its own geometry computation and storage, they all share the same centralized spatial behavior provided by the base class. 

#### *Reflection*
An abstraction represents only the important features while keeping the complex detail about the *thing*.  The base class `SpatialObject` becomes an abstraction because it defines the shared common properties in which the system does not care what specific type the geometry objects are, whether it’s a point or a parcel. In the real-world, it represents that all spatial features exist and have a location in space. Inheritance allows `Point` and `Parcel` subclasses to share common spatial behaviors, such as the bounding box method and geometry-storing code, found in `SpatialObject` without having the need to rewrite it. Moreover, the Dictionary creates an organization for the attributes of the Parcel. It does not affect the actions or behaviors of the Parcel. For instance, it stores values like area and zone but does not provide an additional action to manipulate the Parcel itself. <br>
If a new action such as `distance_to()`is added to the `SpatialObject`, the inheritance is already established wherein the subclasses `Point` and `Parcel` will automatically perform the added function. Once the base class receives a new function, the subclass will automatically utilize it, since the goal of inheritance is to avoid rewriting the same method. This hierarchical design is straightforward and makes it easier and more efficient to extend the code from the previous exercise. The base class was established so that all functions are inherited by the subclasses. Adding a subclass is easier, since the functionality from the base class does not need to be rewritten.

### *Challenge Exercise*
These challenges aim to implement `from_dict()` in Point, `as_dict()` in Point and Parcel, and `intersects()` in SpatialObject, which is automatically inherited by Point and Parcel subclasses. 

### *Reflection*
1.	In the Point class, the `__init__`constructor already contains the rules to validate longitude and latitude. There is no need to rewrite these conditions every time a Point is created or a geometry is called, since `from_dict()` delegates validation to the constructor to refrain from duplicating the condition and ensuring that all created objects are validated automatically.<br> 
2.	The `as_dict()` is placed inside the object rather than in the running script because the object already stores its own data and knows how it should be returned or represented. For instance, it was placed in the Parcel subclass, and once it is called, it automatically provides the bounding box and other attributes of `Parcel`. <br>
3.	The `as_dict()` only returns numbers, strings, tuples, and other primitive data types because these can be easily stored and printed by a database. For instance, JSON was imported to easily print the stored attributes in `as_dict()`. Shapely geometry objects are more complex to process since it handles spatial operations, while JSON is limited in printing lists or basic structures.<br>
4.	Any function in the `SpatialObject` base class will be inherited by the `Point` and `Parcel` subclasses. Both subclasses need intersection checks to see overlapping geometries, which is why it is placed in the base class. In this way, these subclasses can consistently perform the functionality.<br>
5.	If a new subclass (`Building`) is added under the `SpatialObject` base class, there is no need to change or write an extra code to satisfy `intersects()` since the `intersect()` already belongs to the `SpatialObject` base class is automatically inherited by the new subclass.<br> 

## Author
Maria Graciella L. Roque  
Discord:[@grachiebob]

## Acknowledgements
* GmE 205 Laboratory Exercise 3 Manual
* [MarkDown](https://www.markdownguide.org/cheat-sheet/)

Edited on VS Code